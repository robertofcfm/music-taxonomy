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
2. VIABILIDAD
--------------------------------------------------

La estrategia es VIABLE.

Pero debe entenderse correctamente:

- La IA no hace imports reales como un compilador.
- El "import" es una carga explícita de documentos.
- Esa carga puede ser manual, asistida por script o guiada
  por una plantilla operativa.

MODELO ABSTRACTO / CONCRETO

Este documento es la PLANTILLA ABSTRACTA.

Contiene la estructura base, principios y criterios
pero no tiene los valores de una tarea particular.

Su función es equivalente a una clase abstracta.

Puede contener contratos, campos obligatorios y bloques
marcados como pendientes de implementación.

Formato recomendado para contratos abstractos:

- [DEFINIR_TAREA]
- [DEFINIR_OBJETIVO]
- [TIPO_TEMPLATE]
- [DEFINIR_IMPORTS_MANDATORY]
- [DEFINIR_IMPORTS_CONDITIONAL]
- [DEFINIR_IMPORTS_REFERENTIAL]
- [DEFINIR_RESTRICCIONES]
- [DEFINIR_CRITERIO_CIERRE]

Mientras una plantilla conserve marcadores de este tipo,
debe considerarse ABSTRACTA.

MODELO DE HERENCIA SIMPLE

Este sistema debe usar un solo TEMPLATE PADRE por instancia.

Restricción:

- una instancia concreta puede heredar de un solo padre
- no se permite herencia múltiple por complejidad
- los templates hijos agregan definiciones, no redefinen
  el flujo estructural del padre

El padre define el flujo general y los contratos mínimos.

El hijo especializa definiciones usando el marcador:

[TIPO_TEMPLATE]

Valores iniciales soportados:

- Prompt
- Tarea

Por tanto:

- AI_PROMPT_BASE_TEMPLATE.md es el padre
- AI_PROMPT_BASE_TEMPLATE_TIPO_PROMPT.md es un hijo
- AI_PROMPT_BASE_TEMPLATE_TIPO_TAREA.md es un hijo

Para cada tipo de trabajo se genera una INSTANCIA CONCRETA:
un documento específico con los imports ya resueltos,
los archivos seleccionados y el objetivo definido.

La instancia concreta es equivalente a una clase que
implementa todos los contratos abstractos.

Una instancia concreta solo se considera LISTA PARA USO
FINAL si no conserva marcadores abstractos pendientes.

Si todavía contiene bloques como:

- [DEFINIR_*]
- [COLOCAR_AQUI_*]
- [PENDIENTE_*]

entonces sigue siendo una plantilla parcial o un borrador,
no un documento final de trabajo.

Para generar una instancia concreta:

Una IA lee esta plantilla abstracta y produce el documento
de prompt particular para la tarea indicada.

Ventaja principal:

Si un documento fuente del proyecto se actualiza,
solo hay que regenerar la instancia concreta a partir
de esta plantilla abstracta para que los cambios queden
aplicados sin editar el prompt a mano.

Conclusión práctica:

Sí conviene trabajar con este modelo siempre que exista
una selección disciplinada y no se inyecte todo el
repositorio en el prompt concreto generado.

--------------------------------------------------
3. PRINCIPIOS DE COMPOSICIÓN
--------------------------------------------------

P1 — NÚCLEO PEQUEÑO Y ESTABLE

Toda sesión debe cargar un conjunto mínimo de documentos
canónicos que evite respuestas erráticas.

P2 — CARGA SELECTIVA POR TAREA

Cada prompt debe sumar solo reglas y contexto que tengan
injerencia directa en el trabajo actual.

P3 — CONTEXTO NO ES REGLA

Los documentos contextuales ayudan a orientar decisiones,
pero no deben convertirse en fuente de obligaciones si no
son documentos normativos.

P4 — CONSISTENCIA NORMATIVA

No debe existir conflicto entre documentos normativos.

Si se detecta un conflicto durante la generación o uso
de una instancia, debe reportarse y corregirse en el
documento fuente antes de continuar.

Un sistema bien gobernado no resuelve conflictos por
precedencia en tiempo de ejecución; los elimina en el origen.

P5 — TAMAÑO CONTROLADO

Si el prompt crece demasiado, baja la calidad operativa.
Debe existir un presupuesto de contexto por sesión.

La instancia concreta debe incluir un campo de estado
de capacidad que la IA monitoree y reporte durante
la conversación.

Ver: sección 11 — PROTOCOLO DE CIERRE DE CONVERSACIÓN

--------------------------------------------------
4. MODELO DE DIVISIÓN RECOMENDADO
--------------------------------------------------

Se recomienda dividir reglas y contexto en cuatro capas.

CAPA A — CORE OBLIGATORIO

Se carga siempre.

- docs/governance/GLOBAL_RULES.md
- docs/governance/SYSTEM_CONTRACT.md
- docs/architecture/PROJECT_CONTEXT.md

Función:

- fijar límites del sistema
- fijar autoridad normativa
- fijar propósito del proyecto

