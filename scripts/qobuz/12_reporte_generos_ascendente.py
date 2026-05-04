import csv
import os
from collections import Counter


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
TREE_FILE = os.path.join(BASE_DIR, 'taxonomy', 'genre_tree.md')
INPUT_CSV = os.path.join(BASE_DIR, 'catalog', 'cancionesConGenero.csv')
OUTPUT_CSV = os.path.join(BASE_DIR, 'reports', 'conteo_generos_ascendente.csv')


def cargar_hojas_arbol(path):
    nodos = []
    stack = []

    with open(path, encoding='utf-8') as file_handle:
        for line in file_handle:
            raw_line = line.rstrip('\n')
            if not raw_line.strip() or raw_line.strip().startswith('#'):
                continue

            indent = len(raw_line) - len(raw_line.lstrip(' '))
            level = indent // 2
            node_name = raw_line.strip()

            if len(stack) > level:
                stack = stack[:level]

            stack.append(node_name)
            nodos.append({
                'node_path': ' > '.join(stack),
                'level': level,
            })

    return [
        node['node_path']
        for index, node in enumerate(nodos)
        if index == len(nodos) - 1 or nodos[index + 1]['level'] <= node['level']
    ]


def contar_generos(csv_path):
    conteos = Counter()
    filas_sin_genero = 0

    with open(csv_path, encoding='utf-8', newline='') as file_handle:
        reader = csv.DictReader(file_handle)
        for row in reader:
            genero = (row.get('genre') or '').strip()
            if not genero:
                filas_sin_genero += 1
                continue
            conteos[genero] += 1

    return conteos, filas_sin_genero


def construir_filas(hojas_arbol, conteos):
    rows = [
        {
            'genre': genero,
            'num_canciones': conteos.get(genero, 0),
        }
        for genero in hojas_arbol
    ]

    generos_en_arbol = set(hojas_arbol)
    rows.extend(
        {
            'genre': genero,
            'num_canciones': cantidad,
        }
        for genero, cantidad in conteos.items()
        if genero not in generos_en_arbol
    )

    return sorted(rows, key=lambda item: (item['num_canciones'], item['genre']))


def escribir_reporte(output_path, rows):
    fieldnames = ['genre', 'num_canciones']

    with open(output_path, 'w', encoding='utf-8', newline='') as file_handle:
        writer = csv.DictWriter(file_handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main():
    hojas_arbol = cargar_hojas_arbol(TREE_FILE)
    conteos, filas_sin_genero = contar_generos(INPUT_CSV)
    rows = construir_filas(hojas_arbol, conteos)
    unknown_genres = sorted(genero for genero in conteos if genero not in set(hojas_arbol))
    escribir_reporte(OUTPUT_CSV, rows)

    print(f'Reporte generado: {OUTPUT_CSV}')
    print(f'Total de generos hoja en el arbol: {len(hojas_arbol)}')
    print(f'Total de filas en el reporte: {len(rows)}')
    print(f'Filas sin genero: {filas_sin_genero}')

    if unknown_genres:
        print('\nGeneros presentes en el CSV pero ausentes en las hojas del arbol:')
        for genero in unknown_genres:
            print(f'- {genero}')


if __name__ == '__main__':
    main()