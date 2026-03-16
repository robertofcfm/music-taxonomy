# Reporte de Validación MVET (Capa 2 — Semántica IA)

- Fecha: 2026-03-16T04:44:52+00:00
- Decisión: PASS_WITH_WARNINGS
- FATAL: 0
- WARNING: 6
- SUGGESTION: 0

## Hallazgos

### MVET-L2-001 [FB-05] - WARNING
- Nodo: Music > Soul / Funk / R&B
- Evidencia: Los nodos hermanos Soul y Rhythm & Blues presentan una frontera estilística difusa en muchas discografías modernas. Gran parte del catálogo contemporáneo clasificado como Soul también se etiqueta como R&B, lo que puede producir playlists con contenido altamente indistinguible.
- Recomendación: Revisar la distinción curatorial entre Soul y Rhythm & Blues para asegurar criterios claros de clasificación (era, instrumentación, tradición estilística). Si no se pueden mantener playlists claramente diferenciadas, considerar redefinir criterios editoriales o documentar explícitamente el límite semántico.
- Confianza: 0.86

### MVET-L2-002 [FB-05] - WARNING
- Nodo: Music > Instrumental / Score
- Evidencia: El nodo mezcla potencialmente música instrumental genérica con música de score cinematográfico o de videojuegos. Estos dominios pueden producir playlists con objetivos musicales distintos (ambiental, cinematográfico, orquestal, minimalista, etc.).
- Recomendación: Evaluar si el nodo debe representar exclusivamente música de score o si debe mantenerse como nodo paraguas. Si se mantiene, documentar explícitamente el alcance para evitar mezcla incoherente de playlists.
- Confianza: 0.81

### MVET-L2-003 [FB-05] - WARNING
- Nodo: Music > Pop > Pop Rock > Alternative Pop Rock
- Evidencia: Alternative Pop Rock puede solaparse semánticamente con Indie Rock dentro de Music > Rock > Alternative & Indie. Ambos estilos pueden generar playlists con repertorio altamente coincidente dependiendo del artista.
- Recomendación: Revisar el límite entre Alternative Pop Rock e Indie Rock. Si el criterio diferenciador es la orientación comercial o la producción pop, documentar esa diferencia para evitar redundancia estructural.
- Confianza: 0.78

### MVET-L2-006 [FB-06] - WARNING
- Nodo: Music > Rock > Roots & Early Rock > Blues Rock
- Evidencia: Blues Rock es históricamente un subgénero consolidado del Rock en general y no exclusivamente del periodo 'Roots & Early Rock'. Además, su desarrollo principal ocurre en décadas posteriores al Rock & Roll temprano.
- Recomendación: Evaluar si Blues Rock debería ser hermano directo dentro de Rock en lugar de estar contenido bajo Roots & Early Rock. La ubicación actual puede sugerir erróneamente que pertenece solo al periodo fundacional del género.
- Confianza: 0.88

### MVET-L2-002 [FB-05] - WARNING
- Nodo: Music > Electronic & Dance > Downtempo
- Evidencia: Downtempo puede actuar como categoría paraguas que incluye estilos muy diversos (chillout, trip hop instrumental, lounge electrónico, ambient beat). Esta amplitud puede producir playlists estilísticamente inconsistentes.
- Recomendación: Verificar si el nodo se usa como categoría operativa amplia o si se requiere documentación curatorial para mantener coherencia musical en las playlists generadas.
- Confianza: 0.76

### MVET-L2-005 [FB-05] - WARNING
- Nodo: Music > Rock > Alternative & Indie > Post Punk > Gothic Rock
- Evidencia: Gothic Rock es un subgénero históricamente bien definido con identidad musical clara y generalmente no se subdivide más sin entrar en micro-escenas o etiquetas híbridas.
- Recomendación: Considerar tratar Gothic Rock como nodo atómico en la política editorial para evitar subdivisiones artificiales en futuras expansiones.
- Confianza: 0.83
