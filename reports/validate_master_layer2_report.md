# Reporte de Validación MVET (Capa 2 — Semántica IA)

- Fecha: 2026-03-16T03:51:48+00:00
- Decisión: FAIL
- FATAL: 1
- WARNING: 4
- SUGGESTION: 0

## Hallazgos

### MVET-L2-008 [FB-04] - FATAL
- Nodo: Music > Pop > Pop Rock > Latin Pop Rock
- Evidencia: Se detectó un nodo de dominio 'Latin' (Latin Pop Rock) ubicado dentro de una rama de dominio 'no-Latin' (Pop Rock), violando la separación obligatoria e inviolable de dominios.
- Recomendación: Mover 'Latin Pop Rock' a una rama bajo el nodo raíz 'Latin' o crear un nodo clone en la ubicación actual que apunte a una ubicación canónica dentro del dominio 'Latin'.
- Confianza: 1.00

### MVET-L2-001 [FB-05] - WARNING
- Nodo: Music > Rock > Alternative & Indie > Indie Rock > Brit Pop
- Evidencia: El Brit Pop, aunque históricamente ligado al Indie Rock, presenta estructuras melódicas y de producción que a menudo lo acercan más al Pop Rock o Alternative Pop Rock, generando potencial indistinguibilidad en playlists de Indie Rock purista.
- Recomendación: Evaluar si Brit Pop debe ser un nodo hermano de Indie Rock en lugar de un hijo, para mantener la cohesión de la rama Indie.
- Confianza: 0.85

### MVET-L2-003 [FB-05] - WARNING
- Nodo: Music > Rock > Alternative & Indie > Post Punk > New Wave
- Evidencia: Existe un solapamiento significativo entre New Wave y Synth Pop (ubicado en la rama Pop). Muchos artistas de New Wave son indistinguibles de los de Synth Pop en una selección musical automatizada.
- Recomendación: Considerar el uso de nodos clone para conectar estas identidades o definir criterios de segmentación tímbrica más estrictos.
- Confianza: 0.90

### MVET-L2-005 [FB-05] - WARNING
- Nodo: Music > Latin > Regional Mexicano / Texano > Norteño > Norteño Clásico
- Evidencia: Nodos como Norteño Clásico y Norteño Moderno han alcanzado el límite de especificidad musical útil para la gestión de catálogos generales; subdividir más fragmentaría la audiencia sin beneficio sonoro claro.
- Recomendación: Marcar estos nodos como Atomic para evitar sobre-fragmentación futura.
- Confianza: 0.95

### MVET-L2-006 [FB-06] - WARNING
- Nodo: Music > Pop > Synth & Electronic Pop > Electronic Dream Pop
- Evidencia: Musicalmente, el Electronic Dream Pop comparte más texturas y estructuras con Dream Pop (ubicado en Rock > Alternative & Indie) que con el Synth Pop convencional.
- Recomendación: Evaluar la reubicación como hijo de Dream Pop o establecer una relación de proximidad mediante nodos clone.
- Confianza: 0.80
