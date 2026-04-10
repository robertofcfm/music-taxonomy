import csv
import os
from collections import Counter


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
INPUT_CSV = os.path.join(BASE_DIR, 'catalog', 'cancionesConGenero.csv')
OUTPUT_CSV = os.path.join(BASE_DIR, 'reports', 'conteo_generos_ascendente.csv')


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


def construir_filas(conteos):
    return [
        {
            'genre': genero,
            'num_canciones': cantidad,
        }
        for genero, cantidad in sorted(conteos.items(), key=lambda item: (item[1], item[0]))
    ]


def escribir_reporte(output_path, rows):
    fieldnames = ['genre', 'num_canciones']

    with open(output_path, 'w', encoding='utf-8', newline='') as file_handle:
        writer = csv.DictWriter(file_handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main():
    conteos, filas_sin_genero = contar_generos(INPUT_CSV)
    rows = construir_filas(conteos)
    escribir_reporte(OUTPUT_CSV, rows)

    print(f'Reporte generado: {OUTPUT_CSV}')
    print(f'Total de generos distintos: {len(rows)}')
    print(f'Filas sin genero: {filas_sin_genero}')


if __name__ == '__main__':
    main()