CAPA B — MÓDULOS DE DOMINIO

Se cargan según el tipo de tarea.

Ejemplos:

- docs/governance/TAXONOMY_RULES.md
- docs/governance/TAXONOMY_DEPTH_POLICY.md
- docs/governance/TAXONOMY_NAMING_CONVENTION.md
- docs/governance/TAXONOMY_QUALITY_CHECKLIST.md
- docs/governance/TAXONOMY_CHANGE_POLICY.md

Función:

- agregar reglas especializadas
- restringir decisiones técnicas de un área concreta

CAPA C — MÓDULOS OPERATIVOS

Se cargan cuando la tarea pertenece a un proceso específico.

Ejemplos:

- docs/operations/PROJECT_BOOTSTRAP.md
- docs/operations/VALIDATE_MASTER_STRATEGY.md
- docs/operations/PHASE1_FINAL_CHECKLIST.md

Función:

- definir flujo de trabajo
- definir criterios de ejecución
- definir entregables y checks de proceso

CAPA D — ESTADO Y EVIDENCIA

Se cargan solo si son necesarios para continuidad.

Ejemplos:

- docs/project-management/PROJECT_STATE.md
- docs/project-management/PROJECT_MEMORY.md
- docs/project-management/PROJECT_CHECKPOINT_001.md
- reports/validate_master_report.md

Función:

- recuperar contexto reciente
- evitar perder decisiones previas
- aportar evidencia operativa puntual

NOTA: GRANULARIDAD Y SECCIONES DENTRO DE ARCHIVOS

Para evitar proliferación de archivos pequeños, un mismo
archivo puede dividirse en secciones delimitadas por
encabezado.

Formato de referencia:

[nombre_sección]
...contenido relevante para esa tarea...

[otra_sección]
...contenido relevante para otra tarea...

Al cargar ese archivo, se indica qué sección se activa
para la tarea actual. Solo esa parte entra al contexto.

Esto permite centralizar reglas relacionadas en un solo
archivo y cargar selectivamente sin crear un archivo
separado por cada variante de tarea.

Los archivos actuales en docs/governance/ deben evaluarse
para determinar si requieren subdivisión en secciones
o si la selección por capa ya es suficiente.

USO DE [TIPO_TEMPLATE] DENTRO DE DEFINICIONES

Un documento puede incluir definiciones que dependan del
valor de [TIPO_TEMPLATE] sin necesidad de crear múltiples
versiones del flujo base.

Ejemplo conceptual:

[TIPO_TEMPLATE]
Prompt

o

[TIPO_TEMPLATE]
Tarea

Con eso, un template hijo puede reutilizar el flujo del padre
y especializar solo las definiciones que cambian para ese tipo.

--------------------------------------------------
5. REGLA DE SELECCIÓN
--------------------------------------------------

Para cada prompt debe aplicarse esta matriz simple.

MANDATORY

Documentos sin los cuales la tarea quedaría mal gobernada.

CONDITIONAL

Documentos que aplican solo si el escenario los activa.

REFERENTIAL

Documentos que ayudan a entender pero no deben imponer reglas.

EXCLUDED

Documentos que no deben cargarse porque no afectan la tarea
o introducirían ruido.

Esta clasificación ya es consistente con el enfoque usado en:

docs/operations/VALIDATE_MASTER_STRATEGY.md

Por tanto, no se está introduciendo un modelo nuevo sino
formalizando uno ya presente en el proyecto.

--------------------------------------------------
6. CRITERIO DE USO POR ESCENARIO
--------------------------------------------------

ESCENARIO: EDICIÓN O REVISIÓN DE TAXONOMÍA

MANDATORY:

- docs/governance/GLOBAL_RULES.md
- docs/governance/SYSTEM_CONTRACT.md
- docs/governance/TAXONOMY_RULES.md
- docs/governance/TAXONOMY_NAMING_CONVENTION.md
- docs/governance/TAXONOMY_DEPTH_POLICY.md

CONDITIONAL:

- docs/governance/TAXONOMY_CHANGE_POLICY.md
- docs/governance/TAXONOMY_QUALITY_CHECKLIST.md

REFERENTIAL:

- docs/architecture/PROJECT_CONTEXT.md

ESCENARIO: VALIDACIÓN DEL ÁRBOL MAESTRO

MANDATORY:

- docs/governance/GLOBAL_RULES.md
- docs/governance/SYSTEM_CONTRACT.md
- docs/governance/TAXONOMY_RULES.md
- docs/governance/TAXONOMY_DEPTH_POLICY.md
- docs/governance/TAXONOMY_NAMING_CONVENTION.md
- docs/governance/TAXONOMY_QUALITY_CHECKLIST.md
- docs/operations/VALIDATE_MASTER_STRATEGY.md

CONDITIONAL:

- docs/governance/TAXONOMY_CHANGE_POLICY.md

REFERENTIAL:

- docs/architecture/PROJECT_CONTEXT.md
- docs/architecture/SYSTEM_OVERVIEW.md

ESCENARIO: CLASIFICACIÓN DE CANCIONES

