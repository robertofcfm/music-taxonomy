import csv
from collections import defaultdict

# Leer el árbol de géneros desde genre_tree.md
def cargar_arbol_generos(path):
    with open(path, encoding='utf-8') as f:
        lineas = [line.rstrip() for line in f if line.strip()]
    arbol = set()
    padres = {}
    nodos = []
    for idx, linea in enumerate(lineas):
        nivel = (len(linea) - len(linea.lstrip(' '))) // 2
        nombre = linea.strip()
        nodos.append((nivel, nombre))
        if nivel == 0:
            arbol.add(nombre)
            padres[nombre] = None
        else:
            # Buscar el padre inmediato
            for j in range(idx-1, -1, -1):
                prev_nivel, prev_nombre = nodos[j]
                if prev_nivel == nivel-1:
                    padre = prev_nombre
                    break
            rama = []
            actual_nivel = nivel
            for j in range(idx-1, -1, -1):
                prev_nivel, prev_nombre = nodos[j]
                if prev_nivel < actual_nivel:
                    rama.insert(0, prev_nombre)
                    actual_nivel = prev_nivel
            full_path = ' > '.join(rama + [nombre])
            arbol.add(full_path)
            padres[full_path] = rama[-1] if rama else None
    return arbol, padres

def encontrar_genero_valido(genero, ramas):
    if not genero:
        return ''
    partes = [p.strip() for p in genero.split('>')]
    for i in range(len(partes), 0, -1):
        rama = ' > '.join(partes[:i])
        if rama in ramas:
            return rama
    return partes[0]  # fallback

def sumar_hijos(conteo, padres):
    suma = defaultdict(int)
    for nodo in conteo:
        actual = nodo
        while actual:
            suma[actual] += conteo[nodo]
            actual = padres.get(actual)
    return suma

# Procesar canciones
def procesar_canciones(input_csv, arbol_path, output_csv):
    ramas, padres = cargar_arbol_generos(arbol_path)
    conteo = defaultdict(int)
    with open(input_csv, encoding='utf-8') as fin, open(output_csv, 'w', encoding='utf-8', newline='') as fout:
        reader = csv.DictReader(fin)
        writer = csv.DictWriter(fout, fieldnames=['title', 'artist', 'genre'])
        writer.writeheader()
        for row in reader:
            genero_original = row.get('genre')
            if not genero_original or not genero_original.strip():
                continue
            genero_valido = encontrar_genero_valido(genero_original, ramas)
            writer.writerow({'title': row['title'], 'artist': row['artist'], 'genre': genero_valido})
            conteo[genero_valido] += 1
    suma = sumar_hijos(conteo, padres)
    print('Reporte de asignación por nodo:')
    # Mostrar todos los nodos del árbol, aunque no tengan canciones directas, ordenados jerárquicamente
    def ordenar_nodos(nodos):
        # Ordena jerárquicamente por nivel y alfabéticamente
        return sorted(nodos, key=lambda n: (n.count('>'), n))

    for nodo in ordenar_nodos(ramas):
        if nodo.startswith('Music'):
            cantidad = suma.get(nodo, 0)
            # Si el nodo no tiene canciones directas pero sí hijos, sumar hijos
            hijos = [n for n in ramas if n != nodo and n.startswith(nodo + ' >')]
            if cantidad == 0 and hijos:
                cantidad = sum(suma.get(h, 0) for h in hijos)
            print(f'{nodo}: {cantidad}')

if __name__ == '__main__':
    procesar_canciones(
        'catalog/songs_with_genres.csv',
        'taxonomy/genre_tree.md',
        'catalog/cancionesConGenero.csv'
    )
