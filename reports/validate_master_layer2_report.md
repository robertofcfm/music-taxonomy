# Reporte de Validación MVET (Capa 2 — Semántica IA)

- Fecha: 2026-03-17T06:24:15+00:00
- Decisión: PASS_WITH_WARNINGS
- FATAL: 0
- WARNING: 3
- SUGGESTION: 0

## Hallazgos

### MVET-L2-005 [FB-05] - WARNING
- Nodo: Multiple > Leaf Nodes
- Evidencia: 21 nodos hoja carecen del marcador (Atomic) a pesar de no tener hijos y representar géneros donde la subdivisión adicional sería forzada o deterioraría la coherencia de playlist. Nodos afectados: Indie Rock, Post Punk, Blues Rock, Heavy Metal, Thrash Metal, Nu Metal, Pop Rock, Disco, Deep House, Electro House, Dark Ambient, Cinematic Ambient, Rock Latino, Pop Latino, Hip Hop Latino, Norteño, Ranchero, Texano, Vallenato, Soul / Rhythm & Blues, Funk.
- Recomendación: Marcar estos nodos hoja con el sufijo (Atomic) para indicar explícitamente que representan géneros atómicos que no deben subdividirse más, alineado con la sección 10 de TAXONOMY_RULES.
- Confianza: 0.82

### MVET-L2-006 [FB-06] - WARNING
- Nodo: Rock > Dream Pop (Atomic)
- Evidencia: Dream Pop se caracteriza por sensibilidades indie fusionadas con atmósferas electrónicas oníricas. La literatura musical asocia Dream Pop primariamente con tradiciones Indie Pop o Synth Pop, no con Rock central. Su ubicación bajo Rock puede reducir la precisión de clasificación y navegación taxonómica.
- Recomendación: Evaluar la reubicación de Dream Pop a Pop > Synth Pop o considerar crear una rama Indie bajo Pop para reflejar con precisión la naturaleza musical del género.
- Confianza: 0.72

### MVET-L2-006 [FB-06] - WARNING
- Nodo: Rock > New Wave (Atomic)
- Evidencia: New Wave combina elementos rock y electrónicos pero está alieneado históricamente con tradiciones Electronic/Synth. El género emergió junto a synth-pop y experimentación electrónica. La ubicación actual bajo Rock diverge de patrones de taxonomía musical establecidos.
- Recomendación: Evaluar reubicación de New Wave a Electronic & Dance o a Pop > Synth Pop para reflejar mejor el carácter electrónico del género y mejorar la precisión de clasificación.
- Confianza: 0.75
