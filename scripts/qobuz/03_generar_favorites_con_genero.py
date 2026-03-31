import csv
from collections import defaultdict
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from scripts.generar_canciones_con_genero import cargar_arbol_generos, encontrar_genero_valido

import unicodedata

import re
def normalizar_texto(texto):
    # Quita cualquier tipo de comillas, normaliza unicode, minúsculas y elimina espacios dobles
    if texto is None:
        return ''
    texto = str(texto)
    # Elimina cualquier tipo de comillas (simples, dobles, dobles dobles, escapadas) y barras invertidas
    texto = re.sub(r'["\'\u201c\u201d\u2018\u2019\\]', '', texto)
    texto = texto.strip().lower()
    texto = unicodedata.normalize('NFKD', texto)
    texto = ''.join([c for c in texto if not unicodedata.combining(c)])
    # Reemplaza múltiples espacios internos por uno solo
    texto = re.sub(r'\s+', ' ', texto)
    return texto

def cargar_generos_dict(path):
    """Carga un diccionario {(title, artist): genre} desde songs_with_genres.csv, normalizando claves"""
    generos = {}
    with open(path, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            key = (normalizar_texto(row['title']), normalizar_texto(row['artist']))
            generos[key] = row['genre'].strip()
    return generos

def main():
    ramas, _ = cargar_arbol_generos('taxonomy/genre_tree.md')
    generos_dict = cargar_generos_dict('catalog/songs_with_genres.csv')
    canciones_sin_genero = []
    with open('catalog/favorites_qobuz.csv', encoding='utf-8') as fin, \
         open('catalog/cancionesConGenero.csv', 'w', encoding='utf-8', newline='') as fout:
        reader = csv.DictReader(fin)
        fieldnames = ['title', 'artist', 'album', 'isrc', 'genre']
        writer = csv.DictWriter(fout, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            key_norm = (normalizar_texto(row['title']), normalizar_texto(row['artist']))
            genero = generos_dict.get(key_norm, '')
            genero_valido = encontrar_genero_valido(genero, ramas) if genero else ''
            # Elimina comillas dobles de cada valor antes de escribir
            clean_row = {k: (v.replace('"', '') if isinstance(v, str) else v) for k, v in row.items()}
            if not genero_valido:
                canciones_sin_genero.append({
                    'title': clean_row['title'],
                    'artist': clean_row['artist'],
                    'album': clean_row['album'],
                    'isrc': clean_row['isrc']
                })
            writer.writerow({
                'title': clean_row['title'],
                'artist': clean_row['artist'],
                'album': clean_row['album'],
                'isrc': clean_row['isrc'],
                'genre': genero_valido.replace('"', '') if isinstance(genero_valido, str) else genero_valido
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
