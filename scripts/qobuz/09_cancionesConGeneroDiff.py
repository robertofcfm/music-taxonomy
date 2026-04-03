
import csv
import os

# Rutas absolutas basadas en la ubicación de este script
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
file_canciones_con_genero = os.path.join(BASE_DIR, 'catalog', 'cancionesConGenero.csv')
file_list_qobuz = os.path.join(BASE_DIR, 'catalog', 'list_qobuz.csv')
file_output = os.path.join(BASE_DIR, 'catalog', 'cancionesConGeneroDiff.csv')


# Leer pares (isrc, genre) de list_qobuz.csv, concatenando 'Music > ' al genre
isrc_genre_qobuz = set()
with open(file_list_qobuz, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        isrc = row['isrc'].strip()
        genre = row.get('genre', '').strip()
        genre = f"Music > {genre}" if genre else ''
        isrc_genre_qobuz.add((isrc, genre))



# Filtrar canciones de cancionesConGenero.csv que no están en list_qobuz.csv, aplicando strip y concatenando versiones
rows_diff = []
with open(file_canciones_con_genero, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    # Aseguramos que los headers incluyan los campos esperados
    base_fields = ['title', 'artist', 'album', 'isrc', 'genre']
    extra_fields = []
    if 'title_version' in reader.fieldnames:
        extra_fields.append('title_version')
    if 'album_version' in reader.fieldnames:
        extra_fields.append('album_version')
    header = base_fields.copy()
    # Para compatibilidad, no agregamos los campos version al header, solo los usamos para concatenar
    for row in reader:
        row_clean = {k: (v.strip() if isinstance(v, str) else v) for k, v in row.items()}
        isrc = row_clean.get('isrc', '')
        genre = row_clean.get('genre', '')
        if (isrc, genre) not in isrc_genre_qobuz:
            # Concatenar title + title_version si existe
            title = row_clean.get('title', '')
            title_version = row_clean.get('title_version', '')
            if title_version:
                title = f"{title} {title_version}"
            # Concatenar album + album_version si existe
            album = row_clean.get('album', '')
            album_version = row_clean.get('album_version', '')
            if album_version:
                album = f"{album} {album_version}"
            # Construir la fila de salida
            row_out = {
                'title': title,
                'artist': row_clean.get('artist', ''),
                'album': album,
                'isrc': row_clean.get('isrc', ''),
                'genre': row_clean.get('genre', '')
            }
            rows_diff.append(row_out)

# Escribir resultado
with open(file_output, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=base_fields)
    writer.writeheader()
    writer.writerows(rows_diff)

print(f"Canciones exportadas: {len(rows_diff)}")
