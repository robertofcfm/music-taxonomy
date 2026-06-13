from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[2]
SONGS_CSV = ROOT / 'catalog' / 'songs_with_genres.csv'
if not SONGS_CSV.exists():
    raise SystemExit(f"File not found: {SONGS_CSV}")

ratings = [
    ("The Day Of The Greys","4hero","Music > Electronic > Drum And Bass","96"),
    ("Hyper Sun","Black Sun Empire","Music > Electronic > Drum And Bass","98"),
    ("Why We Lose","Cartoon","Music > Electronic > Drum And Bass","83"),
    ("Renegade Snares","Omni Trio","Music > Electronic > Drum And Bass","99"),
    ("Feel the Love (feat. John Newman)","Rudimental","Music > Electronic > Drum And Bass","88"),
    ("Waiting All Night (feat. Ella Eyre)","Rudimental","Music > Electronic > Drum And Bass","90"),
    ("Stompbox","The Qemists","Music > Electronic > Drum And Bass","87"),
]

# Build lookup by exact match of title, artist, genre
lookup = { (t.strip(), a.strip(), g.strip()): val.strip() for t,a,g,val in ratings }

with SONGS_CSV.open('r', newline='', encoding='utf-8') as fin:
    rows = list(csv.reader(fin))
    if not rows:
        raise SystemExit('Empty songs file')
    header = rows[0]
    data = rows[1:]

# find indices
hl = [h.strip().lower() for h in header]
if 'calificacion' not in hl:
    # add column
    header.append('calificacion')
    cal_idx = len(header)-1
    for i,row in enumerate(data):
        if len(row) < len(header):
            row.extend([''] * (len(header)-len(row)))
else:
    cal_idx = hl.index('calificacion')

if 'genre' in hl:
    genre_idx = hl.index('genre')
elif 'genero' in hl:
    genre_idx = hl.index('genero')
else:
    raise SystemExit('No genre column')

# locate title and artist indices (common names)
if 'title' in hl:
    title_idx = hl.index('title')
else:
    title_idx = 0
if 'artist' in hl:
    artist_idx = hl.index('artist')
else:
    artist_idx = 1

updated = []
for row in data:
    title = row[title_idx].strip()
    artist = row[artist_idx].strip()
    genre = row[genre_idx].strip()
    key = (title, artist, genre)
    if key in lookup:
        row_len_needed = len(header)
        if len(row) < row_len_needed:
            row.extend([''] * (row_len_needed - len(row)))
        row[cal_idx] = lookup[key]
        updated.append((title, artist, genre, lookup[key]))

# write back
with SONGS_CSV.open('w', newline='', encoding='utf-8') as fout:
    writer = csv.writer(fout)
    writer.writerow(header)
    writer.writerows(data)

print(f'Updated {len(updated)} rows')
for u in updated:
    print(','.join(u))
