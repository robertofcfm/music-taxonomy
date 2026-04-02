import csv
import json
import os

# Rutas absolutas basadas en la ubicación de este script
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
file_diff = os.path.join(BASE_DIR, 'catalog', 'cancionesConGeneroDiff.csv')
file_criteria = os.path.join(BASE_DIR, 'taxonomy', 'genre_tree_node_criteria.json')

# Leer archivo de criterios
with open(file_criteria, encoding='utf-8') as f:
    data = json.load(f)
    nodes = data.get('nodes', [])
    node_dict = {n['node_path']: n for n in nodes}

def escape_csv_field(field):
    """Escapa comillas dobles y encierra el campo si contiene comas o comillas"""
    if field is None:
        return ''
    field = str(field)
    if '"' in field:
        field = field.replace('"', '""')
    if ',' in field or '"' in field or '\n' in field:
        return f'"{field}"'
    return field

# Leer géneros disponibles en el diff
with open(file_diff, encoding='utf-8') as f:
    reader = csv.DictReader(f)
    canciones = list(reader)
    generos = sorted(set(row['genre'] for row in canciones))



# Procesar géneros uno a uno, preguntando al usuario si desea continuar
idx = 0
while idx < len(generos):
    genero = generos[idx]
    print(f'\nGénero seleccionado: {genero}')

    nodo = node_dict.get(genero)
    if nodo:
        print('\nnode_path:', nodo['node_path'])
        print('membership_criteria:', nodo['membership_criteria'])
    else:
        print(f'\nFalta información de criterios para el nodo: {genero}')

    filtradas = [row for row in canciones if row['genre'] == genero]

    print('\nCSV para copiar:')
    print('title,artist,album,isrc')
    for row in filtradas:
        print(','.join(f'"{row[campo].replace("\"", "\"\"")}"' if row[campo] is not None else '""' for campo in ['title','artist','album','isrc']))

    if idx < len(generos) - 1:
        resp = input('\n¿Quieres procesar el siguiente género? (s/n): ').strip().lower()
        if resp == 's':
            idx += 1
            continue
        elif resp == 'n':
            print('Proceso finalizado por el usuario.')
            break
        else:
            print('Respuesta no reconocida. Saliendo.')
            break
    else:
        print('\nYa no hay más géneros por mostrar.')
        break
