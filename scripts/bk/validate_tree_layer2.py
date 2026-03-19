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
import sys
from pathlib import Path

from layer2_governance_loader import (
    load_governance_context,
    load_layer2_rules_from_governance,
    load_prompt_context,
    load_prompt_template,
)
from layer2_prompt_builder import build_prompt
from layer2_response_processor import (
    load_response_json,
    process_layer2_response,
)
from taxonomy_criteria_sync import (
    build_criteria_sync,
    build_missing_criteria_stub,
    load_node_criteria,
)


REPO_ROOT = Path(__file__).resolve().parents[1]
GOVERNANCE_DIR = REPO_ROOT / "docs" / "governance"
DEFAULT_TAXONOMY_PATH = REPO_ROOT / "taxonomy" / "genre_tree_master.md"
DEFAULT_CRITERIA_PATH = REPO_ROOT / "taxonomy" / "genre_tree_node_criteria.json"
PROMPTS_DIR = REPO_ROOT / "prompts"
PROMPT_TEMPLATE = PROMPTS_DIR / "generadores" / "validate_master_layer2_prompt_template.md"
PROMPT_CONTEXT = PROMPTS_DIR / "generadores" / "validate_master_layer2_prompt_context.json"
VALIDATE_MASTER_STRATEGY = REPO_ROOT / "docs" / "operations" / "VALIDATE_MASTER_STRATEGY.md"
REPORTS_DIR = REPO_ROOT / "reports"
PROMPT_OUTPUT = PROMPTS_DIR / "validate_master_layer2_prompt.txt"
DEFAULT_CYCLE_RESPONSE_BASENAME = "validate_master_layer2_response"
DEFAULT_MISSING_CRITERIA_OUTPUT = REPORTS_DIR / "genre_tree_node_criteria.missing.json"


def load_taxonomy_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def is_response_stale(response_path: Path, taxonomy_path: Path) -> bool:
    """Return True when a response is older than taxonomy source file."""
    return response_path.stat().st_mtime < taxonomy_path.stat().st_mtime


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validación semántica (Capa 2) — taxonomy/genre_tree_master.md."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--print-prompt",
        action="store_true",
        help="Genera el prompt para la IA y lo guarda en prompts/.",
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
        "--criteria-file",
        default=str(DEFAULT_CRITERIA_PATH),
        help="Ruta al JSON de criterios por nodo sincronizados.",
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
    parser.add_argument(
        "--missing-criteria-output",
        default=str(DEFAULT_MISSING_CRITERIA_OUTPUT),
        help=(
            "Ruta de salida para plantilla JSON de nodos sin criterio. "
            "Se genera automaticamente si hay faltantes."
        ),
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    taxonomy_path = Path(args.taxonomy_file).resolve()
    if not taxonomy_path.exists():
        print(f"ERROR: no existe el archivo: {taxonomy_path}")
        return 2

    criteria_path = Path(args.criteria_file).resolve()
    missing_criteria_output = Path(args.missing_criteria_output).resolve()

    try:
        layer2_rules = load_layer2_rules_from_governance(GOVERNANCE_DIR)
    except (FileNotFoundError, ValueError) as e:
        print(f"ERROR: {e}")
        return 2

    try:
        taxonomy_text = load_taxonomy_text(taxonomy_path)
        criteria_by_path = load_node_criteria(criteria_path)
        criteria_sync = build_criteria_sync(taxonomy_text, criteria_by_path)
    except (FileNotFoundError, ValueError) as e:
        print(f"ERROR: {e}")
        return 2

    if criteria_sync.missing_paths:
        missing_criteria_output.parent.mkdir(parents=True, exist_ok=True)
        missing_payload = build_missing_criteria_stub(criteria_sync.missing_paths)
        missing_criteria_output.write_text(
            json.dumps(missing_payload, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

        print("ERROR: faltan criterios para nodos del árbol maestro.")
        for path in criteria_sync.missing_paths:
            print(f"  - {path}")
        print(f"Actualiza: {criteria_path}")
        print(f"Plantilla generada: {missing_criteria_output}")
        return 2

    if missing_criteria_output.exists():
        missing_criteria_output.unlink()

    if criteria_sync.orphan_paths:
        print("ADVERTENCIA: hay criterios huérfanos que no existen en el árbol actual.")
        for path in criteria_sync.orphan_paths:
            print(f"  - {path}")

    valid_rule_ids = {r["rule_id"] for r in layer2_rules}

    if args.print_prompt:
        try:
            prompt_context = load_prompt_context(PROMPT_CONTEXT)
            prompt_template = load_prompt_template(PROMPT_TEMPLATE)
            governance_context = load_governance_context(
                VALIDATE_MASTER_STRATEGY, REPO_ROOT, prompt_context
            )
        except (FileNotFoundError, ValueError) as e:
            print(f"ERROR: {e}")
            return 2

        prompt = build_prompt(
            taxonomy_text,
            governance_context,
            layer2_rules,
            prompt_template,
            prompt_context,
            node_criteria_context=criteria_sync.context_block,
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

        if is_response_stale(response_path, taxonomy_path):
            print(
                "ERROR: la respuesta IA está desactualizada respecto al árbol activo."
            )
            print(f"  - Taxonomía activa: {taxonomy_path}")
            print(f"  - Respuesta desactualizada: {response_path}")
            print("Regenera prompt y respuesta con el árbol actual antes de aplicar.")
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
        ) = process_layer2_response(response_data, layer2_rules, valid_rule_ids, REPORTS_DIR)

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

    def expected_cycle_response_path(iteration: int) -> Path:
        if iteration == 1:
            return response_dir / f"{base_name}.json"
        return response_dir / f"{base_name}.iter{iteration}.json"

    for iteration in range(1, args.max_iterations + 1):
        response_path = expected_cycle_response_path(iteration)
        if not response_path.exists():
            if iteration == 1:
                print(f"ERROR: no existe archivo de iteración 1: {response_path}")
                return 2

            print(
                "PENDIENTE: no se encontró la siguiente respuesta para continuar ciclo: "
                f"{response_path.name}"
            )
            return 1

        if is_response_stale(response_path, taxonomy_path):
            print(
                "ERROR: respuesta de ciclo desactualizada respecto al árbol activo."
            )
            print(f"  - Iteración: {iteration}")
            print(f"  - Taxonomía activa: {taxonomy_path}")
            print(f"  - Respuesta desactualizada: {response_path}")
            print("Regenera prompt y respuesta con el árbol actual antes de continuar ciclo.")
            return 2

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
        ) = process_layer2_response(response_data, layer2_rules, valid_rule_ids, REPORTS_DIR)

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
