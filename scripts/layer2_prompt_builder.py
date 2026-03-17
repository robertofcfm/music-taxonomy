from __future__ import annotations

from layer2_contract import find_unresolved_placeholders


def build_prompt(
    taxonomy_text: str,
    governance_context: str,
    layer2_rules: list[dict[str, str]],
    prompt_template: str,
    prompt_context: dict[str, str],
) -> str:
    rules_block = "\n".join(
        f"  {r['rule_id']} [{r['fb']}] {r['severity']}\n"
        f"  Descripción: {r['description']}\n"
        f"  Check: {r['check']}\n"
        for r in layer2_rules
    )

    output_schema = """\
{
  "layer": "MVET-LAYER2",
  "findings": [
    {
      "rule_id": "<RULE_ID>",
      "severity": "<FATAL|WARNING|SUGGESTION>",
      "result": "<PASS si la recomendación es no hacer cambios | FAIL si se requiere o sugiere una acción>",
      "node_path": "<ruta completa: Padre > Hijo>",
      "evidence": "<descripción objetiva de lo observado>",
      "recommendation": "<propuesta de mejora o confirmación sin cambio>",
      "confidence": <0.00 a 1.00>
    }
  ],
  "summary": {
    "total_fatal": <int>,
    "total_warning": <int>,
    "total_suggestion": <int>,
    "decision_recommendation": "<PASS|PASS_WITH_WARNINGS|FAIL>"
  }
}"""

    rendered = (
        prompt_template.replace("{{SYSTEM_CONTEXT}}", prompt_context["system_context"])
        .replace("{{CLONE_CONTEXT}}", prompt_context["clone_context"])
        .replace("{{GOVERNANCE_CONTEXT}}", governance_context)
        .replace("{{RULES_BLOCK}}", rules_block)
        .replace("{{TAXONOMY_TEXT}}", taxonomy_text)
        .replace("{{OUTPUT_SCHEMA}}", output_schema)
    )

    unresolved = find_unresolved_placeholders(rendered)
    if unresolved:
        raise ValueError(
            "La plantilla de prompt L2 dejo placeholders sin resolver: "
            + ", ".join(unresolved)
        )

    return rendered
