import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import requests
import re
import unicodedata
from openpyxl import Workbook

# ==============================
# CONFIG
# ==============================

APP_ID = "798273057"
USER_TOKEN = "Qc0Ymlge2cx2NvQcEmF7tEK5lpmORoeEy1zSjUqkyyEas7mdXOnsPkYcGRoBfSNat2SmkY7oqWCjkZ9SzTUYfQ"

BASE_URL = "https://www.qobuz.com/api.json/0.2"

HEADERS = {"X-App-Id": APP_ID}
PARAMS_AUTH = {"user_auth_token": USER_TOKEN}

# ==============================
# NORMALIZACIÓN (COPIADA DE TU SCRIPT MAESTRO)
# ==============================

def normalize_for_match(text):
    if not text:
        return ""
    text = text.lower()
    text = ''.join(c for c in unicodedata.normalize('NFD', text)
                   if unicodedata.category(c) != 'Mn')
    text = re.sub(r'[^a-z0-9]', '', text)
    return text

def get_album_type(version_text):
    if not version_text:
        return "Estudio"
    version_text = version_text.lower()
    if "live" in version_text or "en vivo" in version_text:
        return "Live"
    if "cover" in version_text:
        return "Cover"
    if "demo" in version_text:
        return "Demo"
    return "Estudio"

# ==============================
# BUSCAR EN CATALOG
# ==============================

def search_track(query, limit=10):
    """Busca tracks en Qobuz con límite configurable"""
    params = {
        **PARAMS_AUTH,
        "query": query,
        "type": "tracks",
        "limit": min(limit, 100),  # máximo 100 por request según API
        "offset": 0
    }

    try:
        r = requests.get(
            f"{BASE_URL}/catalog/search",
            headers=HEADERS,
            params=params,
            timeout=10  # timeout de 10 segundos
        )

        if r.status_code != 200:
            print(f"[DEBUG] Error HTTP {r.status_code}: {r.text}")
            return []

        data = r.json()
        tracks_block = data.get("tracks", {})
        items = tracks_block.get("items", [])
        
        return items[:limit]  # devolver máximo 'limit' resultados
        
    except requests.exceptions.Timeout:
        print(f"[DEBUG] Timeout en búsqueda: {query}")
        return []
    except requests.exceptions.RequestException as e:
        print(f"[DEBUG] Error de conexión: {str(e)}")
        return []
    except Exception as e:
        print(f"[DEBUG] Error inesperado: {str(e)}")
        return []


# ==============================
# LÓGICA PRINCIPAL
# ==============================

def ejecutar_busqueda():
    tree.delete(*tree.get_children())
    print("\n===============================")
    print("🔎 Iniciando búsqueda...")

    titulo = entry_titulo.get()
    artista = entry_artista.get()

    if not titulo or not artista:
        messagebox.showwarning("Error", "Ingresa título y artista")
        return

    normalized_title_original = normalize_for_match(titulo)
    normalized_artist_original = normalize_for_match(artista)

    resultados = search_track(f"{titulo} {artista}")

    print(f"[DEBUG] Resultados obtenidos: {len(resultados)}")

    exactos = []
    parciales = []

    for res in resultados:

        normalized_title_candidate = normalize_for_match(res.get("title"))
        normalized_artist_candidate = normalize_for_match(res.get("performer", {}).get("name"))

        album_type_candidate = get_album_type(
            res.get("album", {}).get("version")
        )

        registro = {
            "ISRC": res.get("isrc"),
            "Id Titulo": res.get("id"),
            "Título": res.get("title"),
            "Versión del título": res.get("version"),
            "Id Artista": res.get("performer", {}).get("id"),
            "Artista": res.get("performer", {}).get("name"),
            "Disco": res.get("album", {}).get("title"),
            "Versión del disco": res.get("album", {}).get("version"),
            "maximum_bit_depth": res.get("maximum_bit_depth"),
            "maximum_sampling_rate": res.get("maximum_sampling_rate"),
            "maximum_channel_count": res.get("maximum_channel_count"),
        }

        # MATCH EXACTO NORMALIZADO
        if (
            normalized_title_candidate == normalized_title_original and
            normalized_artist_candidate == normalized_artist_original
        ):
            exactos.append(registro)
        else:
            parciales.append(registro)

    final = exactos + parciales

    print(f"[DEBUG] Exact matches: {len(exactos)}")
    print(f"[DEBUG] Parciales: {len(parciales)}")

    for t in final:
        tree.insert("", "end", values=(
            t["ISRC"],
            t["Id Titulo"],
            t["Título"],
            t["Versión del título"],
            t["Id Artista"],
            t["Artista"],
            t["Disco"],
            t["Versión del disco"],
            t["maximum_bit_depth"],
            t["maximum_sampling_rate"],
            t["maximum_channel_count"]
        ))

    global tracks_guardados
    tracks_guardados = final

    print("✅ Búsqueda finalizada")
    print("===============================\n")


# ==============================
# EXPORTAR
# ==============================

def exportar_excel():
    if not tracks_guardados:
        messagebox.showwarning("Aviso", "No hay datos")
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".xlsx",
        filetypes=[("Excel files", "*.xlsx")]
    )

    if not file_path:
        return

    wb = Workbook()
    ws = wb.active

    ws.append([
        "ISRC", "Id Titulo", "Título", "Versión del título",
        "Id Artista", "Artista",
        "Disco", "Versión del disco",
        "maximum_bit_depth", "maximum_sampling_rate",
        "maximum_channel_count"
    ])

    for t in tracks_guardados:
        ws.append([
            t["ISRC"],
            t["Id Titulo"],
            t["Título"],
            t["Versión del título"],
            t["Id Artista"],
            t["Artista"],
            t["Disco"],
            t["Versión del disco"],
            t["maximum_bit_depth"],
            t["maximum_sampling_rate"],
            t["maximum_channel_count"]
        ])

    wb.save(file_path)
    messagebox.showinfo("Éxito", "Archivo exportado")


# ==============================
# UI
# ==============================

root = tk.Tk()
root.title("Qobuz Smart Search")
root.geometry("1400x700")

frame_inputs = tk.Frame(root)
frame_inputs.pack(pady=10)

tk.Label(frame_inputs, text="Título:").grid(row=0, column=0)
entry_titulo = tk.Entry(frame_inputs, width=25)
entry_titulo.grid(row=0, column=1)

tk.Label(frame_inputs, text="Artista:").grid(row=0, column=2)
entry_artista = tk.Entry(frame_inputs, width=25)
entry_artista.grid(row=0, column=3)

tk.Button(frame_inputs, text="Buscar", command=ejecutar_busqueda).grid(row=0, column=4, padx=10)
tk.Button(frame_inputs, text="Exportar Excel", command=exportar_excel).grid(row=0, column=5)

columns = (
    "ISRC", "Id Titulo", "Título", "Versión del título",
    "Id Artista", "Artista",
    "Disco", "Versión del disco",
    "maximum_bit_depth", "maximum_sampling_rate",
    "maximum_channel_count"
)

tree = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=130)

tree.pack(fill="both", expand=True)

tracks_guardados = []

root.mainloop()