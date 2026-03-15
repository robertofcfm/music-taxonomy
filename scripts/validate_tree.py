"""Validación determinista (Capa 1) de taxonomy/genre_tree_master.md.

Salida mínima:
- reports/validate_master_report.json
- reports/validate_master_report.md
- reports/validate_master_run_metadata.json
"""

from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TAXONOMY_PATH = REPO_ROOT / "taxonomy" / "genre_tree_master.md"
REPORTS_DIR = REPO_ROOT / "reports"


# Fuentes de conocimiento por bloque funcional (FB).
FB_SOURCES: dict[str, list[str]] = {
	"FB-01": [
		"docs/governance/SYSTEM_CONTRACT.md",
		"docs/governance/TAXONOMY_RULES.md",
	],
	"FB-02": [
		"docs/governance/TAXONOMY_NAMING_CONVENTION.md",
	],
	"FB-03": [
		"docs/governance/TAXONOMY_DEPTH_POLICY.md",
		"docs/governance/TAXONOMY_RULES.md",
	],
	"FB-04": [
		"docs/governance/GLOBAL_RULES.md",
		"docs/governance/SYSTEM_CONTRACT.md",
	],
	"FB-05": [
		"docs/governance/TAXONOMY_QUALITY_CHECKLIST.md",
		"docs/governance/TAXONOMY_RULES.md",
	],
	"FB-06": [
		"docs/governance/TAXONOMY_CHANGE_POLICY.md",
		"docs/governance/TAXONOMY_QUALITY_CHECKLIST.md",
	],
}


AMBIGUOUS_TERMS = {
	"latin style",
	"mixed music",
	"various genres",
	"latin rhythms",
	"latin music",
	"world music",
	"misc",
	"fusion style",
	"misc genres",
}


@dataclass
class TaxonomyNode:
	name: str
	indent: int
	line_no: int
	parent: TaxonomyNode | None = None
	children: list[TaxonomyNode] = field(default_factory=list)

	@property
	def depth(self) -> int:
		depth = 1
		node = self.parent
		while node is not None:
			depth += 1
			node = node.parent
		return depth

	@property
	def path(self) -> str:
		names: list[str] = []
		node: TaxonomyNode | None = self
		while node is not None:
			names.append(node.name)
			node = node.parent
		names.reverse()
		return " > ".join(names)


@dataclass
class Finding:
	rule_id: str
	fb: str
	severity: str
	passed: bool
	description: str
	evidence: str
	causes: list[str] = field(default_factory=list)


def iso_now() -> str:
	return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def file_sha256(path: Path) -> str:
	h = hashlib.sha256()
	with path.open("rb") as f:
		for chunk in iter(lambda: f.read(8192), b""):
			h.update(chunk)
	return h.hexdigest()


def load_lines(path: Path) -> list[str]:
	return path.read_text(encoding="utf-8").splitlines()


def first_root_index(lines: list[str]) -> int:
	for i, raw in enumerate(lines):
		line = raw.strip()
		if not line:
			continue
		if line.startswith("#"):
			continue
		# Ignora líneas descriptivas hasta encontrar la raíz editable.
		if line.endswith(".") or line.endswith(":"):
			continue
		if raw.startswith(" "):
			continue
		return i
	raise ValueError("No se encontró un nodo raíz candidato en el archivo maestro.")


def parse_tree(lines: list[str]) -> tuple[list[TaxonomyNode], list[str]]:
	errors: list[str] = []
	nodes: list[TaxonomyNode] = []
	stack: list[TaxonomyNode] = []

	start = first_root_index(lines)
	for line_no, raw in enumerate(lines[start:], start=start + 1):
		if not raw.strip():
			continue
		if raw.lstrip().startswith("#"):
			continue

		indent = len(raw) - len(raw.lstrip(" "))
		if "\t" in raw:
			errors.append(f"Línea {line_no}: no se permiten tabulaciones.")
			continue
		if indent % 2 != 0:
			errors.append(
				f"Línea {line_no}: indentación inválida ({indent} espacios, se esperan múltiplos de 2)."
			)
			continue

		name = raw.strip()
		node = TaxonomyNode(name=name, indent=indent, line_no=line_no)

		if not stack:
			if indent != 0:
				errors.append(f"Línea {line_no}: el primer nodo debe tener indentación 0.")
				continue
			nodes.append(node)
			stack.append(node)
			continue

		if indent > stack[-1].indent + 2:
			errors.append(
				f"Línea {line_no}: salto de nivel inválido (de {stack[-1].indent} a {indent})."
			)
			continue

		while stack and indent <= stack[-1].indent:
			stack.pop()

		if indent != 0 and not stack:
			errors.append(f"Línea {line_no}: nodo huérfano sin padre válido.")
			continue

		if stack:
			parent = stack[-1]
			node.parent = parent
			parent.children.append(node)

		nodes.append(node)
		stack.append(node)

	return nodes, errors


