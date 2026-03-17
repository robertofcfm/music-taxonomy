from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest.mock import patch


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = REPO_ROOT / "scripts"

if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import validate_tree_layer2 as l2


class ValidateTreeLayer2Tests(unittest.TestCase):
    def test_build_prompt_rejects_unresolved_placeholders(self) -> None:
        with self.assertRaises(ValueError):
            l2.build_prompt(
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

        with patch.object(l2, "write_layer2_reports"):
            findings, schema_errors, _, fatal_count, warning_count, suggestion_count, decision = (
                l2.process_layer2_response(
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
                )
            )

        self.assertEqual(findings, [])
        self.assertEqual((fatal_count, warning_count, suggestion_count, decision), (0, 0, 0, "PASS"))
        self.assertTrue(any("result PASS no permitido" in error for error in schema_errors))
        self.assertTrue(any("summary.total_warning inconsistente" in error for error in schema_errors))
        self.assertTrue(any("summary.decision_recommendation inconsistente" in error for error in schema_errors))

    def test_load_governance_doc_groups_derives_strategy_matrix(self) -> None:
        groups = l2.load_governance_doc_groups()

        mandatory = {path.as_posix().split("music-taxonomy/")[-1] for path in groups["MANDATORY"]}
        conditional = {path.as_posix().split("music-taxonomy/")[-1] for path in groups["CONDITIONAL"]}

        self.assertIn("docs/governance/GLOBAL_RULES.md", mandatory)
        self.assertIn("docs/governance/SYSTEM_CONTRACT.md", mandatory)
        self.assertIn("docs/governance/TAXONOMY_CHANGE_POLICY.md", conditional)


if __name__ == "__main__":
    unittest.main()