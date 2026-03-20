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
