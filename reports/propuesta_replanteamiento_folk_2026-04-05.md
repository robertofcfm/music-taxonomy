# Propuesta de replanteamiento de la rama Folk - 2026-04-05

## Veredicto

Si, la rama Folk se puede y se deberia replantear.

La conclusion principal es esta:

- `Traditional Folk` debe mantenerse, pero con una definicion mas estricta y claramente limitada a folk tradicional real.
- `Folk Rock` debe quedarse en la rama `Rock`.
- Hace falta un nodo nuevo para cubrir folk moderno no tradicional sin groove rock dominante.
- No conviene abrir a la vez `Contemporary Folk` y `Songwriter Folk`, porque hoy se superponen demasiado y duplicarian frontera con `Singer-Songwriter Pop`.

## Recomendacion estructural minima

Arbol propuesto:

```text
Music
  Roots
    Folk
      Traditional Folk
      Contemporary Folk
      Latin Folk
        Latin Folk Pop
        Trova Cubana
        Vallenato
```

Sin cambios:

- `Music > Rock > Folk Rock` se mantiene exactamente donde esta.

## Por que no abrir tambien Songwriter Folk

Abrir al mismo tiempo `Contemporary Folk` y `Songwriter Folk` hoy seria prematuro por estas razones:

1. La diferencia operativa entre ambos todavia no esta suficientemente estabilizada en el catalogo.
2. `Songwriter Folk` chocaria frontalmente con `Singer-Songwriter Pop`.
3. La gobernanza pide expansion minima y evitar nodos especulativos o redundantes.
4. Con la evidencia actual, un solo nodo nuevo resuelve el hueco principal sin introducir ambiguedad adicional.

## Logica taxonomica propuesta

### 1. Traditional Folk

Debe quedar como nodo estricto para:

- folk tradicional real
- raiz cultural o folclorica clara
- fuerte sensacion de tradicion heredada o marco tradicional reconocible
- instrumentacion acustica predominante
- sin groove de banda moderna estructural

No debe absorber:

- cancion de autor moderna
- folk intimista contemporaneo
- baladas acusticas solo por sonar sobrias
- canciones con bateria/bajo estructural o logica de banda

### 2. Contemporary Folk

Nuevo nodo propuesto para:

- canciones modernas con identidad folk clara, pero sin condicion de tradicion oral o raiz folclorica heredada
- predominio acustico o semiacustico
- enfoque en voz, letra, timbre organico y cancion sobria
- groove tenue, no bailable, no rock dominante, no pop claramente rector
- sensibilidad folk contemporanea antes que pop o rock

Debe excluir:

- folk tradicional real -> `Traditional Folk`
- canciones con estructura de banda rock dominante -> `Folk Rock`
- canciones cuya identidad principal sea pop accesible o cancion pop autoral -> `Singer-Songwriter Pop` o `Pop Ballad`

### 3. Folk Rock

Debe seguir en `Rock` porque ahi domina:

- groove de banda
- bateria y bajo estructurales
- logica de cancion de banda
- fusion de elementos folk con sistema rock

Moverlo a `Roots > Folk` debilitaria el principio base del arbol, que clasifica por sistema dominante.

### 4. Singer-Songwriter Pop

Debe estrecharse. No deberia recibir automaticamente toda cancion de autor intimista.

Debe reservarse para:

- cancion autoral con identidad principal pop
- melodia y estructura pop claramente rectoras
- accesibilidad pop mas fuerte que identidad folk

No deberia absorber:

- folk moderno acustico donde el color folk pese mas que la logica pop

## Justificacion por groove e identidad

La reestructuracion es coherente con la gobernanza actual porque:

1. Respeta el principio de sistema dominante.
2. Evita meter en `Roots` canciones con groove rock claro, por eso `Folk Rock` se queda en `Rock`.
3. Corrige un hueco real: canciones que no son tradicionales, pero tampoco son pop limpias.
4. Reduce el uso forzado de `Singer-Songwriter Pop` como paraguas para casos folk contemporaneos.

