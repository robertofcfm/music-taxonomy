# Reporte de Validación MVET (Capa 2 — Semántica IA)

- Fecha: 2026-03-16T06:24:21+00:00
- Decisión: PASS_WITH_WARNINGS
- FATAL: 0
- WARNING: 5
- SUGGESTION: 0

## Hallazgos

### MVET-L2-001 [FB-05] - WARNING
- Nodo: Music > Rock > Alternative & Indie > Post Punk
- Evidencia: Los géneros hermanos Gothic Rock, Coldwave y Darkwave comparten raíces directas en el movimiento post-punk y presentan instrumentación, estética y tempo muy similares. En muchos catálogos musicales y playlists editoriales, las canciones de estos tres estilos suelen mezclarse sin una separación clara.
- Recomendación: Revisar si los criterios de diferenciación musical entre Gothic Rock, Coldwave y Darkwave están suficientemente definidos para justificar tres nodos hermanos independientes. Si no existen criterios curatoriales claros, considerar consolidación conceptual o documentación adicional que justifique la separación.
- Confianza: 0.82

### MVET-L2-002 [FB-05] - WARNING
- Nodo: Music > Latin > Regional Mexicano / Texano
- Evidencia: El nodo agrupa estilos con diferencias musicales marcadas: Norteño, Texano, Banda y Ranchero presentan instrumentación, tradición interpretativa y estructuras rítmicas distintas. La mezcla indiscriminada dentro del nodo padre podría generar playlists estilísticamente inconsistentes.
- Recomendación: Mantener el nodo como agrupador estructural si su propósito es navegación regional, pero considerar documentar explícitamente que funciona como agrupador estructural y no como género reproducible para playlists.
- Confianza: 0.87

### MVET-L2-003 [FB-05] - WARNING
- Nodo: Music > Pop > Synth & Electronic Pop
- Evidencia: Synth Pop y Electro Pop pueden solaparse significativamente en producción musical, instrumentación electrónica y estética sonora. En muchos catálogos contemporáneos ambos términos se utilizan de manera intercambiable.
- Recomendación: Verificar que existan criterios curatoriales claros para diferenciar Synth Pop y Electro Pop dentro del árbol. Si la distinción se basa en época, estética o producción específica, debería documentarse para evitar redundancia taxonómica.
- Confianza: 0.76

### MVET-L2-006 [FB-06] - WARNING
- Nodo: Music > Rock > Alternative & Indie > New Wave
- Evidencia: New Wave históricamente deriva del movimiento post-punk y comparte rasgos estilísticos con ese ecosistema musical. Su ubicación directa bajo Alternative & Indie puede ocultar su relación estructural con Post Punk.
- Recomendación: Evaluar si New Wave funcionaría mejor como nodo hermano o subnodo dentro del dominio conceptual de Post Punk, o si su posición actual responde a una decisión editorial deliberada basada en uso contemporáneo.
- Confianza: 0.63

### MVET-L2-005 [FB-05] - WARNING
- Nodo: Music > Rock > Classic Rock > Hard Rock
- Evidencia: Hard Rock se marca como nodo Atomic. El género es ampliamente reconocido como estilo consolidado y subdividirlo adicionalmente dentro de esta rama podría introducir fragmentación innecesaria sin beneficio musical claro en esta taxonomía.
- Recomendación: Mantener Hard Rock como nodo atómico dentro de esta estructura salvo que se introduzcan subgéneros con criterios curatoriales sólidos.
- Confianza: 0.80
