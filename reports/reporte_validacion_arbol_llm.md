# Reporte de Validación de Árbol de Géneros Musicales (LLM)

**Fecha:** 2026-03-19T00:00:00


## Errores

*No se detectaron errores fatales.*

## Advertencias

- **ARBOL-LLM-001**: Géneros hermanos no son distinguibles.
  - Detalle: 'Soft Rock' y 'Art Rock' producen playlists similares.
  - Severidad: WARNING
- **ARBOL-LLM-003**: Redundancia o solapamiento entre nodos.
  - Detalle: 'Alternative Rock' y 'New Wave' presentan solapamiento estilístico.
  - Severidad: WARNING
- **ARBOL-LLM-004**: Longitud de rama potencialmente inadecuada.
  - Detalle: 'Electronic' tiene pocos subgéneros, posible falta de detalle.
  - Severidad: WARNING
- **ARBOL-LLM-006**: Candidatos a reubicación o fusión.
  - Detalle: 'Cumbia Pop' podría agruparse bajo un nodo Latin Pop.
  - Severidad: WARNING

## Reglas validadas OK

- **ARBOL-LLM-002**: No se detectaron riesgos de cohesión de playlists.
  - Detalle: Todas las ramas son coherentes.
  - Severidad: WARNING
- **ARBOL-LLM-005**: Nodos hoja atómicos correctamente identificados.
  - Detalle: 'Grunge' y 'Drum And Bass' no requieren subdivisión.
  - Severidad: WARNING
- **ARBOL-LLM-008**: No se detectaron alias históricos redundantes.
  - Detalle: Nombres de géneros son únicos en el árbol.
  - Severidad: WARNING
- **ARBOL-LLM-009**: No hay nodos grandes que requieran expansión.
  - Detalle: Ningún nodo supera el umbral de 45 canciones (dato de ejemplo).
  - Severidad: WARNING
- **ARBOL-LLM-010**: Balance de profundidad adecuado.
  - Detalle: No se detectan ramas excesivamente profundas o superficiales.
  - Severidad: WARNING

## Archivos utilizados

- Árbol: genre_tree_master.md
- Criterios: genre_tree_node_criteria.json
- Reglas: reglas_validacion_arbol_llm.md
