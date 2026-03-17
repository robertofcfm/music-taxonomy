"""Validación semántica (Capa 2) de taxonomy/genre_tree_master.md.

Modos de operación:

  --print-prompt
      Genera el prompt determinista para la IA y lo escribe en
      prompts/validate_master_layer2_prompt.txt.
      Ese texto debe enviarse a un modelo de lenguaje externo.

  --apply-response <archivo.json>
      Lee la respuesta JSON de la IA, valida su esquema contra el
      contrato definido en VALIDATE_MASTER_STRATEGY.md, y genera
      los reportes de Capa 2.

    --apply-cycle <directorio>
            Aplica respuestas de IA en forma cíclica hasta que no haya
            hallazgos pendientes o se alcance el máximo de iteraciones.
            Convención de archivos esperada:
                iteración 1: validate_master_layer2_response.json
                iteración N>1: validate_master_layer2_response.iterN.json

Salida mínima (modo --apply-response):
  reports/validate_master_layer2_report.json
  reports/validate_master_layer2_report.md
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
GOVERNANCE_DIR = REPO_ROOT / "docs" / "governance"
DEFAULT_TAXONOMY_PATH = REPO_ROOT / "taxonomy" / "genre_tree_master.md"
PROMPTS_DIR = REPO_ROOT / "prompts"
PROMPT_TEMPLATE = PROMPTS_DIR / "generadores" / "validate_master_layer2_prompt_template.md"
PROMPT_CONTEXT = PROMPTS_DIR / "generadores" / "validate_master_layer2_prompt_context.json"
VALIDATE_MASTER_STRATEGY = REPO_ROOT / "docs" / "operations" / "VALIDATE_MASTER_STRATEGY.md"
REPORTS_DIR = REPO_ROOT / "reports"
PROMPT_OUTPUT = PROMPTS_DIR / "validate_master_layer2_prompt.txt"
DEFAULT_CYCLE_RESPONSE_BASENAME = "validate_master_layer2_response"


# ---------------------------------------------------------------------------
# Definición dinámica de reglas MVET-L2 desde docs/governance
# ---------------------------------------------------------------------------

RULE_MARKER_START = "<!-- MVET:LAYER2_RULE_START -->"
RULE_MARKER_END = "<!-- MVET:LAYER2_RULE_END -->"
RULE_BLOCK_RE = re.compile(
    re.escape(RULE_MARKER_START) + r"\s*(\{.*?\})\s*" + re.escape(RULE_MARKER_END),
    re.DOTALL,
)
LAYER2_RULE_REQUIRED_FIELDS = {
    "rule_id",
    "fb",
    "severity",
    "description",
    "check",
}
VALID_SEVERITIES = {"FATAL", "WARNING", "SUGGESTION"}
VALID_DECISIONS = {"PASS", "PASS_WITH_WARNINGS", "FAIL"}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def iso_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def load_taxonomy_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_prompt_template() -> str:
    if not PROMPT_TEMPLATE.exists():
        raise FileNotFoundError(f"No existe plantilla de prompt L2: {PROMPT_TEMPLATE}")
    return PROMPT_TEMPLATE.read_text(encoding="utf-8")


def load_prompt_context() -> dict[str, str]:
    if not PROMPT_CONTEXT.exists():
        raise FileNotFoundError(f"No existe contexto de prompt L2: {PROMPT_CONTEXT}")

    try:
        payload = json.loads(PROMPT_CONTEXT.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        raise ValueError(f"Contexto de prompt L2 invalido: {e}") from e

    required_fields = {"system_context", "clone_context", "applicability_context"}
    missing = required_fields - payload.keys()
    if missing:
        raise ValueError(f"Contexto de prompt L2 incompleto: faltan {sorted(missing)}")

    return {field: str(payload[field]).strip() for field in required_fields}


def load_governance_doc_groups() -> dict[str, list[Path]]:
    if not VALIDATE_MASTER_STRATEGY.exists():
        raise FileNotFoundError(
            f"No existe documento estrategico de validacion: {VALIDATE_MASTER_STRATEGY}"
        )

    section_names = ("MANDATORY", "CONDITIONAL", "REFERENTIAL", "EXCLUDED")
    groups: dict[str, list[Path]] = {name: [] for name in section_names}
    current_section: str | None = None

    for raw_line in VALIDATE_MASTER_STRATEGY.read_text(encoding="utf-8").splitlines():
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

        groups[current_section].append(REPO_ROOT / Path(candidate))

    if not groups["MANDATORY"]:
        raise ValueError(
            "No se pudieron derivar documentos MANDATORY desde VALIDATE_MASTER_STRATEGY.md"
        )

    return groups


def load_governance_context() -> str:
    """Construye contexto normativo dinámico desde docs/governance/."""
    prompt_context = load_prompt_context()
    doc_groups = load_governance_doc_groups()
    blocks: list[str] = []

    for doc in doc_groups["MANDATORY"]:
        if not doc.exists():
            raise FileNotFoundError(f"No existe documento obligatorio de governance: {doc}")
        rel = doc.relative_to(REPO_ROOT)
        content = doc.read_text(encoding="utf-8").strip()
        blocks.append(f"=== {rel} (MANDATORY) ===\n{content}")

    for doc in doc_groups["CONDITIONAL"]:
        rel = doc.relative_to(REPO_ROOT)
        if doc.exists():
            content = doc.read_text(encoding="utf-8").strip()
            blocks.append(f"=== {rel} (CONDITIONAL) ===\n{content}")
        else:
            blocks.append(f"=== {rel} (CONDITIONAL) ===\nArchivo no presente en este workspace.")

    return f"{prompt_context['applicability_context']}\n\n" + "\n\n".join(blocks)


def load_layer2_rules_from_governance() -> list[dict[str, str]]:
    """Carga reglas MVET-L2 marcadas en docs/governance mediante bloques JSON."""
    if not GOVERNANCE_DIR.exists():
        raise FileNotFoundError(f"No existe directorio de governance: {GOVERNANCE_DIR}")

    rules: list[dict[str, str]] = []
    seen_ids: set[str] = set()

    for doc in sorted(GOVERNANCE_DIR.glob("*.md")):
        text = doc.read_text(encoding="utf-8")
        for match in RULE_BLOCK_RE.finditer(text):
            block = match.group(1)
            try:
                parsed = json.loads(block)
            except json.JSONDecodeError as e:
                raise ValueError(
                    f"Regla L2 con JSON inválido en {doc.relative_to(REPO_ROOT)}: {e}"
                ) from e

            if not isinstance(parsed, dict):
                raise ValueError(
                    f"Regla L2 inválida en {doc.relative_to(REPO_ROOT)}: debe ser objeto JSON."
                )

            missing = LAYER2_RULE_REQUIRED_FIELDS - parsed.keys()
            if missing:
                raise ValueError(
                    f"Regla L2 inválida en {doc.relative_to(REPO_ROOT)}: faltan campos {sorted(missing)}."
                )

            rule_id = str(parsed["rule_id"]).strip()
            severity = str(parsed["severity"]).strip()
            if not rule_id:
                raise ValueError(f"Regla L2 inválida en {doc.relative_to(REPO_ROOT)}: rule_id vacío.")
            if rule_id in seen_ids:
                raise ValueError(f"rule_id duplicado en reglas L2: {rule_id}")
            if severity not in VALID_SEVERITIES:
                raise ValueError(
                    f"Regla L2 '{rule_id}' con severity inválida '{severity}'."
                )

            normalized = {
                "rule_id": rule_id,
                "fb": str(parsed["fb"]).strip(),
                "severity": severity,
                "description": str(parsed["description"]).strip(),
                "check": str(parsed["check"]).strip(),
            }
            rules.append(normalized)
            seen_ids.add(rule_id)

    if not rules:
        raise ValueError(
            "No se encontraron reglas L2 marcadas en docs/governance. "
            f"Usa bloques {RULE_MARKER_START} ... {RULE_MARKER_END}."
        )

    return rules


# ---------------------------------------------------------------------------
# Modo: --print-prompt
# ---------------------------------------------------------------------------

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

    return (
        prompt_template.replace("{{SYSTEM_CONTEXT}}", prompt_context["system_context"])
        .replace("{{CLONE_CONTEXT}}", prompt_context["clone_context"])
        .replace("{{GOVERNANCE_CONTEXT}}", governance_context)
        .replace("{{RULES_BLOCK}}", rules_block)
        .replace("{{TAXONOMY_TEXT}}", taxonomy_text)
        .replace("{{OUTPUT_SCHEMA}}", output_schema)
    )


# ---------------------------------------------------------------------------
# Modo: --apply-response
# ---------------------------------------------------------------------------


VALID_RESULTS = {"PASS", "FAIL"}


@dataclass
class Layer2Finding:
    rule_id: str
    severity: str
    result: str
    node_path: str
    evidence: str
    recommendation: str
    confidence: float
    schema_valid: bool = True
    schema_error: str = ""


def validate_response_schema(
    data: dict, valid_rule_ids: set[str]
) -> tuple[list[Layer2Finding], list[str]]:
    """Valida el JSON de respuesta de la IA contra el contrato MVET."""
    errors: list[str] = []
    findings: list[Layer2Finding] = []

    if not isinstance(data.get("findings"), list):
        errors.append("Campo 'findings' faltante o no es un arreglo.")
        return findings, errors

    for i, item in enumerate(data["findings"]):
        prefix = f"findings[{i}]"
        rule_id = item.get("rule_id", "")
        severity = item.get("severity", "")
        result = item.get("result", "")
        node_path = item.get("node_path", "")
        evidence = item.get("evidence", "")
        recommendation = item.get("recommendation", "")
        confidence = item.get("confidence")

        item_errors: list[str] = []
        if rule_id not in valid_rule_ids:
            item_errors.append(f"{prefix}: rule_id inválido '{rule_id}'.")
        if severity not in VALID_SEVERITIES:
            item_errors.append(f"{prefix}: severity inválida '{severity}'.")
        if result not in VALID_RESULTS:
            item_errors.append(f"{prefix}: result inválido '{result}' (debe ser PASS o FAIL).")
        if not node_path:
            item_errors.append(f"{prefix}: node_path vacío.")
        if not evidence:
            item_errors.append(f"{prefix}: evidence vacío.")
        if not recommendation:
            item_errors.append(f"{prefix}: recommendation vacío.")
        if not isinstance(confidence, (int, float)) or not (0.0 <= confidence <= 1.0):
            item_errors.append(f"{prefix}: confidence debe ser número entre 0 y 1.")

        if item_errors:
            errors.extend(item_errors)
            findings.append(
                Layer2Finding(
                    rule_id=rule_id or "UNKNOWN",
                    severity=severity or "UNKNOWN",
                    result=result if result in VALID_RESULTS else "FAIL",
                    node_path=node_path,
                    evidence=evidence,
                    recommendation=recommendation,
                    confidence=float(confidence) if isinstance(confidence, (int, float)) else 0.0,
                    schema_valid=False,
                    schema_error=" | ".join(item_errors),
                )
            )
        else:
            findings.append(
                Layer2Finding(
                    rule_id=rule_id,
                    severity=severity,
                    result=result,
                    node_path=node_path,
                    evidence=evidence,
                    recommendation=recommendation,
                    confidence=float(confidence),
                )
            )

    summary = data.get("summary", {})
    if not isinstance(summary, dict):
        errors.append("Campo 'summary' faltante o no es un objeto.")
    else:
        if summary.get("decision_recommendation") not in VALID_DECISIONS:
            errors.append(
                f"summary.decision_recommendation inválido: '{summary.get('decision_recommendation')}'."
            )

    return findings, errors


def summarize_layer2(findings: list[Layer2Finding]) -> tuple[int, int, int, str]:
    fatals = sum(1 for f in findings if f.severity == "FATAL" and f.schema_valid)
    warnings = sum(1 for f in findings if f.severity == "WARNING" and f.schema_valid)
    suggestions = sum(1 for f in findings if f.severity == "SUGGESTION" and f.schema_valid)

    if fatals:
        decision = "FAIL"
    elif warnings or suggestions:
        decision = "PASS_WITH_WARNINGS"
    else:
        decision = "PASS"

    return fatals, warnings, suggestions, decision


def write_layer2_reports(
    layer2_rules: list[dict[str, str]],
    findings: list[Layer2Finding],
    schema_errors: list[str],
    ai_summary: dict,
    decision: str,
    fatal_count: int,
    warning_count: int,
    suggestion_count: int,
) -> None:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = iso_now()

    rule_map = {r["rule_id"]: r for r in layer2_rules}
    payload = {
        "process": "MVET-LAYER2",
        "generated_at": timestamp,
        "schema_errors": schema_errors,
        "summary": {
            "decision": decision,
            "total_fatal": fatal_count,
            "total_warning": warning_count,
            "total_suggestion": suggestion_count,
            "total_findings": len(findings),
        },
        "ai_summary": ai_summary,
        "findings": [
            {
                "rule_id": f.rule_id,
                "fb": rule_map.get(f.rule_id, {}).get("fb", ""),
                "severity": f.severity,
                "result": f.result,
                "node_path": f.node_path,
                "evidence": f.evidence,
                "recommendation": f.recommendation,
                "confidence": f.confidence,
                "schema_valid": f.schema_valid,
                "schema_error": f.schema_error,
            }
            for f in findings
        ],
    }

    report_json = REPORTS_DIR / "validate_master_layer2_report.json"
    report_md = REPORTS_DIR / "validate_master_layer2_report.md"

    report_json.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    md_lines = [
        "# Reporte de Validación MVET (Capa 2 — Semántica IA)",
        "",
        f"- Fecha: {timestamp}",
        f"- Decisión: {decision}",
        f"- FATAL: {fatal_count}",
        f"- WARNING: {warning_count}",
        f"- SUGGESTION: {suggestion_count}",
    ]

    if schema_errors:
        md_lines += ["", "## Errores de esquema en respuesta IA", ""]
        for e in schema_errors:
            md_lines.append(f"- {e}")

    if findings:
        md_lines += ["", "## Hallazgos", ""]
        for f in findings:
            status = "SCHEMA_ERROR" if not f.schema_valid else f.severity
            fb = rule_map.get(f.rule_id, {}).get("fb", "")
            md_lines += [
                f"### {f.rule_id} [{fb}] - {status}",
                f"- Nodo: {f.node_path}",
                f"- Evidencia: {f.evidence}",
                f"- Recomendación: {f.recommendation}",
                f"- Confianza: {f.confidence:.2f}",
                "",
            ]
    else:
        md_lines += ["", "Sin hallazgos.", ""]

    report_md.write_text("\n".join(md_lines), encoding="utf-8")


def load_response_json(response_path: Path) -> dict:
    try:
        return json.loads(response_path.read_text(encoding="utf-8-sig"))
    except json.JSONDecodeError as e:
        raise ValueError(f"el archivo de respuesta no es JSON válido: {e}") from e


def process_layer2_response(
    response_data: dict,
    layer2_rules: list[dict[str, str]],
    valid_rule_ids: set[str],
) -> tuple[list[Layer2Finding], list[str], dict, int, int, int, str]:
    findings, schema_errors = validate_response_schema(response_data, valid_rule_ids)
    findings = [f for f in findings if f.result != "PASS"]
    fatal_count, warning_count, suggestion_count, decision = summarize_layer2(findings)
    ai_summary = response_data.get("summary", {})

    write_layer2_reports(
        layer2_rules=layer2_rules,
        findings=findings,
        schema_errors=schema_errors,
        ai_summary=ai_summary,
        decision=decision,
        fatal_count=fatal_count,
        warning_count=warning_count,
        suggestion_count=suggestion_count,
    )

    return (
        findings,
        schema_errors,
        ai_summary,
        fatal_count,
        warning_count,
        suggestion_count,
        decision,
    )


def expected_cycle_response_path(response_dir: Path, iteration: int, base_name: str) -> Path:
    if iteration == 1:
        return response_dir / f"{base_name}.json"
    return response_dir / f"{base_name}.iter{iteration}.json"


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validación semántica (Capa 2) — taxonomy/genre_tree_master.md."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--print-prompt",
        action="store_true",
        help="Genera el prompt para la IA y lo guarda en reports/.",
    )
    group.add_argument(
        "--apply-response",
        metavar="ARCHIVO_JSON",
        help="Procesa la respuesta JSON de la IA y genera reportes.",
    )
    group.add_argument(
        "--apply-cycle",
        metavar="DIRECTORIO_RESPUESTAS",
        help=(
            "Procesa respuestas en ciclo hasta no encontrar hallazgos. "
            "Espera validate_master_layer2_response.json (iteración 1) y "
            "validate_master_layer2_response.iterN.json (iteraciones siguientes)."
        ),
    )
    parser.add_argument(
        "--taxonomy-file",
        default=str(DEFAULT_TAXONOMY_PATH),
        help="Ruta al archivo maestro de taxonomía.",
    )
    parser.add_argument(
        "--max-iterations",
        type=int,
        default=10,
        help="Máximo de iteraciones para --apply-cycle (default: 10).",
    )
    parser.add_argument(
        "--cycle-response-basename",
        default=DEFAULT_CYCLE_RESPONSE_BASENAME,
        help=(
            "Nombre base de archivos para --apply-cycle (sin extensión). "
            "Default: validate_master_layer2_response"
        ),
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    taxonomy_path = Path(args.taxonomy_file).resolve()
    if not taxonomy_path.exists():
        print(f"ERROR: no existe el archivo: {taxonomy_path}")
        return 2

    try:
        layer2_rules = load_layer2_rules_from_governance()
    except (FileNotFoundError, ValueError) as e:
        print(f"ERROR: {e}")
        return 2

    valid_rule_ids = {r["rule_id"] for r in layer2_rules}

    if args.print_prompt:
        taxonomy_text = load_taxonomy_text(taxonomy_path)
        try:
            prompt_context = load_prompt_context()
            governance_context = load_governance_context()
            prompt_template = load_prompt_template()
        except (FileNotFoundError, ValueError) as e:
            print(f"ERROR: {e}")
            return 2

        prompt = build_prompt(
            taxonomy_text,
            governance_context,
            layer2_rules,
            prompt_template,
            prompt_context,
        )
        PROMPTS_DIR.mkdir(parents=True, exist_ok=True)
        PROMPT_OUTPUT.write_text(prompt, encoding="utf-8")
        print(f"Prompt generado: {PROMPT_OUTPUT.relative_to(REPO_ROOT)}")
        print("Copia el contenido de ese archivo a un modelo de lenguaje externo.")
        print("Guarda la respuesta JSON y pásala con --apply-response <archivo.json>")
        return 0

    if args.apply_response:
        # Modo --apply-response
        response_path = Path(args.apply_response).resolve()
        if not response_path.exists():
            print(f"ERROR: no existe el archivo de respuesta: {response_path}")
            return 2

        try:
            response_data = load_response_json(response_path)
        except ValueError as e:
            print(f"ERROR: {e}")
            return 2

        (
            findings,
            schema_errors,
            _,
            fatal_count,
            warning_count,
            suggestion_count,
            decision,
        ) = process_layer2_response(response_data, layer2_rules, valid_rule_ids)

        if schema_errors:
            print(f"ADVERTENCIA: {len(schema_errors)} errores de esquema en la respuesta IA.")
            for e in schema_errors:
                print(f"  - {e}")

        print(f"Decision: {decision}")
        print(f"FATAL: {fatal_count} | WARNING: {warning_count} | SUGGESTION: {suggestion_count}")
        print("Reportes: reports/validate_master_layer2_report.json, reports/validate_master_layer2_report.md")
        return 1 if decision == "FAIL" else 0

    # Modo --apply-cycle
    if args.max_iterations < 1:
        print("ERROR: --max-iterations debe ser >= 1")
        return 2

    response_dir = Path(args.apply_cycle).resolve()
    if not response_dir.exists() or not response_dir.is_dir():
        print(f"ERROR: no existe el directorio de respuestas: {response_dir}")
        return 2

    base_name = str(args.cycle_response_basename).strip()
    if not base_name:
        print("ERROR: --cycle-response-basename no puede estar vacío")
        return 2

    for iteration in range(1, args.max_iterations + 1):
        response_path = expected_cycle_response_path(response_dir, iteration, base_name)
        if not response_path.exists():
            if iteration == 1:
                print(f"ERROR: no existe archivo de iteración 1: {response_path}")
                return 2

            print(
                "PENDIENTE: no se encontró la siguiente respuesta para continuar ciclo: "
                f"{response_path.name}"
            )
            return 1

        try:
            response_data = load_response_json(response_path)
        except ValueError as e:
            print(f"ERROR en iteración {iteration}: {e}")
            return 2

        (
            findings,
            schema_errors,
            _,
            fatal_count,
            warning_count,
            suggestion_count,
            decision,
        ) = process_layer2_response(response_data, layer2_rules, valid_rule_ids)

        print(
            f"Iteración {iteration}: decision={decision} | "
            f"FATAL={fatal_count} WARNING={warning_count} SUGGESTION={suggestion_count}"
        )

        if schema_errors:
            print(f"ADVERTENCIA iteración {iteration}: {len(schema_errors)} errores de esquema.")
            for e in schema_errors:
                print(f"  - {e}")

        if not findings and not schema_errors:
            print(f"Ciclo cerrado en iteración {iteration}: no hay hallazgos pendientes.")
            print(
                "Reportes: reports/validate_master_layer2_report.json, "
                "reports/validate_master_layer2_report.md"
            )
            return 0

    print(
        "PENDIENTE: se alcanzó el máximo de iteraciones sin quedar limpio. "
        f"max_iterations={args.max_iterations}"
    )
    print(
        "Reportes: reports/validate_master_layer2_report.json, "
        "reports/validate_master_layer2_report.md"
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
