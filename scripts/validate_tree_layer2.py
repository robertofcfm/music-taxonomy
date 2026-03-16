"""Validación semántica (Capa 2) de taxonomy/genre_tree_master.md.

Modos de operación:

  --print-prompt
      Genera el prompt determinista para la IA y lo escribe en
      reports/validate_master_layer2_prompt.txt.
      Ese texto debe enviarse a un modelo de lenguaje externo.

  --apply-response <archivo.json>
      Lee la respuesta JSON de la IA, valida su esquema contra el
      contrato definido en VALIDATE_MASTER_STRATEGY.md, y genera
      los reportes de Capa 2.

Prerrequisito:
  Capa 1 debe haber terminado con decisión PASS o PASS_WITH_WARNINGS.
  Este script verifica ese requisito antes de continuar.

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
REPORTS_DIR = REPO_ROOT / "reports"
LAYER1_REPORT = REPORTS_DIR / "validate_master_report.json"
PROMPT_OUTPUT = REPORTS_DIR / "validate_master_layer2_prompt.txt"

GOVERNANCE_DOCS_MANDATORY = [
    GOVERNANCE_DIR / "GLOBAL_RULES.md",
    GOVERNANCE_DIR / "SYSTEM_CONTRACT.md",
    GOVERNANCE_DIR / "MVET_LAYER2_RULES.md",
    GOVERNANCE_DIR / "TAXONOMY_RULES.md",
    GOVERNANCE_DIR / "TAXONOMY_DEPTH_POLICY.md",
    GOVERNANCE_DIR / "TAXONOMY_NAMING_CONVENTION.md",
    GOVERNANCE_DIR / "TAXONOMY_QUALITY_CHECKLIST.md",
]
GOVERNANCE_DOC_CHANGE_POLICY = GOVERNANCE_DIR / "TAXONOMY_CHANGE_POLICY.md"


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


def load_governance_context() -> str:
    """Construye contexto normativo dinámico desde docs/governance/."""
    blocks: list[str] = []

    for doc in GOVERNANCE_DOCS_MANDATORY:
        if not doc.exists():
            raise FileNotFoundError(f"No existe documento obligatorio de governance: {doc}")
        rel = doc.relative_to(REPO_ROOT)
        content = doc.read_text(encoding="utf-8").strip()
        blocks.append(f"=== {rel} (MANDATORY) ===\n{content}")

    if GOVERNANCE_DOC_CHANGE_POLICY.exists():
        rel = GOVERNANCE_DOC_CHANGE_POLICY.relative_to(REPO_ROOT)
        content = GOVERNANCE_DOC_CHANGE_POLICY.read_text(encoding="utf-8").strip()
        blocks.append(f"=== {rel} (CONDITIONAL) ===\n{content}")
    else:
        blocks.append(
            "=== docs/governance/TAXONOMY_CHANGE_POLICY.md (CONDITIONAL) ===\n"
            "Archivo no presente en este workspace."
        )

    applicability = """\
=== ALCANCE DE APLICACIÓN PARA CAPA 2 ===

Aplica únicamente reglas semánticas y estructurales de taxonomía para validar coherencia musical del árbol.
Ignora reglas operativas fuera de alcance de esta capa (por ejemplo: modos de ejecución,
batching, logging, continuidad de lotes, o detalles de pipeline de clasificación de canciones).

Precedencia obligatoria:
- Si hay conflicto interpretativo, prioriza SYSTEM_CONTRACT y GLOBAL_RULES.
- No inventar reglas fuera del corpus de governance cargado abajo.
"""

    return f"{applicability}\n\n" + "\n\n".join(blocks)


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


def check_layer1_prerequisite() -> tuple[bool, str]:
    """Verifica que Capa 1 haya terminado con decisión no FAIL."""
    if not LAYER1_REPORT.exists():
        return False, "No se encontró el reporte de Capa 1. Ejecutar validate_tree.py primero."
    try:
        data = json.loads(LAYER1_REPORT.read_text(encoding="utf-8"))
        decision = data.get("summary", {}).get("decision", "")
        if decision == "FAIL":
            return False, f"Capa 1 terminó en FAIL. Capa 2 bloqueada hasta resolver issues fatales."
        return True, decision
    except Exception as e:
        return False, f"No se pudo leer el reporte de Capa 1: {e}"


# ---------------------------------------------------------------------------
# Modo: --print-prompt
# ---------------------------------------------------------------------------

SYSTEM_CONTEXT = """\
Eres un experto en taxonomía de géneros musicales.
Tu rol es evaluar la coherencia, calidad musical y estructura semántica
de un árbol taxonómico de géneros musicales.

PRINCIPIOS OBLIGATORIOS:
- No proponer cambios automáticos al archivo maestro.
- No inventar reglas fuera del corpus de gobernanza proporcionado.
- No ocultar incertidumbre: reflejar confianza real en el campo confidence.
- La separación entre géneros Latin y no-Latin es obligatoria e inviolable.
- El árbol es controlado manualmente por el propietario del proyecto.
  El sistema solo puede sugerir; nunca modificar.
