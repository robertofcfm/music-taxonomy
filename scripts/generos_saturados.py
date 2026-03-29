
import csv
import json
from collections import defaultdict

def extraer_ramas_arbol(path):
    """
    Lee el archivo genre_tree_master.md y devuelve una lista de paths completos (ramas).
    """
    ramas = []
    stack = []
    with open(path, encoding='utf-8') as f:
        for line in f:
            stripped = line.rstrip('\n')
            if not stripped.strip():
                continue
            indent = len(stripped) - len(stripped.lstrip(' '))
            nivel = indent // 2
            nombre = stripped.strip()
            if len(stack) > nivel:
                stack = stack[:nivel]
            stack.append(nombre)
            ramas.append(' > '.join(stack))
    return ramas

# Parámetro de umbral
X = 45  # Puedes ajustar este valor según necesidad

input_csv = 'catalog/songs_with_genres.csv'
output_json = 'reports/generos_saturados.json'
output_all_json = 'reports/generos_conteo_total.json'
output_md = 'reports/generos_saturados.md'

# Leer el archivo CSV y recolectar todos los géneros y canciones
rows = []
with open(input_csv, encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows.append(row)

# Solo géneros no vacíos ni nulos
genres = [row['genre'] for row in rows if row.get('genre') and row['genre'].strip()]

# Obtener todos los prefijos posibles
all_prefixes = set()
for genre in genres:
    if not genre:
        continue
    parts = genre.split(' > ')
    for i in range(1, len(parts)+1):
        prefix = ' > '.join(parts[:i])
        all_prefixes.add(prefix)

# Contar acumulativamente por prefijo
prefix_counts = {}
for prefix in all_prefixes:
    prefix_counts[prefix] = sum(1 for g in genres if prefix in g)

# Filtrar géneros saturados
saturados = [
    {"genre": genre, "count": count}
    for genre, count in prefix_counts.items() if count > X
]

# Nueva lógica: distinguir Nodo saturado y Género de Paso
reporte = []
for entry in saturados:
    nodo = entry['genre']
    canciones_con_prefijo = [row for row in rows if row.get('genre') and nodo in row['genre']]
    exactos = [row for row in canciones_con_prefijo if row['genre'] == nodo]
    de_paso = [row for row in canciones_con_prefijo if row['genre'] != nodo]
    clasificacion = "Nodo saturado" if len(exactos) > 0 else "Género de Paso"
    reporte.append({
        "nodo": nodo,
        "total": len(canciones_con_prefijo),
        "exactos": len(exactos),
        "de_paso": len(de_paso),
        "clasificacion": clasificacion,
        "ejemplos_exactos": exactos[:3],
        "ejemplos_de_paso": de_paso[:3]
    })

# Guardar resultado en JSON de saturados extendido
with open(output_json, 'w', encoding='utf-8') as f:
    json.dump(reporte, f, ensure_ascii=False, indent=2)

# Guardar el conteo total de todos los prefijos
all_genres = [
    {"genre": genre, "count": count}
    for genre, count in sorted(prefix_counts.items(), key=lambda x: x[1], reverse=True)
]
with open(output_all_json, 'w', encoding='utf-8') as f:
    json.dump(all_genres, f, ensure_ascii=False, indent=2)

# Generar Markdown
with open(output_md, 'w', encoding='utf-8') as f:
    f.write(f"# Reporte de Géneros Saturados (umbral: {X})\n\n")
    for r in reporte:
        f.write(f"## {r['nodo']}\n")
        f.write(f"- Total canciones con este prefijo: {r['total']}\n")
        f.write(f"- Coincidencia exacta (Nodo saturado): {r['exactos']}\n")
        f.write(f"- Solo de paso: {r['de_paso']}\n")
        f.write(f"- Clasificación: **{r['clasificacion']}**\n")
        if r['ejemplos_exactos']:
            f.write(f"  - Ejemplos exactos:\n")
            for e in r['ejemplos_exactos']:
                f.write(f"    - {e['title']} — {e['artist']}\n")
        if r['ejemplos_de_paso']:
            f.write(f"  - Ejemplos de paso:\n")
            for e in r['ejemplos_de_paso']:
                f.write(f"    - {e['title']} — {e['artist']} ({e['genre']})\n")
        f.write("\n")


# Presentación legible para usuario

# --- Comparar ramas del árbol con prefijos de géneros ---
arbol_path = 'taxonomy/genre_tree_master.md'
ramas_arbol = set(extraer_ramas_arbol(arbol_path))
ramas_en_datos = set(all_prefixes)

ramas_presentes = ramas_arbol & ramas_en_datos
ramas_faltantes = ramas_arbol - ramas_en_datos
ramas_sobrantes = ramas_en_datos - ramas_arbol

print("\n--- Comparación ramas del árbol vs. datos ---")
print(f"Total ramas en árbol: {len(ramas_arbol)}")
print(f"Ramas presentes en datos: {len(ramas_presentes)}")
print(f"Ramas faltantes en datos: {len(ramas_faltantes)}")
if ramas_faltantes:
    print("\nLista de ramas faltantes:")
    for rama in sorted(ramas_faltantes):
        print(f"- {rama}")

print(f"\nRamas sobrantes en datos (no existen en árbol): {len(ramas_sobrantes)}")
if ramas_sobrantes:
    print("\nLista de ramas sobrantes:")
    for rama in sorted(ramas_sobrantes):
        print(f"- {rama}")

# Ordenar la lista de géneros alfabéticamente por node path
all_genres_sorted = sorted(all_genres, key=lambda x: x['genre'])
print("Conteo acumulado de canciones por género (orden alfabético por node path):")
for g in all_genres_sorted:
    print(f"- {g['genre']}: {g['count']} canciones")

print(f"\nReporte de géneros saturados (umbral: {X}):\n")
# Ordenar reporte alfabéticamente por el path del nodo
for r in sorted(reporte, key=lambda x: x['nodo']):
    print(f"- {r['nodo']}: Total={r['total']} | Exactos={r['exactos']} | De paso={r['de_paso']} | Clasificación={r['clasificacion']}")
