import csv
import os
import re

from utils_posible_mejor_version import normalize_for_match


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE = os.path.join(BASE_DIR, '../../reports/posibleMejorVersion_01.csv')
OUTPUT_FILE = os.path.join(BASE_DIR, '../../reports/posibleMejorVersion_03.csv')
DUPLICATES_REPORT_FILE = os.path.join(BASE_DIR, '../../reports/posibleMejorVersion_duplicados_favoritos.csv')
EXCLUDED_FILE = os.path.join(BASE_DIR, '../../reports/posibleMejorVersion_duplicados_excluidos.csv')


def cargar_registros(path):
    with open(path, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader), reader.fieldnames


def guardar_registros(path, fieldnames, registros):
    with open(path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(registros)


def es_favorito(valor):
    return (valor or '').strip().lower() == 'true'


def normalizar_titulo_para_clave(titulo):
    titulo_sin_parentesis = re.sub(r'\(.*?\)', '', titulo or '')
    return normalize_for_match(titulo_sin_parentesis)


def construir_clave(row):
    return (
        normalizar_titulo_para_clave(row.get('Título', '')),
        (row.get('Id Artista', '') or '').strip(),
        (row.get('Tipo Disco', '') or '').strip().lower(),
    )


def obtener_clave_duplicado(row):
    clave_existente = (row.get('Clave Duplicado', '') or '').strip()
    if clave_existente:
        return clave_existente
    titulo_normalizado, id_artista, tipo_disco = construir_clave(row)
    return f'{titulo_normalizado}|{id_artista}|{tipo_disco}'


def agrupar_duplicados(registros):
    grupos = {}
    for row in registros:
        if not es_favorito(row.get('Es favorito')):
            continue
        clave = construir_clave(row)
        grupos.setdefault(clave, []).append(row)

    return {clave: grupo for clave, grupo in grupos.items() if len(grupo) >= 2}


def cargar_claves_excluidas(path):
    if not os.path.exists(path):
        return set()

    registros, _ = cargar_registros(path)
    return {
        obtener_clave_duplicado(row)
        for row in registros
        if obtener_clave_duplicado(row)
    }


def encontrar_duplicados(registros, claves_excluidas):
    grupos = agrupar_duplicados(registros)

    duplicados = []
    for clave, grupo in grupos.items():
        titulo_normalizado, id_artista, tipo_disco = clave
        clave_duplicado = f'{titulo_normalizado}|{id_artista}|{tipo_disco}'
        if clave_duplicado in claves_excluidas:
            continue
        for row in grupo:
            row_con_metadatos = dict(row)
            row_con_metadatos['Titulo Normalizado'] = titulo_normalizado
            row_con_metadatos['Cantidad Duplicados'] = str(len(grupo))
            row_con_metadatos['Clave Duplicado'] = clave_duplicado
            duplicados.append(row_con_metadatos)

    duplicados.sort(
        key=lambda row: (
            row['Titulo Normalizado'],
            row.get('Id Artista', ''),
            row.get('Tipo Disco', ''),
            row.get('Título', ''),
            row.get('Id Titulo', ''),
        )
    )
    return duplicados


def guardar_reporte(path, fieldnames, registros):
    output_fields = list(fieldnames) + [
        'Titulo Normalizado',
        'Cantidad Duplicados',
        'Clave Duplicado',
    ]
    with open(path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=output_fields)
        writer.writeheader()
        writer.writerows(registros)


def main():
    registros, fieldnames = cargar_registros(INPUT_FILE)
    guardar_registros(OUTPUT_FILE, fieldnames, registros)
    claves_excluidas = cargar_claves_excluidas(EXCLUDED_FILE)
    duplicados = encontrar_duplicados(registros, claves_excluidas)
    guardar_reporte(DUPLICATES_REPORT_FILE, fieldnames, duplicados)
    print(f'Archivo intermedio generado: {OUTPUT_FILE}')
    print(f'Reporte generado: {DUPLICATES_REPORT_FILE}')
    print(f'Registros duplicados exportados: {len(duplicados)}')


if __name__ == '__main__':
    main()