"""

CLONE_CONTEXT = """\
Glosario operativo mínimo para Capa 2:

Nodo clone:
- Nodo portal que referencia un nodo canónico.
- No tiene hijos ni contiene canciones.
- Existe para navegación y soporte de clasificación.

Nodo General:
- Nodo de respaldo para contenido válido del dominio del padre
    que no encaja en subgéneros más específicos.

Nodo Atomic:
- Nodo hoja que no debe subdividirse más sin perder coherencia musical.

Nodo Agrupador Estructural:
- Nodo padre usado principalmente para organización estructural
    y navegación taxonómica.
- No debe asumirse por defecto como género reproducible principal.
- Cuando existan hijos musicalmente distinguibles, la evaluación debe
    priorizar esos hijos por encima del padre.

Identificación operativa para esta validación:
- Si un nodo está marcado explícitamente como clone, trátalo como clone.
- Si el nombre del nodo contiene la palabra "clone", trátalo como clone.
- Si el nombre del nodo contiene el marcador "->", trátalo como clone.

Instrucción de evaluación:
- Cuando una regla indique excluir nodos clone, exclúyelos completamente del análisis.
- No reportes como conflicto semántico una mezcla Latin/no-Latin si la aparente mezcla ocurre solo por nodos clone.
"""


def build_prompt(taxonomy_text: str, governance_context: str, layer2_rules: list[dict[str, str]]) -> str:
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

    return f"""{SYSTEM_CONTEXT}
{CLONE_CONTEXT}
=== CONTEXTO NORMATIVO DINÁMICO ===

{governance_context}
=== REGLAS DE VALIDACIÓN A APLICAR ===

{rules_block}
=== ÁRBOL TAXONÓMICO A EVALUAR ===

{taxonomy_text}
=== INSTRUCCIÓN DE SALIDA ===

Responde ÚNICAMENTE con un JSON válido siguiendo el esquema a continuación.
No incluyas texto fuera del JSON. No incluyas markdown ni bloques de código.

Esquema obligatorio:
{output_schema}

Descarta explícitamente cualquier hallazgo con "result": "PASS".
No incluyas elementos con result PASS dentro del arreglo findings.
Si una regla no presenta hallazgos, no la incluyas en el arreglo findings.
Si no hay ningún hallazgo, devuelve findings como arreglo vacío [].
"""


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
    parser.add_argument(
        "--taxonomy-file",
        default=str(DEFAULT_TAXONOMY_PATH),
        help="Ruta al archivo maestro de taxonomía.",
    )
    parser.add_argument(
        "--skip-layer1-check",
        action="store_true",
        help="Omite la verificación de prerequisito de Capa 1.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    taxonomy_path = Path(args.taxonomy_file).resolve()
    if not taxonomy_path.exists():
        print(f"ERROR: no existe el archivo: {taxonomy_path}")
        return 2

    if not args.skip_layer1_check:
        ok, info = check_layer1_prerequisite()
        if not ok:
            print(f"BLOQUEADO: {info}")
            return 1
        print(f"Prerequisito Capa 1: {info}")

    try:
        layer2_rules = load_layer2_rules_from_governance()
    except (FileNotFoundError, ValueError) as e:
        print(f"ERROR: {e}")
        return 2

    valid_rule_ids = {r["rule_id"] for r in layer2_rules}

    if args.print_prompt:
        taxonomy_text = load_taxonomy_text(taxonomy_path)
        try:
            governance_context = load_governance_context()
        except FileNotFoundError as e:
            print(f"ERROR: {e}")
            return 2

        prompt = build_prompt(taxonomy_text, governance_context, layer2_rules)
        REPORTS_DIR.mkdir(parents=True, exist_ok=True)
        PROMPT_OUTPUT.write_text(prompt, encoding="utf-8")
        print(f"Prompt generado: {PROMPT_OUTPUT.relative_to(REPO_ROOT)}")
        print("Copia el contenido de ese archivo a un modelo de lenguaje externo.")
        print("Guarda la respuesta JSON y pásala con --apply-response <archivo.json>")
        return 0

    # Modo --apply-response
    response_path = Path(args.apply_response).resolve()
    if not response_path.exists():
        print(f"ERROR: no existe el archivo de respuesta: {response_path}")
        return 2

    try:
        response_data = json.loads(response_path.read_text(encoding="utf-8-sig"))
    except json.JSONDecodeError as e:
        print(f"ERROR: el archivo de respuesta no es JSON válido: {e}")
        return 2

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

    if schema_errors:
        print(f"ADVERTENCIA: {len(schema_errors)} errores de esquema en la respuesta IA.")
        for e in schema_errors:
            print(f"  - {e}")

    print(f"Decision: {decision}")
    print(f"FATAL: {fatal_count} | WARNING: {warning_count} | SUGGESTION: {suggestion_count}")
    print("Reportes: reports/validate_master_layer2_report.json, reports/validate_master_layer2_report.md")
    return 1 if decision == "FAIL" else 0


if __name__ == "__main__":
    raise SystemExit(main())
