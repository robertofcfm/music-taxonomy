import csv
import os
from collections import Counter


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
TREE_FILE = os.path.join(BASE_DIR, 'taxonomy', 'genre_tree.md')
INPUT_CSV = os.path.join(BASE_DIR, 'catalog', 'cancionesConGenero.csv')
OUTPUT_CSV = os.path.join(BASE_DIR, 'reports', 'conteo_canciones_por_nodo.csv')


def cargar_nodos_arbol(path):
    """Devuelve los nodos del arbol en el mismo orden en que aparecen en el markdown."""
    nodes = []
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
            node_path = ' > '.join(stack)
            nodes.append({
                'node_path': node_path,
                'level': level,
                'node_name': node_name,
            })

    return nodes


def contar_generos(csv_path):
    """Cuenta asignaciones exactas de genero en cancionesConGenero.csv."""
    exact_counts = Counter()
    empty_genre_rows = 0

    with open(csv_path, encoding='utf-8', newline='') as file_handle:
        reader = csv.DictReader(file_handle)
        for row in reader:
            genre = (row.get('genre') or '').strip()
            if not genre:
                empty_genre_rows += 1
                continue
            exact_counts[genre] += 1

    return exact_counts, empty_genre_rows


def construir_conteo_acumulado(exact_counts):
    """Acumula cada cancion en todos los prefijos de su rama."""
    accumulated_counts = Counter()

    for genre_path, count in exact_counts.items():
        parts = [part.strip() for part in genre_path.split('>')]
        for index in range(1, len(parts) + 1):
            prefix = ' > '.join(parts[:index])
            accumulated_counts[prefix] += count

    return accumulated_counts


def construir_filas(nodes, exact_counts, accumulated_counts):
    rows = []

    for node in nodes:
        node_path = node['node_path']
        rows.append({
            'node_path': node_path,
            'level': node['level'],
            'node_name': node['node_name'],
            'canciones_exactas': exact_counts.get(node_path, 0),
            'canciones_acumuladas': accumulated_counts.get(node_path, 0),
        })

    return rows


def escribir_reporte(output_path, rows):
    fieldnames = [
        'node_path',
        'level',
        'node_name',
        'canciones_exactas',
        'canciones_acumuladas',
    ]

    with open(output_path, 'w', encoding='utf-8', newline='') as file_handle:
        writer = csv.DictWriter(file_handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main():
    nodes = cargar_nodos_arbol(TREE_FILE)
    exact_counts, empty_genre_rows = contar_generos(INPUT_CSV)
    accumulated_counts = construir_conteo_acumulado(exact_counts)
    rows = construir_filas(nodes, exact_counts, accumulated_counts)

    tree_node_paths = {node['node_path'] for node in nodes}
    unknown_genres = sorted(genre for genre in exact_counts if genre not in tree_node_paths)

    escribir_reporte(OUTPUT_CSV, rows)

    print(f'Reporte generado: {OUTPUT_CSV}')
    print(f'Total de nodos en el arbol: {len(rows)}')
    print(f'Total de generos distintos en el CSV: {len(exact_counts)}')
    print(f'Filas sin genero: {empty_genre_rows}')

    if unknown_genres:
        print('\nGeneros presentes en el CSV pero ausentes en el arbol:')
        for genre in unknown_genres:
            print(f'- {genre}')


if __name__ == '__main__':
    main()