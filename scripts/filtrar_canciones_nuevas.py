import csv
import json
import os
import unicodedata

# Archivos de entrada y salida (rutas relativas al root del proyecto)
songs_raw = 'catalog/songs_raw.csv'
songs_with_genres = 'catalog/songs_with_genres.csv'
output_json = 'reports/canciones_nuevas.json'


def normaliza(texto):
    # Normaliza a Unicode NFC para evitar diferencias entre ñ compuesta y precompuesta
    texto = unicodedata.normalize('NFC', texto)
    # Elimina cualquier tipo de comillas (rectas y tipográficas)
    caracteres_a_eliminar = ['"', "'", '“', '”', '‘', '’', '«', '»', '`', '´', '\\', '/']
    for c in caracteres_a_eliminar:
        texto = texto.replace(c, '')
    return texto.strip().lower()

try:
    # Leer canciones ya procesadas
    procesadas = set()
    with open(songs_with_genres, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            key = (normaliza(row['title']), normaliza(row['artist']))
            procesadas.add(key)
    print(f"Canciones procesadas: {len(procesadas)}")

    # Leer todas las canciones y filtrar nuevas
    nuevas = []
    total_raw = 0
    claves_raw = set()
    duplicados_raw = 0
    registros_duplicados = []
    with open(songs_raw, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            total_raw += 1
            key = (normaliza(row['title']), normaliza(row['artist']))
            if key in claves_raw:
                duplicados_raw += 1
                registros_duplicados.append({"title": row['title'], "artist": row['artist']})
            else:
                claves_raw.add(key)
            if key not in procesadas:
                nuevas.append({"title": row['title'], "artist": row['artist']})
    print(f"Total canciones en songs_raw.csv: {total_raw}")
    print(f"Canciones únicas en songs_raw.csv: {len(claves_raw)}")
    print(f"Duplicados en songs_raw.csv: {duplicados_raw}")
    if registros_duplicados:
        print("Ejemplos de registros duplicados:")
        for reg in registros_duplicados[:10]:
            print(f"- {reg['title']} / {reg['artist']}")
        if len(registros_duplicados) > 10:
            print(f"... y {len(registros_duplicados) - 10} más")
    print(f"Canciones nuevas detectadas: {len(nuevas)}")

    # Guardar solo las primeras 20 canciones nuevas en JSON
    lote = nuevas[:20]
    os.makedirs(os.path.dirname(output_json), exist_ok=True)
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(lote, f, ensure_ascii=False, indent=2)

    if lote:
        print("Ejemplo de canciones nuevas (lote actual):")
        for c in lote:
            print(f"- {c['title']} / {c['artist']}")
    else:
        print("No hay canciones nuevas para procesar.")
except Exception as e:
    print(f"Error durante la ejecución: {e}")
