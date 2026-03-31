
import requests
import csv
import time
import os

# ==============================
# CONFIGURACIÓN QOBUZ
# ==============================
APP_ID = "798273057"
USER_TOKEN = "Qc0Ymlge2cx2NvQcEmF7tEK5lpmORoeEy1zSjUqkyyEas7mdXOnsPkYcGRoBfSNat2SmkY7oqWCjkZ9SzTUYfQ"
BASE_URL = "https://www.qobuz.com/api.json/0.2"
HEADERS = {"X-App-Id": APP_ID}
PARAMS_AUTH = {"user_auth_token": USER_TOKEN}

# ==============================
# FUNCIONES
# ==============================
def get_all_favorites():
    print("Descargando favoritos completos...")
    limit, offset, all_tracks = 100, 0, []
    while True:
        params = {**PARAMS_AUTH, "limit": limit, "offset": offset}
        response = requests.get(f"{BASE_URL}/favorite/getUserFavorites", headers=HEADERS, params=params)
        data = response.json()
        tracks = data.get("tracks", {}).get("items", [])
        total = data.get("tracks", {}).get("total", 0)
        all_tracks.extend(tracks)
        print(f"   Cargados: {len(all_tracks)} / {total}")
        if len(all_tracks) >= total:
            break
        offset += limit
        time.sleep(0.3)
    print(f"Total favoritos cargados: {len(all_tracks)}")
    return all_tracks

# ==============================
# MAIN
# ==============================
def main():
    favoritos = get_all_favorites()
    output_dir = "catalog"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "favorites_qobuz.csv")

    activas = []
    inactivas = []
    for track in favoritos:
        title = track.get("title", "")
        title_version = track.get("version", "")
        artist = track.get("performer", {}).get("name", "")
        album = track.get("album", {}).get("title", "")
        album_version = track.get("album", {}).get("version", "")
        isrc = track.get("isrc", "")
        genre = track.get("genre", "") if "genre" in track else ""
        is_available = track.get("is_available", True)
        row = {
            "title": title,
            "title_version": title_version,
            "artist": artist,
            "album": album,
            "album_version": album_version,
            "isrc": isrc,
            "genre": genre
        }
        if not title or not artist or not album or not isrc or not is_available:
            inactivas.append(row)
        else:
            activas.append(row)


    # Guardar solo las activas en el archivo principal con los campos requeridos
    with open(output_path, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["title", "title_version", "artist", "album", "album_version", "isrc", "genre"])
        for track in activas:
            writer.writerow([
                track["title"],
                track["title_version"],
                track["artist"],
                track["album"],
                track["album_version"],
                track["isrc"],
                track["genre"]
            ])

    # Guardar las inactivas en un archivo aparte (mismos campos)
    output_inactivas = os.path.join(output_dir, "favorites_qobuz_inactivas.csv")
    with open(output_inactivas, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["title", "title_version", "artist", "album", "album_version", "isrc", "genre"])
        for track in inactivas:
            writer.writerow([
                track["title"],
                track["title_version"],
                track["artist"],
                track["album"],
                track["album_version"],
                track["isrc"],
                track["genre"]
            ])

    print(f"Archivo {output_path} generado correctamente.")
    print(f"Canciones activas: {len(activas)}")
    print(f"Canciones NO disponibles: {len(inactivas)}")
    if inactivas:
        print(f"Archivo con canciones no disponibles: {output_inactivas}")

if __name__ == "__main__":
    main()
