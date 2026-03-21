# Reglas de Validación de Árbol (LLM)

Aquí se colocarán únicamente las reglas que requieren interpretación o razonamiento de un modelo de lenguaje (LLM).


## Principios y estructura taxonómica obligatoria
- La estructura del árbol debe seguir: Music (raíz) > Macroárea (Global, Latin) > Género > Subgénero > Estilo/Microgénero/Escena/Fusión.
- La separación entre macroáreas "Global" y "Latin" es inviolable en el segundo nivel.
- Los géneros faltantes deben reportarse con la máxima especificidad posible, evitando categorías genéricas (ej. no usar solo "Pop", "Ballad", "Rock").
- Toda sugerencia de género faltante debe incluir justificación y criterios claros, alineados con el contexto operativo y los criterios de nodos.
- No se permite inventar géneros fuera de la lógica taxonómica y los criterios definidos.

(Agregar reglas conforme se identifiquen en la migración)

## Reglas semánticas y estructurales que requieren LLM para validación de árbol
- id: ARBOL-LLM-001
  descripcion: "¿Los géneros hermanos son musicalmente distinguibles?"
  severidad: WARNING
  prompt: "Evalúa si los géneros que comparten el mismo padre son musicalmente distinguibles entre sí. Si dos hermanos producirían playlists indistinguibles, deben reportarse."
- id: ARBOL-LLM-002
  descripcion: "¿Existen riesgos de cohesión de playlists por estructura?"
  severidad: WARNING
  prompt: "Identifica nodos donde la mezcla estilística potencial del contenido del nodo podría producir playlists inconsistentes."
- id: ARBOL-LLM-003
  descripcion: "¿Hay redundancia o solapamiento entre nodos?"
  severidad: WARNING
  prompt: "Detecta parejas de géneros que representan estilos potencialmente equivalentes o solapados en el conjunto del árbol, excluyendo nodos clone."
- id: ARBOL-LLM-004
  descripcion: "¿La longitud de la rama es adecuada?"
  severidad: WARNING
  prompt: "Evalúa si los nodos hijos de cada rama son lo suficientemente detallados para que las canciones clasificadas no desentonen entre sí (no sean disonantes). Advierte si la rama es demasiado corta (falta de detalle) o si la división de nodos es forzada (excesiva granularidad sin justificación musical)."
- id: ARBOL-LLM-005
  descripcion: "¿Existen nodos hoja que deberían considerarse atómicos?"
  severidad: WARNING
  prompt: "Evalúa nodos hoja donde subdividir más sería forzado o deterioraría la coherencia musical. Estos nodos deben considerarse atómicos."
- id: ARBOL-LLM-006
  descripcion: "¿Hay candidatos de reubicación, fusión o agrupación jerárquica?"
  severidad: WARNING
  prompt: "Propón nodos que encajarían mejor bajo otro padre, que deberían fusionarse o que justificarían la creación de un nodo agrupador intermedio."
- id: ARBOL-LLM-007
  descripcion: "¿Se respeta la separación Latin/no-Latin?"
  severidad: FATAL
  prompt: "Detecta cualquier mezcla de géneros Latin y no-Latin que contraríe la separación de dominio obligatoria, excluyendo nodos clone."
- id: ARBOL-LLM-008
  descripcion: "¿Existen redundancias o alias históricos entre géneros?"
  severidad: WARNING
  prompt: "Detecta si dos géneros representan el mismo estilo, ya sea por alias, solapamiento o inconsistencias históricas de nombrado. Sugiere fusiones si corresponde."
- id: ARBOL-LLM-009
  descripcion: "¿Nodos grandes requieren expansión? (umbral de referencia: 45 canciones)"
  severidad: WARNING
  prompt: "Identifica nodos con un gran número de canciones o playlists demasiado diversas. Sugiere subdivisión si existen subgéneros reconocibles."
- id: ARBOL-LLM-010
  descripcion: "¿El balance de profundidad de la taxonomía es adecuado?"
  severidad: WARNING
  prompt: "Evalúa si existen ramas excesivamente profundas, superficiales o con crecimiento jerárquico desigual."
- id: ARBOL-LLM-011
  descripcion: "¿Algún género debería reubicarse bajo otro padre?"
  severidad: WARNING
  prompt: "Detecta géneros que pertenecerían de forma más natural a otra rama y sugiere reubicación."
- id: ARBOL-LLM-012
  descripcion: "¿Existen casos de sobre-fragmentación?"
  severidad: WARNING
  prompt: "Detecta ramas subdivididas en exceso: géneros hermanos demasiado pequeños, difíciles de distinguir o con especialización excesiva. Sugiere simplificación."
- id: ARBOL-LLM-013
  descripcion: "¿Existen nombres de género ambiguos, vagos o no musicales?"
  severidad: FATAL
  prompt: "Detecta nombres que sean descripciones estilísticas vagas, etiquetas de marketing o descriptores no musicales. Sugiere reemplazo por nombres válidos."
- id: ARBOL-LLM-014
  descripcion: "¿Algún nombre de género es excesivamente largo o combina múltiples descriptores innecesarios?"
  severidad: WARNING
  prompt: "Detecta nombres innecesariamente largos o compuestos. Sugiere nombres de género claramente establecidos y concisos."
