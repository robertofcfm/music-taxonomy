# Funciones reutilizadas de 1.0_auditoria_canciones_pre_V2.py para posibleMejorVersion
import re
import unicodedata

def normalize_for_match(text):
    if not text: return ""
    text = text.lower()
    text = ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')
    text = re.sub(r'[^a-z0-9]', '', text)
    return text

def normalize_for_keyword_search(text):
    if not text:
        return ""
    text = text.lower()
    text = ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')
    text = re.sub(r'[^a-z0-9]+', ' ', text)
    return re.sub(r'\s+', ' ', text).strip()

def contains_keyword(text, keywords):
    searchable_text = f" {normalize_for_keyword_search(text)} "
    for keyword in keywords:
        normalized_keyword = normalize_for_keyword_search(keyword)
        if normalized_keyword and f" {normalized_keyword} " in searchable_text:
            return True
    return False

def classify_track_type(track):
    track_title = track.get("title") or ""
    version_title = track.get("version") or ""
    album_data = track.get("album") or {}
    album_version = album_data.get("version") or ""
    all_text = f"{track_title} {version_title} {album_version}"
    live_keywords = [
        "live", "en vivo", "vivo", "concierto", "directo", "unplugged",
        "mtv unplugged", "live at", "live from", "live in", "live version",
        "recorded live", "grabado en vivo", "ao vivo"
    ]
    cover_keywords = ["cover", "tribute", "cover version", "interpret", "revisited"]
    demo_keywords = ["demo", "rough", "early version", "pre-production"]
    remix_keywords = [
        "remix", "mix", "edit", "dub", "extended", "club mix",
        "radio edit"
    ]
    acoustic_keywords = ["acoustic", "acústico", "unplugged", "stripped", "piano version"]
    if contains_keyword(all_text, live_keywords):
        return "Live"
    if contains_keyword(all_text, cover_keywords):
        return "Cover"
    if contains_keyword(all_text, demo_keywords):
        return "Demo"
    if contains_keyword(all_text, remix_keywords):
        return "Remix"
    if contains_keyword(all_text, acoustic_keywords):
        return "Acoustic"
    return "Studio"

def compare_quality(original, candidate):
    o_bit = original.get("maximum_bit_depth") or 0
    o_rate = original.get("maximum_sampling_rate") or 0
    o_ch = original.get("maximum_channel_count") or 0
    c_bit = candidate.get("maximum_bit_depth") or 0
    c_rate = candidate.get("maximum_sampling_rate") or 0
    c_ch = candidate.get("maximum_channel_count") or 0
    if c_bit > o_bit:
        return 1
    if c_bit < o_bit:
        return -1
    if c_rate > o_rate:
        return 1
    if c_rate < o_rate:
        return -1
    if c_ch > o_ch:
        return 1
    if c_ch < o_ch:
        return -1
    return 0

def normalize_title(title):
    if not title: return ""
    title = title.lower()
    title = re.sub(r"\(.*?\)", "", title)
    title = re.sub(r"\[.*?\]", "", title)
    title = re.sub(r" - .*", "", title)
    return title.strip()

def normalize_artist(name):
    if not name: return ""
    name = name.lower()
    name = re.sub(r"\(.*?\)", "", name)
    name = re.split(r"feat\.|&| and |,", name)[0]
    return name.strip()
