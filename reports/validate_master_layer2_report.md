# Reporte de Validación MVET (Capa 2 — Semántica IA)

- Fecha: 2026-03-16T04:25:23+00:00
- Decisión: PASS_WITH_WARNINGS
- FATAL: 0
- WARNING: 4
- SUGGESTION: 1

## Hallazgos

### MVET-L2-001 [FB-05] - WARNING
- Nodo: Music > Rock > Alternative & Indie > Indie Rock > Brit Pop
- Evidencia: Brit Pop, aunque históricamente ligado al Indie Rock, presenta una estructura melódica y producción que a menudo lo hace indistinguible de ramas de Power Pop o Pop Rock en términos de curación de playlists.
- Recomendación: Evaluar si Brit Pop debe mantenerse como hijo de Indie Rock o si su proximidad al Pop amerita una referencia cruzada (clone).
- Confianza: 0.85

### MVET-L2-003 [FB-05] - WARNING
- Nodo: Music > Pop > New Wave > Electronic Dream Pop
- Evidencia: Potencial redundancia con Music > Rock > Alternative & Indie > Dream Pop. La distinción entre ambos nodos para la generación de playlists es baja debido al solapamiento de texturas etéreas y sintetizadores.
- Recomendación: Fusionar bajo Dream Pop o definir Electronic Dream Pop como un nodo atómico con reglas de producción estrictamente electrónicas.
- Confianza: 0.90

### MVET-L2-005 [FB-05] - SUGGESTION
- Nodo: Music > Rock > Alternative & Indie > Grunge (Atomic)
- Evidencia: El nodo está correctamente marcado como Atomic. Subdividirlo en sub-escenas (Seattle Sound vs Post-Grunge) degradaría la cohesión de la rama madre.
- Recomendación: Mantener como Atomic y no permitir descendencia.
- Confianza: 1.00

### MVET-L2-006 [FB-06] - WARNING
- Nodo: Music > Soul / Funk / R&B > Disco
- Evidencia: Musicalmente, Disco comparte más rasgos estructurales de BPM y patrones rítmicos con 'Electronic & Dance' que con las formas tradicionales de Soul o R&B.
- Recomendación: Considerar reubicación bajo Electronic & Dance o crear un nodo portal (clone) en dicha sección.
- Confianza: 0.80

### MVET-L2-007 [FB-06] - WARNING
- Nodo: Music > Rock > Roots & Early Rock > Blues Rock
- Evidencia: Los nodos hermanos 'Texas Blues Rock' y 'Classic Blues Rock' presentan un solapamiento estilístico alto que podría no justificar la separación en la Capa 2.
- Recomendación: Fusionar en un único nodo Blues Rock o mover a una capa de mayor profundidad si se requiere granularidad geográfica.
- Confianza: 0.75
