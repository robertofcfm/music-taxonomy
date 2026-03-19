from __future__ import annotations

import json
import re
from pathlib import Path

from layer2_contract import LAYER2_RULE_REQUIRED_FIELDS, VALID_SEVERITIES

RULE_MARKER_START = "<!-- MVET:LAYER2_RULE_START -->"
RULE_MARKER_END = "<!-- MVET:LAYER2_RULE_END -->"
RULE_BLOCK_RE = re.compile(
    re.escape(RULE_MARKER_START) + r"\s*(\{.*?\})\s*" + re.escape(RULE_MARKER_END),
    re.DOTALL,
)


def load_prompt_template(prompt_template_path: Path) -> str:
    if not prompt_template_path.exists():
        raise FileNotFoundError(f"No existe plantilla de prompt L2: {prompt_template_path}")
    return prompt_template_path.read_text(encoding="utf-8")


def load_prompt_context(prompt_context_path: Path) -> dict[str, str]:
    if not prompt_context_path.exists():
        raise FileNotFoundError(f"No existe contexto de prompt L2: {prompt_context_path}")

    try:
        payload = json.loads(prompt_context_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        raise ValueError(f"Contexto de prompt L2 invalido: {e}") from e

    required_fields = {"system_context", "clone_context", "applicability_context"}
    missing = required_fields - payload.keys()
    if missing:
        raise ValueError(f"Contexto de prompt L2 incompleto: faltan {sorted(missing)}")

    return {field: str(payload[field]).strip() for field in required_fields}


def load_governance_doc_groups(strategy_path: Path, repo_root: Path) -> dict[str, list[Path]]:
    if not strategy_path.exists():
        raise FileNotFoundError(f"No existe documento estrategico de validacion: {strategy_path}")

    section_names = ("MANDATORY", "CONDITIONAL", "REFERENTIAL", "EXCLUDED")
    groups: dict[str, list[Path]] = {name: [] for name in section_names}
    current_section: str | None = None

    for raw_line in strategy_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()

        if line in section_names:
            current_section = line
            continue

        if line.startswith("Resumen de matriz:") or line.startswith("Alcance de derivación"):
            current_section = None
            continue

        if current_section is None or not line.startswith("- "):
            continue

        candidate = line[2:].strip()
        if not candidate.endswith(".md"):
            continue

        groups[current_section].append(repo_root / Path(candidate))

    if not groups["MANDATORY"]:
        raise ValueError(
            "No se pudieron derivar documentos MANDATORY desde VALIDATE_MASTER_STRATEGY.md"
        )

    return groups


def load_governance_context(
    strategy_path: Path, repo_root: Path, prompt_context: dict[str, str]
) -> str:
    doc_groups = load_governance_doc_groups(strategy_path, repo_root)
    blocks: list[str] = []

    for doc in doc_groups["MANDATORY"]:
        if not doc.exists():
            raise FileNotFoundError(f"No existe documento obligatorio de governance: {doc}")
        rel = doc.relative_to(repo_root)
        content = doc.read_text(encoding="utf-8").strip()
        blocks.append(f"=== {rel} (MANDATORY) ===\n{content}")

    for doc in doc_groups["CONDITIONAL"]:
        rel = doc.relative_to(repo_root)
        if doc.exists():
            content = doc.read_text(encoding="utf-8").strip()
            blocks.append(f"=== {rel} (CONDITIONAL) ===\n{content}")
        else:
            blocks.append(f"=== {rel} (CONDITIONAL) ===\nArchivo no presente en este workspace.")

    return f"{prompt_context['applicability_context']}\n\n" + "\n\n".join(blocks)


def load_layer2_rules_from_governance(governance_dir: Path) -> list[dict[str, str]]:
    if not governance_dir.exists():
        raise FileNotFoundError(f"No existe directorio de governance: {governance_dir}")

    rules: list[dict[str, str]] = []
    seen_ids: set[str] = set()

    for doc in sorted(governance_dir.glob("*.md")):
        text = doc.read_text(encoding="utf-8")
        for match in RULE_BLOCK_RE.finditer(text):
            block = match.group(1)
            try:
                parsed = json.loads(block)
            except json.JSONDecodeError as e:
                raise ValueError(
                    f"Regla L2 con JSON inválido en {doc.relative_to(governance_dir.parent.parent)}: {e}"
                ) from e

            if not isinstance(parsed, dict):
                raise ValueError(
                    f"Regla L2 inválida en {doc.name}: debe ser objeto JSON."
                )

            missing = LAYER2_RULE_REQUIRED_FIELDS - parsed.keys()
            if missing:
                raise ValueError(
                    f"Regla L2 inválida en {doc.name}: faltan campos {sorted(missing)}."
                )

            rule_id = str(parsed["rule_id"]).strip()
            severity = str(parsed["severity"]).strip()
            if not rule_id:
                raise ValueError(f"Regla L2 inválida en {doc.name}: rule_id vacío.")
            if rule_id in seen_ids:
                raise ValueError(f"rule_id duplicado en reglas L2: {rule_id}")
            if severity not in VALID_SEVERITIES:
                raise ValueError(f"Regla L2 '{rule_id}' con severity inválida '{severity}'.")

            rules.append(
                {
                    "rule_id": rule_id,
                    "fb": str(parsed["fb"]).strip(),
                    "severity": severity,
                    "description": str(parsed["description"]).strip(),
                    "check": str(parsed["check"]).strip(),
                }
            )
            seen_ids.add(rule_id)

    if not rules:
        raise ValueError(
            f"No se encontraron reglas L2 marcadas en {governance_dir}. "
            f"Usa bloques {RULE_MARKER_START} ... {RULE_MARKER_END}."
        )

    return rules
