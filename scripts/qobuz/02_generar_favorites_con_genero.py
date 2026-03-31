import csv
from collections import defaultdict

import os
def cargar_arbol_generos(path):
    """Carga un árbol de géneros desde un archivo markdown. Devuelve (ramas, set_todos_los_generos)."""
    generos = set()
    ramas = set()
    stack = []  # (nivel, nombre)
    with open(path, encoding='utf-8') as f:
        for line in f:
            if not line.strip() or line.strip().startswith('#'):
                continue
            # Detecta nivel de indentación (2 espacios por nivel)
            raw = line.rstrip('\n')
            nivel = len(raw) - len(raw.lstrip(' '))
            nombre = raw.strip()
            # Ajusta la pila al nivel actual
            while stack and stack[-1][0] >= nivel:
                stack.pop()
            stack.append((nivel, nombre))
            # Construye la ruta completa
            ruta = ' > '.join([n for _, n in stack])
            ramas.add(ruta)
            generos.add(nombre)
    return ramas, generos

def encontrar_genero_valido(genero, ramas):
    """Devuelve el género si está en ramas, si no, intenta buscarlo ignorando mayúsculas/minúsculas y espacios."""
    if not genero:
        return ''
    genero = genero.strip()
    # Probar la rama completa y luego ir quitando desde el final
    partes = [p.strip() for p in genero.split('>')]
    for i in range(len(partes), 0, -1):
        rama = ' > '.join(partes[:i])
        if rama in ramas:
            return rama
        # Búsqueda flexible: sin espacios y minúsculas
        rama_norm = rama.lower().replace(' ', '')
        for r in ramas:
            if rama_norm == r.lower().replace(' ', ''):
                return r
    return ''

import unicodedata

import re
def normalizar_texto(texto):
    # Normaliza: elimina comillas, espacios extra, deja solo letras/números/tildes, minúsculas
    if texto is None:
        return ''
    texto = str(texto)
    # Elimina comillas dobles al inicio y final
    if texto.startswith('"') and texto.endswith('"'):
        texto = texto[1:-1]
    # Elimina todos los signos de puntuación y símbolos Unicode de forma robusta
    import string
    texto = ''.join(c for c in texto if unicodedata.category(c)[0] not in ('P', 'S'))
    # Normaliza unicode y minúsculas
    texto = texto.strip().lower()
    texto = unicodedata.normalize('NFKD', texto)
    texto = ''.join([c for c in texto if not unicodedata.combining(c)])
    # Elimina cualquier carácter que no sea letra, número, tilde o espacio
    texto = re.sub(r'[^a-z0-9áéíóúüñ\s]', '', texto)
    # Reemplaza múltiples espacios internos por uno solo
    texto = re.sub(r'\s+', ' ', texto)
    return texto.strip()

def cargar_generos_dict(path):
    """Carga dos diccionarios: por (title, artist) y por isrc si está disponible."""
    generos_title_artist = defaultdict(list)
    generos_isrc = defaultdict(list)
    with open(path, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            key = (normalizar_texto(row['title']), normalizar_texto(row['artist']))
            genero = row['genre'].strip()
            generos_title_artist[key].append(genero)
            if 'isrc' in row and row['isrc']:
                generos_isrc[row['isrc'].strip()].append(genero)
    return generos_title_artist, generos_isrc

def main():
    ramas, _ = cargar_arbol_generos('taxonomy/genre_tree.md')
    generos_title_artist, _ = cargar_generos_dict('catalog/songs_with_genres.csv')
    canciones_sin_genero = []
    with open('catalog/favorites_qobuz.csv', encoding='utf-8') as fin, \
         open('catalog/cancionesConGenero.csv', 'w', encoding='utf-8', newline='') as fout:
        reader = csv.DictReader(fin)
        # Añadir los nuevos campos
        fieldnames = ['title', 'title_version', 'artist', 'album', 'album_version', 'isrc', 'genre']
        writer = csv.DictWriter(fout, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            key_norm = (normalizar_texto(row['title']), normalizar_texto(row['artist']))
            generos = generos_title_artist.get(key_norm, [])
            # Limpiar campos y obtener versiones si existen
            clean_row = {k: (v.replace('"', '') if isinstance(v, str) else v) for k, v in row.items()}
            title_version = clean_row.get('title_version', '')
            album_version = clean_row.get('album_version', '')
            if generos:
                for genero in generos:
                    genero_valido = encontrar_genero_valido(genero, ramas) if genero else ''
                    writer.writerow({
                        'title': clean_row['title'],
                        'title_version': title_version,
                        'artist': clean_row['artist'],
                        'album': clean_row['album'],
                        'album_version': album_version,
                        'isrc': clean_row['isrc'],
                        'genre': genero_valido.replace('"', '') if isinstance(genero_valido, str) else genero_valido
                    })
            else:
                canciones_sin_genero.append({
                    'title': clean_row['title'],
                    'title_version': title_version,
                    'artist': clean_row['artist'],
                    'album': clean_row['album'],
                    'album_version': album_version,
                    'isrc': clean_row['isrc']
                })
                writer.writerow({
                    'title': clean_row['title'],
                    'title_version': title_version,
                    'artist': clean_row['artist'],
                    'album': clean_row['album'],
                    'album_version': album_version,
                    'isrc': clean_row['isrc'],
                    'genre': ''
                })

    # Reporte en pantalla
    cantidad = len(canciones_sin_genero)
    print(f"\nCanciones sin género asignado: {cantidad}")
    if cantidad > 0:
        print("Lista de canciones sin género:")
        for c in canciones_sin_genero:
            print(f"- {c['title']} | {c['artist']} | {c['album']} | {c['isrc']}")

if __name__ == '__main__':
    main()
