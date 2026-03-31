
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
        # Una canción está inactiva si tiene el campo 'isrc' vacío o si el campo 'album' está vacío o si el campo 'title' está vacío
        title = track.get("title", "")
        artist = track.get("performer", {}).get("name", "")
        album = track.get("album", {}).get("title", "")
        isrc = track.get("isrc", "")
        # Consideramos inactiva si falta title, artist, album o isrc, o si el track tiene un campo 'is_available' y es False
        is_available = track.get("is_available", True)
        if not title or not artist or not album or not isrc or not is_available:
            inactivas.append({"title": title, "artist": artist, "album": album, "isrc": isrc})
        else:
            activas.append({"title": title, "artist": artist, "album": album, "isrc": isrc})

    # Guardar solo las activas en el archivo principal
    with open(output_path, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["title", "artist", "album", "isrc"])
        for track in activas:
            writer.writerow([track["title"], track["artist"], track["album"], track["isrc"]])

    # Guardar las inactivas en un archivo aparte
    output_inactivas = os.path.join(output_dir, "favorites_qobuz_inactivas.csv")
    with open(output_inactivas, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["title", "artist", "album", "isrc"])
        for track in inactivas:
            writer.writerow([track["title"], track["artist"], track["album"], track["isrc"]])

    print(f"Archivo {output_path} generado correctamente.")
    print(f"Canciones activas: {len(activas)}")
    print(f"Canciones NO disponibles: {len(inactivas)}")
    if inactivas:
        print(f"Archivo con canciones no disponibles: {output_inactivas}")

if __name__ == "__main__":
    main()
