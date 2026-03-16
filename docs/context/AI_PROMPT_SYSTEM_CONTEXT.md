# CONTEXTO DEL SISTEMA DE PLANTILLAS DE PROMPT
Sistema de Taxonomía de Géneros Musicales

--------------------------------------------------
METADATOS DEL DOCUMENTO
--------------------------------------------------

Alcance:

Contexto del sistema de plantillas de prompt para IA.
Explica el modelo abstracto/concreto, la herencia,
la división en capas y los criterios por escenario.

Propietario:

Propietario del proyecto

Última actualización:

2026-03-16

--------------------------------------------------
1. VIABILIDAD DEL MODELO
--------------------------------------------------

La estrategia de usar plantillas con carga selectiva es VIABLE.

Pero debe entenderse correctamente:

- La IA no hace imports reales como un compilador.
- El "import" es una carga explícita de documentos.
- Esa carga puede ser manual, asistida por script o guiada
  por una plantilla operativa.

--------------------------------------------------
2. MODELO ABSTRACTO / CONCRETO
--------------------------------------------------

La plantilla base es un documento ABSTRACTO.

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

Una IA lee la plantilla abstracta y produce el documento
de prompt particular para la tarea indicada.

Ventaja principal:

Si un documento fuente del proyecto se actualiza,
solo hay que regenerar la instancia concreta a partir
de la plantilla abstracta para que los cambios queden
aplicados sin editar el prompt a mano.

--------------------------------------------------
3. MODELO DE HERENCIA
--------------------------------------------------

El sistema usa un solo TEMPLATE PADRE por instancia.

Restricción:

- una instancia concreta puede heredar de un solo padre
- no se permite herencia múltiple por complejidad
- los templates hijos agregan definiciones, no redefinen
  el flujo estructural del padre

La herencia puede tener múltiples niveles.

Ejemplo válido:

- nivel 1: template padre base
- nivel 2: template hijo por tipo
- nivel 3: template hijo especializado por proceso
- nivel 4: instancia concreta final

La restricción es linealidad, no profundidad.

Por tanto, sí se permiten templates de 3er o 4to nivel,
siempre que cada nodo tenga un solo padre directo.

El padre define el flujo general y los contratos mínimos.

El hijo especializa definiciones usando el marcador:

[TIPO_TEMPLATE]

Valores iniciales soportados:

- Prompt
- Tarea

Ejemplo de niveles posteriores permitidos:

- un template de validación puede heredar de TIPO_TAREA
- un template de validación del árbol maestro puede heredar
  del template de validación

RESOLUCIÓN ASCENDENTE OBLIGATORIA

La concreción no se valida solo contra el último padre directo.

Debe resolverse toda la cadena de abstracción hacia arriba
hasta el ancestro raíz.

Esto implica:

- resolver los contratos del template actual
- resolver los contratos heredados del padre directo
- resolver los contratos heredados de abuelos y niveles superiores
- confirmar que ningún marcador abstracto permanezca en ningún nivel

Si un template de nivel 3 implementa su propio contenido pero deja
sin resolver un contrato heredado desde nivel 1, entonces sigue
siendo ABSTRACTO.

USO DE [TIPO_TEMPLATE] DENTRO DE DEFINICIONES

Un documento puede incluir definiciones que dependan del
valor de [TIPO_TEMPLATE] sin necesidad de crear múltiples
versiones del flujo base.

Ejemplo:

[TIPO_TEMPLATE]
Prompt

o

[TIPO_TEMPLATE]
Tarea

Con eso, un template hijo puede reutilizar el flujo del padre
y especializar solo las definiciones que cambian para ese tipo.

--------------------------------------------------
4. MODELO DE DIVISIÓN EN CAPAS
--------------------------------------------------

Se recomienda dividir reglas y contexto en cuatro capas.

CAPA A — CORE OBLIGATORIO

Se carga siempre.

- docs/governance/GLOBAL_RULES.md
- docs/governance/SYSTEM_CONTRACT.md
- docs/context/PROJECT_CONTEXT.md

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

--------------------------------------------------
5. CRITERIO DE USO POR ESCENARIO
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

- docs/context/PROJECT_CONTEXT.md

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

- docs/context/PROJECT_CONTEXT.md
- docs/context/SYSTEM_OVERVIEW.md

ESCENARIO: CLASIFICACIÓN DE CANCIONES

MANDATORY:

- docs/governance/GLOBAL_RULES.md
- docs/governance/SYSTEM_CONTRACT.md
- docs/governance/TAXONOMY_RULES.md
- docs/context/PROJECT_CONTEXT.md

CONDITIONAL:

- docs/governance/TAXONOMY_CHANGE_POLICY.md
- docs/project-management/PROJECT_STATE.md

REFERENTIAL:

- docs/context/PROJECT_OPERATING_MODEL.md

--------------------------------------------------
6. PLANTILLA MÍNIMA RECOMENDADA
--------------------------------------------------

Si no hay tiempo para preparar un prompt completo,
usar al menos:

MANDATORY

- docs/governance/GLOBAL_RULES.md
- docs/governance/SYSTEM_CONTRACT.md
- docs/context/PROJECT_CONTEXT.md

Y sumar solo un bloque especializado según la tarea principal.

Ejemplos:

- Validación de taxonomía: docs/operations/VALIDATE_MASTER_STRATEGY.md
- Trabajo estructural de taxonomía: docs/governance/TAXONOMY_RULES.md
- Arranque de sesión: docs/operations/PROJECT_BOOTSTRAP.md

--------------------------------------------------
7. DUDAS Y RIESGOS A CONTROLAR
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
8. OPINIÓN EXPERTA
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
FIN DEL DOCUMENTO
