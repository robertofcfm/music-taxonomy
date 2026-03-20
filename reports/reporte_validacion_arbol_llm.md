# Reporte de Validación de Árbol LLM

**Fecha:** 2026-03-20

## Errores

_No se detectaron errores fatales._

## Advertencias

- **ARBOL-LLM-001:** Los géneros hermanos bajo 'Rock' son musicalmente distinguibles, pero se recomienda revisar posibles solapamientos entre 'Art Rock' y 'Alternative Rock'.
  - Ambos géneros pueden compartir elementos experimentales, pero sus criterios de inclusión y exclusión están bien definidos.
- **ARBOL-LLM-003:** Posible redundancia entre 'Art Rock' y 'Alternative Rock'.
  - Ambos pueden incluir música experimental, pero los criterios de exclusión minimizan el solapamiento.

## Reglas validadas

- Separación Latin/no-Latin respetada.
- No se detectan nombres ambiguos ni excesivamente largos.
- No hay nodos hoja que requieran subdivisión adicional.
- No se detectan ramas excesivamente profundas ni superficiales.

## Archivos utilizados

- taxonomy/genre_tree_master.md
- context/contexto_validacion_arbol_llm.md
- governance/reglas_validacion_arbol_llm.md
- taxonomy/genre_tree_node_criteria.json
# Reporte de Validación de Árbol LLM

**Fecha:** 2026-03-20

## Errores

_No se detectaron errores fatales._

## Advertencias

- **ARBOL-LLM-001:** Los géneros hermanos bajo 'Rock' son musicalmente distinguibles, pero se recomienda revisar posibles solapamientos entre 'Art Rock' y 'Alternative Rock'.
  - Ambos géneros pueden compartir elementos experimentales, pero sus criterios de inclusión y exclusión están bien definidos.
- **ARBOL-LLM-003:** Posible redundancia entre 'Art Rock' y 'Alternative Rock'.
  - Ambos pueden incluir música experimental, pero los criterios de exclusión minimizan el solapamiento.

## Reglas validadas

- Separación Latin/no-Latin respetada.
- No se detectan nombres ambiguos ni excesivamente largos.
- No hay nodos hoja que requieran subdivisión adicional.
- No se detectan ramas excesivamente profundas ni superficiales.

## Archivos utilizados

- taxonomy/genre_tree_master.md
- context/contexto_validacion_arbol_llm.md
- governance/reglas_validacion_arbol_llm.md
- taxonomy/genre_tree_node_criteria.json
# Reporte de Validación LLM – Árbol de Géneros Musicales

**Fecha:** 2026-03-19T00:00:00

## Errores

- **ARBOL-LLM-007**: Se detectó mezcla indebida de géneros Latin y no-Latin.  
  _Detalle:_ 'Cumbia Pop' bajo rama Latin puede requerir revisión si su producción y estilo son predominantemente pop internacional y no latino.  
  _Severidad:_ FATAL

## Advertencias

- **ARBOL-LLM-001**: Géneros hermanos no son completamente distinguibles.  
  _Detalle:_ 'Soft Rock' y 'Art Rock' pueden solaparse en algunos contextos estilísticos.  
  _Severidad:_ WARNING

- **ARBOL-LLM-003**: Redundancia o solapamiento potencial.  
  _Detalle:_ 'Alternative Rock' y 'Grunge' pueden compartir repertorio y artistas, revisar criterios de exclusión.  
  _Severidad:_ WARNING

- **ARBOL-LLM-004**: Longitud de rama potencialmente insuficiente.  
  _Detalle:_ Rama 'Electronic' tiene solo un subgénero, considerar expansión.  
  _Severidad:_ WARNING

## Reglas validadas

- ARBOL-LLM-001 a ARBOL-LLM-011 (todas aplicadas según contexto y criterios).

## Archivos utilizados

- taxonomy/genre_tree_master.md
- taxonomy/genre_tree_node_criteria.json
- governance/reglas_validacion_arbol_llm.md
- context/contexto_validacion_arbol_llm.md

---
