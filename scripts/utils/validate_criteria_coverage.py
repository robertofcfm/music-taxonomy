# Validación de cobertura de criterios para cada nodo del árbol

import json
import sys

with open('taxonomy/genre_tree_master.md', encoding='utf-8') as f:
    lines = [line.strip() for line in f if line.strip()]

def extract_paths(lines):
    paths = []
    stack = []
    for line in lines:
        indent = len(line) - len(line.lstrip())
        name = line.strip()
        level = indent // 2
        stack = stack[:level]
        stack.append(name)
        paths.append(' > '.join(stack))
    return paths

with open('taxonomy/genre_tree_node_criteria.json', encoding='utf-8') as f:
    data = json.load(f)
    criteria_nodes = set(node['node_path'] for node in data['nodes'])

tree_paths = set(extract_paths(lines))

missing = tree_paths - criteria_nodes
extra = criteria_nodes - tree_paths

if missing:
    print('ERROR: Los siguientes nodos del árbol no tienen criterios definidos en genre_tree_node_criteria.json:')
    for m in sorted(missing):
        print('  -', m)
    sys.exit(1)
if extra:
    print('ERROR: Existen criterios definidos para nodos inexistentes en el árbol:')
    for e in sorted(extra):
        print('  -', e)
    sys.exit(1)
print('OK: Todos los nodos del árbol tienen criterios y no hay criterios huérfanos.')
