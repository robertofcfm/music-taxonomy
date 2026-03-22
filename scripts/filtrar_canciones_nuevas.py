import csv
import json
import os

# Archivos de entrada y salida (rutas relativas al root del proyecto)
songs_raw = 'catalog/songs_raw.csv'
songs_with_genres = 'catalog/songs_with_genres.csv'
output_json = 'reports/canciones_nuevas.json'

try:
    # Leer canciones ya procesadas
    procesadas = set()
    with open(songs_with_genres, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            key = (row['title'].strip().lower(), row['artist'].strip().lower())
            procesadas.add(key)
    print(f"Canciones procesadas: {len(procesadas)}")

    # Leer todas las canciones y filtrar nuevas
    nuevas = []
    total_raw = 0
    with open(songs_raw, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            total_raw += 1
            key = (row['title'].strip().lower(), row['artist'].strip().lower())
            if key not in procesadas:
                nuevas.append({"title": row['title'], "artist": row['artist']})
    print(f"Total canciones en songs_raw.csv: {total_raw}")
    print(f"Canciones nuevas detectadas: {len(nuevas)}")

    # Guardar resultado en JSON
    os.makedirs(os.path.dirname(output_json), exist_ok=True)
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(nuevas, f, ensure_ascii=False, indent=2)

    if nuevas:
        print("Ejemplo de canciones nuevas:")
        for c in nuevas[:10]:
            print(f"- {c['title']} / {c['artist']}")
    else:
        print("No hay canciones nuevas para procesar.")
except Exception as e:
    print(f"Error durante la ejecución: {e}")
