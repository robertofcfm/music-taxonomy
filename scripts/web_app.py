"""Servidor web local — Validación de Taxonomía de Géneros Musicales.

Uso:
    python scripts/web_app.py          (puerto 8080 por defecto)
    python scripts/web_app.py --port 9000

Abre http://localhost:8080 en el navegador.
Presiona Ctrl+C para detener.
"""

from __future__ import annotations

import argparse
import http.server
import json
import re
import socketserver
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
REPORTS_DIR = REPO_ROOT / "reports"
PYTHON = sys.executable
VALIDATE_L1 = REPO_ROOT / "scripts" / "validate_tree.py"
VALIDATE_L2 = REPO_ROOT / "scripts" / "validate_tree_layer2.py"
LAYER1_REPORT = REPORTS_DIR / "validate_master_report.json"
LAYER2_REPORT = REPORTS_DIR / "validate_master_layer2_report.json"
LAYER2_RESPONSE = REPORTS_DIR / "validate_master_layer2_response.json"
LAYER2_PROMPT = REPO_ROOT / "prompts" / "validate_master_layer2_prompt.txt"
LAYER1_REPORT_MD = REPORTS_DIR / "validate_master_report.md"
LAYER1_RUN_METADATA = REPORTS_DIR / "validate_master_run_metadata.json"
LAYER2_REPORT_MD = REPORTS_DIR / "validate_master_layer2_report.md"
HOME_HTML_FILE = REPO_ROOT / "web" / "home.html"
HTML_FILE = REPO_ROOT / "web" / "index.html"
UTILERIAS_HTML_FILE = REPO_ROOT / "web" / "utilerias.html"
AUDITORIA_HTML_FILE = REPO_ROOT / "web" / "auditoria.html"
PROMPTS_DIR = REPO_ROOT / "prompts"
GENERADORES_DIR = PROMPTS_DIR / "generadores"


