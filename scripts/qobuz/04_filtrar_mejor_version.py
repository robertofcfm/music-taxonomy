
import csv
import os
import unicodedata

from utils_posible_mejor_version import normalize_for_match

# Archivos de entrada y salida (rutas absolutas basadas en la ubicación del script)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE = os.path.join(BASE_DIR, '../../reports/posibleMejorVersion_03.csv')
EXCLUDE_FILE = os.path.join(BASE_DIR, '../../reports/posibleMejorVersion_Excluidos.csv')
OUTPUT_FILE = os.path.join(BASE_DIR, '../../reports/posibleMejorVersion.csv')

# Leer IDs a excluir
def cargar_ids_excluir(path):
    if not os.path.exists(path):
        return set()

    ids = set()
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            ids.add(row['Id Titulo'])
    return ids

# Leer registros del archivo principal
def cargar_registros(path):
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader), reader.fieldnames

# Filtrar registros excluidos
def filtrar_excluidos(registros, ids_excluir):
    return [
        r for r in registros
        if r['Es favorito'] == 'True' or r['Id Titulo'] not in ids_excluir
    ]

# Filtrar favoritos según condición
def filtrar_favoritos(registros):
    ids_favoritos = {
        r['Id Titulo']
        for r in registros
        if r['Es favorito'] == 'True'
    }

    resultado = []
    for r in registros:
        if r['Es favorito'] == 'True':
            resultado.append(r)
            continue
        if r['Id Titulo'] in ids_favoritos:
            continue
        resultado.append(r)
    return resultado


def normalizar_para_ordenar(texto):
    texto = (texto or '').strip().lower()
    texto = unicodedata.normalize('NFD', texto)
    return ''.join(c for c in texto if unicodedata.category(c) != 'Mn')


def normalizar_para_agrupar(texto):
    return normalize_for_match(texto or '')


def filtrar_combinaciones_con_candidato(registros):
    grupos_con_candidato = set()
    for row in registros:
        clave = (
            normalizar_para_agrupar(row.get('Título', '')),
            normalizar_para_agrupar(row.get('Artista', '')),
            normalizar_para_agrupar(row.get('Tipo Disco', '')),
        )
        if row.get('Es favorito', '') == 'False':
            grupos_con_candidato.add(clave)

    return [
        row for row in registros
        if (
            normalizar_para_agrupar(row.get('Título', '')),
            normalizar_para_agrupar(row.get('Artista', '')),
            normalizar_para_agrupar(row.get('Tipo Disco', '')),
        ) in grupos_con_candidato
    ]


def ordenar_registros(registros):
    return sorted(
        registros,
        key=lambda row: (
            normalizar_para_ordenar(row.get('Título', '')),
            normalizar_para_ordenar(row.get('Artista', '')),
            row.get('Es favorito', ''),
            row.get('Id Titulo', ''),
        )
    )

def main():
    ids_excluir = cargar_ids_excluir(EXCLUDE_FILE)
    registros, fieldnames = cargar_registros(INPUT_FILE)
    filtrados = filtrar_excluidos(registros, ids_excluir)
    resultado = filtrar_favoritos(filtrados)
    resultado = filtrar_combinaciones_con_candidato(resultado)
    resultado = ordenar_registros(resultado)
    with open(OUTPUT_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(resultado)
    print(f'IDs excluidos cargados: {len(ids_excluir)}')
    print(f'Registros False excluidos por archivo: {len(registros) - len(filtrados)}')
    print(f'Registros generados: {len(resultado)}')

if __name__ == '__main__':
    main()