def is_title_case_name(name: str) -> bool:
	def valid_word(word: str) -> bool:
		if not any(ch.isalpha() for ch in word):
			return True
		first_alpha = next((ch for ch in word if ch.isalpha()), None)
		return bool(first_alpha and first_alpha.isupper())

	sanitized = (
		name.replace("(", " ")
		.replace(")", " ")
		.replace("/", " ")
		.replace("&", " ")
		.replace("-", " ")
	)
	words = [w for w in sanitized.split() if w]
	return all(valid_word(w) for w in words)


def likely_clone(name: str) -> bool:
	lowered = name.lower()
	return " clone" in lowered or "clone " in lowered or "->" in name


def collect_name_counts(nodes: Iterable[TaxonomyNode]) -> dict[str, int]:
	counts: dict[str, int] = {}
	for n in nodes:
		counts[n.name] = counts.get(n.name, 0) + 1
	return counts


def run_layer1_checks(
	taxonomy_path: Path,
	before_hash: str,
	after_hash: str,
	nodes: list[TaxonomyNode],
	parser_errors: list[str],
) -> list[Finding]:
	findings: list[Finding] = []

	roots = [n for n in nodes if n.parent is None]
	name_counts = collect_name_counts(nodes)
	latin_nodes = [n for n in nodes if n.name == "Latin"]

	# MVET-L1-001
	findings.append(
		Finding(
			rule_id="MVET-L1-001",
			fb="FB-01",
			severity="FATAL",
			passed=len(roots) == 1,
			description="Debe existir un nodo raíz único.",
			evidence=f"Raíces detectadas: {len(roots)}",
			causes=[] if len(roots) == 1 else [f"Raíces detectadas: {', '.join(n.name for n in roots)}"],
		)
	)

	# MVET-L1-002
	findings.append(
		Finding(
			rule_id="MVET-L1-002",
			fb="FB-01",
			severity="FATAL",
			passed=len(parser_errors) == 0,
			description="Jerarquía válida por indentación.",
			evidence="Sin errores de parser" if not parser_errors else " | ".join(parser_errors),
			causes=[] if not parser_errors else parser_errors,
		)
	)

	# MVET-L1-003
	duplicate_names = [name for name, count in name_counts.items() if count > 1]
	non_clone_duplicates = [name for name in duplicate_names if not likely_clone(name)]
	findings.append(
		Finding(
			rule_id="MVET-L1-003",
			fb="FB-02",
			severity="FATAL",
			passed=len(non_clone_duplicates) == 0,
			description="Nombres de género únicos (excepto clone permitido).",
			evidence=(
				"Sin duplicados inválidos"
				if not non_clone_duplicates
				else f"Duplicados inválidos: {', '.join(sorted(non_clone_duplicates))}"
			),
			causes=[] if not non_clone_duplicates else [f"Nombre duplicado: {name}" for name in sorted(non_clone_duplicates)],
		)
	)

	# MVET-L1-004
	invalid_case = [n for n in nodes if not is_title_case_name(n.name)]
	bad_general_suffix = [n for n in nodes if "general" in n.name.lower() and not n.name.endswith("(General)")]
	findings.append(
		Finding(
			rule_id="MVET-L1-004",
			fb="FB-02",
			severity="FATAL",
			passed=(len(invalid_case) == 0 and len(bad_general_suffix) == 0),
			description="Formato de nombrado válido (Title Case y patrón General).",
			evidence=(
				"Formato válido"
				if not invalid_case and not bad_general_suffix
				else (
					f"No Title Case: {', '.join(f'{n.name} (L{n.line_no})' for n in invalid_case[:8])}; "
					f"General inválido: {', '.join(f'{n.name} (L{n.line_no})' for n in bad_general_suffix[:8])}"
				)
			),
			causes=(
				[f"No Title Case: {n.name} (L{n.line_no})" for n in invalid_case]
				+ [f"General inválido: {n.name} (L{n.line_no})" for n in bad_general_suffix]
			),
		)
	)

	# MVET-L1-005
	invalid_general_parent: list[str] = []
	for n in nodes:
		if not n.name.endswith("(General)"):
			continue
		base = n.name[: -len("(General)")].strip()
		if n.parent is None or n.parent.name != base:
			invalid_general_parent.append(f"{n.name} (L{n.line_no})")
	findings.append(
		Finding(
			rule_id="MVET-L1-005",
			fb="FB-01",
			severity="FATAL",
			passed=len(invalid_general_parent) == 0,
			description="Nodos General explícitos y bajo su padre correspondiente.",
			evidence=(
				"Nodos General válidos"
				if not invalid_general_parent
				else f"Ubicación inválida de General: {', '.join(invalid_general_parent)}"
			),
			causes=invalid_general_parent,
		)
	)

	# MVET-L1-006
	clone_with_children = [
		f"{n.name} (L{n.line_no})"
		for n in nodes
		if likely_clone(n.name) and n.children
	]
	findings.append(
		Finding(
			rule_id="MVET-L1-006",
			fb="FB-01",
			severity="FATAL",
			passed=len(clone_with_children) == 0,
			description="Restricciones de nodo clone (sin hijos).",
			evidence=(
				"Sin clones con hijos"
				if not clone_with_children
				else f"Clones con hijos: {', '.join(clone_with_children)}"
			),
			causes=clone_with_children,
		)
	)

	# MVET-L1-007
	leaf_nodes = [n for n in nodes if not n.children]
	leaf_depths = [n.depth for n in leaf_nodes]
	max_leaf_depth = max(leaf_depths) if leaf_depths else 0
	# Nueva regla: mínimo de profundidad = 3. Sin máximo numérico fijo;
	# la profundidad alta se considera válida si responde a granularidad atómica.
	depth_warning = max_leaf_depth < 3
	shallow_leaf_paths = [f"{n.path} (L{n.line_no}, depth={n.depth})" for n in leaf_nodes if n.depth < 3]
	findings.append(
		Finding(
			rule_id="MVET-L1-007",
			fb="FB-03",
			severity="WARNING",
			passed=not depth_warning,
			description="Profundidad mínima estructural >= 3; sin máximo numérico fijo.",
			evidence=(
				f"Max leaf depth: {max_leaf_depth}. "
				"La profundidad máxima se justifica por criterio de nodo atómico."
			),
			causes=shallow_leaf_paths if depth_warning else [],
		)
	)

	# MVET-L1-008
	findings.append(
		Finding(
			rule_id="MVET-L1-008",
			fb="FB-04",
			severity="FATAL",
			passed=before_hash == after_hash,
			description="Inmutabilidad del archivo maestro.",
			evidence=(
				"Hash estable durante la ejecución"
				if before_hash == after_hash
				else "El hash cambió durante la validación"
			),
			causes=[] if before_hash == after_hash else ["SHA256 before != SHA256 after"],
		)
	)

	# MVET-L1-009
	ambiguous_hits: list[str] = []
	for n in nodes:
		lowered = n.name.lower().strip()
		if lowered in AMBIGUOUS_TERMS:
			ambiguous_hits.append(f"{n.name} (L{n.line_no})")
	findings.append(
		Finding(
			rule_id="MVET-L1-009",
			fb="FB-02",
			severity="FATAL",
			passed=len(ambiguous_hits) == 0,
			description="Términos ambiguos prohibidos.",
			evidence=(
				"Sin términos ambiguos"
				if not ambiguous_hits
				else f"Términos ambiguos detectados: {', '.join(ambiguous_hits)}"
			),
			causes=ambiguous_hits,
		)
	)

	# MVET-L1-010
	latin_ok = len(latin_nodes) == 1 and latin_nodes[0].parent is not None and latin_nodes[0].parent.name == "Music"
	findings.append(
		Finding(
			rule_id="MVET-L1-010",
			fb="FB-04",
			severity="FATAL",
			passed=latin_ok,
			description="Separación de dominio Latin en estructura base.",
			evidence=(
				"Rama Latin válida bajo Music"
				if latin_ok
				else "Debe existir exactamente un nodo Latin directo bajo Music"
			),
			causes=[] if latin_ok else ["Nodo Latin ausente o mal ubicado (debe ser hijo directo de Music)"],
		)
	)

	return findings


