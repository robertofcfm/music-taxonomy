import requests
import csv
import time
import sys
import os

# ==========================
# CONFIGURACIÓN
# ==========================
APP_ID = "798273057"
USER_TOKEN = "Qc0Ymlge2cx2NvQcEmF7tEK5lpmORoeEy1zSjUqkyyEas7mdXOnsPkYcGRoBfSNat2SmkY7oqWCjkZ9SzTUYfQ"
BASE_URL = "https://www.qobuz.com/api.json/0.2"

HEADERS = {
    "X-App-Id": APP_ID,
    "X-User-Auth-Token": USER_TOKEN
}

LIMIT = 100

# ==========================
# UTILIDADES
# ==========================
def safe_request(url, params):
    r = requests.get(url, headers=HEADERS, params=params)
    if "application/json" not in r.headers.get("Content-Type", ""):
        print("\n[ERROR] Qobuz devolvió HTML. Token inválido o rate limit.")
        sys.exit()
    return r.json()

def clean_value(val):
    if isinstance(val, str):
        return val.replace('"', '').strip()
    return val

# ==========================
# PLAYLISTS
# ==========================
def get_all_playlists():
    playlists = []
    offset = 0
    print("\n[*] Descargando playlists...")
    while True:
        data = safe_request(
            f"{BASE_URL}/playlist/getUserPlaylists",
            {"limit": LIMIT, "offset": offset}
        )
        items = data.get("playlists", {}).get("items", [])
        total = data.get("playlists", {}).get("total", 0)
        if not items:
            break
        playlists.extend(items)
        offset += LIMIT
        print(f"   → {len(playlists)}/{total}", end="\r")
    print(f"\n[OK] Playlists: {len(playlists)}")
    return playlists

def get_playlist_tracks(playlist_id):
    offset = 0
    tracks = []
    while True:
        data = safe_request(
            f"{BASE_URL}/playlist/get",
            {
                "playlist_id": playlist_id,
                "extra": "tracks",
                "limit": LIMIT,
                "offset": offset
            }
        )
        items = data.get("tracks", {}).get("items", [])
        if not items:
            break
        tracks.extend(items)
        offset += LIMIT
    return tracks

# ==========================
# EJECUCIÓN Y REPORTE
# ==========================
def main():
    playlists = get_all_playlists()
    print("\n[*] Descargando tracks de playlists...")
    rows = []
    for idx, pl in enumerate(playlists, start=1):
        print(f"   → {idx}/{len(playlists)} {pl['name']}", end="\r")
        tracks = get_playlist_tracks(pl["id"])
        for t in tracks:
            row = {
                'title': clean_value(t.get('title', '')),
                'artist': clean_value(t.get('performer', {}).get('name', '')),
                'album': clean_value(t.get('album', {}).get('title', '')),
                'isrc': clean_value(t.get('isrc', '')),
                'genre': clean_value(pl['name'])
            }
            rows.append(row)
    print(f"\n[OK] Total canciones: {len(rows)}")
    out_path = os.path.join('catalog', 'list_qobuz.csv')
    with open(out_path, 'w', encoding='utf-8', newline='') as fout:
        fieldnames = ['title', 'artist', 'album', 'isrc', 'genre']
        writer = csv.DictWriter(fout, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    print(f"[OK] Archivo generado: {out_path}")

if __name__ == "__main__":
    main()
