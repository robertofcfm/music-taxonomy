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
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
REPORTS_DIR = REPO_ROOT / "reports"
PYTHON = sys.executable
VALIDATE_L1 = REPO_ROOT / "scripts" / "validate_tree.py"
VALIDATE_L2 = REPO_ROOT / "scripts" / "validate_tree_layer2.py"
LAYER1_REPORT = REPORTS_DIR / "validate_master_report.json"
LAYER2_REPORT = REPORTS_DIR / "validate_master_layer2_report.json"
LAYER2_RESPONSE = REPORTS_DIR / "validate_master_layer2_response.json"
HTML_FILE = REPO_ROOT / "web" / "index.html"


class Handler(http.server.BaseHTTPRequestHandler):
    def _send_json(self, data: dict, status: int = 200) -> None:
        body = json.dumps(data, ensure_ascii=False, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_html(self) -> None:
        content = HTML_FILE.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

    def do_GET(self) -> None:
        if self.path in ("/", "/index.html"):
            self._send_html()

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
            payload: dict = {
                "layer1": None,
                "layer2": None,
                "pipeline": {
                    "layer2_executed": False,
                    "message": "",
                },
            }
            if LAYER1_REPORT.exists():
                payload["layer1"] = json.loads(LAYER1_REPORT.read_text(encoding="utf-8"))
            if LAYER2_REPORT.exists():
                payload["layer2"] = json.loads(LAYER2_REPORT.read_text(encoding="utf-8"))
                payload["pipeline"]["layer2_executed"] = True
                payload["pipeline"]["message"] = "Se encontró reporte previo de Capa 2."
            else:
                payload["pipeline"]["message"] = "Sin reporte de Capa 2."
            self._send_json(payload)

        else:
            self.send_error(404)

    def do_POST(self) -> None:
        if self.path == "/api/validate/layer1":
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
            l1_proc = subprocess.run(
                [PYTHON, str(VALIDATE_L1)],
                capture_output=True,
                text=True,
                cwd=str(REPO_ROOT),
            )

            if not LAYER1_REPORT.exists():
                self._send_json(
                    {
                        "error": l1_proc.stderr or l1_proc.stdout,
                        "pipeline": {
                            "layer2_executed": False,
                            "message": "Fallo en Capa 1: no se generó reporte.",
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
                "pipeline": {
                    "layer1_exit_code": l1_proc.returncode,
                    "layer2_executed": False,
                    "message": "",
                },
            }

            if l1_decision == "FAIL":
                response["pipeline"]["message"] = "Capa 2 omitida: Capa 1 terminó en FAIL."
                self._send_json(response)
                return

            if not LAYER2_RESPONSE.exists():
                response["pipeline"]["message"] = (
                    "Capa 2 omitida: no existe reports/validate_master_layer2_response.json"
                )
                self._send_json(response)
                return

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

            if LAYER2_REPORT.exists():
                response["layer2"] = json.loads(LAYER2_REPORT.read_text(encoding="utf-8"))
                response["pipeline"]["message"] = "Capa 1 y Capa 2 ejecutadas."
            else:
                response["pipeline"]["message"] = "Capa 2 ejecutada pero sin reporte generado."
                response["pipeline"]["layer2_stdout"] = l2_proc.stdout
                response["pipeline"]["layer2_stderr"] = l2_proc.stderr

            self._send_json(response)

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
