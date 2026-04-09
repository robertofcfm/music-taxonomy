# REGLAS DE ASIGNACIÓN DE GÉNEROS CON LLM
Sistema de Taxonomía de Géneros Musicales

--------------------------------------------------
METADATOS DEL DOCUMENTO
--------------------------------------------------

Alcance:

Reglas específicas para la asignación de géneros musicales a canciones usando LLM, siguiendo la taxonomía y criterios definidos en el sistema.

Responsable:

Propietario del proyecto

Última actualización:

2026-03-20

--------------------------------------------------
PROPÓSITO
--------------------------------------------------

Este documento define las reglas que debe seguir el proceso de asignación de géneros con LLM:

- Solo se pueden asignar géneros existentes en la taxonomía maestra.
- No se permite inventar géneros ni modificar la taxonomía desde el proceso LLM.
- Cada canción puede tener uno o más géneros, pero todos deben ser válidos y justificados.
- Si el LLM no puede asignar un género válido, debe reportar el caso como "no clasificable".
- El proceso debe ser auditable y dejar registro de las decisiones tomadas.

--------------------------------------------------
REGLAS ESPECÍFICAS
--------------------------------------------------

R1 — VALIDACIÓN CONTRA TAXONOMÍA
Toda asignación debe validarse contra la estructura de géneros definida en taxonomy/genre_tree_master.md.

R2 — PROHIBIDO INVENTAR GÉNEROS
No se permite crear, sugerir ni asignar géneros que no existan en la taxonomía.

R3 — JUSTIFICACIÓN DE ASIGNACIÓN
Cada asignación debe estar justificada con base en criterios musicales y contexto disponible.

R4 — REPORTE DE CASOS NO CLASIFICABLES
Si una canción no puede ser clasificada con los géneros existentes, debe reportarse explícitamente.

R5 — NO MODIFICACIÓN DE TAXONOMÍA
El proceso LLM no puede modificar la taxonomía ni los criterios, solo consultarlos.

R6 — AUDITORÍA
Debe generarse un registro auditable de las asignaciones y justificaciones.

--------------------------------------------------
PROTOCOLOS OPERATIVOS ADICIONALES
--------------------------------------------------

P1 — PARADA POR FALTANTES
La ejecución se detiene automáticamente si se acumulan 5 casos de género faltante (GENRE_MISSING), o al finalizar el lote completo de canciones, lo que ocurra primero.

P2 — CLASIFICACIÓN SOLO EN NODOS HOJA
Solo se permite asignar géneros que sean nodos hoja en la taxonomía. Si un candidato tiene hijos, se deben proponer los hijos como alternativas.

P3 — SINCRONIZACIÓN OBLIGATORIA DE CRITERIOS
Toda propuesta de nuevo nodo en genre_tree_master.md debe incluir su entrada correspondiente en genre_tree_node_criteria.json (membership_criteria, exclusion_criteria, reference_examples). Ambos archivos deben mantenerse sincronizados.

P4 — REPORTE DE FALTANTES CRÍTICOS
Si no existe género adecuado para una canción, se debe reportar el faltante con justificación, propuesta de ubicación en la taxonomía y criterios sugeridos. No escribir en songs_with_genres.csv para esos casos.

P5 — AUTORIZACIÓN Y TRAZABILIDAD
El sistema solo sugiere asignaciones; el usuario final valida y autoriza. No aplicar cambios silenciosos ni masivos. Toda clasificación debe ser trazable y auditable.

P6 — PROTOCOLO DE CARGA DINÁMICA
Diagnosticar y clasificar fuentes y reglas en cada ejecución como: MANDATORY, CONDITIONAL, REFERENTIAL, EXCLUDED. Activar solo reglas con injerencia directa en validez de nodo hoja, criterios de pertenencia, cohesión musical y normalización de nombres.

P7 — FORMATO DE RESPUESTA
Toda ejecución debe generar un reporte estructurado con:
- Diagnóstico de carga dinámica
- Candidatos identificados y validación de nodo hoja
- Asignaciones finales con confianza y justificación
- Faltantes críticos (si aplica) con propuesta de criterios
- Control de ejecución y estado final
- Indicador de capacidad (🟢/🟡/🔴)

--------------------------------------------------
TABLA CORTA DE DECISIÓN: FOLK Y CANCIÓN AUTORAL
--------------------------------------------------

Usar esta tabla para resolver ambigüedad entre nodos cercanos cuando una canción parezca moverse entre folk, pop autoral y cruces latinos.

1. Folk (Standard)
- Usar cuando domina una identidad folk clara dentro de Roots.
- Debe sentirse como continuidad con tradición folk heredada, base acústica u orgánica y poca lógica pop o rock.
- No usar si la canción encaja claramente en Latin Folk o si la lógica principal ya es Pop, Rock o Electronic.

2. Latin Folk Pop
- Usar cuando hay raíz folk latina clara, pero con estructura, producción o accesibilidad pop ya visibles.
- La canción sigue anclada en Latin Folk, pero el acabado es más melódico, amplio o moderno que en un formato austero de canción de autor.
- No usar si domina una austeridad trovadoresca o si el peso principal ya es de Pop sin raíz folk suficientemente clara.

3. Folk Rock
- Usar cuando la herencia folk existe, pero la base estructural ya es Rock.
- Deben mandar la lógica de banda, la instrumentación rock y el sistema rítmico de Rock.
- No usar para folk acústico puro ni para pop autoral íntimo sin base rock estructural.

4. Singer-Songwriter Pop
- Usar cuando la canción es autoral, íntima y personal, pero sigue perteneciendo primero a Pop.
- La melodía, la forma de canción pop y la sensibilidad accesible pesan más que una raíz folk heredada.
- No usar solo porque el artista sea cantautor; si la raíz folk domina, resolver en Roots.

5. Latin Folk Singer-Songwriter
- Usar cuando la canción pertenece claramente a una tradición de canción de autor de raíz folk latinoamericana.
- Deben pesar la lírica, la voz, el acompañamiento sobrio y la impronta personal antes que la producción pop.
- Incluye trova cubana y corrientes afines cuando el tema conserva austeridad arreglística y centralidad del texto.
- No usar si la canción ya funciona mejor como Latin Folk Pop, Pop Ballad o Singer-Songwriter Pop.

Micro-regla de desempate entre Latin Folk Pop y Latin Folk Singer-Songwriter:
- Si el arreglo sigue siendo sobrio, contenido y centrado en voz, texto y acompañamiento acústico/orgánico, priorizar `Latin Folk Singer-Songwriter`.
- Si el acabado melódico, la amplitud del arreglo o la producción expanden claramente la canción más allá del formato austero de autor, priorizar `Latin Folk Pop`.

Regla de desempate:
- Si domina la raíz folk heredada, clasificar en Roots.
- Si domina la forma pop personal, clasificar en Pop.
- Si domina la lógica de banda, clasificar en Rock.
- Si el caso es latino y autoral, priorizar revisar primero Latin Folk Singer-Songwriter contra Latin Folk Pop antes de caer en Singer-Songwriter Pop.
