from pathlib import Path
import csv
import sys

ROOT = Path(__file__).resolve().parents[2]
SONGS_INPUT = ROOT / 'catalog' / 'songs_with_genres.csv'
CONTEO = ROOT / 'reports' / 'conteo_generos_ascendente.csv'
OUTPUT_DIR = ROOT / 'reports'
OUTPUT = OUTPUT_DIR / 'unrated_first_20.csv'
LIMIT = 20

if not SONGS_INPUT.exists():
    raise SystemExit(f"Songs file not found: {SONGS_INPUT}")
if not CONTEO.exists():
    raise SystemExit(f"Conteo file not found: {CONTEO}")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Load songs into memory once
with SONGS_INPUT.open('r', newline='', encoding='utf-8') as fin:
    reader = list(csv.reader(fin))
    if not reader:
        raise SystemExit('Songs CSV is empty')
    header = reader[0]
    rows = reader[1:]

header_lower = [h.strip().lower() for h in header]
if 'calificacion' not in header_lower:
    raise SystemExit('No "calificacion" column found in songs header')
if 'genre' not in header_lower and 'genero' not in header_lower:
    raise SystemExit('No "genre" column found in songs header')

cal_idx = header_lower.index('calificacion')
# prefer 'genre' but accept 'genero'
if 'genre' in header_lower:
    genre_idx = header_lower.index('genre')
else:
    genre_idx = header_lower.index('genero')

# Read conteo file and iterate genres in order
with CONTEO.open('r', newline='', encoding='utf-8') as fcon:
    creader = csv.reader(fcon)
    try:
        ch = next(creader)
    except StopIteration:
        raise SystemExit('Conteo CSV is empty')

    found = False
    collected = []
    for crow in creader:
        if not crow:
            continue
        genre_value = crow[0].strip()
        if not genre_value:
            continue

        # collect up to LIMIT songs matching this genre with empty calificacion
        matches = []
        for row in rows:
            # safe access
            r_genre = row[genre_idx].strip() if len(row) > genre_idx else ''
            r_cal = row[cal_idx].strip() if len(row) > cal_idx else ''
            if r_cal == '' and r_genre == genre_value:
                matches.append(row)
            if len(matches) >= LIMIT:
                break

        if matches:
            collected.extend(matches)
            print(f'Found {len(matches)} unrated songs for genre: "{genre_value}"')
            found = True
            break
    # write collected results at the end
    if found and collected:
        with OUTPUT.open('w', newline='', encoding='utf-8') as fout:
            writer = csv.writer(fout)
            writer.writerow(header)
            for r in collected:
                if len(r) < len(header):
                    r = r + [''] * (len(header) - len(r))
                writer.writerow(r)
        print(f'Wrote {len(collected)} unrated rows to: {OUTPUT}')
    else:
        print('No unrated songs found for any genre in conteo_generos_ascendente.csv')
        with OUTPUT.open('w', newline='', encoding='utf-8') as fout:
            writer = csv.writer(fout)
            writer.writerow(header)

    sys.exit(0)
