# Auditoria del nodo Traditional Folk - 2026-04-05

## Fuentes autoritativas usadas

- governance/01_auditar_arbol
- taxonomy/genre_tree_master.md
- taxonomy/genre_tree_node_criteria.json
- catalog/songs_with_genres.csv

## Definicion vigente del nodo

Nodo: Music > Roots > Folk > Traditional Folk

Criterio de pertenencia:

> Musica folclorica de transmision oral, propia de una region o cultura, interpretada con instrumentos tradicionales y sin estructura de banda moderna. Voz y acompanamiento acustico predominante, sin groove de banda (sin bateria/bajo estructural).

Exclusiones:

> Folk fusionado con rock/pop, canciones con bateria o estructura de banda, o musica de autor moderna sin raiz tradicional clara.

## Canciones actualmente asignadas

1. The Times They Are A-Changin' - Bob Dylan
2. Hallelujah - Leonard Cohen
3. The Sound of Silence - Simon & Garfunkel

## Dictamen por cancion

### 1. The Times They Are A-Changin' - Bob Dylan

- Estado: correcta
- Puntuacion regla 15 para Traditional Folk: 96
- Motivo: ademas de encajar por formato acustico y ausencia de groove de banda, esta cancion aparece como ejemplo explicito del propio nodo en genre_tree_node_criteria.json. Bajo la definicion vigente, debe mantenerse.

### 2. Hallelujah - Leonard Cohen

- Estado: incorrecta
- Puntuacion regla 15 para Traditional Folk: 34
- Motivo: no es una obra de transmision oral ni de raiz tradicional clara; es una cancion de autor moderna. La asignacion actual viola de forma directa la exclusion del nodo: "musica de autor moderna sin raiz tradicional clara".
- Nodo alternativo recomendado: Music > Roots > Folk > Contemporary Folk
- Puntuacion estimada en nodo alternativo: 88
- Justificacion del nodo alternativo: cancion moderna sobria, organica, lirica y de sensibilidad folk contemporanea, sin raiz tradicional clara pero tambien sin una logica pop lo bastante rectora como para resolverla mejor en Singer-Songwriter Pop.

### 3. The Sound of Silence - Simon & Garfunkel

- Estado: incorrecta, version confirmada
- Puntuacion regla 15 para Traditional Folk: 45
- Motivo: la metadata del catalogo y de Qobuz confirma que la pista es `Electric Version` con ISRC `USSM16401131`, por lo que cae en la exclusion de Traditional Folk y encaja mejor en Folk Rock.
- Nodo alternativo recomendado: Music > Rock > Folk Rock
- Puntuacion estimada en nodo alternativo: 88
- Observacion critica: el caso ya no esta pendiente; la fila fue resuelta y movida a Folk Rock al confirmarse la version electrificada.

## Conclusiones de auditoria

- El nodo Traditional Folk no esta totalmente mal poblado, pero contenia dos asignaciones incorrectas ya resueltas fuera del nodo.
- Cancion que debe mantenerse: The Times They Are A-Changin' - Bob Dylan.
- Cancion que debe moverse: Hallelujah - Leonard Cohen -> Music > Roots > Folk > Contemporary Folk.
- Cancion resuelta por metadata: The Sound of Silence - Simon & Garfunkel -> Music > Rock > Folk Rock.

## Riesgo taxonomico detectado

Traditional Folk corre el riesgo de absorber canciones de autor acusticas o folk-rock solo por cercania estetica. Eso contradice la definicion vigente del nodo, que exige raiz tradicional clara y ausencia de estructura moderna de banda.