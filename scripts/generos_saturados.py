import csv
import json
from collections import Counter

# Parámetro de umbral
X = 45  # Puedes ajustar este valor según necesidad

input_csv = '../catalog/songs_with_genres.csv'
output_json = '../reports/generos_saturados.json'
output_all_json = '../reports/generos_conteo_total.json'

# Leer el archivo CSV y contar géneros
with open(input_csv, encoding='utf-8') as f:
    reader = csv.DictReader(f)
    genre_counts = Counter(row['genre'] for row in reader)

# Filtrar géneros saturados
saturados = [
    {"genre": genre, "count": count}
    for genre, count in genre_counts.items() if count > X
]

# Guardar resultado en JSON de saturados
with open(output_json, 'w', encoding='utf-8') as f:
    json.dump(saturados, f, ensure_ascii=False, indent=2)

# Guardar el conteo total de todos los géneros
all_genres = [
    {"genre": genre, "count": count}
    for genre, count in genre_counts.items()
]
with open(output_all_json, 'w', encoding='utf-8') as f:
    json.dump(all_genres, f, ensure_ascii=False, indent=2)

# Presentación legible para usuario
print("Conteo de canciones por género:")
for g in sorted(all_genres, key=lambda x: x['count'], reverse=True):
    print(f"- {g['genre']}: {g['count']} canciones")

if saturados:
    print(f"\nGéneros saturados (más de {X} canciones):")
    for g in saturados:
        print(f"- {g['genre']}: {g['count']} canciones")
else:
    print(f"\nNo hay géneros saturados para el umbral actual ({X}).")
