# Reporte de Validación MVET (Capa 2 — Semántica IA)

- Fecha: 2026-03-16T04:07:46+00:00
- Decisión: PASS_WITH_WARNINGS
- FATAL: 0
- WARNING: 5
- SUGGESTION: 0

## Hallazgos

### MVET-L2-001 [FB-05] - WARNING
- Nodo: Music > Pop > Synth & Electronic Pop > New Wave
- Evidencia: New Wave es un término paraguas que históricamente precede y engloba gran parte del Synth Pop, pero en esta estructura se presenta como un subgénero hijo de Synth & Electronic Pop, lo que genera confusión en la distinción de playlists.
- Recomendación: Evaluar si New Wave debe ser hermano de Synth & Electronic Pop o si debe contenerlo, dada su amplitud histórica y musical.
- Confianza: 0.85

### MVET-L2-003 [FB-05] - WARNING
- Nodo: Music > Rock > Classic Rock
- Evidencia: Classic Rock no es un género musical per se, sino un formato radial. Existe un solapamiento masivo con Rock & Roll, Blues Rock y Hard Rock que ya cuelgan del mismo nivel.
- Recomendación: Considerar a Classic Rock como un nodo organizador o etiqueta, ya que su contenido musical es redundante con los nodos hermanos específicos.
- Confianza: 0.90

### MVET-L2-006 [FB-06] - WARNING
- Nodo: Music > Electronic & Dance > Disco
- Evidencia: Musicalmente, el Disco es el precursor directo del House. Aunque se clasifica como Electronic & Dance, su estructura rítmica y origen lo vinculan estrechamente con Soul / Funk / R&B.
- Recomendación: Evaluar la creación de un nodo clone en Soul / Funk / R&B o reubicar si la intención es priorizar el origen estilístico sobre el entorno de consumo (Dance).
- Confianza: 0.80

### MVET-L2-007 [FB-06] - WARNING
- Nodo: Music > Latin > Regional Mexicano / Texano > Texano
- Evidencia: Alta redundancia entre Texano y Norteño en el contexto actual de la industria, donde la distinción sonora es mínima para la generación de playlists automatizadas.
- Recomendación: Fusionar en un nodo 'Norteño & Texano' o clarificar fronteras si se mantiene la separación.
- Confianza: 0.75

### MVET-L2-005 [FB-05] - WARNING
- Nodo: Music > Rock > Alternative & Indie > Grunge
- Evidencia: Nodo identificado como hoja (atomic). Subdividir Grunge (ej. Seattle Sound vs Post-Grunge) suele diluir la identidad del género original sin beneficio taxonómico claro.
- Recomendación: Marcar formalmente como nodo Atomic.
- Confianza: 0.95
