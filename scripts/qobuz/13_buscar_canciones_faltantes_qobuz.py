import csv
import os
import sys
import time

import requests


sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from utils_posible_mejor_version import classify_track_type, normalize_for_match


APP_ID = "798273057"
USER_TOKEN = "Qc0Ymlge2cx2NvQcEmF7tEK5lpmORoeEy1zSjUqkyyEas7mdXOnsPkYcGRoBfSNat2SmkY7oqWCjkZ9SzTUYfQ"
BASE_URL = "https://www.qobuz.com/api.json/0.2"
HEADERS = {"X-App-Id": APP_ID}
PARAMS_AUTH = {"user_auth_token": USER_TOKEN}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE = os.path.join(BASE_DIR, "../../catalog/canciones_faltantes.csv")
FOUND_FILE = os.path.join(BASE_DIR, "../../reports/canciones_faltantes_encontradas_qobuz.csv")
NOT_FOUND_FILE = os.path.join(BASE_DIR, "../../reports/canciones_faltantes_pendientes_qobuz.csv")

SEARCH_LIMIT = 50
REQUEST_DELAY_SECONDS = 0.3


def clean_value(value):
    if value is None:
        return ""
    return str(value).strip()


def normalize_disk_type(value):
    normalized = clean_value(value).lower()
    equivalences = {
        "estudio": "Studio",
        "studio": "Studio",
        "live": "Live",
        "en vivo": "Live",
        "cover": "Cover",
        "demo": "Demo",
        "remix": "Remix",
        "acoustic": "Acoustic",
        "acustico": "Acoustic",
        "acústico": "Acoustic",
    }
    return equivalences.get(normalized, clean_value(value))


def get_track_artist(track):
    performer = clean_value((track.get("performer") or {}).get("name"))
    if performer:
        return performer

    album_artist = clean_value((((track.get("album") or {}).get("artist") or {}).get("name")))
    if album_artist:
        return album_artist

    performers = clean_value(track.get("performers"))
    if performers:
        for performer_info in performers.split(" - "):
            parts = [part.strip() for part in performer_info.split(",") if part.strip()]
            if len(parts) >= 2 and "MainArtist" in parts[1:]:
                return parts[0]

        first_performer = performers.split(" - ", 1)[0].split(",", 1)[0].strip()
        if first_performer:
            return first_performer

    return ""


