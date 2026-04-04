
import csv
import os
import unicodedata

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
    return [r for r in registros if r['Id Titulo'] not in ids_excluir]

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


def filtrar_combinaciones_con_multiples_registros(registros):
    conteos = {}
    for row in registros:
        clave = (
            normalizar_para_ordenar(row.get('Título', '')),
            normalizar_para_ordenar(row.get('Artista', '')),
            normalizar_para_ordenar(row.get('Tipo Disco', '')),
        )
        conteos[clave] = conteos.get(clave, 0) + 1

    return [
        row for row in registros
        if conteos[
            (
                normalizar_para_ordenar(row.get('Título', '')),
                normalizar_para_ordenar(row.get('Artista', '')),
                normalizar_para_ordenar(row.get('Tipo Disco', '')),
            )
        ] >= 2
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
    resultado = filtrar_combinaciones_con_multiples_registros(resultado)
    resultado = ordenar_registros(resultado)
    with open(OUTPUT_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(resultado)

if __name__ == '__main__':
    main()
