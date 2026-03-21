# Contexto para Validación de Árbol (LLM)

Contexto mínimo necesario para validaciones que requieren LLM.

## Principios obligatorios
- No proponer cambios automáticos al archivo maestro.
- No inventar reglas fuera del corpus de gobernanza proporcionado.
- No ocultar incertidumbre: reflejar confianza real en el campo confidence.
	- Los géneros faltantes deben reportarse con la máxima especificidad posible, evitando categorías genéricas (ej. no usar solo "Pop", "Ballad", "Rock").
	- Toda sugerencia de género faltante debe incluir justificación y criterios claros, alineados con la estructura taxonómica y los criterios de nodos.
## Estructura taxonómica recomendada
Nivel 1: Music (raíz)
Nivel 2: Género principal
Nivel 3: Género (ej. Rock, Pop, Cumbia, etc.)
Nivel 4: Subgénero (ej. Alternative Rock, Cumbia Pop, etc.)
Nivel 5: Estilo / Microgénero / Escena / Fusión (ej. Dream Pop Latino, Power Ballad Anglo, Madchester, Electro Cumbia, etc.)

El nivel 5 es flexible y puede usarse para estilos, microgéneros, escenas o fusiones, según la riqueza y diversidad de la colección. No todas las ramas requieren llegar siempre a este nivel.
- El árbol es controlado manualmente por el propietario del proyecto. El sistema solo puede sugerir; nunca modificar.

## Glosario operativo mínimo para Capa 2
- **Nodo clone**: Nodo portal que referencia un nodo canónico. No tiene hijos ni contiene canciones. Existe para navegación y soporte de clasificación.
- **Nodo General**: Nodo de respaldo para contenido válido del dominio del padre que no encaja en subgéneros más específicos.
- **Nodo Atómico**: Nodo hoja que no debe subdividirse más sin perder coherencia musical.
- **Nodo Agrupador Estructural**: Nodo padre usado principalmente para organización estructural y navegación taxonómica. No debe asumirse por defecto como género reproducible principal. Cuando existan hijos musicalmente distinguibles, la evaluación debe priorizar esos hijos por encima del padre.

Identificación operativa para esta validación:
- Si un nodo está marcado explícitamente como clone, trátalo como clone.
- Si el nombre del nodo contiene la palabra "clone", trátalo como clone.
- Si el nombre del nodo contiene el marcador "->", trátalo como clone.

Instrucción de evaluación:
- Cuando una regla indique excluir nodos clone, exclúyelos completamente del análisis.

## Alcance de aplicación para Capa 2
Aplica únicamente reglas semánticas y estructurales de taxonomía para validar coherencia musical del árbol. Ignora reglas operativas fuera de alcance de esta capa (por ejemplo: modos de ejecución, batching, logging, continuidad de lotes, o detalles de pipeline de clasificación de canciones).

Precedencia obligatoria:
- Si hay conflicto interpretativo, prioriza SYSTEM_CONTRACT y GLOBAL_RULES.
- No inventar reglas fuera del corpus de governance cargado abajo.

## Contexto adicional para validaciones LLM
- La redundancia puede surgir por alias, solapamiento o inconsistencias históricas de nombrado.
- Nodos con muchas canciones o playlists diversas pueden requerir subdivisión si existen subgéneros reconocibles (umbral sugerido: 45 canciones).
- Un nodo atómico no debe subdividirse si representa un estilo muy específico y la cohesión de playlists se vería afectada.
- El balance de profundidad busca evitar ramas excesivamente profundas o superficiales y crecimiento jerárquico desigual.
Los géneros deben estar bajo el nodo padre más apropiado según afinidad musical.
- La sobre-fragmentación ocurre cuando hay hermanos pequeños, difícil de distinguir o especialización excesiva.
- Nombres ambiguos, vagos, de marketing o no musicales deben evitarse; priorizar nombres musicales reconocidos.
- Los nombres de género deben ser concisos y no combinar múltiples descriptores innecesarios.

(Agregar detalles conforme se identifiquen en la migración)
