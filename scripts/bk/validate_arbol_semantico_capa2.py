"""Validación semántica (Capa 2) de taxonomy/genre_tree_master.md.

Modos de operación:

	--print-prompt
			Genera el prompt determinista para la IA y lo escribe en
			prompts/prompt_arbol_semantico_capa2.txt.
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
import json
from pathlib import Path
import sys
import hashlib
import argparse
import datetime
import re
from utils.validate_criteria_coverage import *

REPO_ROOT = Path(__file__).resolve().parents[1]
GOVERNANCE_DIR = REPO_ROOT / "docs" / "governance"
DEFAULT_TAXONOMY_PATH = REPO_ROOT / "taxonomy" / "genre_tree_master.md"
DEFAULT_CRITERIA_PATH = REPO_ROOT / "taxonomy" / "genre_tree_node_criteria.json"
PROMPTS_DIR = REPO_ROOT / "prompts"
PROMPT_TEMPLATE = PROMPTS_DIR / "generadores" / "validate_master_layer2_prompt_template.md"
PROMPT_CONTEXT = PROMPTS_DIR / "generadores" / "validate_master_layer2_prompt_context.json"
VALIDATE_MASTER_STRATEGY = REPO_ROOT / "docs" / "operations" / "VALIDATE_MASTER_STRATEGY.md"
REPORTS_DIR = REPO_ROOT / "reports"
PROMPT_OUTPUT = PROMPTS_DIR / "prompt_arbol_semantico_capa2.txt"
DEFAULT_CYCLE_RESPONSE_BASENAME = "validate_master_layer2_response"
DEFAULT_MISSING_CRITERIA_OUTPUT = REPORTS_DIR / "genre_tree_node_criteria.missing.json"

# Cargar la última versión de contexto y template
CONTEXT_PATH = REPO_ROOT / "prompts" / "generadores" / "validate_master_layer2_prompt_context.json"
TEMPLATE_PATH = REPO_ROOT / "prompts" / "generadores" / "validate_master_layer2_prompt_template.md"
LOCAL_CONTEXT_PATH = REPO_ROOT / "context" / "contexto_validacion_arbol_llm.json"
LOCAL_TEMPLATE_PATH = REPO_ROOT / "prompts" / "generadores" / "template_prompt_arbol_semantico_capa2.md"

# Función para calcular hash de archivo
def file_hash(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

# Sincronizar contexto
if not LOCAL_CONTEXT_PATH.exists() or file_hash(CONTEXT_PATH) != file_hash(LOCAL_CONTEXT_PATH):
    print("Actualizando contexto local...")
    LOCAL_CONTEXT_PATH.write_text(CONTEXT_PATH.read_text(encoding="utf-8"), encoding="utf-8")
else:
    print("Contexto local ya está sincronizado.")

# Sincronizar template
if not LOCAL_TEMPLATE_PATH.exists() or file_hash(TEMPLATE_PATH) != file_hash(LOCAL_TEMPLATE_PATH):
    print("Actualizando template local...")
    LOCAL_TEMPLATE_PATH.write_text(TEMPLATE_PATH.read_text(encoding="utf-8"), encoding="utf-8")
else:
    print("Template local ya está sincronizado.")

# Argumentos principales
def parse_args():
    parser = argparse.ArgumentParser(description="Validación semántica (Capa 2) — Árbol de géneros musicales.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--print-prompt', action='store_true', help='Genera el prompt para la IA y lo guarda en prompts/.')
    group.add_argument('--apply-response', metavar='ARCHIVO_JSON', help='Procesa la respuesta JSON de la IA y genera reportes.')
    group.add_argument('--apply-cycle', metavar='DIRECTORIO_RESPUESTAS', help='Procesa respuestas en ciclo hasta no encontrar hallazgos.')
    return parser.parse_args()


def main():
    args = parse_args()
    if args.print_prompt:
        print("[MODO] Generar prompt para IA (por implementar)")
        # Aquí irá la lógica para construir y guardar el prompt
    elif args.apply_response:
        print(f"[MODO] Procesar respuesta IA: {args.apply_response} (por implementar)")
        # Aquí irá la lógica para procesar el JSON de respuesta
    elif args.apply_cycle:
        print(f"[MODO] Procesar ciclo de respuestas en: {args.apply_cycle} (por implementar)")
        # Aquí irá la lógica para el ciclo de respuestas
    else:
        print("[MODO] Validación determinista por defecto")
        resultados = validar_arbol_determinista()
        exportar_resultado_json(resultados, REPO_ROOT / "reports" / "reporte_validacion_arbol_script.json")
        exportar_resultado_md(resultados, REPO_ROOT / "reports" / "reporte_validacion_arbol_script.md")
        print("Validación determinista completada.")

def validar_arbol_determinista():
    tree_path = REPO_ROOT / "taxonomy" / "genre_tree_master.md"
    criteria_path = REPO_ROOT / "taxonomy" / "genre_tree_node_criteria.json"
    reglas_path = REPO_ROOT / "governance" / "reglas_validacion_arbol_script.md"
    with open(tree_path, encoding="utf-8") as f:
        tree_lines = f.readlines()
    with open(criteria_path, encoding="utf-8") as f:
        criterios = json.load(f)
    with open(reglas_path, encoding="utf-8") as f:
        reglas = f.read()
    nodos = parse_tree(tree_lines)
    nombres = [n['name'] for n in nodos]
    padres = [n['parent'] for n in nodos]
    resultados = {"timestamp": datetime.datetime.now().isoformat(), "errores": [], "advertencias": [], "ok": [], "detalle": {"arbol": tree_path.name, "criterios": criteria_path.name, "reglas": reglas_path.name}}

    # 1. Nodo raíz único (ARBOL-S-001)
    raices = [n for n in nodos if n['parent'] is None]
    if len(raices) != 1:
        resultados["errores"].append({"regla": "ARBOL-S-001", "descripcion": "La taxonomía debe tener un nodo raíz único.", "detalle": f"Se encontraron {len(raices)} nodos raíz: {[r['name'] for r in raices]}", "severidad": "FATAL"})
    else:
        resultados["ok"].append({"regla": "ARBOL-S-001", "descripcion": "La taxonomía debe tener un nodo raíz único.", "detalle": f"Raíz: {raices[0]['name']}", "severidad": "FATAL"})

    # 2. Unicidad de nombres (excepto clones) (ARBOL-S-002)
    # Considerar clones explícitos (nodos con atributo 'clone' o nombre igual a otro pero con sufijo/atributo especial)
    nombre_count = {}
    for n in nodos:
        nombre = n['name']
        nombre_count[nombre] = nombre_count.get(nombre, 0) + 1
    duplicados = [nombre for nombre, count in nombre_count.items() if count > 1]
    if duplicados:
        resultados["errores"].append({"regla": "ARBOL-S-002", "descripcion": "Cada nombre de género debe ser único en toda la taxonomía.", "detalle": f"Duplicados: {duplicados}", "severidad": "FATAL"})
    else:
        resultados["ok"].append({"regla": "ARBOL-S-002", "descripcion": "Cada nombre de género debe ser único en toda la taxonomía.", "detalle": "Sin duplicados detectados.", "severidad": "FATAL"})

    # 3. Checklist de calidad estructural (ARBOL-S-005)
    # Ejemplo simple: verificar que todos los nodos tengan nombre no vacío y que la profundidad máxima no sea excesiva
    profundidad_max = max([n['indent'] // 2 for n in nodos]) if nodos else 0
    nodos_vacios = [n['name'] for n in nodos if not n['name'].strip()]
    if nodos_vacios or profundidad_max > 6:
        detalle = []
        if nodos_vacios:
            detalle.append(f"Nodos sin nombre: {nodos_vacios}")
        if profundidad_max > 6:
            detalle.append(f"Profundidad máxima excesiva: {profundidad_max}")
        resultados["advertencias"].append({"regla": "ARBOL-S-005", "descripcion": "Checklist de calidad estructural debe cumplirse antes de release.", "detalle": "; ".join(detalle), "severidad": "WARNING"})
    else:
        resultados["ok"].append({"regla": "ARBOL-S-005", "descripcion": "Checklist de calidad estructural debe cumplirse antes de release.", "detalle": "Checklist estructural básica cumplida.", "severidad": "WARNING"})

    # 4. Idioma según rama Latin (ARBOL-S-003)
    for n in nodos:
        if n['parent'] == 'Latin':
            if not (re.match(r'^[A-Za-zÁÉÍÓÚáéíóúÑñ ]+$', n['name'])):
                resultados["advertencias"].append({"regla": "ARBOL-S-003", "descripcion": "Nombres en Latin deben estar en español o inglés reconocido.", "detalle": f"Nodo '{n['name']}' bajo Latin no cumple idioma.", "severidad": "WARNING"})
        elif n['parent'] and n['parent'] != 'Latin':
            if not re.match(r'^[A-Za-z ]+$', n['name']):
                resultados["advertencias"].append({"regla": "ARBOL-S-003", "descripcion": "Fuera de Latin, nombres deben estar en inglés.", "detalle": f"Nodo '{n['name']}' fuera de Latin no cumple idioma.", "severidad": "WARNING"})
    if not any(a['regla'] == 'ARBOL-S-003' for a in resultados['advertencias']):
        resultados["ok"].append({"regla": "ARBOL-S-003", "descripcion": "Idioma según rama Latin.", "detalle": "Todos los nodos cumplen idioma según rama.", "severidad": "WARNING"})

    # 5. Title Case (ARBOL-S-004)
    for n in nodos:
        if not is_title_case(n['name']):
            resultados["advertencias"].append({"regla": "ARBOL-S-004", "descripcion": "Todos los nombres de género deben estar en Title Case.", "detalle": f"Nodo '{n['name']}' no cumple Title Case.", "severidad": "WARNING"})
    if not any(a['regla'] == 'ARBOL-S-004' for a in resultados['advertencias']):
        resultados["ok"].append({"regla": "ARBOL-S-004", "descripcion": "Todos los nombres de género deben estar en Title Case.", "detalle": "Todos los nodos cumplen Title Case.", "severidad": "WARNING"})

    # 6. Nodos General (ARBOL-S-006)
    for n in nodos:
        if 'General' in n['name'] and not n['name'].endswith('(General)'):
            resultados["advertencias"].append({"regla": "ARBOL-S-006", "descripcion": "Los nodos General deben nombrarse como 'Parent Genre (General)'.", "detalle": f"Nodo '{n['name']}' no cumple convención General.", "severidad": "WARNING"})
    if not any(a['regla'] == 'ARBOL-S-006' for a in resultados['advertencias']):
        resultados["ok"].append({"regla": "ARBOL-S-006", "descripcion": "Los nodos General deben nombrarse como 'Parent Genre (General)'.", "detalle": "Todos los nodos General cumplen convención.", "severidad": "WARNING"})

    # 7. Nodos clone (ARBOL-S-007)
    # Para este ejemplo, consideramos que los clones tienen el mismo nombre que otro nodo y no deben tener hijos ni canciones propias
    # (En este árbol, no hay información de canciones por nodo, pero se puede validar unicidad y estructura)
    clones = [n for n in nodos if '(Clone)' in n['name'] or 'clone' in n['name'].lower()]
    for clone in clones:
        # Debe haber otro nodo con el mismo nombre base (sin sufijo Clone)
        base_name = clone['name'].replace('(Clone)', '').replace('clone', '').strip()
        if base_name not in nombres:
            resultados["advertencias"].append({"regla": "ARBOL-S-007", "descripcion": "Los nodos clone deben usar el mismo nombre que su nodo canónico.", "detalle": f"Clone '{clone['name']}' no tiene nodo canónico '{base_name}'.", "severidad": "WARNING"})
        # No debe tener hijos
        if clone['children']:
            resultados["advertencias"].append({"regla": "ARBOL-S-007", "descripcion": "Los nodos clone no deben tener hijos.", "detalle": f"Clone '{clone['name']}' tiene hijos: {clone['children']}", "severidad": "WARNING"})
    if not clones:
        resultados["ok"].append({"regla": "ARBOL-S-007", "descripcion": "Los nodos clone deben usar el mismo nombre que su nodo canónico y no deben tener canciones propias.", "detalle": "No hay nodos clone en el árbol.", "severidad": "WARNING"})

    # 8. Coincidencia exacta de nombres usados en clasificación vs definidos (ARBOL-S-008)
    # Leer géneros usados en catalog/songs_with_genres.csv y alias en data/genre_alias.csv
    import csv
    used_genres = set()
    try:
        with open(REPO_ROOT / 'catalog' / 'songs_with_genres.csv', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                for g in row['genres'].split('|'):
                    g = g.strip()
                    if g:
                        used_genres.add(g)
    except Exception as e:
        resultados["errores"].append({"regla": "ARBOL-S-008", "descripcion": "Error al leer géneros usados en clasificación.", "detalle": str(e), "severidad": "FATAL"})
        return resultados
    # Leer alias
    alias_map = {}
    try:
        with open(REPO_ROOT / 'data' / 'genre_alias.csv', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                alias_map[row['alias'].strip()] = row['canonical'].strip()
    except Exception as e:
        # Si no hay archivo de alias, continuar sin alias
        pass
    nombres_definidos = set(nombres)
    # Expandir géneros usados con alias
    used_genres_canon = set()
    for g in used_genres:
        if g in nombres_definidos:
            used_genres_canon.add(g)
        elif g in alias_map and alias_map[g] in nombres_definidos:
            used_genres_canon.add(alias_map[g])
        else:
            used_genres_canon.add(g)  # dejar el nombre original si no hay match
    # Buscar géneros usados no definidos
    no_definidos = [g for g in used_genres_canon if g not in nombres_definidos]
    if no_definidos:
        resultados["errores"].append({"regla": "ARBOL-S-008", "descripcion": "Los nombres de género usados en clasificación deben coincidir exactamente con los definidos en la taxonomía.", "detalle": f"No definidos: {no_definidos}", "severidad": "FATAL"})
    else:
        resultados["ok"].append({"regla": "ARBOL-S-008", "descripcion": "Los nombres de género usados en clasificación deben coincidir exactamente con los definidos en la taxonomía.", "detalle": "Todos los géneros usados están definidos o cubiertos por alias.", "severidad": "FATAL"})

    return resultados


def parse_tree(lines):
    """Convierte el árbol indentado en una lista de nodos con jerarquía."""
    stack = []
    nodes = []
    for line in lines:
        stripped = line.rstrip('\n')
        if not stripped.strip():
            continue
        indent = len(stripped) - len(stripped.lstrip(' '))
        name = stripped.strip()
        node = {'name': name, 'children': [], 'parent': None, 'indent': indent}
        while stack and stack[-1]['indent'] >= indent:
            stack.pop()
        if stack:
            node['parent'] = stack[-1]['name']
            stack[-1]['children'].append(name)
        nodes.append(node)
        stack.append(node)
    return nodes


def is_title_case(name):
    return name == name.title()


def exportar_resultado_json(resultados, ruta):
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(resultados, f, ensure_ascii=False, indent=2)
    print(f"Reporte JSON generado en: {ruta}")


def exportar_resultado_md(resultados, ruta_md):
    with open(ruta_md, "w", encoding="utf-8") as f:
        f.write(f"# Reporte de Validación Determinista del Árbol\n")
        f.write(f"Fecha: {resultados['timestamp']}\n\n")
        f.write(f"## Archivos utilizados\n")
        f.write(f"- Árbol: {resultados['detalle']['arbol']}\n")
        f.write(f"- Criterios: {resultados['detalle']['criterios']}\n")
        f.write(f"- Reglas: {resultados['detalle']['reglas']}\n\n")
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
