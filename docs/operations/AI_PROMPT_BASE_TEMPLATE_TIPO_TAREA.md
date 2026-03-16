# PLANTILLA HIJA PARA TIPO TAREA
Sistema de Taxonomía de Géneros Musicales

--------------------------------------------------
METADATOS DEL DOCUMENTO
--------------------------------------------------

Alcance:

Especializar la plantilla base para instancias cuyo
objetivo sea ejecutar o describir una tarea específica.

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
Tarea

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
Tarea

[DEFINIR_OBJETIVO]

Generar una instancia enfocada en resolver una tarea
específica del proyecto con reglas, contexto y criterios
de cierre alineados al trabajo operativo.

[DEFINIR_SALIDA_ESPERADA]

- tarea operativa concreta
- alcance delimitado
- entradas y salidas claras
- restricciones explícitas
- validación de cobertura reportada

[DEFINIR_CRITERIO_CIERRE]

La instancia generada debe dejar claro qué se considera
terminado para esa tarea y qué hallazgos deben reportarse.

--------------------------------------------------
4. ENFOQUE DE USO
--------------------------------------------------

Este template aplica cuando la conversación debe conducir
a una acción o entrega específica del proyecto.

No aplica cuando la salida principal buscada es solo la
redacción de un prompt final reusable.

--------------------------------------------------
FIN DEL DOCUMENTO