# PLANTILLA HIJA PARA TIPO PROMPT
Sistema de Taxonomía de Géneros Musicales

--------------------------------------------------
METADATOS DEL DOCUMENTO
--------------------------------------------------

Alcance:

Especializar la plantilla base para instancias cuyo
objetivo sea generar un prompt final pulido.

Propietario:

Propietario del proyecto

Última actualización:

2026-03-16

--------------------------------------------------
1. PROPÓSITO
--------------------------------------------------

Este documento es un TEMPLATE HIJO.

Debe usarse junto con:

docs/operations/AI_PROMPT_BASE_TEMPLATE.md

No define un flujo alterno.

Su función es completar definiciones específicas para
instancias donde:

[TIPO_TEMPLATE]
Prompt

--------------------------------------------------
2. CONTRATO CON EL PADRE
--------------------------------------------------

Este template hijo hereda el flujo del padre y solo puede
existir con un único padre.

Reglas:

- no redefine secciones estructurales del padre
- no agrega un segundo padre
- solo especializa definiciones dependientes de [TIPO_TEMPLATE]

--------------------------------------------------
3. DEFINICIONES ESPECIALIZADAS
--------------------------------------------------

[TIPO_TEMPLATE]
Prompt

[DEFINIR_OBJETIVO]

Generar un prompt final, pulido, coherente y listo para
ser usado en una conversación nueva o en un proceso de IA.

[DEFINIR_SALIDA_ESPERADA]

- prompt final listo para uso
- estructura clara
- imports resueltos
- restricciones explícitas
- validación de cobertura reportada

[DEFINIR_CRITERIO_CIERRE]

La instancia generada no debe conservar marcadores abstractos
y debe poder usarse directamente como prompt final.

--------------------------------------------------
4. ENFOQUE DE USO
--------------------------------------------------

Este template aplica cuando la tarea principal es redactar
o ensamblar un prompt final.

No aplica cuando la salida buscada es una tarea operativa
específica distinta del prompt mismo.

--------------------------------------------------
FIN DEL DOCUMENTO