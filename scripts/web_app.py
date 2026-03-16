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
import socketserver
import subprocess
import sys
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
REPORTS_DIR = REPO_ROOT / "reports"
PYTHON = sys.executable
VALIDATE_L1 = REPO_ROOT / "scripts" / "validate_tree.py"
VALIDATE_L2 = REPO_ROOT / "scripts" / "validate_tree_layer2.py"
LAYER1_REPORT = REPORTS_DIR / "validate_master_report.json"
LAYER2_REPORT = REPORTS_DIR / "validate_master_layer2_report.json"
LAYER2_RESPONSE = REPORTS_DIR / "validate_master_layer2_response.json"
LAYER2_PROMPT = REPORTS_DIR / "validate_master_layer2_prompt.txt"
LAYER1_REPORT_MD = REPORTS_DIR / "validate_master_report.md"
LAYER1_RUN_METADATA = REPORTS_DIR / "validate_master_run_metadata.json"
LAYER2_REPORT_MD = REPORTS_DIR / "validate_master_layer2_report.md"
HOME_HTML_FILE = REPO_ROOT / "web" / "home.html"
HTML_FILE = REPO_ROOT / "web" / "index.html"
UTILERIAS_HTML_FILE = REPO_ROOT / "web" / "utilerias.html"
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
            layer1 = self._load_layer1_report()
            decision = (layer1 or {}).get("summary", {}).get("decision", "")
            if decision and decision != "FAIL":
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
                "path": "reports/validate_master_layer2_prompt.txt",
                "text": "",
            }
        return {
            "exists": True,
            "path": "reports/validate_master_layer2_prompt.txt",
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
