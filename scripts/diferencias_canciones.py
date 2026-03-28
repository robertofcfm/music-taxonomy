
import csv
import unicodedata
from collections import Counter

def normaliza(texto):
    texto = unicodedata.normalize('NFC', texto)
    return texto.replace('"', '').replace("'", '').strip().lower()


def main():
    songs_raw = 'catalog/songs_raw.csv'
    songs_with_genres = 'catalog/songs_with_genres.csv'

    # Leer canciones en songs_raw.csv (solo título y artista)
    raw_set = set()
    with open(songs_raw, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            key = (normaliza(row['title']), normaliza(row['artist']))
            raw_set.add(key)

    # Leer canciones en songs_with_genres.csv y contar duplicados (título, artista, género)
    proc_counter = Counter()
    proc_title_artist_set = set()
    with open(songs_with_genres, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            key = (normaliza(row['title']), normaliza(row['artist']), normaliza(row['genre']))
            proc_counter[key] += 1
            # Para comparar con raw, solo título y artista
            proc_title_artist_set.add((normaliza(row['title']), normaliza(row['artist'])))

    # Canciones procesadas que no están en el raw (por título y artista)
    solo_en_proc = proc_title_artist_set - raw_set
    # Canciones en raw que no están procesadas (por título y artista)
    solo_en_raw = raw_set - proc_title_artist_set
    # Duplicados en songs_with_genres.csv (título, artista, género)
    duplicados = {k: v for k, v in proc_counter.items() if v > 1}

    print('Canciones en songs_with_genres.csv que NO están en songs_raw.csv:')
    for t, a in sorted(solo_en_proc):
        print(f'  - "{t}" / "{a}"')

    print('\nCanciones en songs_raw.csv que NO están en songs_with_genres.csv:')
    for t, a in sorted(solo_en_raw):
        print(f'  - "{t}" / "{a}"')

    print(f'\nTotal solo en procesadas: {len(solo_en_proc)}')
    print(f'Total solo en raw: {len(solo_en_raw)}')
    print(f'Total en ambos: {len(raw_set & proc_title_artist_set)}')

    print('\nDuplicados en songs_with_genres.csv (título, artista, género):')
    for (t, a, g), v in sorted(duplicados.items(), key=lambda x: (-x[1], x[0])):
        print(f'  - "{t}" / "{a}" / "{g}" (veces: {v})')
    print(f'Total de pares duplicados: {len(duplicados)}')

if __name__ == "__main__":
    main()
