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
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TAXONOMY_PATH = REPO_ROOT / "taxonomy" / "genre_tree_master.md"
REPORTS_DIR = REPO_ROOT / "reports"
LAYER1_REPORT = REPORTS_DIR / "validate_master_report.json"
PROMPT_OUTPUT = REPORTS_DIR / "validate_master_layer2_prompt.txt"


# ---------------------------------------------------------------------------
# Definición de reglas MVET-L2 (fuente de conocimiento: FB)
# ---------------------------------------------------------------------------

MVET_L2_RULES: list[dict] = [
    {
        "rule_id": "MVET-L2-001",
        "fb": "FB-05",
        "severity": "WARNING",
        "description": "Distinción musical entre géneros hermanos.",
        "check": (
            "Evalúa si los géneros que comparten el mismo padre son musicalmente "
            "distinguibles entre sí. Si dos hermanos producirían playlists "
            "indistinguibles, deben reportarse."
        ),
    },
    {
        "rule_id": "MVET-L2-002",
        "fb": "FB-05",
        "severity": "WARNING",
        "description": "Riesgos de cohesión de playlists por estructura.",
        "check": (
            "Identifica nodos donde la mezcla estilística potencial del contenido "
            "del nodo podría producir playlists inconsistentes."
        ),
    },
    {
        "rule_id": "MVET-L2-003",
        "fb": "FB-05",
        "severity": "WARNING",
        "description": "Redundancia entre nodos.",
        "check": (
            "Detecta parejas de géneros que representan estilos potencialmente "
            "equivalentes o solapados en el conjunto del árbol, excluyendo "
            "nodos clone."
        ),
    },
    {
        "rule_id": "MVET-L2-004",
        "fb": "FB-05",
        "severity": "WARNING",
        "description": "Sobre-fragmentación estructural.",
        "check": (
            "Detecta subramas donde el número de hijos es excesivo sin que "
            "exista valor musical claro para esa granularidad."
        ),
    },
    {
        "rule_id": "MVET-L2-005",
        "fb": "FB-05",
        "severity": "WARNING",
        "description": "Criterio atómico para límite de profundidad máxima.",
        "check": (
            "Evalúa nodos hoja donde subdividir más sería forzado o deterioraría "
            "la coherencia musical. Estos nodos deben considerarse atómicos."
        ),
    },
    {
        "rule_id": "MVET-L2-006",
        "fb": "FB-06",
        "severity": "WARNING",
        "description": "Candidatos de reubicación estructural.",
        "check": (
            "Propone con evidencia musical nodos que encajarían mejor "
            "bajo un padre diferente al actual."
        ),
    },
    {
        "rule_id": "MVET-L2-007",
        "fb": "FB-06",
        "severity": "WARNING",
        "description": "Candidatos de fusión de nodos hermanos.",
        "check": (
            "Identifica parejas de hermanos con solapamiento tan alto que "
            "la fusión mejoraría la coherencia del árbol."
        ),
    },
    {
        "rule_id": "MVET-L2-008",
        "fb": "FB-04",
        "severity": "FATAL",
        "description": "Violación semántica de separación Latin y no-Latin.",
        "check": (
            "Detecta cualquier evidencia de mezcla de géneros Latin y "
            "no-Latin que contraríe la separación de dominio obligatoria, "
            "excluyendo nodos clone."
        ),
    },
]

RULE_IDS = {r["rule_id"] for r in MVET_L2_RULES}
VALID_SEVERITIES = {"FATAL", "WARNING", "SUGGESTION"}
VALID_DECISIONS = {"PASS", "PASS_WITH_WARNINGS", "FAIL"}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def iso_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def load_taxonomy_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


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
=== CONTEXTO NORMATIVO Y OPERATIVO ===

Fuentes normativas MANDATORY para esta validación:
- docs/governance/GLOBAL_RULES.md
- docs/governance/SYSTEM_CONTRACT.md
- docs/governance/TAXONOMY_RULES.md
- docs/governance/TAXONOMY_DEPTH_POLICY.md
- docs/governance/TAXONOMY_NAMING_CONVENTION.md
- docs/governance/TAXONOMY_QUALITY_CHECKLIST.md

Fuente CONDITIONAL (solo cuando aplique escenario post-cambio/pre-release):
- docs/governance/TAXONOMY_CHANGE_POLICY.md

Precedencia y alcance:
- No inventar reglas fuera del corpus normativo.
- Si hay conflicto interpretativo, prioriza SYSTEM_CONTRACT y GLOBAL_RULES.
- Usa documentos referenciales solo como contexto, no como fuente de reglas nuevas.

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


def build_prompt(taxonomy_text: str) -> str:
    rules_block = "\n".join(
        f"  {r['rule_id']} [{r['fb']}] {r['severity']}\n"
        f"  Descripción: {r['description']}\n"
        f"  Check: {r['check']}\n"
        for r in MVET_L2_RULES
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
=== REGLAS DE VALIDACIÓN A APLICAR ===

{rules_block}
=== ÁRBOL TAXONÓMICO A EVALUAR ===

{taxonomy_text}
=== INSTRUCCIÓN DE SALIDA ===

Responde ÚNICAMENTE con un JSON válido siguiendo el esquema a continuación.
No incluyas texto fuera del JSON. No incluyas markdown ni bloques de código.

Esquema obligatorio:
{output_schema}

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


def validate_response_schema(data: dict) -> tuple[list[Layer2Finding], list[str]]:
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
        if rule_id not in RULE_IDS:
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

    rule_map = {r["rule_id"]: r for r in MVET_L2_RULES}
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

    if args.print_prompt:
        taxonomy_text = load_taxonomy_text(taxonomy_path)
        prompt = build_prompt(taxonomy_text)
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

    findings, schema_errors = validate_response_schema(response_data)
    fatal_count, warning_count, suggestion_count, decision = summarize_layer2(findings)
    ai_summary = response_data.get("summary", {})

    write_layer2_reports(
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
