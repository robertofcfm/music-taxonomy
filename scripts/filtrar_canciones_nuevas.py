import csv
import json
import os
import unicodedata

# Archivos de entrada y salida (rutas relativas al root del proyecto)
songs_raw = 'catalog/favorites_qobuz.csv'
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
            key = (normaliza(row['title']), normaliza(row['artist']), normaliza(row.get('isrc','')))
            if key in claves_raw:
                duplicados_raw += 1
                registros_duplicados.append({"title": row['title'], "artist": row['artist'], "isrc": row.get('isrc','')})
            else:
                claves_raw.add(key)
            if (normaliza(row['title']), normaliza(row['artist'])) not in procesadas:
                nuevas.append({"title": row['title'], "artist": row['artist'], "isrc": row.get('isrc','')})
    print(f"Total canciones en favorites_qobuz.csv: {total_raw}")
    print(f"Canciones únicas en favorites_qobuz.csv: {len(claves_raw)}")
    print(f"Duplicados en favorites_qobuz.csv: {duplicados_raw}")
    if registros_duplicados:
        print("Ejemplos de registros duplicados:")
        for reg in registros_duplicados[:10]:
            print(f"- {reg['title']} / {reg['artist']} / {reg['isrc']}")
        if len(registros_duplicados) > 10:
            print(f"... y {len(registros_duplicados) - 10} más")
    print(f"Canciones nuevas detectadas: {len(nuevas)}")

    # Guardar solo las primeras 20 canciones nuevas en JSON
    lote = nuevas[:20]
    os.makedirs(os.path.dirname(output_json), exist_ok=True)
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(lote, f, ensure_ascii=False, indent=2)


    # Guardar el detalle completo de canciones nuevas en CSV
    detalle_csv = 'reports/canciones_nuevas_detalle.csv'
    with open(detalle_csv, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['title', 'artist', 'isrc'])
        writer.writeheader()
        for c in nuevas:
            writer.writerow(c)
    print(f"Reporte de canciones nuevas generado: {detalle_csv} ({len(nuevas)} canciones)")

    # Si hay diferencia, guardar los pares (title, artist) de favorites_qobuz.csv que no están en songs_with_genres.csv
    if len(claves_raw) != len(procesadas):
        faltantes = []
        with open(songs_raw, encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                key = (normaliza(row['title']), normaliza(row['artist']))
                if key not in procesadas:
                    faltantes.append({'title': row['title'], 'artist': row['artist'], 'isrc': row.get('isrc','')})
        faltantes_csv = 'reports/canciones_faltantes_title_artist.csv'
        with open(faltantes_csv, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['title', 'artist', 'isrc'])
            writer.writeheader()
            for c in faltantes:
                writer.writerow(c)
        print(f"Reporte de pares (title, artist) faltantes generado: {faltantes_csv} ({len(faltantes)} canciones)")

    if lote:
        print("Ejemplo de canciones nuevas (lote actual):")
        for c in lote:
            print(f"- {c['title']} / {c['artist']} / {c['isrc']}")
    else:
        print("No hay canciones nuevas para procesar.")
except Exception as e:
    print(f"Error durante la ejecución: {e}")
