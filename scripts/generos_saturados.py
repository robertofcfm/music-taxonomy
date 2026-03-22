import csv
import json
from collections import Counter, defaultdict

# Parámetro de umbral
X = 45  # Puedes ajustar este valor según necesidad

input_csv = 'catalog/songs_with_genres.csv'
output_json = 'reports/generos_saturados.json'
output_all_json = 'reports/generos_conteo_total.json'

# Leer el archivo CSV y recolectar todos los géneros
with open(input_csv, encoding='utf-8') as f:
    reader = csv.DictReader(f)
    genres = [row['genre'] for row in reader]

# Obtener todos los prefijos posibles
all_prefixes = set()
for genre in genres:
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

# Guardar resultado en JSON de saturados
with open(output_json, 'w', encoding='utf-8') as f:
    json.dump(saturados, f, ensure_ascii=False, indent=2)

# Guardar el conteo total de todos los prefijos
all_genres = [
    {"genre": genre, "count": count}
    for genre, count in sorted(prefix_counts.items(), key=lambda x: x[1], reverse=True)
]
with open(output_all_json, 'w', encoding='utf-8') as f:
    json.dump(all_genres, f, ensure_ascii=False, indent=2)

# Presentación legible para usuario
print("Conteo acumulado de canciones por género:")
for g in all_genres:
    print(f"- {g['genre']}: {g['count']} canciones")

if saturados:
    print(f"\nGéneros saturados (más de {X} canciones):")
    for g in saturados:
        print(f"- {g['genre']}: {g['count']} canciones")
else:
    print(f"\nNo hay géneros saturados para el umbral actual ({X}).")
