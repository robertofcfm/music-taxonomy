# INICIO DE PROYECTO
Sistema de Taxonomía de Géneros Musicales

--------------------------------------------------
METADATOS DEL DOCUMENTO
--------------------------------------------------

Alcance:

Pasos de inicialización de sesión y documentos requeridos
para comenzar trabajo con el contexto actual del proyecto.

Propietario:

Propietario del proyecto

Última Actualización:

2026-03-15

--------------------------------------------------
1. PROPÓSITO
--------------------------------------------------

Este documento define cómo inicializar el proyecto
al comenzar una nueva sesión de trabajo.

Su objetivo es garantizar que el sistema cargue
el contexto correcto del proyecto y evite inventar
información u operar con datos taxonómicos desactualizados.

--------------------------------------------------
2. DOCUMENTOS REQUERIDOS
--------------------------------------------------

Al iniciar una nueva sesión, los siguientes documentos
deben cargarse antes de realizar cualquier trabajo.

REGLAS DEL SISTEMA

docs/governance/SYSTEM_CONTRACT.md

REGLAS DE ESTRUCTURA TAXONÓMICA

docs/governance/TAXONOMY_RULES.md

CONTEXTO DEL PROYECTO

docs/context/CONTEXT_REGISTRY.md
docs/context/PROJECT_CONTEXT.md

GOBERNANZA TAXONÓMICA

docs/governance/TAXONOMY_CHANGE_POLICY.md
docs/governance/TAXONOMY_DEPTH_POLICY.md
docs/governance/TAXONOMY_NAMING_CONVENTION.md
docs/governance/TAXONOMY_QUALITY_CHECKLIST.md

--------------------------------------------------
3. ARCHIVOS DE TAXONOMÍA
--------------------------------------------------

La taxonomía editable se almacena en:

taxonomy/genre_tree_master.md

Este archivo define la jerarquía de géneros mediante indentación.

La representación operativa usada por scripts es:

taxonomy/genre_tree_operational.csv

Reglas:

• El árbol operativo siempre debe coincidir con el árbol maestro  
• Si las versiones no coinciden, el archivo operativo debe regenerarse  

--------------------------------------------------
4. CONTROL DE VERSIÓN DE TAXONOMÍA
--------------------------------------------------

La información de versión de taxonomía se almacena en:

taxonomy/taxonomy_version.md

Esta versión garantiza compatibilidad entre:

• estructura taxonómica  
• resultados de clasificación  
• árboles generados  

--------------------------------------------------
5. DOCUMENTOS DE ESTADO DEL PROYECTO
--------------------------------------------------

Los siguientes documentos almacenan el avance del proyecto:

docs/project-management/PROJECT_STATE.md  
docs/project-management/PROJECT_MEMORY.md  
docs/project-management/PROJECT_FILE_INDEX.md  
docs/project-management/PROJECT_CHECKPOINT_*.md  

Ayudan a restaurar contexto si el proyecto se retoma
después de un periodo largo.

5A. COMPOSICIÓN DE PROMPTS IA
--------------------------------------------------

Para sesiones asistidas por IA que requieran carga selectiva
de reglas y contexto, usar prompts operativos en:

prompts/

Prompt bootstrap recomendado:

- prompts/prompt_bootstrap_generador_prompts_v1.md

Prompt final standalone base recomendado:

- prompts/generadores/prompt_operativo_base.md

Este enfoque usa dos fases. El generador debe construir el prompt final
cargando de forma
explícita documentos desde:

- docs/context/
- docs/governance/

La selección de imports se declara por grupos:

- documentos obligatorios
- documentos condicionales
- documentos referenciales
- documentos excluidos

Reglas de uso:

- evitar cargar contexto no activado por la tarea
- reportar conflictos normativos antes de ejecutar
- mantener presupuesto de contexto corto
- entregar un prompt final utilizable sin contexto del repositorio

--------------------------------------------------
6. ARCHIVOS DE ENTRADA DE CLASIFICACIÓN
--------------------------------------------------

Los catálogos de canciones se almacenan en:

catalog/songs_raw.csv

Después de la clasificación, la salida se escribe en:

catalog/songs_with_genres.csv

Solo se escriben canciones clasificadas correctamente.

--------------------------------------------------
FIN INICIO DE PROYECTO

