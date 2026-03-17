from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


@dataclass
class CriteriaSyncResult:
    context_block: str
    missing_paths: list[str]
    orphan_paths: list[str]
    covered_count: int
    required_count: int


@dataclass
class _Node:
    name: str
    indent: int
    path: str


def _first_root_index(lines: list[str]) -> int:
    for i, raw in enumerate(lines):
        line = raw.strip()
        if not line:
            continue
        if line.startswith("#"):
            continue
        if line.endswith(".") or line.endswith(":"):
            continue
        if raw.startswith(" "):
            continue
        return i
    raise ValueError("No se encontro un nodo raiz candidato en el arbol.")


def taxonomy_paths_from_text(taxonomy_text: str) -> list[str]:
    lines = taxonomy_text.splitlines()
    start = _first_root_index(lines)

    stack: list[_Node] = []
    paths: list[str] = []

    for raw in lines[start:]:
        if not raw.strip():
            continue
        if raw.lstrip().startswith("#"):
            continue

        indent = len(raw) - len(raw.lstrip(" "))
        if "\t" in raw:
            raise ValueError("El arbol no permite tabulaciones.")
        if indent % 2 != 0:
            raise ValueError(
                f"Indentacion invalida ({indent} espacios, se esperan multiplos de 2)."
            )

        name = raw.strip()
        if not stack:
            if indent != 0:
                raise ValueError("El primer nodo del arbol debe tener indentacion 0.")
            node = _Node(name=name, indent=indent, path=name)
            stack.append(node)
            paths.append(node.path)
            continue

        if indent > stack[-1].indent + 2:
            raise ValueError("El arbol contiene un salto de nivel invalido.")

        while stack and indent <= stack[-1].indent:
            stack.pop()

        if indent != 0 and not stack:
            raise ValueError("Se detecto un nodo huerfano sin padre valido.")

        parent_path = stack[-1].path if stack else ""
        path = f"{parent_path} > {name}" if parent_path else name
        node = _Node(name=name, indent=indent, path=path)
        stack.append(node)
        paths.append(node.path)

    return paths


def load_node_criteria(criteria_path: Path) -> dict[str, dict[str, object]]:
    if not criteria_path.exists():
        raise FileNotFoundError(f"No existe archivo de criterios por nodo: {criteria_path}")

    try:
        payload = json.loads(criteria_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        raise ValueError(f"Archivo de criterios por nodo invalido: {e}") from e

    if not isinstance(payload, dict):
        raise ValueError("El archivo de criterios debe ser un objeto JSON.")

    nodes = payload.get("nodes")
    if not isinstance(nodes, list):
        raise ValueError("El archivo de criterios debe incluir un arreglo 'nodes'.")

    criteria_by_path: dict[str, dict[str, object]] = {}
    for i, item in enumerate(nodes):
        if not isinstance(item, dict):
            raise ValueError(f"nodes[{i}] debe ser un objeto.")

        node_path = str(item.get("node_path", "")).strip()
        membership = str(item.get("membership_criteria", "")).strip()
        exclusion = str(item.get("exclusion_criteria", "")).strip()
        examples = item.get("reference_examples", [])

        if not node_path:
            raise ValueError(f"nodes[{i}].node_path es obligatorio.")
        if not membership:
            raise ValueError(f"nodes[{i}].membership_criteria es obligatorio.")
        if not exclusion:
            raise ValueError(f"nodes[{i}].exclusion_criteria es obligatorio.")
        if not isinstance(examples, list) or not all(isinstance(x, str) for x in examples):
            raise ValueError(f"nodes[{i}].reference_examples debe ser arreglo de strings.")
        if node_path in criteria_by_path:
            raise ValueError(f"node_path duplicado en criterios: {node_path}")

        criteria_by_path[node_path] = {
            "membership_criteria": membership,
            "exclusion_criteria": exclusion,
            "reference_examples": examples,
        }

    return criteria_by_path


def build_criteria_sync(
    taxonomy_text: str,
    criteria_by_path: dict[str, dict[str, object]],
) -> CriteriaSyncResult:
    paths = taxonomy_paths_from_text(taxonomy_text)
    required_paths = [p for p in paths if " > " in p]

    missing = sorted(path for path in required_paths if path not in criteria_by_path)
    orphan = sorted(path for path in criteria_by_path if path not in set(paths))

    lines: list[str] = [
        "Aplica estos criterios para decidir inserciones y validar coherencia semantica.",
        "Si una recomendacion contradice estos criterios, prioriza estos criterios sincronizados.",
        "",
    ]

    for path in paths:
        if path not in criteria_by_path:
            continue
        data = criteria_by_path[path]
        examples = data["reference_examples"]
        examples_text = ", ".join(examples) if examples else "Sin ejemplos de referencia"
        lines.extend(
            [
                f"- Node: {path}",
                f"  Membership: {data['membership_criteria']}",
                f"  Exclusion: {data['exclusion_criteria']}",
                f"  Examples: {examples_text}",
            ]
        )

    lines.extend(
        [
            "",
            f"Cobertura criterios: {len(required_paths) - len(missing)}/{len(required_paths)} nodos no-raiz.",
        ]
    )
    if missing:
        lines.append("FALTANTES: " + "; ".join(missing))
    if orphan:
        lines.append("HUERFANOS: " + "; ".join(orphan))

    return CriteriaSyncResult(
        context_block="\n".join(lines).strip(),
        missing_paths=missing,
        orphan_paths=orphan,
        covered_count=len(required_paths) - len(missing),
        required_count=len(required_paths),
    )


def build_missing_criteria_stub(missing_paths: list[str]) -> dict[str, object]:
    return {
        "version": "1.0",
        "generated_for": "missing-node-criteria",
        "nodes": [
            {
                "node_path": path,
                "membership_criteria": "TODO: definir criterio de pertenencia para este nodo.",
                "exclusion_criteria": "TODO: definir criterio de exclusion para este nodo.",
                "reference_examples": [
                    "TODO: ejemplo 1",
                    "TODO: ejemplo 2",
                ],
            }
            for path in missing_paths
        ],
    }
