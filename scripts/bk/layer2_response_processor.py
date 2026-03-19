from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from layer2_contract import (
    RESPONSE_LAYER,
    VALID_DECISIONS,
    VALID_RESULTS,
    VALID_SEVERITIES,
    compute_decision,
)


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


def iso_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def validate_response_schema(
    data: dict, valid_rule_ids: set[str]
) -> tuple[list[Layer2Finding], list[str]]:
    errors: list[str] = []
    findings: list[Layer2Finding] = []

    if not isinstance(data, dict):
        return findings, ["La respuesta IA debe ser un objeto JSON."]

    if data.get("layer") != RESPONSE_LAYER:
        errors.append(f"Campo 'layer' inválido: '{data.get('layer')}'.")

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
        if result == "PASS":
            item_errors.append(f"{prefix}: result PASS no permitido en findings.")
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
        for field in ("total_fatal", "total_warning", "total_suggestion"):
            value = summary.get(field)
            if not isinstance(value, int) or value < 0:
                errors.append(f"summary.{field} inválido: '{value}'.")

    return findings, errors


def validate_ai_summary(
    ai_summary: dict,
    fatal_count: int,
    warning_count: int,
    suggestion_count: int,
    decision: str,
) -> list[str]:
    if not isinstance(ai_summary, dict):
        return []

    errors: list[str] = []
    expected_values = {
        "total_fatal": fatal_count,
        "total_warning": warning_count,
        "total_suggestion": suggestion_count,
        "decision_recommendation": decision,
    }

    for field, expected in expected_values.items():
        observed = ai_summary.get(field)
        if observed != expected:
            errors.append(
                f"summary.{field} inconsistente: esperado '{expected}', recibido '{observed}'."
            )

    return errors


def summarize_layer2(findings: list[Layer2Finding]) -> tuple[int, int, int, str]:
    fatals = sum(1 for f in findings if f.severity == "FATAL" and f.schema_valid)
    warnings = sum(1 for f in findings if f.severity == "WARNING" and f.schema_valid)
    suggestions = sum(1 for f in findings if f.severity == "SUGGESTION" and f.schema_valid)
    decision = compute_decision(fatals, warnings, suggestions)
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
    reports_dir: Path,
) -> None:
    reports_dir.mkdir(parents=True, exist_ok=True)
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

    report_json = reports_dir / "validate_master_layer2_report.json"
    report_md = reports_dir / "validate_master_layer2_report.md"

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
    reports_dir: Path,
) -> tuple[list[Layer2Finding], list[str], dict, int, int, int, str]:
    findings, schema_errors = validate_response_schema(response_data, valid_rule_ids)
    findings = [f for f in findings if f.result != "PASS"]
    fatal_count, warning_count, suggestion_count, decision = summarize_layer2(findings)
    ai_summary = response_data.get("summary", {})
    schema_errors.extend(
        validate_ai_summary(
            ai_summary,
            fatal_count,
            warning_count,
            suggestion_count,
            decision,
        )
    )

    write_layer2_reports(
        layer2_rules=layer2_rules,
        findings=findings,
        schema_errors=schema_errors,
        ai_summary=ai_summary,
        decision=decision,
        fatal_count=fatal_count,
        warning_count=warning_count,
        suggestion_count=suggestion_count,
        reports_dir=reports_dir,
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
