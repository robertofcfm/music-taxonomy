# Reporte de Validación MVET (Capa 2 — Semántica IA)

- Fecha: 2026-03-16T06:00:47+00:00
- Decisión: PASS_WITH_WARNINGS
- FATAL: 0
- WARNING: 7
- SUGGESTION: 0

## Hallazgos

### MVET-L2-001 [FB-05] - WARNING
- Nodo: Music > Rock > Alternative & Indie > Post Punk
- Evidencia: Los nodos hijos New Wave, Coldwave y Darkwave comparten fuerte herencia directa del Post-Punk con características sonoras cercanas (uso prominente de sintetizadores, estética oscura y estructuras rítmicas similares). En contextos de playlists, New Wave y Coldwave pueden producir resultados estilísticamente cercanos dependiendo del periodo histórico o selección de artistas.
- Recomendación: Revisar si la separación actual entre New Wave, Coldwave y Darkwave produce playlists suficientemente distinguibles o si requiere clarificación semántica adicional a nivel taxonómico. No se recomienda modificación automática.
- Confianza: 0.63

### MVET-L2-001 [FB-05] - WARNING
- Nodo: Music > Pop > Synth & Electronic Pop > Synth Pop
- Evidencia: Los nodos hijos Electro Pop y New Romantic presentan una intersección histórica fuerte dentro del ecosistema Synth Pop de los años 80 y revival posterior. En muchos catálogos discográficos los artistas pueden aparecer simultáneamente clasificados en ambos estilos, lo que puede producir playlists parcialmente indistinguibles.
- Recomendación: Revisar si el nodo Electro Pop está siendo utilizado como subgénero estilístico claro o como extensión moderna del Synth Pop. Considerar si la distinción se sostiene consistentemente en clasificación musical.
- Confianza: 0.66

### MVET-L2-002 [FB-05] - WARNING
- Nodo: Music > Electronic & Dance
- Evidencia: El nodo mezcla estilos orientados a pista de baile (Disco, House, Electro House) con estilos predominantemente atmosféricos o no rítmicos (Ambient, Dark Ambient, Cinematic Ambient). Esto puede generar playlists con coherencia rítmica inconsistente si el nodo se utiliza como punto de reproducción.
- Recomendación: Tratar el nodo principalmente como agrupador estructural y priorizar la reproducción desde sus subgéneros más específicos para evitar mezclas estilísticas amplias.
- Confianza: 0.82

### MVET-L2-003 [FB-05] - WARNING
- Nodo: Music > Rock > Alternative & Indie > Dream Pop / Music > Rock > Alternative & Indie > Post Punk > Coldwave
- Evidencia: Dream Pop y Coldwave comparten estética sonora atmosférica, uso extensivo de reverberación y estructuras melódicas etéreas. En algunos catálogos y escenas musicales (especialmente en Europa y revival post-2000) los artistas pueden aparecer etiquetados indistintamente en ambos estilos.
- Recomendación: Revisar si existe solapamiento excesivo en clasificación práctica entre ambos nodos dentro del árbol. No implica necesariamente fusión, pero sí monitoreo taxonómico.
- Confianza: 0.55

### MVET-L2-004 [FB-05] - WARNING
- Nodo: Music > Rock > Alternative & Indie > Post Punk
- Evidencia: El nodo contiene cuatro subgéneros (New Wave, Gothic Rock, Coldwave, Darkwave) que representan evoluciones estilísticas históricamente relacionadas del Post-Punk. Aunque distinguibles, la granularidad puede acercarse a fragmentación dependiendo del volumen de contenido disponible en el catálogo.
- Recomendación: Monitorear crecimiento del catálogo en esta rama para validar que cada subgénero mantiene volumen musical suficiente para justificar su nivel estructural.
- Confianza: 0.52

### MVET-L2-005 [FB-05] - WARNING
- Nodo: Music > Rock > Classic Rock > Hard Rock
- Evidencia: Hard Rock está marcado como nodo Atomic. El estilo posee subdivisiones históricamente reconocidas (por ejemplo Glam Metal, Arena Rock o variantes regionales), lo que sugiere que su condición de atómico puede depender más de una decisión operativa del sistema que de un límite musical absoluto.
- Recomendación: Revisar periódicamente si la condición Atomic sigue siendo adecuada para el catálogo real del sistema.
- Confianza: 0.47

### MVET-L2-006 [FB-06] - WARNING
- Nodo: Music > Rock > Alternative & Indie > Post Punk > New Wave
- Evidencia: New Wave evolucionó históricamente desde el Post-Punk pero en muchos sistemas taxonómicos se clasifica como un movimiento pop-rock más amplio asociado a Synth Pop y al pop de los años 80. Su ubicación estricta bajo Post-Punk puede limitar su contexto estilístico completo.
- Recomendación: Evaluar si New Wave debe mantenerse como derivado directo de Post-Punk o si funcionaría mejor como nodo paralelo dentro de una estructura pop/rock de los 80.
- Confianza: 0.61
