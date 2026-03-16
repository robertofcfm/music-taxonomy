# REGISTRO DE ARCHIVOS DE CONTEXTO
Sistema de Taxonomía de Géneros Musicales

--------------------------------------------------
METADATOS DEL DOCUMENTO
--------------------------------------------------

Alcance:

Identificar y clasificar los archivos de contexto del
repositorio para facilitar carga selectiva en sesiones
asistidas por IA y en procesos de arranque del proyecto.

Propietario:

Propietario del proyecto

Última actualización:

2026-03-16

--------------------------------------------------
1. PROPÓSITO
--------------------------------------------------

Este documento define qué archivos deben tratarse como
CONTEXT en el proyecto.

Ayuda a evitar mezclar contexto con reglas normativas y
reduce errores por carga excesiva o incorrecta.

--------------------------------------------------
2. CONTEXTO CANÓNICO (NIVEL 1)
--------------------------------------------------

Estos archivos describen el sistema y deben considerarse
la fuente primaria de contexto conceptual:

- docs/context/PROJECT_CONTEXT.md
- docs/context/SYSTEM_OVERVIEW.md
- docs/context/PROJECT_OPERATING_MODEL.md

--------------------------------------------------
3. CONTEXTO OPERATIVO (NIVEL 2)
--------------------------------------------------

Estos archivos aportan contexto de ejecución o continuidad,
pero no sustituyen al contexto canónico:

- docs/project-management/PROJECT_STATE.md
- docs/project-management/PROJECT_MEMORY.md
- docs/project-management/PROJECT_CHECKPOINT_001.md
- docs/operations/PROJECT_BOOTSTRAP.md

--------------------------------------------------
4. CONTEXTO DE PLANTILLAS IA (NIVEL 3)
--------------------------------------------------

Contexto específico del subsistema de templates IA:

- docs/context/AI_PROMPT_SYSTEM_CONTEXT.md

--------------------------------------------------
5. EXCLUSIONES
--------------------------------------------------

No deben tratarse como contexto canónico:

- Documentos en docs/governance/* de tipo reglas o contrato
- Checklists operativos como fuente de reglas
- Releases y notas históricas no activas

--------------------------------------------------
6. REGLA DE CARGA RECOMENDADA
--------------------------------------------------

Para sesión nueva:

- cargar al menos un archivo de CONTEXTO CANÓNICO
- sumar CONTEXTO OPERATIVO solo si aporta continuidad
- sumar CONTEXTO DE PLANTILLAS IA solo si se trabajará
  con templates o generación de prompts

--------------------------------------------------
FIN DEL DOCUMENTO
