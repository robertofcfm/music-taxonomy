Este archivo ha sido migrado. Las reglas de validación semántica de Capa 2 han sido cubiertas por las tareas desarrolladas y sus archivos correspondientes.

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
