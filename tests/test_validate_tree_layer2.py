from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest.mock import patch, MagicMock


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = REPO_ROOT / "scripts"

if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import layer2_governance_loader as governance
import layer2_prompt_builder as prompt_builder
import layer2_response_processor as response_processor
import taxonomy_criteria_sync as criteria_sync


class ValidateTreeLayer2Tests(unittest.TestCase):
    def test_build_prompt_includes_node_criteria_context(self) -> None:
        prompt = prompt_builder.build_prompt(
            taxonomy_text="Music\n  Rock",
            governance_context="ctx",
            layer2_rules=[],
            prompt_template="{{SYSTEM_CONTEXT}}\n{{NODE_CRITERIA_CONTEXT}}\n{{TAXONOMY_TEXT}}",
            prompt_context={
                "system_context": "sys",
                "clone_context": "clone",
                "applicability_context": "app",
            },
            node_criteria_context="- Node: Music > Rock",
        )

        self.assertIn("- Node: Music > Rock", prompt)

    def test_build_prompt_rejects_unresolved_placeholders(self) -> None:
        with self.assertRaises(ValueError):
            prompt_builder.build_prompt(
                taxonomy_text="Music\n  Rock",
                governance_context="ctx",
                layer2_rules=[],
                prompt_template="{{SYSTEM_CONTEXT}}\n{{UNKNOWN_BLOCK}}",
                prompt_context={
                    "system_context": "sys",
                    "clone_context": "clone",
                    "applicability_context": "app",
                },
            )

    def test_build_criteria_sync_detects_missing_paths(self) -> None:
        taxonomy_text = "Music\n  Rock\n    Grunge\n  Latin"
        criteria = {
            "Music > Rock": {
                "membership_criteria": "m",
                "exclusion_criteria": "e",
                "reference_examples": [],
            }
        }

        result = criteria_sync.build_criteria_sync(taxonomy_text, criteria)

        self.assertEqual(result.required_count, 3)
        self.assertEqual(result.covered_count, 1)
        self.assertIn("Music > Rock > Grunge", result.missing_paths)
        self.assertIn("Music > Latin", result.missing_paths)

    def test_load_node_criteria_rejects_duplicate_node_path(self) -> None:
        criteria_path = REPO_ROOT / "taxonomy" / "test_duplicate_criteria.json"
        criteria_path.write_text(
            """
{
  "nodes": [
    {
      "node_path": "Music > Rock",
      "membership_criteria": "m1",
      "exclusion_criteria": "e1",
      "reference_examples": []
    },
    {
      "node_path": "Music > Rock",
      "membership_criteria": "m2",
      "exclusion_criteria": "e2",
      "reference_examples": []
    }
  ]
}
""".strip(),
            encoding="utf-8",
        )
        try:
            with self.assertRaises(ValueError):
                criteria_sync.load_node_criteria(criteria_path)
        finally:
            criteria_path.unlink(missing_ok=True)

    def test_build_missing_criteria_stub_contains_todo_fields(self) -> None:
        payload = criteria_sync.build_missing_criteria_stub(
            ["Music > Latin > Regional Mexicano"]
        )

        self.assertEqual(payload["version"], "1.0")
        self.assertEqual(payload["generated_for"], "missing-node-criteria")
        self.assertEqual(len(payload["nodes"]), 1)
        node = payload["nodes"][0]
        self.assertEqual(node["node_path"], "Music > Latin > Regional Mexicano")
        self.assertIn("TODO", node["membership_criteria"])
        self.assertIn("TODO", node["exclusion_criteria"])
        self.assertEqual(len(node["reference_examples"]), 2)

    def test_process_layer2_response_reports_summary_mismatch_and_pass_items(self) -> None:
        response_data = {
            "layer": "MVET-LAYER2",
            "findings": [
                {
                    "rule_id": "MVET-L2-001",
                    "severity": "WARNING",
                    "result": "PASS",
                    "node_path": "Music > Pop",
                    "evidence": "dummy",
                    "recommendation": "dummy",
                    "confidence": 0.8,
                }
            ],
            "summary": {
                "total_fatal": 0,
                "total_warning": 1,
                "total_suggestion": 0,
                "decision_recommendation": "PASS_WITH_WARNINGS",
            },
        }

        with patch.object(response_processor, "write_layer2_reports"):
            findings, schema_errors, _, fatal_count, warning_count, suggestion_count, decision = (
                response_processor.process_layer2_response(
                    response_data,
                    layer2_rules=[
                        {
                            "rule_id": "MVET-L2-001",
                            "fb": "FB-05",
                            "severity": "WARNING",
                            "description": "desc",
                            "check": "check",
                        }
                    ],
                    valid_rule_ids={"MVET-L2-001"},
                    reports_dir=REPO_ROOT / "reports",
                )
            )

        self.assertEqual(findings, [])
        self.assertEqual((fatal_count, warning_count, suggestion_count, decision), (0, 0, 0, "PASS"))
        self.assertTrue(any("result PASS no permitido" in error for error in schema_errors))
        self.assertTrue(any("summary.total_warning inconsistente" in error for error in schema_errors))
        self.assertTrue(any("summary.decision_recommendation inconsistente" in error for error in schema_errors))

    def test_load_governance_doc_groups_derives_strategy_matrix(self) -> None:
        strategy_path = REPO_ROOT / "docs" / "operations" / "VALIDATE_MASTER_STRATEGY.md"
        groups = governance.load_governance_doc_groups(strategy_path, REPO_ROOT)

        mandatory = {path.as_posix().split("music-taxonomy/")[-1] for path in groups["MANDATORY"]}
        conditional = {path.as_posix().split("music-taxonomy/")[-1] for path in groups["CONDITIONAL"]}

        self.assertIn("docs/governance/GLOBAL_RULES.md", mandatory)
        self.assertIn("docs/governance/SYSTEM_CONTRACT.md", mandatory)
        self.assertIn("docs/governance/TAXONOMY_CHANGE_POLICY.md", conditional)

    def test_response_processor_writes_both_report_formats(self) -> None:
        """Test que proceso_layer2_response genera ambos formatos de reporte."""
        response_data = {
            "layer": "MVET-LAYER2",
            "findings": [
                {
                    "rule_id": "MVET-L2-001",
                    "severity": "WARNING",
                    "result": "FAIL",
                    "node_path": "Music > Pop",
                    "evidence": "Test evidence",
                    "recommendation": "Test recommendation",
                    "confidence": 0.75,
                }
            ],
            "summary": {
                "total_fatal": 0,
                "total_warning": 1,
                "total_suggestion": 0,
                "decision_recommendation": "PASS_WITH_WARNINGS",
            },
        }

        test_reports_dir = REPO_ROOT / "reports"
        findings, schema_errors, _, fatal_count, warning_count, _, decision = (
            response_processor.process_layer2_response(
                response_data,
                layer2_rules=[
                    {
                        "rule_id": "MVET-L2-001",
                        "fb": "FB-05",
                        "severity": "WARNING",
                        "description": "Test rule",
                        "check": "Test check",
                    }
                ],
                valid_rule_ids={"MVET-L2-001"},
                reports_dir=test_reports_dir,
            )
        )

        self.assertEqual(len(findings), 1)
        self.assertEqual(warning_count, 1)
        self.assertEqual(decision, "PASS_WITH_WARNINGS")
        self.assertTrue((test_reports_dir / "validate_master_layer2_report.json").exists())
        self.assertTrue((test_reports_dir / "validate_master_layer2_report.md").exists())


if __name__ == "__main__":
    unittest.main()