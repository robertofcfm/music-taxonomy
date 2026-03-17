"""Valida que el prompt bootstrap cumpla reglas mínimas de gobernanza.

Objetivo:
- Evitar deriva del prompt base entre sesiones.
- Forzar la regla de faltantes base (NADA).
- Mantener GLOBAL_RULES y SYSTEM_CONTRACT como REFERENTIAL por defecto.
- Garantizar instrucción del indicador de capacidad (🟢/🟡/🔴).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PROMPT_PATH = REPO_ROOT / "prompts" / "prompt_bootstrap_generador_prompts.md"

REQUIRED_BASE_FILES = [
    "docs/context/CONTEXT_REGISTRY.md",
    "docs/governance/RULES_REGISTRY.md",
]

CONDITIONAL_FILES = [
    "docs/context/AI_PROMPT_SYSTEM_CONTEXT.md",
    "docs/governance/AI_PROMPT_SYSTEM_RULES.md",
]

REFERENTIAL_FILES = [
    "docs/governance/GLOBAL_RULES.md",
    "docs/governance/SYSTEM_CONTRACT.md",
]


@dataclass
class CheckResult:
    name: str
    passed: bool
    detail: str


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip().lower())


def has_all_fragments(text: str, fragments: list[str]) -> bool:
    normalized = normalize(text)
    return all(normalize(fragment) in normalized for fragment in fragments)


def existing_paths(paths: list[str]) -> list[str]:
    return [p for p in paths if (REPO_ROOT / p).exists()]


def missing_paths(paths: list[str]) -> list[str]:
    return [p for p in paths if not (REPO_ROOT / p).exists()]


def validate(prompt_path: Path) -> tuple[list[CheckResult], dict[str, list[str]]]:
    prompt_text = prompt_path.read_text(encoding="utf-8")
    checks: list[CheckResult] = []

    # Recomendación 1: GLOBAL_RULES + SYSTEM_CONTRACT referenciales por defecto.
    checks.append(
        CheckResult(
            name="referential_default_policy",
            passed=has_all_fragments(
                prompt_text,
                [
                    "por defecto en tareas de prompting",
                    "global_rules",
                    "system_contract",
                    "referential",
                ],
            ),
            detail=(
                "Debe explicitar que GLOBAL_RULES y SYSTEM_CONTRACT son REFERENTIAL por defecto."
            ),
        )
    )

    # Recomendación 2: regla dura de faltantes base -> devolver NADA.
    checks.append(
        CheckResult(
            name="hard_missing_base_rule",
            passed=has_all_fragments(
                prompt_text,
                [
                    "regla dura de faltantes base",
                    "docs/context/context_registry.md",
                    "docs/governance/rules_registry.md",
                    "devolver \"nada\"",
                    "sin excepción",
                ],
            ),
            detail=(
                "Debe forzar NADA cuando falte CONTEXT_REGISTRY o RULES_REGISTRY."
            ),
        )
    )

    # Recomendación 3: estandarización del prompt de arranque + indicador.
    checks.append(
        CheckResult(
            name="capacity_status_instruction",
            passed=has_all_fragments(
                prompt_text,
                [
                    "indicador de estado de capacidad",
                    "🟢/🟡/🔴",
                    "al final de cada respuesta",
                ],
            ),
            detail=(
                "Debe incluir instrucción explícita de reportar estado 🟢/🟡/🔴 en cada respuesta."
            ),
        )
    )

    checks.append(
        CheckResult(
            name="startup_question",
            passed="¿Cuál es el objetivo específico de este prompt?" in prompt_text,
            detail=(
                "Debe incluir la pregunta de arranque al cierre cuando el contexto mínimo esté cubierto."
            ),
        )
    )

    imports = {
        "MANDATORY": existing_paths(REQUIRED_BASE_FILES),
        "CONDITIONAL": existing_paths(CONDITIONAL_FILES),
        "REFERENTIAL": existing_paths(REFERENTIAL_FILES),
        "EXCLUDED": [],
        "MISSING_BASE": missing_paths(REQUIRED_BASE_FILES),
    }

    return checks, imports


def print_markdown_report(prompt_path: Path, checks: list[CheckResult], imports: dict[str, list[str]]) -> int:
    print("[DIAGNOSTICO_IMPORTS]")
    print(f"- MANDATORY: {', '.join(imports['MANDATORY']) or '(vacio)'}")
    print(f"- CONDITIONAL: {', '.join(imports['CONDITIONAL']) or '(vacio)'}")
    print(f"- REFERENTIAL: {', '.join(imports['REFERENTIAL']) or '(vacio)'}")
    print(f"- EXCLUDED: {', '.join(imports['EXCLUDED']) or '(vacio)'}")
    coverage = "insuficiente" if imports["MISSING_BASE"] else "suficiente"
    print(f"- Cobertura: {coverage}")

    print("\n[VALIDACION_POLITICAS]")
    for c in checks:
        status = "OK" if c.passed else "FAIL"
        print(f"- {c.name}: {status} | {c.detail}")

    failed_checks = [c for c in checks if not c.passed]
    if imports["MISSING_BASE"]:
        print("\n[PROMPT_FINAL_STANDALONE]")
        print("NADA")
        print("\n[FALTANTES_SI_APLICA]")
        for path in imports["MISSING_BASE"]:
            print(f"- {path}")
        return 1

    if failed_checks:
        print("\n[PROMPT_FINAL_STANDALONE]")
        print("NADA")
        print("\n[FALTANTES_SI_APLICA]")
        for check in failed_checks:
            print(f"- Ajustar politica: {check.name}")
        return 1

    print("\n[PROMPT_FINAL_STANDALONE]")
    print(
        "VALIDO: el bootstrap cumple politicas base. "
        "Puedes usar este archivo como prompt generador de arranque."
    )
    print("\n[FALTANTES_SI_APLICA]")
    print("- vacio")
    print("\nArchivo validado:")
    print(f"- {prompt_path}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Valida politicas obligatorias del prompt bootstrap generador."
    )
    parser.add_argument(
        "--prompt",
        default=str(DEFAULT_PROMPT_PATH),
        help="Ruta del prompt bootstrap a validar.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emite salida JSON en lugar de formato markdown.",
    )
    args = parser.parse_args()

    prompt_path = Path(args.prompt)
    if not prompt_path.exists():
        print(f"ERROR: no existe el prompt: {prompt_path}")
        return 2

    checks, imports = validate(prompt_path)
    failed_checks = [c for c in checks if not c.passed]
    exit_code = 1 if failed_checks or imports["MISSING_BASE"] else 0

    if args.json:
        payload = {
            "prompt": str(prompt_path),
            "imports": imports,
            "checks": [c.__dict__ for c in checks],
            "exit_code": exit_code,
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return exit_code

    return print_markdown_report(prompt_path, checks, imports)


if __name__ == "__main__":
    sys.exit(main())
