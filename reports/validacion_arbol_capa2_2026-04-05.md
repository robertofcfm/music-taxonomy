# Validacion Capa 2 - 2026-04-05

## Fuentes usadas

- governance/01_auditar_arbol
- taxonomy/genre_tree_master.md
- taxonomy/genre_tree_node_criteria.json
- catalog/songs_with_genres.csv
- reports/canciones_nuevas.json

## Canciones nuevas evaluadas

Se evaluaron las 4 canciones devueltas por scripts/filtrar_canciones_nuevas.py.

| Cancion | Artista | Nodo propuesto | Nodo existente o nuevo | Puntuacion regla 15 | Decision |
|---|---|---|---|---:|---|
| Hard to Say I'M Sorry / Get Away | Chicago | Music > Rock > Soft Rock | Existente | 78 | Asignar a nodo existente |
| Alone Again (Naturally) | Gilbert O'sullivan | Music > Pop > Pop Ballad | Existente | 86 | Asignar a nodo existente |
| A Whiter Shade of Pale | Procol Harum | Music > Rock > Psychedelic Rock | Existente | 84 | Asignar a nodo existente |
| California Dreamin' | The Mamas & The Papas | Music > Rock > Folk Rock | Existente | 95 | Asignar a nodo existente |

## Justificacion resumida

### Hard to Say I'M Sorry / Get Away - Chicago

- La identidad dominante sigue siendo de banda organica y rock suave/adult contemporary.
- La cancion prioriza melodia, armonia y arreglo suave por encima de groove rhythmic o beat electronico.
- La coda de Get Away agrega energia, pero no desplaza la base general fuera de Soft Rock.

### Alone Again (Naturally) - Gilbert O'sullivan

- Balada centrada en melodia, voz y piano.
- La estructura de cancion domina claramente sobre cualquier groove.
- No hay una identidad rock de banda suficientemente fuerte para moverla a Soft Rock.

### A Whiter Shade of Pale - Procol Harum

- La identidad principal descansa en atmosfera expansiva, organo prominente y psicodelia de banda.
- El caracter surreal y la sensacion psicodelica pesan mas que una lectura estrictamente pop o soft rock.
- No exige un nodo nuevo porque Psychedelic Rock ya existe y resuelve bien el caso.

### California Dreamin' - The Mamas & The Papas

- Caso canonico de Folk Rock: fusion de sensibilidad folk con instrumentacion y forma de banda.
- Guitarras, armonias vocales y composicion encajan de forma muy fuerte en el nodo existente.

## Conclusiones

- Ninguna de las 4 canciones requiere nodo nuevo.
- Las 4 pueden asignarse de forma estable a nodos ya presentes en catalog/songs_with_genres.csv.
- Bajo la regla 15, todas quedan en rango valido de pertenencia (>= 70), por lo que no hay justificacion para expandir el blueprint en este lote.