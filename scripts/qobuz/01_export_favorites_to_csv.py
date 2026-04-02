
import requests
import csv
import time
import os
import pandas as pd
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from utils_posible_mejor_version import (
    normalize_for_match, classify_track_type, compare_quality, normalize_title, normalize_artist
)

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
        streamable = track.get("streamable", True)
        row = {
            "title": title,
            "title_version": title_version,
            "artist": artist,
            "album": album,
            "album_version": album_version,
            "isrc": isrc,
            "genre": genre
        }
        # Ahora también se considera 'streamable' para marcar inactivas
        if (not title or not artist or not album or not isrc or not is_available or not streamable):
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
    
    # ==============================
    # VALIDACIÓN DE ISRC DUPLICADOS
    # ==============================
    isrc_count = {}
    for track in activas:
        isrc = track.get("isrc", "SIN_ISRC")
        isrc_count[isrc] = isrc_count.get(isrc, 0) + 1

    duplicados = [isrc for isrc, count in isrc_count.items() if count > 1 and isrc != "SIN_ISRC"]

    if duplicados:
        print("\n🚨 Se encontraron ISRC duplicados en las canciones activas:")
        print(f"Cantidad de ISRC duplicados: {len(duplicados)}")
        for d in duplicados:
            print(f" - {d} (apariciones: {isrc_count[d]})")

        # Generar CSV con los duplicados
        output_duplicados = os.path.join(output_dir, "favorites_qobuz_duplicados_isrc.csv")
        with open(output_duplicados, "w", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["title", "title_version", "artist", "album", "album_version", "isrc", "genre"])
            for track in activas:
                if track.get("isrc", "SIN_ISRC") in duplicados:
                    writer.writerow([
                        track["title"],
                        track["title_version"],
                        track["artist"],
                        track["album"],
                        track["album_version"],
                        track["isrc"],
                        track["genre"]
                    ])
        print(f"Archivo con duplicados generado: {output_duplicados}\n")
    else:
        print("No se encontraron ISRC duplicados en las canciones activas.\n")

    

    # ==============================
    # NUEVA FUNCIONALIDAD: POSIBLE MEJOR VERSIÓN (opcional)
    # ==============================
    respuesta = input("¿Deseas obtener posibles candidatos a mejores canciones? (Esto puede tardar varios minutos) [s/N]: ").strip().lower()
    if respuesta == "s":
        mejor_version_registros = []
        for track in favoritos:
            # Extraer datos clave
            isrc = track.get("isrc", "")
            track_id = track.get("id", "")
            title = track.get("title", "")
            version = track.get("version", "")
            artist = track.get("performer", {}).get("name", "")
            artist_id = track.get("performer", {}).get("id", "")
            album = track.get("album", {}).get("title", "")
            album_version = track.get("album", {}).get("version", "")
            tipo_disco = classify_track_type(track)
            bit_depth = track.get("maximum_bit_depth")
            sampling_rate = track.get("maximum_sampling_rate")
            channel_count = track.get("maximum_channel_count")
            registro = {
                "ISRC": isrc,
                "Id Titulo": track_id,
                "Título": title,
                "Versión del título": version,
                "Id Artista": artist_id,
                "Artista": artist,
                "Disco": album,
                "Tipo Disco": tipo_disco,
                "Versión del disco": album_version,
                "maximum_bit_depth": bit_depth,
                "maximum_sampling_rate": sampling_rate,
                "maximum_channel_count": channel_count,
                "Es favorito": True
            }
            mejor_version_registros.append(registro)

        # Búsqueda de coincidencias en Qobuz para cada favorito
        def search_track_qobuz(title, artist, limit=10):
            params = {**PARAMS_AUTH, "query": f"{title} {artist}", "type": "tracks", "limit": limit}
            try:
                response = requests.get(f"{BASE_URL}/catalog/search", headers=HEADERS, params=params, timeout=10)
                response.raise_for_status()
                return response.json().get("tracks", {}).get("items", [])
            except Exception:
                return []

        total_favs = len(favoritos)
        for idx, fav in enumerate(favoritos, 1):
            title = fav.get("title", "")
            artist = fav.get("performer", {}).get("name", "")
            tipo_disco = classify_track_type(fav)
            track_id = fav.get("id", "")
            if not title or not artist:
                print(f"[{idx}/{total_favs}] Saltando favorito sin título o artista.")
                continue
            print(f"[{idx}/{total_favs}] Buscando mejores versiones para: '{title}' - '{artist}' ({tipo_disco})")
            norm_title = normalize_for_match(title)
            norm_artist = normalize_for_match(artist)
            search_results = search_track_qobuz(title, artist, limit=10)
            encontrados = 0
            for res in search_results:
                if res.get("id", "") == track_id:
                    continue
                if classify_track_type(res) != tipo_disco:
                    continue
                if normalize_for_match(res.get("title", "")) != norm_title:
                    continue
                if normalize_for_match(res.get("performer", {}).get("name", "")) != norm_artist:
                    continue
                # Comparar calidad
                if compare_quality(fav, res) == 1:
                    registro = {
                        "ISRC": res.get("isrc", ""),
                        "Id Titulo": res.get("id", ""),
                        "Título": res.get("title", ""),
                        "Versión del título": res.get("version", ""),
                        "Id Artista": res.get("performer", {}).get("id", ""),
                        "Artista": res.get("performer", {}).get("name", ""),
                        "Disco": res.get("album", {}).get("title", ""),
                        "Tipo Disco": classify_track_type(res),
                        "Versión del disco": res.get("album", {}).get("version", ""),
                        "maximum_bit_depth": res.get("maximum_bit_depth"),
                        "maximum_sampling_rate": res.get("maximum_sampling_rate"),
                        "maximum_channel_count": res.get("maximum_channel_count"),
                        "Es favorito": False
                    }
                    mejor_version_registros.append(registro)
                    encontrados += 1
            print(f"   → {encontrados} mejores versiones agregadas para este favorito.")

        # Guardar DataFrame en CSV
        df_mejor = pd.DataFrame(mejor_version_registros, columns=[
            "ISRC", "Id Titulo", "Título", "Versión del título", "Id Artista", "Artista",
            "Disco", "Tipo Disco", "Versión del disco", "maximum_bit_depth",
            "maximum_sampling_rate", "maximum_channel_count", "Es favorito"
        ])
        output_mejor = os.path.join("reports", "posibleMejorVersion.csv")
        os.makedirs("reports", exist_ok=True)
        df_mejor.to_csv(output_mejor, index=False, encoding="utf-8")
        print(f"Archivo generado: {output_mejor}")

if __name__ == "__main__":
    main()