def summarize(findings: list[Finding]) -> tuple[int, int, str]:
	fatals = [f for f in findings if f.severity == "FATAL" and not f.passed]
	warnings = [f for f in findings if f.severity == "WARNING" and not f.passed]

	if fatals:
		decision = "FAIL"
	elif warnings:
		decision = "PASS_WITH_WARNINGS"
	else:
		decision = "PASS"

	return len(fatals), len(warnings), decision


def write_reports(
	taxonomy_path: Path,
	taxonomy_sha256: str,
	findings: list[Finding],
	decision: str,
	fatal_count: int,
	warning_count: int,
) -> None:
	REPORTS_DIR.mkdir(parents=True, exist_ok=True)

	timestamp = iso_now()
	report_json_path = REPORTS_DIR / "validate_master_report.json"
	report_md_path = REPORTS_DIR / "validate_master_report.md"
	run_meta_path = REPORTS_DIR / "validate_master_run_metadata.json"

	payload = {
		"process": "MVET-LAYER1",
		"generated_at": timestamp,
		"taxonomy_file": str(taxonomy_path.relative_to(REPO_ROOT)).replace("\\", "/"),
		"taxonomy_sha256": taxonomy_sha256,
		"applied_sources_by_fb": FB_SOURCES,
		"summary": {
			"decision": decision,
			"total_fatal": fatal_count,
			"total_warning": warning_count,
			"total_checks": len(findings),
		},
		"findings": [
			{
				"rule_id": f.rule_id,
				"fb": f.fb,
				"severity": f.severity,
				"passed": f.passed,
				"description": f.description,
				"evidence": f.evidence,
				"causes": f.causes,
				"sources": FB_SOURCES.get(f.fb, []),
			}
			for f in findings
		],
	}
	report_json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

	md_lines = [
		"# Reporte de Validación MVET (Capa 1)",
		"",
		f"- Fecha: {timestamp}",
		f"- Archivo: {payload['taxonomy_file']}",
		f"- SHA256: {taxonomy_sha256}",
		f"- Decisión: {decision}",
		f"- FATAL: {fatal_count}",
		f"- WARNING: {warning_count}",
		"",
		"## Hallazgos",
		"",
	]
	for f in findings:
		status = "PASS" if f.passed else "FAIL"
		md_lines.extend(
			[
				f"### {f.rule_id} [{f.fb}] - {f.severity} - {status}",
				f"- Descripción: {f.description}",
				f"- Evidencia: {f.evidence}",
				f"- Causantes: {'; '.join(f.causes) if f.causes else 'N/A'}",
				f"- Fuentes: {', '.join(FB_SOURCES.get(f.fb, []))}",
				"",
			]
		)
	report_md_path.write_text("\n".join(md_lines), encoding="utf-8")

	metadata = {
		"process": "MVET-LAYER1",
		"generated_at": timestamp,
		"report_json": str(report_json_path.relative_to(REPO_ROOT)).replace("\\", "/"),
		"report_md": str(report_md_path.relative_to(REPO_ROOT)).replace("\\", "/"),
		"decision": decision,
	}
	run_meta_path.write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(description="Valida taxonomy/genre_tree_master.md (Capa 1).")
	parser.add_argument(
		"--taxonomy-file",
		default=str(DEFAULT_TAXONOMY_PATH),
		help="Ruta al archivo maestro de taxonomía.",
	)
	return parser.parse_args()


def main() -> int:
	args = parse_args()
	taxonomy_path = Path(args.taxonomy_file).resolve()
	if not taxonomy_path.exists():
		print(f"ERROR: no existe el archivo: {taxonomy_path}")
		return 2

	before_hash = file_sha256(taxonomy_path)
	lines = load_lines(taxonomy_path)
	nodes, parser_errors = parse_tree(lines)
	after_hash = file_sha256(taxonomy_path)

	findings = run_layer1_checks(
		taxonomy_path=taxonomy_path,
		before_hash=before_hash,
		after_hash=after_hash,
		nodes=nodes,
		parser_errors=parser_errors,
	)
	fatal_count, warning_count, decision = summarize(findings)

	write_reports(
		taxonomy_path=taxonomy_path,
		taxonomy_sha256=before_hash,
		findings=findings,
		decision=decision,
		fatal_count=fatal_count,
		warning_count=warning_count,
	)

	print(f"Decision: {decision}")
	print(f"FATAL: {fatal_count} | WARNING: {warning_count}")
	print("Reportes: reports/validate_master_report.json, reports/validate_master_report.md")
	return 1 if decision == "FAIL" else 0


if __name__ == "__main__":
	raise SystemExit(main())