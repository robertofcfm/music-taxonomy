# Reporte de Validación MVET (Capa 2 — Semántica IA)

- Fecha: 2026-03-16T06:39:51+00:00
- Decisión: PASS_WITH_WARNINGS
- FATAL: 0
- WARNING: 5
- SUGGESTION: 0

## Hallazgos

### MVET-L2-001 [FB-05] - WARNING
- Nodo: Music > Rock > Alternative & Indie > Post-Punk Era
- Evidencia: The sibling nodes 'New Wave' and 'Post Punk' share significant historical and sonic overlap (late-70s/early-80s post-punk lineage, similar instrumentation and production aesthetics). Many artists and playlists frequently cross-classify between both, potentially producing partially indistinguishable playlists.
- Recomendación: Maintain separation but ensure classification guidelines clearly distinguish melodic pop-leaning New Wave from darker or more experimental Post Punk to preserve playlist cohesion.
- Confianza: 0.78

### MVET-L2-002 [FB-05] - WARNING
- Nodo: Music > Rock > Alternative & Indie
- Evidencia: The parent node contains stylistically diverse children (Indie Rock, Grunge, Dream Pop, Post-Punk derived styles). If content is assigned directly to the parent node rather than its children, resulting playlists could mix very different aesthetics (lo-fi indie rock, heavy grunge, atmospheric dream pop, post-punk derivatives).
- Recomendación: Encourage classification into the specific subgenres rather than the parent node to avoid stylistically inconsistent playlists at this level.
- Confianza: 0.83

### MVET-L2-003 [FB-05] - WARNING
- Nodo: Music > Latin > Regional Colombiano > Cumbia Colombiana
- Evidencia: The subgenres 'Cumbia Clásica' and 'Cumbia Moderna' may overlap significantly depending on interpretation. Many modern recordings reproduce traditional arrangements, and playlist differentiation between these two nodes may become ambiguous without strict temporal or stylistic criteria.
- Recomendación: Clarify classification criteria (e.g., instrumentation modernization, production era, fusion elements) to ensure playlists under each node remain musically distinguishable.
- Confianza: 0.74

### MVET-L2-006 [FB-06] - WARNING
- Nodo: Music > Rock > Alternative & Indie > Dream Pop
- Evidencia: Dream Pop historically derives from both alternative rock and post-punk/shoegaze traditions and is often categorized closer to the shoegaze/dream-pop continuum rather than the broader indie rock grouping. Its atmospheric and ethereal sound profile differs significantly from most Indie Rock and Grunge siblings.
- Recomendación: Evaluate whether Dream Pop would fit better under a more specific atmospheric/post-punk derived branch (e.g., near shoegaze/post-punk related nodes) rather than within the broader Alternative & Indie grouping.
- Confianza: 0.63

### MVET-L2-005 [FB-05] - WARNING
- Nodo: Music > Rock > Alternative & Indie > Grunge > Seattle Grunge
- Evidencia: Seattle Grunge represents a historically and geographically specific scene tied to the early 1990s Seattle movement. Further subdivision would likely fragment the style without producing musically coherent subgenres.
- Recomendación: Treat this node as an atomic genre boundary unless future taxonomy introduces historically justified micro-scenes.
- Confianza: 0.86
