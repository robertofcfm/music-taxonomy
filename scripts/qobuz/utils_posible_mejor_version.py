# Funciones reutilizadas de 1.0_auditoria_canciones_pre_V2.py para posibleMejorVersion
import re
import unicodedata

def normalize_for_match(text):
    if not text: return ""
    text = text.lower()
    text = ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')
    text = re.sub(r'[^a-z0-9]', '', text)
    return text

def classify_track_type(track):
    version_title = (track.get("version") or "").lower()
    album_data = track.get("album") or {}
    album_version = (album_data.get("version") or "").lower()
    all_text = f"{version_title} {album_version}"
    live_keywords = [
        "live", "en vivo", "vivo", "concierto", "directo", "unplugged",
        "mtv unplugged", "live at", "live from", "live in", "live version",
        "recorded live", "grabado en vivo", "ao vivo"
    ]
    cover_keywords = ["cover", "tribute", "version", "interpret", "revisited"]
    demo_keywords = ["demo", "rough", "early version", "pre-production"]
    remix_keywords = [
        "remix", "mix", "edit", "dub", "extended", "club mix",
        "radio edit", "single version", "album version"
    ]
    acoustic_keywords = ["acoustic", "acústico", "unplugged", "stripped", "piano version"]
    for keyword in live_keywords:
        if keyword in all_text:
            return "Live"
    for keyword in cover_keywords:
        if keyword in all_text:
            return "Cover"
    for keyword in demo_keywords:
        if keyword in all_text:
            return "Demo"
    for keyword in remix_keywords:
        if keyword in all_text:
            return "Remix"
    for keyword in acoustic_keywords:
        if keyword in all_text:
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