## Candidatos claros a mover si se crea Contemporary Folk

### Desde Traditional Folk

1. `Hallelujah` - Leonard Cohen
   - Nodo actual: `Traditional Folk`
   - Problema: no es folk tradicional
   - Nodo propuesto: `Contemporary Folk`
   - Puntuacion estimada en `Traditional Folk`: 34
   - Puntuacion estimada en `Contemporary Folk`: 88

2. `The Sound of Silence` - Simon & Garfunkel
   - Caso resuelto por metadata: la pista del catalogo es `Electric Version`
   - Nodo correcto: `Folk Rock`
   - Puntuacion estimada en `Traditional Folk`: 45
   - Puntuacion estimada en `Folk Rock` para version electrificada: 88

### Desde Singer-Songwriter Pop

1. `Acurrucar` - Ed Maverick
   - Nodo actual: `Singer-Songwriter Pop`
   - Nodo propuesto: `Contemporary Folk`
   - Puntuacion estimada en `Singer-Songwriter Pop`: 63
   - Puntuacion estimada en `Contemporary Folk`: 87

2. `Fuentes de Ortiz` - Ed Maverick
   - Nodo actual: `Singer-Songwriter Pop`
   - Nodo propuesto: `Contemporary Folk`
   - Puntuacion estimada en `Singer-Songwriter Pop`: 66
   - Puntuacion estimada en `Contemporary Folk`: 84

## Casos que probablemente deben quedarse donde estan

1. `Pisando fuerte` - Alejandro Sanz
   - Mantener en `Singer-Songwriter Pop`
   - Folk no domina de forma suficiente

2. `One Of Us` - Joan Osborne
   - Mantener en `Singer-Songwriter Pop`
   - Sigue sintiendose primero como cancion pop de autora, no como folk contemporaneo claro

3. `Imagine` - John Lennon
   - Mantener en `Singer-Songwriter Pop`
   - La identidad folk no domina

4. `Beautiful Boy (Darling Boy)` - John Lennon
   - Mantener en `Singer-Songwriter Pop`
   - Intimista y autoral, pero no lo suficiente folk para moverlo

5. `The Times They Are A-Changin'` - Bob Dylan
   - Mantener en `Traditional Folk`
   - Es ejemplo directo del nodo y encaje fuerte del criterio actual

## Cambios recomendados en criterios

### Traditional Folk

Agregar una aclaracion fuerte:

> No usar este nodo para cancion de autor moderna, aunque sea acustica, austera o liricamente intensa, si no existe raiz tradicional clara.

### Singer-Songwriter Pop

Agregar una aclaracion fuerte:

> Si la identidad principal descansa en sensibilidad folk contemporanea, timbre acustico y marco de cancion folk moderna mas que en una logica pop, no usar este nodo.

### Nuevo Contemporary Folk

Definicion sugerida:

> Canciones modernas de identidad folk clara, generalmente acusticas o semiacusticas, centradas en voz, letra, timbre organico y sensibilidad intimista, sin requerir raiz tradicional heredada y sin estructura de banda rock dominante. El pulso puede existir, pero no debe sentirse como groove pop o rock rector.

Exclusiones sugeridas:

> Folk tradicional de raiz cultural clara (`Traditional Folk`), canciones con bateria y logica de banda dominantes (`Folk Rock`), o canciones cuya identidad principal sea pop autoral accesible (`Singer-Songwriter Pop`).

## Conclusiones finales

1. Si conviene replantear la rama Folk.
2. La mejor expansion hoy es `Traditional Folk` + `Contemporary Folk`.
3. No conviene abrir todavia `Songwriter Folk` como nodo separado.
4. `Folk Rock` debe permanecer en `Rock`.
5. Parte de lo hoy clasificado como `Singer-Songwriter Pop` si parece candidato real a una rama Folk mas apropiada, especialmente Ed Maverick.