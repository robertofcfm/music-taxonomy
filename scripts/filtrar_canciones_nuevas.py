import csv
import json
import os
import unicodedata

# Archivos de entrada y salida (rutas relativas al root del proyecto)
songs_raw = 'catalog/favorites_qobuz.csv'
songs_with_genres = 'catalog/songs_with_genres.csv'
output_json = 'reports/canciones_nuevas.json'


def elimina_tildes_ortograficas(texto):
    descompuesto = unicodedata.normalize('NFD', texto)
    caracteres = []
    for indice, caracter in enumerate(descompuesto):
        if not unicodedata.combining(caracter):
            caracteres.append(caracter)
            continue

        base = descompuesto[indice - 1] if indice > 0 else ''
        # Conserva la ñ/Ñ, pero elimina otros acentos ortográficos.
        if caracter == '\u0303' and base.lower() == 'n':
            caracteres.append(caracter)

    return unicodedata.normalize('NFC', ''.join(caracteres))


def normaliza(texto):
    if texto is None:
        return ''

    # Normaliza a Unicode NFC para evitar diferencias entre ñ compuesta y precompuesta
    texto = unicodedata.normalize('NFC', str(texto))
    texto = elimina_tildes_ortograficas(texto)
    # Elimina cualquier tipo de comillas (rectas y tipográficas)
    caracteres_a_eliminar = ['"', "'", '"', '"', ''', ''', '«', '»', '`', '´', '\\', '/']
    for c in caracteres_a_eliminar:
        texto = texto.replace(c, '')
    return ' '.join(texto.split()).casefold()


def normaliza_header(cabecera):
    if cabecera is None:
        return ''
    cabecera = cabecera.lstrip('\ufeff').strip()
    if cabecera.startswith('"') and cabecera.endswith('"'):
        cabecera = cabecera[1:-1]
    return cabecera.strip().casefold()


def dict_reader_normalizado(path):
    with open(path, encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        if reader.fieldnames:
            reader.fieldnames = [normaliza_header(name) for name in reader.fieldnames]
        for row in reader:
            yield {normaliza_header(key): value for key, value in row.items()}


try:
    # Leer canciones ya procesadas
    procesadas = set()
    for row in dict_reader_normalizado(songs_with_genres):
        key = (normaliza(row['title']), normaliza(row['artist']))
        procesadas.add(key)
    print(f"Canciones procesadas: {len(procesadas)}")

    # Leer todas las canciones y filtrar nuevas
    nuevas = []
    total_raw = 0
    claves_raw = set()
    duplicados_raw = 0
    registros_duplicados = []
    for row in dict_reader_normalizado(songs_raw):
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
    print(f"Reporte de canciones nuevas generado: {output_json} ({len(lote)} canciones)")

except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
