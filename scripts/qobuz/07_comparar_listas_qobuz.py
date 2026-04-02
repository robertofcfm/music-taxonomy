import csv
import os

CATALOG_DIR = os.path.join(os.path.dirname(__file__), '../../catalog')
FILE_A = os.path.join(CATALOG_DIR, 'cancionesConGenero.csv')
FILE_B = os.path.join(CATALOG_DIR, 'list_qobuz.csv')
ADD_FILE = os.path.join(CATALOG_DIR, 'list_qobuz_add.csv')
REMOVE_FILE = os.path.join(CATALOG_DIR, 'list_qobuz_remove.csv')


def read_csv_set(filepath):
    with open(filepath, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        # Buscar índices de los campos
        try:
            idx_title = header.index('title')
            idx_artist = header.index('artist')
            idx_album = header.index('album')
            idx_isrc = header.index('isrc')
            idx_genre = header.index('genre')
        except ValueError:
            raise Exception(f"No se encontraron columnas necesarias en {filepath}")
        rows = []
        for row in reader:
            # Si es cancionesConGenero.csv, limpiar el prefijo 'Music > ' en genre
            genre = row[idx_genre]
            if os.path.basename(filepath) == 'cancionesConGenero.csv' and genre.startswith('Music > '):
                genre = genre[len('Music > '):].strip()
            rows.append((row[idx_title], row[idx_artist], row[idx_album], row[idx_isrc], genre))
    return header, set(rows)


def write_csv(filepath, header, rows):
    # Escribir title, artist, album, isrc, genre
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['title', 'artist', 'album', 'isrc', 'genre'])
        for row in rows:
            writer.writerow(row)


def main():
    print(f"Leyendo {FILE_A} ...")
    header_a, set_a = read_csv_set(FILE_A)
    print(f"Leyendo {FILE_B} ...")
    header_b, set_b = read_csv_set(FILE_B)

    # Comparar por isrc y genre (ya limpio en cancionesConGenero)
    def key_isrc_genre(row):
        return (row[3], row[4])  # isrc, genre

    set_a_keys = set(key_isrc_genre(row) for row in set_a)
    set_b_keys = set(key_isrc_genre(row) for row in set_b)

    add_rows = sorted([row for row in set_a if key_isrc_genre(row) not in set_b_keys])
    remove_rows = sorted([row for row in set_b if key_isrc_genre(row) not in set_a_keys])

    write_csv(ADD_FILE, ['title', 'artist', 'album', 'isrc', 'genre'], add_rows)
    write_csv(REMOVE_FILE, ['title', 'artist', 'album', 'isrc', 'genre'], remove_rows)

    total_a = len(set_a)
    total_b = len(set_b)
    coinciden = len(set_a_keys & set_b_keys)
    solo_a = len(add_rows)
    solo_b = len(remove_rows)

    print("\nResumen de comparación:")
    print(f"Total canciones en {os.path.basename(FILE_A)}: {total_a}")
    print(f"Total canciones en {os.path.basename(FILE_B)}: {total_b}")
    print(f"Coinciden por isrc/genre: {coinciden}")
    print(f"Solo en {os.path.basename(FILE_A)}: {solo_a}")
    print(f"Solo en {os.path.basename(FILE_B)}: {solo_b}")

    print(f"\nRegistros únicos por isrc/genre en {FILE_A} y NO en {FILE_B}: {solo_a} → {ADD_FILE}")
    print(f"Registros únicos por isrc/genre en {FILE_B} y NO en {FILE_A}: {solo_b} → {REMOVE_FILE}")
    print("Comparación por isrc/genre completada.")


if __name__ == '__main__':
    main()