def load_missing_songs(path):
    with open(path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        songs = []
        for index, row in enumerate(reader, start=1):
            title = clean_value(row.get("title") or row.get("Título"))
            artist = clean_value(row.get("artist") or row.get("Artista"))
            disk_type = normalize_disk_type(row.get("Tipo Disco") or row.get("tipo_disco") or row.get("tipo disco"))

            if not title or not artist:
                print(f"[WARN] Fila {index} ignorada por falta de título o artista.")
                continue

            songs.append(
                {
                    "title": title,
                    "artist": artist,
                    "Tipo Disco": disk_type,
                }
            )
        return songs


def search_track(query, limit=SEARCH_LIMIT):
    params = {
        **PARAMS_AUTH,
        "query": query,
        "type": "tracks",
        "limit": min(limit, 100),
        "offset": 0,
    }

    try:
        response = requests.get(
            f"{BASE_URL}/catalog/search",
            headers=HEADERS,
            params=params,
            timeout=15,
        )
        response.raise_for_status()

        if "application/json" not in response.headers.get("Content-Type", ""):
            print(f"[WARN] Respuesta no JSON para consulta: {query}")
            return []

        data = response.json()
        return data.get("tracks", {}).get("items", [])[:limit]
    except requests.exceptions.RequestException as error:
        print(f"[WARN] Error consultando Qobuz para '{query}': {error}")
        return []


def is_exact_match(song, track):
    expected_title = normalize_for_match(song["title"])
    expected_artist = normalize_for_match(song["artist"])
    expected_disk_type = normalize_disk_type(song.get("Tipo Disco", ""))

    candidate_title = normalize_for_match(track.get("title", ""))
    candidate_artist = normalize_for_match(get_track_artist(track))
    candidate_disk_type = classify_track_type(track)

    if candidate_title != expected_title:
        return False
    if candidate_artist != expected_artist:
        return False
    if expected_disk_type and candidate_disk_type != expected_disk_type:
        return False
    return True


def build_found_row(song, query, track, status):
    return {
        "title": song["title"],
        "artist": song["artist"],
        "Tipo Disco": song.get("Tipo Disco", ""),
        "Estado": status,
        "Query": query,
        "ISRC": clean_value(track.get("isrc")),
        "Id Titulo": clean_value(track.get("id")),
        "Título encontrado": clean_value(track.get("title")),
        "Versión del título": clean_value(track.get("version")),
        "Id Artista": clean_value((track.get("performer") or {}).get("id")),
        "Artista encontrado": get_track_artist(track),
        "Disco": clean_value((track.get("album") or {}).get("title")),
        "Tipo Disco encontrado": classify_track_type(track),
        "Versión del disco": clean_value((track.get("album") or {}).get("version")),
        "maximum_bit_depth": clean_value(track.get("maximum_bit_depth")),
        "maximum_sampling_rate": clean_value(track.get("maximum_sampling_rate")),
        "maximum_channel_count": clean_value(track.get("maximum_channel_count")),
    }


def build_pending_row(song, query, total_results, matched_title_artist):
    return {
        "title": song["title"],
        "artist": song["artist"],
        "Tipo Disco": song.get("Tipo Disco", ""),
        "Query": query,
        "Resultados API": total_results,
        "Coincidencias titulo_artista": matched_title_artist,
    }


def write_csv(path, fieldnames, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main():
    songs = load_missing_songs(INPUT_FILE)
    print(f"Canciones faltantes cargadas: {len(songs)}")

    found_rows = []
    pending_rows = []

    for index, song in enumerate(songs, start=1):
        query_parts = [song["title"], song["artist"]]
        if song.get("Tipo Disco") and song["Tipo Disco"].lower() != "studio":
            query_parts.append(song["Tipo Disco"])
        query = " ".join(part for part in query_parts if part)

        print(
            f"[{index}/{len(songs)}] Buscando: {song['title']} | {song['artist']} | {song.get('Tipo Disco', '')}"
        )
        results = search_track(query)
        exact_matches = [track for track in results if is_exact_match(song, track)]
        title_artist_matches = [
            track for track in results
            if normalize_for_match(track.get("title", "")) == normalize_for_match(song["title"])
            and normalize_for_match(get_track_artist(track)) == normalize_for_match(song["artist"])
        ]

        if exact_matches:
            for track in exact_matches:
                found_rows.append(build_found_row(song, query, track, "Encontrada"))
            print(f"   -> Exactas: {len(exact_matches)}")
        else:
            pending_rows.append(
                build_pending_row(song, query, len(results), len(title_artist_matches))
            )
            print("   -> Sin coincidencia exacta")

        time.sleep(REQUEST_DELAY_SECONDS)

    write_csv(
        FOUND_FILE,
        [
            "title",
            "artist",
            "Tipo Disco",
            "Estado",
            "Query",
            "ISRC",
            "Id Titulo",
            "Título encontrado",
            "Versión del título",
            "Id Artista",
            "Artista encontrado",
            "Disco",
            "Tipo Disco encontrado",
            "Versión del disco",
            "maximum_bit_depth",
            "maximum_sampling_rate",
            "maximum_channel_count",
        ],
        found_rows,
    )
    write_csv(
        NOT_FOUND_FILE,
        [
            "title",
            "artist",
            "Tipo Disco",
            "Query",
            "Resultados API",
            "Coincidencias titulo_artista",
        ],
        pending_rows,
    )

    print(f"Archivo generado: {FOUND_FILE}")
    print(f"Archivo generado: {NOT_FOUND_FILE}")
    print(f"Canciones encontradas: {len(found_rows)}")
    print(f"Canciones pendientes: {len(pending_rows)}")


if __name__ == "__main__":
    main()