from pathlib import Path
import csv
ROOT = Path(__file__).resolve().parents[2]
SONGS = ROOT / 'catalog' / 'songs_with_genres.csv'
CONTEO = ROOT / 'reports' / 'conteo_generos_ascendente.csv'

with SONGS.open('r',encoding='utf-8') as f:
    s=list(csv.reader(f))
    header=s[0]; rows=s[1:]
    hl=[h.strip().lower() for h in header]
    print('header:', header)
    print('has calificacion?', 'calificacion' in hl)
    print('has genre?', 'genre' in hl or 'genero' in hl)
    cal_idx=hl.index('calificacion')
    genre_idx=hl.index('genre') if 'genre' in hl else hl.index('genero')

with CONTEO.open('r',encoding='utf-8') as f:
    c=list(csv.reader(f))
    print('first conteo genre:', c[1][0])
    first=c[1][0].strip()

matches=[r for r in rows if (r[cal_idx].strip() if len(r)>cal_idx else '')=='' and (r[genre_idx].strip() if len(r)>genre_idx else '')==first]
print('matches found:', len(matches))
for m in matches[:10]:
    print(m)