MANDATORY:

- docs/governance/GLOBAL_RULES.md
- docs/governance/SYSTEM_CONTRACT.md
- docs/governance/TAXONOMY_RULES.md
- docs/architecture/PROJECT_CONTEXT.md

CONDITIONAL:

- docs/governance/TAXONOMY_CHANGE_POLICY.md
- docs/project-management/PROJECT_STATE.md

REFERENTIAL:

- docs/architecture/PROJECT_OPERATING_MODEL.md

--------------------------------------------------
7. PLANTILLA BASE
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

Si alguna condición falla, el documento sigue siendo ABSTRACTO
o PARCIAL y no debe tratarse como prompt final.

--------------------------------------------------
8. PLANTILLA MÍNIMA RECOMENDADA PARA ESTE PROYECTO
--------------------------------------------------

Si no hay tiempo para preparar un prompt grande, usar al menos:

MANDATORY

- docs/governance/GLOBAL_RULES.md
- docs/governance/SYSTEM_CONTRACT.md
- docs/architecture/PROJECT_CONTEXT.md

Y sumar solo un bloque especializado según la tarea principal.

Ejemplos:

- Validación de taxonomía: docs/operations/VALIDATE_MASTER_STRATEGY.md
- Trabajo estructural de taxonomía: docs/governance/TAXONOMY_RULES.md
- Arranque de sesión: docs/operations/PROJECT_BOOTSTRAP.md

--------------------------------------------------
9. DUDAS Y RIESGOS A CONTROLAR
--------------------------------------------------

D1 — FALSA SENSACIÓN DE IMPORT REAL

Si no existe un paso explícito de carga, la plantilla por sí sola
no garantiza que la IA realmente haya leído esos archivos.

D2 — EXCESO DE DOCUMENTOS MANDATORY

Si demasiados archivos entran al núcleo, el sistema vuelve a caer
en prompts largos y pierde el beneficio de modularizar.

D3 — DUPLICACIÓN DE REGLAS

Si una misma regla se repite en varios documentos sin precedencia
clara, aparecen contradicciones o sobrepeso contextual.

D4 — GRANULARIDAD INCORRECTA

Si los documentos son demasiado grandes, la selección sigue siendo
torpe. Si son demasiado pequeños, la carga operativa se vuelve frágil.

D5 — FALTA DE VERSIONADO DE CARGA

Conviene registrar qué documentos y versiones fueron cargados en una
sesión importante, especialmente en validación o clasificación.

--------------------------------------------------
10. OPINIÓN EXPERTA
--------------------------------------------------

La dirección es correcta.

No intentaría meter todo el conocimiento del proyecto en una sola
plantilla gigante. Eso termina degradando precisión, foco y obediencia.

Lo correcto es:

- un núcleo obligatorio pequeño
- módulos especializados por tarea
- consistencia normativa sin conflictos
- criterio formal de inclusión y exclusión

Con eso ya se obtiene una mejora fuerte sin necesidad de construir
todavía un sistema automatizado complejo.

Como siguiente nivel, más adelante sí tendría sentido crear un
manifiesto o ensamblador de prompts que arme automáticamente la
composición correcta según el tipo de tarea.

--------------------------------------------------
11. PROTOCOLO DE CIERRE DE CONVERSACIÓN
--------------------------------------------------

Una conversación activa puede terminar por límite de contexto,
decisión activa del usuario o completud de la tarea.

En todos los casos, el conocimiento generado no debe perderse.

INDICADOR DE ESTADO DE CAPACIDAD

El asistente debe reportar el estado de la conversación
al final de cada respuesta relevante con uno de estos
indicadores:

🟢 Chat manejable
🟡 Chat extenso, considera cerrar pronto
🔴 Chat crítico, cerrar antes de perder contexto

PROTOCOLO DE RESPALDO ANTES DE CERRAR

Cuando el indicador sea 🟡 o 🔴, ejecutar los siguientes
pasos antes de cerrar:

PASO 1 — RESUMEN DE DECISIONES

Solicitar al asistente el resumen de la sesión
usando el mensaje tipo definido abajo.

PASO 2 — ARCHIVOS MODIFICADOS

Confirmar que todos los archivos editados están guardados.

PASO 3 — ESTADO PENDIENTE

Identificar tareas incompletas y registrarlas en:

docs/project-management/PROJECT_STATE.md

PASO 4 — PUNTO DE REANUDACIÓN

El resumen generado en el PASO 1 se carga al iniciar
la siguiente sesión como contexto inicial junto con
la plantilla base mínima.

MENSAJE TIPO PARA SOLICITAR RESPALDO

Copiar y enviar al asistente cuando se quiera cerrar
la conversación de forma controlada:

---
Vamos a cerrar esta conversación.
Resume en formato copiable:

1. Decisiones tomadas en esta sesión.
2. Archivos modificados y cambios clave.
3. Tareas pendientes.
4. Punto de reanudación recomendado para la siguiente sesión.
---

--------------------------------------------------
FIN DEL DOCUMENTO