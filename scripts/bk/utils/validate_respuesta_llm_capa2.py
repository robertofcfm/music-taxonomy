"""
Validador de respuestas LLM para Capa 2.
- Lee el JSON de hallazgos generado por la IA.
- Valida el cumplimiento del contrato (estructura, campos requeridos, tipos).
- Genera reportes detallados (JSON y Markdown) en reports/.
"""
import json
from pathlib import Path
import sys
import argparse
import datetime
from utils.validate_criteria_coverage import *

REPO_ROOT = Path(__file__).resolve().parents[1]
REPORTS_DIR = REPO_ROOT / "reports"
CONTRACT_PATH = REPO_ROOT / "docs" / "operations" / "VALIDATE_MASTER_STRATEGY.md"


def parse_args():
    parser = argparse.ArgumentParser(description="Validador de respuestas LLM (Capa 2)")
    parser.add_argument('--input', required=True, help='Archivo JSON de respuesta de la IA')
    return parser.parse_args()


def main():
    args = parse_args()
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Archivo no encontrado: {input_path}")
        sys.exit(1)
    with open(input_path, encoding="utf-8") as f:
        data = json.load(f)
    resultados = validar_respuesta_llm(data)
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    exportar_resultado_json(resultados, REPORTS_DIR / f"reporte_llm_{ts}.json")
    exportar_resultado_md(resultados, REPORTS_DIR / f"reporte_llm_{ts}.md")
    print("Validación de respuesta LLM completada.")


def validar_respuesta_llm(data):
    # TODO: Implementar validación de contrato y reglas de negocio
    resultados = {"timestamp": datetime.datetime.now().isoformat(), "errores": [], "advertencias": [], "ok": [], "detalle": {"contrato": str(CONTRACT_PATH.name)}}
    # Ejemplo: validar campos principales
    if not isinstance(data, dict):
        resultados["errores"].append({"regla": "LLM-001", "descripcion": "La respuesta debe ser un objeto JSON.", "detalle": str(type(data)), "severidad": "FATAL"})
        return resultados
    for campo in ["hallazgos", "resumen", "version"]:
        if campo not in data:
            resultados["errores"].append({"regla": "LLM-002", "descripcion": f"Falta el campo obligatorio '{campo}'.", "detalle": "", "severidad": "FATAL"})
    if not resultados["errores"]:
        resultados["ok"].append({"regla": "LLM-000", "descripcion": "Estructura básica de respuesta válida.", "detalle": "Todos los campos principales presentes.", "severidad": "INFO"})
    # Más validaciones pueden agregarse aquí
    return resultados


def exportar_resultado_json(resultados, ruta):
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(resultados, f, ensure_ascii=False, indent=2)
    print(f"Reporte JSON generado en: {ruta}")


def exportar_resultado_md(resultados, ruta_md):
    with open(ruta_md, "w", encoding="utf-8") as f:
        f.write(f"# Reporte de Validación de Respuesta LLM\n")
        f.write(f"Fecha: {resultados['timestamp']}\n\n")
        f.write(f"## Contrato utilizado\n- {resultados['detalle']['contrato']}\n\n")
        if resultados['errores']:
            f.write(f"## ❌ Errores\n")
            for err in resultados['errores']:
                f.write(f"- **{err['regla']}** ({err['severidad']}): {err['descripcion']}\n  - Detalle: {err['detalle']}\n")
        else:
            f.write("## ❌ Errores\n- Ninguno\n")
        if resultados['advertencias']:
            f.write(f"\n## ⚠️ Advertencias\n")
            for adv in resultados['advertencias']:
                f.write(f"- **{adv['regla']}** ({adv['severidad']}): {adv['descripcion']}\n  - Detalle: {adv['detalle']}\n")
        else:
            f.write("\n## ⚠️ Advertencias\n- Ninguna\n")
        if resultados['ok']:
            f.write(f"\n## ✅ Reglas validadas correctamente\n")
            for ok in resultados['ok']:
                f.write(f"- **{ok['regla']}**: {ok['descripcion']}\n  - {ok['detalle']}\n")
        else:
            f.write("\n## ✅ Reglas validadas correctamente\n- Ninguna\n")
    print(f"Reporte Markdown generado en: {ruta_md}")


if __name__ == "__main__":
    main()
