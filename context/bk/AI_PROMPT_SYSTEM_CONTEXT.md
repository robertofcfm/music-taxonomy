Este archivo ha sido migrado. El contexto relevante para asignación de géneros con LLM se encuentra ahora en context/asignacion_generos_llm.md
debe considerarse BORRADOR.

Para cada tipo de trabajo se genera un PROMPT CONCRETO:
un documento con imports resueltos, archivos seleccionados
y objetivo definido.

Un prompt concreto solo se considera LISTO PARA USO
FINAL si no conserva marcadores pendientes.

Si todavía contiene bloques como:

- [DEFINIR_*]
- [COLOCAR_AQUI_*]
- [PENDIENTE_*]

entonces sigue siendo un borrador y no un documento
final de trabajo.

Para generar un prompt concreto:

Una IA selecciona contexto y reglas, y construye el
documento final para la tarea indicada.

Modelo operativo dual:

- fase generadora: realiza diagnostico de imports y validación normativa
- fase standalone: entrega prompt final ejecutable en cualquier chat
  sin depender de contexto documental del repositorio

Ventaja principal:

Si un documento fuente del proyecto se actualiza,
solo hay que recomponer el prompt concreto para que
los cambios queden aplicados sin edicion manual extensa.

--------------------------------------------------
3. MODELO DE ESTRUCTURACIÓN
--------------------------------------------------

El sistema usa composicion directa por instancia.

Restricción:

- no depender de herencia formal entre templates
- no forzar jerarquías de plantilla para tareas simples
- priorizar prompts operativos concretos en prompts/

Cada prompt debe declarar imports resueltos y objetivo.

Flujo recomendado:

- paso 1: cargar docs/context/CONTEXT_REGISTRY.md
- paso 2: cargar docs/governance/RULES_REGISTRY.md
- paso 3: clasificar imports en MANDATORY/CONDITIONAL/REFERENTIAL/EXCLUDED
- paso 4: generar prompt final standalone

Este enfoque reduce complejidad y evita dependencia de
archivos plantilla para cada variante.

La validación se centra en cobertura de imports y
consistencia normativa, no en cadenas de herencia.

--------------------------------------------------
4. MODELO DE DIVISIÓN EN CAPAS
--------------------------------------------------

Se recomienda dividir reglas y contexto en cuatro capas.

CAPA A — CORE REQUERIDO

Se recomienda cargar.

Cargar ambos cuando la tarea impacte comportamiento
sistémico o requiera autoridad normativa transversal.
Para sesiones de solo prompts, aplicar criterio del
RULES_REGISTRY como fuente normativa vinculante.

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

- un núcleo requerido pequeño
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
