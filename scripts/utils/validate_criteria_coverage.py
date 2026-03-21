# Validación de cobertura de criterios para cada nodo del árbol

import json
import sys


with open('taxonomy/genre_tree_master.md', encoding='utf-8') as f:
    lines = [line.rstrip('\n') for line in f if line.strip()]


def extract_all_paths(lines):
    paths = []
    stack = []
    for idx, line in enumerate(lines):
        # Considerar tabs como 2 espacios
        line_expanded = line.replace('\t', '  ')
        indent = len(line_expanded) - len(line_expanded.lstrip())
        name = line_expanded.strip()
        level = indent // 2
        stack = stack[:level]
        stack.append(name)
        if stack and stack[0] == 'Music':
            paths.append(' > '.join(stack))
    return paths

with open('taxonomy/genre_tree_node_criteria.json', encoding='utf-8') as f:
    data = json.load(f)
    criteria_nodes = set(node['node_path'] for node in data['nodes'])



all_paths = extract_all_paths(lines)
tree_paths = set(all_paths)

print('Nodos detectados en el árbol (todos los niveles):')
for path in all_paths:
    print(f'  - {path}')

missing = tree_paths - criteria_nodes
extra = criteria_nodes - tree_paths

if missing:
    print('\nERROR: Los siguientes nodos del árbol no tienen criterios definidos en genre_tree_node_criteria.json:')
    for m in sorted(missing):
        print('  -', m)
    sys.exit(1)
if extra:
    print('\nINFO: Existen criterios definidos para nodos inexistentes en el árbol:')
    for e in sorted(extra):
        print('  -', e)
    confirm = input('¿Deseas eliminar estos criterios de nodos inexistentes? (y/n): ').strip().lower()
    if confirm == 'y':
        data['nodes'] = [node for node in data['nodes'] if node['node_path'] in tree_paths]
        with open('taxonomy/genre_tree_node_criteria.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print('Criterios eliminados.')
    else:
        print('No se realizaron cambios. Revisa los criterios manualmente.')
else:
    print('OK: Todos los nodos del árbol tienen criterios y no hay criterios huérfanos.')
