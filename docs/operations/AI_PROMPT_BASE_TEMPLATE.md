# PLANTILLA BASE DE PROMPT PARA IA
Sistema de Taxonomía de Géneros Musicales

--------------------------------------------------
METADATOS DEL DOCUMENTO
--------------------------------------------------

Alcance:

Definir una plantilla base reusable para trabajo con IA
usando carga selectiva de reglas y contexto del proyecto.

Propietario:

Propietario del proyecto

Última actualización:

2026-03-16

--------------------------------------------------
1. PROPÓSITO
--------------------------------------------------

Este documento define una plantilla base para construir
prompts de trabajo usando archivos del proyecto como
fuente de reglas y contexto.

La idea es evitar prompts monolíticos con demasiada carga
en duro y sustituirlos por una composición controlada
de documentos relevantes para la tarea actual.

--------------------------------------------------
IMPORTS
--------------------------------------------------

CONTEXT

- docs/governance/AI_PROMPT_SYSTEM_CONTEXT.md

RULES

- docs/governance/AI_PROMPT_SYSTEM_RULES.md

--------------------------------------------------
2. DEFINICIÓN DE LA PLANTILLA
--------------------------------------------------

Usar la siguiente estructura al iniciar una sesión o al
construir un prompt operativo.

ESQUELETO MÍNIMO DE INSTANCIA

'''
[DEFINIR_TAREA]
'''

[AQUI_SIGUE_CON_EL_CONTENIDO]

[TIPO_TEMPLATE]
[DEFINIR_TIPO_TEMPLATE]

Este bloque sirve como encabezado mínimo para una instancia
concreta y obliga a declarar primero la tarea antes de cargar
reglas, contexto y restricciones.

Convención:

- Si el bloque conserva [DEFINIR_TAREA], la pieza sigue siendo abstracta.
- Si conserva [DEFINIR_TIPO_TEMPLATE], la pieza sigue siendo abstracta.
- Si el bloque ya contiene una tarea real, puede continuar a validación.
- Una instancia no debe ejecutarse como prompt final si conserva
  cualquier marcador abstracto pendiente.

TÍTULO DE LA TAREA

[describir en una línea qué se quiere hacer]

OBJETIVO OPERATIVO

[definir el resultado esperado]

IMPORTS — MANDATORY

- [archivo obligatorio 1]
- [archivo obligatorio 2]
- [archivo obligatorio 3]

IMPORTS — CONDITIONAL

- [archivo condicional 1]
- [archivo condicional 2]

IMPORTS — REFERENTIAL

- [archivo referencial 1]

IMPORTS — EXCLUDED

- [archivo excluido 1]

REGLAS DE INTERPRETACIÓN

- Tratar MANDATORY como ley operativa.
- Cargar CONDITIONAL solo si el escenario aplica.
- Usar REFERENTIAL como contexto, no como fuente primaria de reglas.
- Ignorar EXCLUDED para reducir ruido y tamaño del prompt.
- Si se detecta conflicto normativo, reportarlo y no continuar hasta resolverlo.

VALIDACIÓN DE COBERTURA

Antes de usar esta instancia, verificar y reportar:

- ¿Algún documento normativo relevante fue clasificado
  como EXCLUDED o quedó sin clasificar por error?
- ¿Las reglas que aplican al escenario están cubiertas
  por los documentos MANDATORY seleccionados?
- ¿Los documentos CONDITIONAL fueron evaluados contra
  el escenario activo?

Si alguna respuesta es positiva, reportarlo y actualizar
la selección antes de iniciar el trabajo.

Este paso es obligatorio al generar cada instancia concreta.

ESTADO DE CONTEXTO

[indicador actual: 🟢 / 🟡 / 🔴]

ENTRADAS DE TRABAJO

- [archivo principal de entrada]
- [archivos secundarios]

SALIDA ESPERADA

- [tipo de salida]
- [formato]
- [criterio de calidad]

RESTRICCIONES

- No inventar reglas no documentadas.
- No modificar taxonomía automáticamente.
- Reportar ambigüedades o conflictos normativos.

CRITERIO DE CIERRE

- [qué debe cumplirse para considerar terminada la tarea]

VALIDACIÓN DE CONCRECIÓN

Antes de considerar lista una instancia concreta, verificar:

- no contiene marcadores [DEFINIR_*]
- no contiene marcadores [COLOCAR_AQUI_*]
- no contiene marcadores [PENDIENTE_*]
- [TIPO_TEMPLATE] fue resuelto con un valor válido
- todos los imports requeridos fueron resueltos
- la validación de cobertura fue ejecutada y reportada
- todos los contratos heredados de niveles superiores fueron resueltos
- la cadena completa de herencia fue recorrida hasta el padre raíz

Si alguna condición falla, el documento sigue siendo ABSTRACTO
o PARCIAL y no debe tratarse como prompt final.

PROTOCOLO DE RESOLUCIÓN DE HERENCIA

Para cada instancia o template derivado, aplicar este orden:

1. Identificar el padre directo.
2. Recorrer la cadena de padres hasta el template raíz.
3. Reunir todos los marcadores abstractos heredados.
4. Resolverlos desde el nivel más alto hacia el más específico.
5. Verificar que el documento final no conserve contratos pendientes.

Si la cadena de herencia no puede reconstruirse con claridad,
el documento no debe considerarse final.

--------------------------------------------------
FIN DEL DOCUMENTO