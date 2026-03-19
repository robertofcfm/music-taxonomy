{{SYSTEM_CONTEXT}}
{{CLONE_CONTEXT}}
=== CONTEXTO NORMATIVO DINAMICO ===

{{GOVERNANCE_CONTEXT}}
=== REGLAS DE VALIDACION A APLICAR ===

{{RULES_BLOCK}}
=== CONTEXTO DE CRITERIOS POR NODO (SINCRONIZADO) ===

{{NODE_CRITERIA_CONTEXT}}
=== ARBOL TAXONOMICO A EVALUAR ===

{{TAXONOMY_TEXT}}
=== INSTRUCCION DE SALIDA ===

Responde UNICAMENTE con un JSON valido siguiendo el esquema a continuacion.
No incluyas texto fuera del JSON. No incluyas markdown ni bloques de codigo.

Esquema obligatorio:
{{OUTPUT_SCHEMA}}

Descarta explicitamente cualquier hallazgo con "result": "PASS".
No incluyas elementos con result PASS dentro del arreglo findings.
Si una regla no presenta hallazgos, no la incluyas en el arreglo findings.
Si no hay ningun hallazgo, devuelve findings como arreglo vacio [].