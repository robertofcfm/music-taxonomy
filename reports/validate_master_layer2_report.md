# Reporte de Validación MVET (Capa 2 — Semántica IA)

- Fecha: 2026-03-16T03:19:14+00:00
- Decisión: FAIL
- FATAL: 1
- WARNING: 4
- SUGGESTION: 0

## Hallazgos

### MVET-L2-008 [FB-04] - FATAL
- Nodo: Music > Pop > Pop Rock > Latin Pop Rock
- Evidencia: El nodo 'Latin Pop Rock' se encuentra bajo la rama 'Pop', que es de dominio no-Latin, violando la separación obligatoria e inviolable entre géneros Latin y no-Latin.
- Recomendación: Reubicar 'Latin Pop Rock' o sus elementos bajo la rama raíz 'Latin' para mantener la integridad de dominios.
- Confianza: 1.00

### MVET-L2-001 [FB-05] - WARNING
- Nodo: Music > Rock > Alternative & Indie > Grunge > Seattle Grunge
- Evidencia: La distinción musical entre 'Seattle Grunge' y el nodo padre 'Grunge' (o su hermano 'Post-Grunge') a nivel de playlist es mínima; el Grunge es inherentemente de Seattle en su origen, generando contenido indistinguible.
- Recomendación: Fusionar 'Seattle Grunge' con el nodo padre 'Grunge' para evitar redundancia geográfica.
- Confianza: 0.90

### MVET-L2-001 [FB-05] - WARNING
- Nodo: Music > Rock > Classic Rock > Hard Rock > Hard Rock (General)
- Evidencia: El nodo 'Hard Rock (General)' es musicalmente indistinguible de su nodo padre 'Hard Rock'. Los nodos 'General' suelen ser redundantes si no hay subgéneros específicos que lo diferencien.
- Recomendación: Eliminar el nodo 'Hard Rock (General)' y utilizar el nodo padre para el contenido genérico.
- Confianza: 0.95

### MVET-L2-006 [FB-06] - WARNING
- Nodo: Music > Rock > Alternative & Indie > Post Punk > New Wave
- Evidencia: Aunque históricamente vinculados, la New Wave evolucionó hacia estructuras pop y sintéticas que encajarían mejor como un puente hacia 'Synth Pop' o en una categoría de mayor espectro debido a su limpieza sonora frente al Post Punk.
- Recomendación: Evaluar la reubicación de 'New Wave' o crear una relación transversal, dado que su cohesión con 'Gothic Rock' es baja.
- Confianza: 0.85

### MVET-L2-003 [FB-05] - WARNING
- Nodo: Music > Pop > Synth & Electronic Pop > Electronic Dream Pop
- Evidencia: Existe un solapamiento potencial con 'Music > Rock > Alternative & Indie > Dream Pop'. La distinción entre ambos suele ser la instrumentación (sintetizadores vs guitarras), pero en playlists modernas suelen mezclarse.
- Recomendación: Definir criterios atómicos estrictos para separar ambos o considerar una referencia cruzada.
- Confianza: 0.80
