# MVET LAYER 2 RULES

Fuente unica de reglas para la validacion semantica de Capa 2.

Formato:
- Cada regla debe ir en un bloque JSON entre las marcas:
  - <!-- MVET:LAYER2_RULE_START -->
  - <!-- MVET:LAYER2_RULE_END -->
- Campos obligatorios: rule_id, fb, severity, description, check
- severity valida: FATAL, WARNING, SUGGESTION

<!-- MVET:LAYER2_RULE_START -->
{
  "rule_id": "MVET-L2-001",
  "fb": "FB-05",
  "severity": "WARNING",
  "description": "Distincion musical entre generos hermanos.",
  "check": "Evalua si los generos que comparten el mismo padre son musicalmente distinguibles entre si. Si dos hermanos producirian playlists indistinguibles, deben reportarse."
}
<!-- MVET:LAYER2_RULE_END -->

<!-- MVET:LAYER2_RULE_START -->
{
  "rule_id": "MVET-L2-002",
  "fb": "FB-05",
  "severity": "WARNING",
  "description": "Riesgos de cohesion de playlists por estructura.",
  "check": "Identifica nodos donde la mezcla estilistica potencial del contenido del nodo podria producir playlists inconsistentes."
}
<!-- MVET:LAYER2_RULE_END -->

<!-- MVET:LAYER2_RULE_START -->
{
  "rule_id": "MVET-L2-003",
  "fb": "FB-05",
  "severity": "WARNING",
  "description": "Redundancia entre nodos.",
  "check": "Detecta parejas de generos que representan estilos potencialmente equivalentes o solapados en el conjunto del arbol, excluyendo nodos clone."
}
<!-- MVET:LAYER2_RULE_END -->

<!-- MVET:LAYER2_RULE_START -->
{
  "rule_id": "MVET-L2-004",
  "fb": "FB-05",
  "severity": "WARNING",
  "description": "Sobre-fragmentacion estructural.",
  "check": "Detecta subramas donde el numero de hijos es excesivo sin que exista valor musical claro para esa granularidad."
}
<!-- MVET:LAYER2_RULE_END -->

<!-- MVET:LAYER2_RULE_START -->
{
  "rule_id": "MVET-L2-005",
  "fb": "FB-05",
  "severity": "WARNING",
  "description": "Criterio atomico para limite de profundidad maxima.",
  "check": "Evalua nodos hoja donde subdividir mas seria forzado o deterioraria la coherencia musical. Estos nodos deben considerarse atomicos."
}
<!-- MVET:LAYER2_RULE_END -->

<!-- MVET:LAYER2_RULE_START -->
{
  "rule_id": "MVET-L2-006",
  "fb": "FB-06",
  "severity": "WARNING",
  "description": "Candidatos de reubicacion estructural.",
  "check": "Propone con evidencia musical nodos que encajarian mejor bajo un padre diferente al actual."
}
<!-- MVET:LAYER2_RULE_END -->

<!-- MVET:LAYER2_RULE_START -->
{
  "rule_id": "MVET-L2-007",
  "fb": "FB-06",
  "severity": "WARNING",
  "description": "Candidatos de fusion de nodos hermanos.",
  "check": "Identifica parejas de hermanos con solapamiento tan alto que la fusion mejoraria la coherencia del arbol."
}
<!-- MVET:LAYER2_RULE_END -->

<!-- MVET:LAYER2_RULE_START -->
{
  "rule_id": "MVET-L2-008",
  "fb": "FB-04",
  "severity": "FATAL",
  "description": "Violacion semantica de separacion Latin y no-Latin.",
  "check": "Detecta cualquier evidencia de mezcla de generos Latin y no-Latin que contrarie la separacion de dominio obligatoria, excluyendo nodos clone."
}
<!-- MVET:LAYER2_RULE_END -->

<!-- MVET:LAYER2_RULE_START -->
{
  "rule_id": "MVET-L2-009",
  "fb": "FB-05",
  "severity": "WARNING",
  "description": "Refactoring de marcadores Atomic inapropiados.",
  "check": "Detecta nodos marcados como (Atomic) que deberian ser descompostos. Esto ocurre cuando nuevos subgeneros musicales validos emergen y justifican subdividir un genero previamente considerado atomico. Recomienda quitar el marcador (Atomic) y crear subgeneros apropiados."
}
<!-- MVET:LAYER2_RULE_END -->

<!-- MVET:LAYER2_RULE_START -->
{
  "rule_id": "MVET-L2-010",
  "fb": "FB-06",
  "severity": "WARNING",
  "description": "Candidatos para agrupacion jerarquica de nodos.",
  "check": "Evalua cada nodo individualmente para determinar si su ubicacion actual es la mas coherente musicalmente. Si un nodo, por su naturaleza o contexto musical, justifica la existencia de un nodo padre intermedio (Agrupador Estructural), debe sugerirse su creacion aunque no existan hermanos. Esto permite mejorar la navegacion y coherencia taxonomica incluso en ramas con un solo hijo."
}
<!-- MVET:LAYER2_RULE_END -->
