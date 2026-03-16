# Reporte de Validación MVET (Capa 2 — Semántica IA)

- Fecha: 2026-03-16T01:56:45+00:00
- Decisión: PASS_WITH_WARNINGS
- FATAL: 0
- WARNING: 8
- SUGGESTION: 0

## Hallazgos

### MVET-L2-001 [FB-05] - WARNING
- Nodo: Music > Metal > Alternative Metal > Post-Grunge Metal
- Evidencia: Post-Grunge Metal tiene solapamiento sonoro alto con Post-Grunge (hermano bajo Alternative & Indie > Indie Rock > Grunge). Ambos comparten influencias de Grunge pesado con producción alternativa, lo que podría hacer sus playlists indistinguibles.
- Recomendación: Evaluar si Post-Grunge Metal es suficientemente distinguible de Post-Grunge. Si el criterio es el peso instrumental y distorsión, documentar esa distinción o considerar consolidar bajo Grunge/Post-Grunge con tag de intensidad.
- Confianza: 0.78

### MVET-L2-001 [FB-05] - WARNING
- Nodo: Music > Pop > Pop Rock
- Evidencia: Alternative Pop Rock y Alternative Pop son hermanos bajo Pop Rock. Sus nombres difieren solo en la presencia de 'Rock', pero musicalmente el límite entre pop alternativo con influencia rock y pop alternativo sin ella es frecuentemente difuso.
- Recomendación: Definir criterio de distinción explícito: si Alternative Pop requiere ausencia de guitarra como elemento central, documentarlo. De lo contrario, evaluar fusión.
- Confianza: 0.70

### MVET-L2-003 [FB-05] - WARNING
- Nodo: Music > Rock > Alternative & Indie > Post Punk > Coldwave
- Evidencia: Coldwave y Darkwave son hermanos con alta superposición estilística. Ambos derivan de Post-Punk con influencias electrónicas oscuras y atmosféricas. La distinción entre ambos es debatida incluso en la literatura musical especializada.
- Recomendación: Si el catálogo no tiene volumen suficiente para justificar ambos nodos por separado, evaluar fusión en un único nodo 'Coldwave / Darkwave' o promover uno como canónico y el otro como clone.
- Confianza: 0.82

### MVET-L2-003 [FB-05] - WARNING
- Nodo: Music > Pop > Pop Rock > Latin Pop Rock
- Evidencia: Latin Pop Rock existe bajo Pop > Pop Rock, mientras la rama Latin está separada en Music > Latin. Un género con nombre explícitamente 'Latin' fuera de la rama Latin genera riesgo de ambigüedad de dominio aunque no viola formalmente la separación si su contenido es non-Latin con influencia soft.
- Recomendación: Clarificar si Latin Pop Rock representa bandas no-Latin con influencia latina superficial, o si debería pertenecer a la rama Latin. Si es el primer caso, considerar renombre para evitar confusión.
- Confianza: 0.72

### MVET-L2-005 [FB-05] - WARNING
- Nodo: Music > Rock > Alternative & Indie > Indie Rock > Grunge > Seattle Grunge
- Evidencia: Seattle Grunge y Post-Grunge son hojas de nivel 6. Seattle Grunge representa un subconjunto geográfico-temporal de Grunge que en la práctica de clasificación es atómico: subdividirlo más (por bandas o décadas) produciría categorías artificiales.
- Recomendación: Confirmar como nodos atómicos. No subdividir. Verificar que el volumen de canciones en cada uno justifique mantenerlos separados o si Grunge como padre directo sería suficiente.
- Confianza: 0.85

### MVET-L2-005 [FB-05] - WARNING
- Nodo: Music > Rock > Alternative & Indie > Indie Rock > Grunge > Post-Grunge
- Evidencia: Post-Grunge en nivel 6. Ver hallazgo anterior. Adicionalmente existe Post-Grunge Metal bajo Metal > Alternative Metal, lo que refuerza que Post-Grunge como concepto ya está fragmentado entre dos ramas.
- Recomendación: Considerar si Post-Grunge debería ser canónico bajo Grunge (nivel 6) o si debería ascender un nivel. Evaluar nodo clone desde Metal > Alternative Metal hacia el canónico.
- Confianza: 0.80

### MVET-L2-006 [FB-06] - WARNING
- Nodo: Music > Electronic & Dance > Downtempo
- Evidencia: Downtempo como hijo directo de Electronic & Dance al mismo nivel que House y Disco es correcto estructuralmente, pero Downtempo tiene mayor afinidad semántica con Ambient que con Disco o House. En flujo de playlist, la transición Disco > Downtempo genera discontinuidad.
- Recomendación: Evaluar si Downtempo como hermano de Ambient (o como hijo de un nuevo nodo 'Atmospheric Electronic') mejora la cohesión de playlists.
- Confianza: 0.65

### MVET-L2-007 [FB-06] - WARNING
- Nodo: Music > Metal > Thrash Metal > Bay Area Thrash
- Evidencia: Bay Area Thrash y Groove Thrash son los únicos dos hijos de Thrash Metal. Bay Area Thrash es una distinción geográfica y de era (1980s California), mientras Groove Thrash es una evolución estilística de los 90s. La distinción es válida pero el volumen de nodos es mínimo.
- Recomendación: Mantener si el catálogo tiene volumen suficiente para cada uno. Si no, Thrash Metal como hoja resulta más cohesivo. Revisar umbral de expansión.
- Confianza: 0.68
