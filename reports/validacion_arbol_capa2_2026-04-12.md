# Validacion Capa 2 - 2026-04-12

## Fuentes utilizadas

- governance/01_auditar_arbol
- taxonomy/genre_tree_master.md
- taxonomy/genre_tree_node_criteria.json
- catalog/songs_with_genres.csv
- catalog/favorites_qobuz.csv
- reports/canciones_nuevas_detalle.csv

## Ejecucion del filtro

Script ejecutado: `scripts/filtrar_canciones_nuevas.py`

Resultado real:

- Canciones nuevas detectadas: 6
- No se detectaron duplicados en `catalog/favorites_qobuz.csv`

## Decision estructural

No se propone nodo nuevo.

Motivos:

1. El nodo existente `Music > Roots > Folk > Latin Folk > Latin Folk Singer-Songwriter` ya cubre de forma explicita la trova cubana y corrientes afines de cancion de autor hispanohablante.
2. Ya existen precedentes en `catalog/songs_with_genres.csv` para Fernando Delgadillo, Pablo Milanes y Silvio Rodriguez dentro de ese mismo nodo.
3. La regla de creacion de nodo nuevo exige multiples canciones con identidad comun que no encajen en nodos existentes; aqui si existe un nodo existente adecuado.

## Asignaciones propuestas

| Titulo | Artista | Nodo propuesto | Tipo | Score regla 15 | Decision |
|---|---|---|---|---:|---|
| Te Doy Una Cancion | Silvio Rodriguez and Pablo Milanes | Music > Roots > Folk > Latin Folk > Latin Folk Singer-Songwriter | Existente | 94 | Mantener en nodo existente |
| No Me Pidas Ser Tu Amigo | Fernando Delgadillo | Music > Roots > Folk > Latin Folk > Latin Folk Singer-Songwriter | Existente | 93 | Mantener en nodo existente |
| El Amor De Mi Vida | Pablo Milanes | Music > Roots > Folk > Latin Folk > Latin Folk Singer-Songwriter | Existente | 76 | Mantener en nodo existente, con monitoreo |
| La Banera | Fernando Delgadillo | Music > Roots > Folk > Latin Folk > Latin Folk Singer-Songwriter | Existente | 92 | Mantener en nodo existente |
| Entre Pairos y Derivas | Fernando Delgadillo | Music > Roots > Folk > Latin Folk > Latin Folk Singer-Songwriter | Existente | 91 | Mantener en nodo existente |
| Gracias a la vida | Violeta Parra | Music > Roots > Folk > Latin Folk > Latin Folk Singer-Songwriter | Existente | 95 | Mantener en nodo existente |

## Justificacion resumida por cancion

### Te Doy Una Cancion - Silvio Rodriguez and Pablo Milanes

- Encaja con el criterio de cancion de autor de raiz folk latino.
- La taxonomia indica expresamente que la trova cubana pertenece a `Latin Folk Singer-Songwriter` cuando conserva austeridad arreglistica y centralidad del texto.
- Existe precedente catalogado de Silvio Rodriguez en el mismo nodo.

### No Me Pidas Ser Tu Amigo - Fernando Delgadillo

- Fernando Delgadillo ya tiene precedente en el catalogo dentro del mismo nodo.
- La identidad operativa del artista en el catalogo responde a cancion de autor hispanohablante, centrada en letra y acompanamiento sobrio.

### El Amor De Mi Vida - Pablo Milanes

- Existe precedente catalogado de Pablo Milanes en el mismo nodo.
- Se asigna al nodo existente por continuidad y porque no hay evidencia documental en los archivos disponibles de una produccion lo bastante expandida como para moverla a `Latin Folk Pop`.
- Queda con score mas bajo porque la version concreta podria requerir verificacion auditiva si se quiere cerrar con mayor certeza.

### La Banera - Fernando Delgadillo

- Mismo patron que el precedente existente del artista.
- No hay evidencia de expansion pop predominante ni de salida de la rama Latin Folk.

### Entre Pairos y Derivas - Fernando Delgadillo

- Mismo razonamiento que para el resto del bloque autoral de Fernando Delgadillo.
- El nodo existente resuelve la clasificacion sin necesidad de abrir subnodo adicional.

### Gracias a la vida - Violeta Parra

- Cancion de autora fundamental del folk latinoamericano, con centro en texto, interpretacion vocal y raiz folk reconocible.
- No hay senales en los archivos disponibles que justifiquen `Latin Folk Pop`, `Bolero` o un nodo nuevo.

## Aplicacion de la regla 15

Segun `governance/01_auditar_arbol`:

- 90-100: encaje perfecto
- 70-89: encaje fuerte (valido)
- 50-69: borderline
- <50: no pertenece

Interpretacion para este lote:

- 5 canciones quedan en rango de asignacion estable o muy fuerte.
- 1 cancion (`El Amor De Mi Vida`) queda en rango valido pero de monitoreo, no por conflicto estructural, sino por falta de evidencia de detalle arreglistico en los archivos consultados.