class Handler(http.server.BaseHTTPRequestHandler):
    def _clear_validation_reports(self) -> list[str]:
        cleared: list[str] = []
        files_to_clear = [
            LAYER1_REPORT,
            LAYER1_REPORT_MD,
            LAYER1_RUN_METADATA,
            LAYER2_PROMPT,
            LAYER2_RESPONSE,
            LAYER2_REPORT,
            LAYER2_REPORT_MD,
        ]
        for path in files_to_clear:
            if path.exists():
                path.unlink()
                cleared.append(path.name)
        return cleared

    @staticmethod
    def _is_fresh(path: Path, started_at_epoch: float) -> bool:
        return path.exists() and path.stat().st_mtime >= started_at_epoch

    def _send_json(self, data: dict, status: int = 200) -> None:
        body = json.dumps(data, ensure_ascii=False, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _read_request_json(self) -> tuple[dict | None, str | None]:
        try:
            content_length = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            return None, "Header Content-Length inválido."

        if content_length <= 0:
            return None, "Cuerpo de solicitud vacío."

        raw_body = self.rfile.read(content_length)
        try:
            payload = json.loads(raw_body.decode("utf-8"))
        except Exception as exc:
            return None, f"No se pudo decodificar el JSON del request: {exc}"

        if not isinstance(payload, dict):
            return None, "El cuerpo JSON debe ser un objeto."

        return payload, None

    def _send_html(self) -> None:
        content = HTML_FILE.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

    def _send_home_html(self) -> None:
        content = HOME_HTML_FILE.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

    def _send_utilerias_html(self) -> None:
        content = UTILERIAS_HTML_FILE.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

    def _send_auditoria_html(self) -> None:
        content = AUDITORIA_HTML_FILE.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

    # ── Audit checks ────────────────────────────────────────────

    @staticmethod
    def _audit_check_separacion_funcional() -> dict:
        """Check 1: cada archivo está en el directorio funcional correcto."""
        hallazgos: list[str] = []
        skip_dirs = {"__pycache__", ".git", ".venv", "node_modules", ".mypy_cache"}

        rules: list[tuple[Path, set[str], str]] = [
            (REPO_ROOT / "scripts",                    {".py"},                    "scripts/"),
            (REPO_ROOT / "web",                        {".html"},                  "web/"),
            (REPO_ROOT / "docs" / "governance",        {".md"},                    "docs/governance/"),
            (REPO_ROOT / "docs" / "context",           {".md"},                    "docs/context/"),
            (REPO_ROOT / "docs" / "project-management",{".md"},                    "docs/project-management/"),
            (REPO_ROOT / "docs" / "operations",        {".md"},                    "docs/operations/"),
            (REPO_ROOT / "docs" / "architecture",      {".md"},                    "docs/architecture/"),
            (REPO_ROOT / "docs" / "releases",          {".md"},                    "docs/releases/"),
            (REPO_ROOT / "reports",                    {".json", ".md", ".txt", ".csv"}, "reports/"),
            (REPO_ROOT / "catalog",                    {".csv"},                   "catalog/"),
            (REPO_ROOT / "data",                       {".csv"},                   "data/"),
            (REPO_ROOT / "prompts",                    {".md"},                    "prompts/"),
        ]

        seen: set[str] = set()
        for folder, allowed_exts, label in rules:
            if not folder.exists():
                continue
            for file in folder.rglob("*"):
                if file.is_dir():
                    continue
                if any(part in skip_dirs for part in file.parts):
                    continue
                if file.suffix.lower() not in allowed_exts:
                    rel = str(file.relative_to(REPO_ROOT))
                    if rel not in seen:
                        seen.add(rel)
                        hallazgos.append(
                            f"Archivo fuera de lugar en {label} → {rel}  (extensión {file.suffix!r})"
                        )

        # Extra: Python files outside scripts/
        scripts_dir = REPO_ROOT / "scripts"
        for py_file in REPO_ROOT.rglob("*.py"):
            if any(part in skip_dirs for part in py_file.parts):
                continue
            if not py_file.is_relative_to(scripts_dir):
                rel = str(py_file.relative_to(REPO_ROOT))
                if rel not in seen:
                    seen.add(rel)
                    hallazgos.append(f"Script .py fuera de scripts/ → {rel}")

        status = "PASS" if not hallazgos else ("WARN" if len(hallazgos) <= 3 else "FAIL")
        return {
            "id": "separacion_funcional",
            "nombre": "Separación por función",
            "descripcion": (
                "Verifica que cada archivo esté en su directorio funcional asignado: "
                "scripts en scripts/, reglas en docs/governance/, reportes en reports/, etc."
            ),
            "status": status,
            "hallazgos": hallazgos,
            "total_hallazgos": len(hallazgos),
        }

    @staticmethod
    def _audit_check_contradicciones_normativas() -> dict:
        """Check 2: no hay secciones duplicadas entre archivos de gobernanza
        ni lenguaje normativo en archivos de contexto."""
        hallazgos: list[str] = []

        # 2a — Detectar headers de sección duplicados entre archivos de gobernanza
        governance_dir = REPO_ROOT / "docs" / "governance"
        section_header_pattern = re.compile(r"^#{2,3}\s+(.+)$", re.MULTILINE)
        header_sources: dict[str, list[str]] = {}
        if governance_dir.exists():
            for md_file in sorted(governance_dir.glob("*.md")):
                text = md_file.read_text(encoding="utf-8")
                for header in section_header_pattern.findall(text):
                    key = header.strip().upper()
                    if len(key) > 4:  # skip trivially short names
                        header_sources.setdefault(key, []).append(
                            str(md_file.relative_to(REPO_ROOT))
                        )
            for header, files in header_sources.items():
                uniq = list(dict.fromkeys(files))
                if len(uniq) > 1:
                    hallazgos.append(
                        f"Sección «{header}» aparece en múltiples archivos de gobernanza: "
                        + ", ".join(uniq)
                    )

        # 2b — Detectar lenguaje normativo fuerte en archivos de contexto
        normative_re = re.compile(
            r"\b(OBLIGATORIO|PROHIBIDO|ESTÁ PROHIBIDO|NO SE PERMITE|SE PROH[IÍ]BE|QUEDA PROHIBIDO)\b",
            re.IGNORECASE,
        )
        context_dir = REPO_ROOT / "docs" / "context"
        if context_dir.exists():
            for md_file in sorted(context_dir.glob("*.md")):
                text = md_file.read_text(encoding="utf-8")
                matches: list[str] = []
                for i, line in enumerate(text.splitlines(), 1):
                    stripped = line.strip()
                    if stripped.startswith("#"):
                        continue
                    if normative_re.search(stripped):
                        matches.append(f"línea {i}: {stripped[:90]}")
                if matches:
                    rel = str(md_file.relative_to(REPO_ROOT))
                    hallazgos.append(
                        f"Lenguaje normativo en archivo de contexto {rel}:\n"
                        + "\n".join(f"  {m}" for m in matches[:3])
                        + (f"\n  … y {len(matches) - 3} más" if len(matches) > 3 else "")
                    )

        # 2c — Verificar que ningún archivo esté en ambos registros como fuente primaria
        ref_pattern = re.compile(r"^\s*-\s+(docs/\S+\.md)", re.MULTILINE)
        context_registry = REPO_ROOT / "docs" / "context" / "CONTEXT_REGISTRY.md"
        rules_registry   = REPO_ROOT / "docs" / "governance" / "RULES_REGISTRY.md"
        ctx_refs: set[str] = set()
        rul_refs: set[str] = set()
        if context_registry.exists():
            ctx_refs = set(ref_pattern.findall(context_registry.read_text(encoding="utf-8")))
        if rules_registry.exists():
            rul_refs = set(ref_pattern.findall(rules_registry.read_text(encoding="utf-8")))
        for shared in sorted(ctx_refs & rul_refs):
            hallazgos.append(
                f"Archivo listado en ambos registros (contexto Y reglas): {shared}"
            )

        status = "PASS" if not hallazgos else ("WARN" if len(hallazgos) <= 2 else "FAIL")
        return {
            "id": "contradicciones_normativas",
            "nombre": "Sin contradicciones normativas",
            "descripcion": (
                "Verifica que no haya secciones duplicadas entre archivos de gobernanza, "
                "que los archivos de contexto no contengan lenguaje normativo fuerte, "
                "y que ningún archivo aparezca a la vez como contexto y como regla."
            ),
            "status": status,
            "hallazgos": hallazgos,
            "total_hallazgos": len(hallazgos),
        }

    @staticmethod
    def _audit_check_reglas_incrustadas() -> dict:
        """Check 3: scripts y prompts no contienen reglas copiadas inline."""
        hallazgos: list[str] = []

        # 3a — Scripts Python: detectar bloques de texto con separadores tipo gobernanza
        separator_re = re.compile(r"-{15,}")
        scripts_dir = REPO_ROOT / "scripts"
        if scripts_dir.exists():
            for py_file in sorted(scripts_dir.glob("*.py")):
                text = py_file.read_text(encoding="utf-8")
                string_blocks = re.findall(r'"""([\s\S]*?)"""', text)
                for block in string_blocks:
                    sep_count = len(separator_re.findall(block))
                    if sep_count >= 2 and len(block) > 200:
                        rel = str(py_file.relative_to(REPO_ROOT))
                        hallazgos.append(
                            f"Posible bloque de reglas inline en {rel} "
                            f"({len(block)} chars, {sep_count} separadores '---'). "
                            "Considerar mover a docs/ y referenciar."
                        )
                        break  # one warning per file is enough

        # 3b — Prompts generadores: detectar secciones normativas incrustadas
        normative_section_re = re.compile(
            r"^#{1,3}\s*(REGLAS|RESTRICCIONES ABSOLUTAS|NORMAS|PROHIBICIONES)\s*$",
            re.MULTILINE | re.IGNORECASE,
        )
        generadores_dir = REPO_ROOT / "prompts" / "generadores"
        if generadores_dir.exists():
            for md_file in sorted(generadores_dir.glob("*.md")):
                if md_file.name.lower() == "readme.md":
                    continue
                text = md_file.read_text(encoding="utf-8")
                if normative_section_re.search(text):
                    rel = str(md_file.relative_to(REPO_ROOT))
                    hallazgos.append(
                        f"Sección normativa incrustada en prompt {rel}. "
                        "Usar referencia a docs/governance/ en lugar de copiar el contenido."
                    )

        # 3c — Comparación de fragmentos: verificar que prompts no repitan párrafos de gobernanza
        governance_dir = REPO_ROOT / "docs" / "governance"
        governance_fingerprints: set[str] = set()
        MIN_PARA_LEN = 60
        if governance_dir.exists():
            for md_file in governance_dir.glob("*.md"):
                text = md_file.read_text(encoding="utf-8")
                for para in re.split(r"\n\s*\n", text):
                    clean = para.strip()
                    if len(clean) >= MIN_PARA_LEN and not clean.startswith("#"):
                        governance_fingerprints.add(clean[:120])

        prompts_dir = REPO_ROOT / "prompts"
        if prompts_dir.exists() and governance_fingerprints:
            for md_file in prompts_dir.rglob("*.md"):
                if "generadores" in str(md_file) and md_file.name.lower() == "readme.md":
                    continue
                text = md_file.read_text(encoding="utf-8")
                copied = [fp for fp in governance_fingerprints if fp in text]
                if copied:
                    rel = str(md_file.relative_to(REPO_ROOT))
                    hallazgos.append(
                        f"Contenido de gobernanza copiado literalmente en {rel} "
                        f"({len(copied)} fragmento(s) coincidente(s)). "
                        "Usar referencia en lugar de copia."
                    )

        status = "PASS" if not hallazgos else ("WARN" if len(hallazgos) <= 2 else "FAIL")
        return {
            "id": "reglas_incrustadas",
            "nombre": "Sin reglas incrustadas en scripts/prompts",
            "descripcion": (
                "Verifica que scripts y prompts no contengan reglas o contexto copiados inline. "
                "Deben usar referencias a los archivos fuente para que siempre tomen los valores más recientes."
            ),
            "status": status,
            "hallazgos": hallazgos,
            "total_hallazgos": len(hallazgos),
        }

    @staticmethod
    def _audit_check_integridad_registros() -> dict:
        """Check 4 (recomendado): todos los archivos listados en los registros existen."""
        hallazgos: list[str] = []
        ref_pattern = re.compile(r"^\s*-\s+(docs/\S+\.md)", re.MULTILINE)
        registries = [
            REPO_ROOT / "docs" / "context" / "CONTEXT_REGISTRY.md",
            REPO_ROOT / "docs" / "governance" / "RULES_REGISTRY.md",
        ]
        for registry_path in registries:
            if not registry_path.exists():
                hallazgos.append(
                    f"Registro no encontrado: {str(registry_path.relative_to(REPO_ROOT))}"
                )
                continue
            text = registry_path.read_text(encoding="utf-8")
            for ref in ref_pattern.findall(text):
                target = REPO_ROOT / ref
                if not target.exists():
                    rel_reg = str(registry_path.relative_to(REPO_ROOT))
                    hallazgos.append(
                        f"[{rel_reg}] Archivo referenciado no existe: {ref}"
                    )

        status = "PASS" if not hallazgos else "FAIL"
        return {
            "id": "integridad_registros",
            "nombre": "Integridad de registros",
            "descripcion": (
                "Verifica que todos los archivos listados en CONTEXT_REGISTRY.md y RULES_REGISTRY.md "
                "existan físicamente en el repositorio."
            ),
            "status": status,
            "hallazgos": hallazgos,
            "total_hallazgos": len(hallazgos),
        }

    @staticmethod
    def _audit_check_marcadores_borrador() -> dict:
        """Check 5 (recomendado): prompts finales no tienen marcadores pendientes."""
        hallazgos: list[str] = []
        draft_pattern = re.compile(
            r"\[(?:DEFINIR|PENDIENTE|COLOCAR_AQUI|COLOCAR_AQUÍ|TODO|FIXME)[_\]]",
            re.IGNORECASE,
        )
        generadores_dir = REPO_ROOT / "prompts" / "generadores"
        if generadores_dir.exists():
            for md_file in sorted(generadores_dir.glob("*.md")):
                if md_file.name.lower() == "readme.md":
                    continue
                text = md_file.read_text(encoding="utf-8")
                matches = draft_pattern.findall(text)
                if matches:
                    rel = str(md_file.relative_to(REPO_ROOT))
                    unique_markers = list(dict.fromkeys(matches))[:4]
                    hallazgos.append(
                        f"{rel}: {len(matches)} marcador(es) de borrador → "
                        + ", ".join(unique_markers)
                    )

        status = "PASS" if not hallazgos else "FAIL"
        return {
            "id": "marcadores_borrador",
            "nombre": "Sin marcadores de borrador en prompts finales",
            "descripcion": (
                "Verifica que los prompts en prompts/generadores/ no contengan marcadores pendientes "
                "como [DEFINIR_*] o [PENDIENTE_*]. Su presencia indica que el prompt es un borrador."
            ),
            "status": status,
            "hallazgos": hallazgos,
            "total_hallazgos": len(hallazgos),
        }

    @staticmethod
    def _audit_check_metadatos_documentos() -> dict:
        """Check 6 (recomendado): documentos clave tienen metadatos de fecha y no están desactualizados."""
        hallazgos: list[str] = []
        date_re = re.compile(r"[Úú]ltima actualizaci[oó]n[:\s]*(\d{4}-\d{2}-\d{2})", re.IGNORECASE)
        STALE_DAYS = 90
        today = datetime.now().date()

        key_docs = [
            REPO_ROOT / "docs" / "governance" / "GLOBAL_RULES.md",
            REPO_ROOT / "docs" / "governance" / "SYSTEM_CONTRACT.md",
            REPO_ROOT / "docs" / "governance" / "AI_PROMPT_SYSTEM_RULES.md",
            REPO_ROOT / "docs" / "governance" / "RULES_REGISTRY.md",
            REPO_ROOT / "docs" / "context" / "AI_PROMPT_SYSTEM_CONTEXT.md",
            REPO_ROOT / "docs" / "context" / "PROJECT_CONTEXT.md",
            REPO_ROOT / "docs" / "context" / "SYSTEM_OVERVIEW.md",
            REPO_ROOT / "docs" / "context" / "CONTEXT_REGISTRY.md",
        ]

        for doc_path in key_docs:
            rel = str(doc_path.relative_to(REPO_ROOT))
            if not doc_path.exists():
                hallazgos.append(f"Documento clave no encontrado: {rel}")
                continue
            text = doc_path.read_text(encoding="utf-8")
            match = date_re.search(text)
            if not match:
                hallazgos.append(f"Sin campo 'Última actualización' en: {rel}")
            else:
                try:
                    doc_date = datetime.strptime(match.group(1), "%Y-%m-%d").date()
                    delta = (today - doc_date).days
                    if delta > STALE_DAYS:
                        hallazgos.append(
                            f"Documento posiblemente desactualizado ({delta} días sin revisión): {rel}"
                        )
                except ValueError:
                    hallazgos.append(f"Fecha de actualización con formato inválido en: {rel}")

        status = "PASS" if not hallazgos else ("WARN" if all("desactualizado" in h for h in hallazgos) else "FAIL")
        return {
            "id": "metadatos_documentos",
            "nombre": "Consistencia de metadatos de documentos",
            "descripcion": (
                "Verifica que los documentos clave tengan el campo 'Última actualización' "
                f"y que no lleven más de {STALE_DAYS} días sin revisión."
            ),
            "status": status,
            "hallazgos": hallazgos,
            "total_hallazgos": len(hallazgos),
        }

    @staticmethod
    def _run_audit() -> dict:
        checks = [
            Handler._audit_check_separacion_funcional(),
            Handler._audit_check_contradicciones_normativas(),
            Handler._audit_check_reglas_incrustadas(),
            Handler._audit_check_integridad_registros(),
            Handler._audit_check_marcadores_borrador(),
            Handler._audit_check_metadatos_documentos(),
        ]
        resumen = {
            "total": len(checks),
            "pass":  sum(1 for c in checks if c["status"] == "PASS"),
            "warn":  sum(1 for c in checks if c["status"] == "WARN"),
            "fail":  sum(1 for c in checks if c["status"] == "FAIL"),
        }
        return {
            "timestamp": datetime.now().isoformat(timespec="seconds"),
            "checks": checks,
            "resumen": resumen,
        }

    @staticmethod
    def _prompt_generation_requests_seed() -> list[dict]:
        items: list[dict] = []
        if not GENERADORES_DIR.exists():
            return items

        paths = sorted(path for path in GENERADORES_DIR.glob("*.md") if path.name.lower() != "readme.md")
        for index, path in enumerate(paths, start=1):
            text = path.read_text(encoding="utf-8").strip()
            rel_path = f"prompts/generadores/{path.name}"
            nombre = Handler._extract_main_title(text) or path.stem.replace("_", " ").strip().title()
            tarea = Handler._extract_section_value(text, "TAREA", "Definir tarea operativa a ejecutar.")
            objetivo = Handler._extract_section_value(text, "OBJETIVO_OPERATIVO", "Definir objetivo operativo de la ejecución.")
            restricciones = Handler._extract_section_value(text, "RESTRICCIONES", "No inventar datos; solicitar faltantes críticos.")
            salida_esperada = Handler._extract_section_value(text, "SALIDA_ESPERADA", "Resultado final utilizable sin placeholders.")

            items.append(
                {
                    "id": f"req-gen-{index:03d}",
                    "nombre": nombre,
                    "archivo": rel_path,
                    "tarea": tarea,
                    "objetivo": objetivo,
                    "restricciones": restricciones,
                    "salida_esperada": salida_esperada,
                    "estado": "pendiente",
                    "prompt_base": text,
                }
            )

        return items

    @staticmethod
    def _list_prompt_templates() -> list[str]:
        templates: list[str] = []
        if not GENERADORES_DIR.exists():
            return templates
        for path in sorted(GENERADORES_DIR.glob("*.md")):
            if path.name.lower() == "readme.md":
                continue
            templates.append(f"prompts/generadores/{path.name}")
        return templates

    @staticmethod
    def _extract_main_title(text: str) -> str:
        for raw_line in text.splitlines():
            line = raw_line.strip()
            if line.startswith("#"):
                return line.lstrip("#").strip()
        return ""

    @staticmethod
    def _extract_section_value(text: str, section_name: str, default: str) -> str:
        lines = text.splitlines()
        marker = f"[{section_name}]"
        inside = False
        captured: list[str] = []

        for raw_line in lines:
            line = raw_line.strip()
            if line == marker:
                inside = True
                continue
            if inside and line.startswith("[") and line.endswith("]"):
                break
            if not inside:
                continue
            if not line or set(line) == {"-"}:
                continue
            cleaned = line
            if cleaned.startswith("- "):
                cleaned = cleaned[2:].strip()
            if cleaned:
                captured.append(cleaned)

        if not captured:
            return default
        return " ".join(captured)

    @staticmethod
    def _validate_prompt_request(item: dict) -> list[str]:
        errors: list[str] = []
        required = {
            "id": "Falta id de solicitud.",
            "nombre": "Falta nombre de solicitud.",
            "tarea": "Falta descripción de la tarea.",
            "objetivo": "Falta objetivo operativo.",
            "salida_esperada": "Falta salida esperada.",
        }
        for key, message in required.items():
            value = str(item.get(key, "")).strip()
            if not value:
                errors.append(message)
        return errors

    @staticmethod
    def _build_standalone_prompt(item: dict) -> str:
        base_prompt = str(item.get("prompt_base", "")).strip()
        nombre = str(item.get("nombre", "Solicitud sin nombre")).strip()
        tarea = str(item.get("tarea", "")).strip()
        objetivo = str(item.get("objetivo", "")).strip()
        restricciones = str(item.get("restricciones", "Sin restricciones adicionales.")).strip()
        salida_esperada = str(item.get("salida_esperada", "")).strip()

        prompt_generado = (
            "Actua como especialista senior en la tarea descrita.\n"
            "No busques complacer ni confirmar supuestos: entrega recomendaciones "
            "reales, accionables y justificadas, incluso si contradicen la propuesta inicial.\n\n"
            f"Contexto de la solicitud: {nombre}.\n\n"
            "Objetivo de esta ejecucion:\n"
            f"{objetivo}\n\n"
            "Tarea:\n"
            f"{tarea}\n\n"
            "Restricciones:\n"
            f"- {restricciones}\n"
            "- No inventar datos no proporcionados por el usuario.\n"
            "- Si falta informacion critica, detener y pedir faltantes exactos.\n\n"
            "Formato de salida obligatorio:\n"
            "[RESPUESTA]\n"
            "- (entregable final)\n\n"
            "[FALTANTES_SI_APLICA]\n"
            "- (lista puntual)\n\n"
            "[RECOMENDACIONES_EXPERTAS]\n"
            "- recomendacion 1\n"
            "- recomendacion 2\n"
            "- recomendacion 3\n\n"
            "[CRITERIO_DE_CIERRE]\n"
            f"- La tarea se considera completa cuando la salida cumple: {salida_esperada}."
        )

        if base_prompt:
            return (
                f"{base_prompt}\n\n"
                "--------------------------------------------------\n"
                "SOLICITUD ACTIVA\n"
                "--------------------------------------------------\n"
                f"Nombre: {nombre}\n"
                f"Tarea: {tarea}\n"
                f"Objetivo: {objetivo}\n"
                f"Restricciones: {restricciones}\n"
                f"Salida esperada: {salida_esperada}\n"
            )

        return prompt_generado

    @staticmethod
    def _load_layer1_report() -> dict | None:
        if not LAYER1_REPORT.exists():
            return None
        return json.loads(LAYER1_REPORT.read_text(encoding="utf-8"))

    def _build_prompt_payload(self, regenerate: bool = False) -> tuple[dict, dict]:
        diagnostics = {
            "executed": False,
            "exit_code": None,
            "stdout": "",
            "stderr": "",
            "file_exists": False,
            "file_fresh": False,
            "regenerated_on_read": False,
        }

        if regenerate:
            started_at = time.time()
            proc = subprocess.run(
                [PYTHON, str(VALIDATE_L2), "--print-prompt"],
                capture_output=True,
                text=True,
                cwd=str(REPO_ROOT),
            )
            diagnostics["executed"] = True
            diagnostics["exit_code"] = proc.returncode
            diagnostics["stdout"] = proc.stdout
            diagnostics["stderr"] = proc.stderr
            diagnostics["file_exists"] = LAYER2_PROMPT.exists()
            diagnostics["file_fresh"] = self._is_fresh(LAYER2_PROMPT, started_at)
            diagnostics["regenerated_on_read"] = True

        payload = self._load_prompt_payload()
        diagnostics["file_exists"] = payload["exists"]
        return payload, diagnostics

    @staticmethod
    def _load_prompt_payload() -> dict:
        if not LAYER2_PROMPT.exists():
            return {
                "exists": False,
                "path": "prompts/validate_master_layer2_prompt.txt",
                "text": "",
            }
        return {
            "exists": True,
            "path": "prompts/validate_master_layer2_prompt.txt",
            "text": LAYER2_PROMPT.read_text(encoding="utf-8"),
        }

    def do_GET(self) -> None:
        if self.path in ("/", "/home", "/home.html"):
            if not HOME_HTML_FILE.exists():
                self._send_json({"error": "No existe web/home.html."}, 404)
                return
            self._send_home_html()

        elif self.path == "/index.html":
            self._send_html()

        elif self.path in ("/utilerias", "/utilerias.html"):
            if not UTILERIAS_HTML_FILE.exists():
                self._send_json({"error": "No existe web/utilerias.html."}, 404)
                return
            self._send_utilerias_html()

        elif self.path in ("/auditoria", "/auditoria.html"):
            if not AUDITORIA_HTML_FILE.exists():
                self._send_json({"error": "No existe web/auditoria.html."}, 404)
                return
            self._send_auditoria_html()

        elif self.path == "/api/utilerias/requests":
            self._send_json(
                {
                    "items": self._prompt_generation_requests_seed(),
                    "templates": self._list_prompt_templates(),
                }
            )

        elif self.path == "/api/report/layer1":
            if LAYER1_REPORT.exists():
                self._send_json(json.loads(LAYER1_REPORT.read_text(encoding="utf-8")))
            else:
                self._send_json({"error": "Sin reporte. Ejecuta la validación primero."}, 404)

        elif self.path == "/api/report/layer2":
            if LAYER2_REPORT.exists():
                self._send_json(json.loads(LAYER2_REPORT.read_text(encoding="utf-8")))
            else:
                self._send_json({"error": "Sin reporte de Capa 2."}, 404)

        elif self.path == "/api/report/full":
            prompt_payload, prompt_diagnostics = self._build_prompt_payload(regenerate=True)
            payload: dict = {
                "layer1": self._load_layer1_report(),
                "layer2": None,
                "prompt": prompt_payload,
                "pipeline": {
                    "layer2_prompt_generated": False,
                    "layer2_executed": False,
                    "diagnostics": {
                        "prompt": prompt_diagnostics,
                    },
                    "message": "",
                },
            }
            if payload["prompt"]["exists"]:
                payload["pipeline"]["layer2_prompt_generated"] = True
            if LAYER2_REPORT.exists():
                payload["layer2"] = json.loads(LAYER2_REPORT.read_text(encoding="utf-8"))
                payload["pipeline"]["layer2_executed"] = True
                payload["pipeline"]["message"] = "Se encontró un reporte previo de Capa 2 procesada."
            elif payload["prompt"]["exists"]:
                payload["pipeline"]["message"] = (
                    "Prompt de Capa 2 disponible. Copia el texto, consúltalo en una IA externa y pega aquí el JSON devuelto."
                )
            elif payload["layer1"]:
                payload["pipeline"]["message"] = "Hay un reporte de Capa 1, pero no hay prompt disponible de Capa 2."
            else:
                payload["pipeline"]["message"] = "Sin ejecución previa de Capa 1."
            self._send_json(payload)

        else:
            self.send_error(404)

    def do_POST(self) -> None:
        if self.path == "/api/report/clear":
            cleared = self._clear_validation_reports()
            self._send_json(
                {
                    "ok": True,
                    "cleared_files": cleared,
                    "message": "Reportes de validación limpiados.",
                }
            )

        elif self.path == "/api/auditoria/run":
            try:
                result = self._run_audit()
            except Exception as exc:
                self._send_json({"error": f"Error interno al ejecutar la auditoría: {exc}"}, 500)
                return
            self._send_json(result)

        elif self.path == "/api/utilerias/process":
            payload, error = self._read_request_json()
            if error:
                self._send_json({"error": error}, 400)
                return

            items = payload.get("items")
            if not isinstance(items, list):
                self._send_json({"error": "El campo items debe ser una lista."}, 400)
                return

            results: list[dict] = []
            processed_at = int(time.time())
            for raw_item in items:
                item = raw_item if isinstance(raw_item, dict) else {}
                req_id = str(item.get("id", "")).strip() or f"req-{processed_at}"
                errors = self._validate_prompt_request(item)

                recommendations = [
                    "Mantener alcance mínimo suficiente para evitar ruido.",
                    "Revisar que la tarea no dependa de contexto implícito.",
                    "Confirmar criterio de cierre antes de ejecutar en chat externo.",
                ]

                if errors:
                    results.append(
                        {
                            "id": req_id,
                            "tarea": str(item.get("tarea", "")).strip(),
                            "status": "REQUIERE_CORRECCION",
                            "prompt_final": "",
                            "errores": errors,
                            "recomendaciones": recommendations,
                        }
                    )
                    continue

                prompt_final = self._build_standalone_prompt(item)
                has_placeholders = "[DEFINIR_" in prompt_final or "[PENDIENTE_" in prompt_final
                if has_placeholders:
                    results.append(
                        {
                            "id": req_id,
                            "tarea": str(item.get("tarea", "")).strip(),
                            "status": "REQUIERE_CORRECCION",
                            "prompt_final": "",
                            "errores": ["El prompt contiene placeholders pendientes."],
                            "recomendaciones": recommendations,
                        }
                    )
                    continue

                results.append(
                    {
                        "id": req_id,
                        "tarea": str(item.get("tarea", "")).strip(),
                        "status": "PROMPT_OK",
                        "prompt_final": prompt_final,
                        "errores": [],
                        "recomendaciones": recommendations,
                    }
                )

            self._send_json({"results": results, "processed_count": len(results)})

        elif self.path == "/api/validate/layer1":
            proc = subprocess.run(
                [PYTHON, str(VALIDATE_L1)],
                capture_output=True,
                text=True,
                cwd=str(REPO_ROOT),
            )
            if LAYER1_REPORT.exists():
                data = json.loads(LAYER1_REPORT.read_text(encoding="utf-8"))
                data["_exit_code"] = proc.returncode
            else:
                data = {
                    "error": proc.stderr or proc.stdout,
                    "_exit_code": proc.returncode,
                }
            self._send_json(data)

        elif self.path == "/api/validate/full":
            self._clear_validation_reports()

            l1_started_at = time.time()
            l1_proc = subprocess.run(
                [PYTHON, str(VALIDATE_L1)],
                capture_output=True,
                text=True,
                cwd=str(REPO_ROOT),
            )

            if not self._is_fresh(LAYER1_REPORT, l1_started_at):
                self._send_json(
                    {
                        "error": l1_proc.stderr or l1_proc.stdout,
                        "pipeline": {
                            "layer2_executed": False,
                            "message": "Falló la Capa 1: no se generó su reporte.",
                        },
                    },
                    500,
                )
                return

            layer1 = json.loads(LAYER1_REPORT.read_text(encoding="utf-8"))
            l1_decision = layer1.get("summary", {}).get("decision", "")

            response: dict = {
                "layer1": layer1,
                "layer2": None,
                "prompt": self._load_prompt_payload(),
                "pipeline": {
                    "started_at_epoch": l1_started_at,
                    "layer1_exit_code": l1_proc.returncode,
                    "layer2_prompt_generated": False,
                    "layer2_executed": False,
                    "diagnostics": {
                        "prompt": {
                            "executed": False,
                            "exit_code": None,
                            "stdout": "",
                            "stderr": "",
                            "file_exists": False,
                            "file_fresh": False,
                        },
                    },
                    "message": "",
                },
            }

            if l1_decision == "FAIL":
                response["pipeline"]["message"] = "Capa 1 terminó en FAIL. No se generó prompt para Capa 2."
                self._send_json(response)
                return

            l2_prompt_started_at = time.time()
            l2_prompt_proc = subprocess.run(
                [
                    PYTHON,
                    str(VALIDATE_L2),
                    "--print-prompt",
                ],
                capture_output=True,
                text=True,
                cwd=str(REPO_ROOT),
            )
            response["pipeline"]["layer2_prompt_generated"] = True
            response["pipeline"]["layer2_prompt_exit_code"] = l2_prompt_proc.returncode
            response["pipeline"]["diagnostics"]["prompt"]["executed"] = True
            response["pipeline"]["diagnostics"]["prompt"]["exit_code"] = l2_prompt_proc.returncode
            response["pipeline"]["diagnostics"]["prompt"]["stdout"] = l2_prompt_proc.stdout
            response["pipeline"]["diagnostics"]["prompt"]["stderr"] = l2_prompt_proc.stderr
            response["pipeline"]["diagnostics"]["prompt"]["file_exists"] = LAYER2_PROMPT.exists()
            response["pipeline"]["diagnostics"]["prompt"]["file_fresh"] = self._is_fresh(
                LAYER2_PROMPT, l2_prompt_started_at
            )

            if not self._is_fresh(LAYER2_PROMPT, l2_prompt_started_at):
                response["pipeline"]["message"] = "La Capa 1 terminó, pero no se pudo generar el prompt de Capa 2."
                self._send_json(response, 500)
                return

            response["prompt"] = self._load_prompt_payload()
            response["pipeline"]["message"] = (
                "Capa 1 ejecutada y prompt de Capa 2 generado. "
                "Copia el prompt, envíalo a una IA externa y pega aquí el JSON devuelto."
            )

            self._send_json(response)

        elif self.path == "/api/validate/layer2-response":
            payload, error = self._read_request_json()
            if error:
                self._send_json({"error": error}, 400)
                return

            response_text = str(payload.get("response_text", "")).strip()
            if not response_text:
                self._send_json({"error": "El campo response_text es obligatorio."}, 400)
                return

            response_started_at = time.time()
            REPORTS_DIR.mkdir(parents=True, exist_ok=True)
            LAYER2_RESPONSE.write_text(response_text, encoding="utf-8")
            prompt_payload, prompt_diagnostics = self._build_prompt_payload(regenerate=True)

            response: dict = {
                "layer1": self._load_layer1_report(),
                "layer2": None,
                "prompt": prompt_payload,
                "pipeline": {
                    "layer2_prompt_generated": prompt_payload["exists"],
                    "layer2_executed": False,
                    "diagnostics": {
                        "prompt": prompt_diagnostics,
                        "response_file": {
                            "file_exists": LAYER2_RESPONSE.exists(),
                            "file_fresh": self._is_fresh(LAYER2_RESPONSE, response_started_at),
                            "json_valid": False,
                            "json_error": "",
                        },
                        "layer2_apply": {
                            "executed": False,
                            "exit_code": None,
                            "stdout": "",
                            "stderr": "",
                            "report_fresh": False,
                        },
                    },
                    "message": "",
                },
            }

            try:
                json.loads(LAYER2_RESPONSE.read_text(encoding="utf-8-sig"))
                response["pipeline"]["diagnostics"]["response_file"]["json_valid"] = True
            except Exception as exc:
                response["pipeline"]["diagnostics"]["response_file"]["json_error"] = str(exc)
                response["pipeline"]["message"] = (
                    "La respuesta fue guardada, pero el contenido pegado no es JSON válido."
                )
                self._send_json(response, 400)
                return

            l2_started_at = time.time()
            l2_proc = subprocess.run(
                [
                    PYTHON,
                    str(VALIDATE_L2),
                    "--apply-response",
                    str(LAYER2_RESPONSE),
                ],
                capture_output=True,
                text=True,
                cwd=str(REPO_ROOT),
            )

            response["pipeline"]["layer2_executed"] = True
            response["pipeline"]["layer2_exit_code"] = l2_proc.returncode
            response["pipeline"]["diagnostics"]["layer2_apply"]["executed"] = True
            response["pipeline"]["diagnostics"]["layer2_apply"]["exit_code"] = l2_proc.returncode
            response["pipeline"]["diagnostics"]["layer2_apply"]["stdout"] = l2_proc.stdout
            response["pipeline"]["diagnostics"]["layer2_apply"]["stderr"] = l2_proc.stderr

            report_fresh = self._is_fresh(LAYER2_REPORT, l2_started_at)
            response["pipeline"]["diagnostics"]["layer2_apply"]["report_fresh"] = report_fresh

            if report_fresh:
                response["layer2"] = json.loads(LAYER2_REPORT.read_text(encoding="utf-8"))
                response["pipeline"]["message"] = "Respuesta JSON guardada y Capa 2 procesada."
                self._send_json(response)
                return

            response["pipeline"]["message"] = "La respuesta JSON fue guardada, pero no se generó un reporte nuevo de Capa 2."
            self._send_json(response, 500)

        else:
            self.send_error(404)

    def log_message(self, fmt: str, *args) -> None:
        method = getattr(self, "command", "?")
        path = getattr(self, "path", "?")
        code = args[1] if len(args) > 1 else "?"
        print(f"  {method:4}  {path}  →  {code}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Servidor web local de validación de taxonomía.")
    parser.add_argument("--port", type=int, default=8080, help="Puerto (default: 8080)")
    args = parser.parse_args()

    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("localhost", args.port), Handler) as server:
        url = f"http://localhost:{args.port}"
        print(f"\n  ▶  Servidor iniciado en {url}")
        print(f"  ·  Abre {url} en tu navegador")
        print("  ·  Presiona Ctrl+C para detener.\n")
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\n  Servidor detenido.")


if __name__ == "__main__":
    main()
