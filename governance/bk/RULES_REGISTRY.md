# REGISTRO DE REGLAS DEL PROYECTO
Sistema de Taxonomía de Géneros Musicales

--------------------------------------------------
METADATOS DEL DOCUMENTO
--------------------------------------------------

Alcance:

Identificar y clasificar los archivos normativos del
repositorio para facilitar carga selectiva en sesiones
asistidas por IA y en generación de prompts.

Propietario:

Propietario del proyecto

Última actualización:

2026-03-16

--------------------------------------------------
1. PROPÓSITO
--------------------------------------------------

Este documento define qué archivos deben tratarse como
RULES en el proyecto.

Ayuda a evitar mezclar reglas globales, reglas de dominio
y reglas operativas en una sola carga monolítica.

--------------------------------------------------
2. REGLAS NUCLEARES (NIVEL 1)
--------------------------------------------------

Estas reglas se consideran base de gobernanza general:

- docs/governance/GLOBAL_RULES.md
- docs/governance/SYSTEM_CONTRACT.md

Uso recomendado:

- Cargar siempre al menos una regla nuclear.
- Cargar ambas cuando la tarea impacta comportamiento del sistema.

--------------------------------------------------
3. REGLAS DEL SUBSISTEMA DE PROMPTS (NIVEL 2)
--------------------------------------------------

Reglas para composición y control de prompts:

- docs/governance/AI_PROMPT_SYSTEM_RULES.md

Uso recomendado:

- Cargar cuando la tarea sea crear, revisar o ejecutar prompts.

--------------------------------------------------
4. REGLAS DE DOMINIO DE TAXONOMÍA (NIVEL 3)
--------------------------------------------------

Reglas especializadas de diseño y calidad taxonómica:

- docs/governance/TAXONOMY_RULES.md
- docs/governance/TAXONOMY_CHANGE_POLICY.md
- docs/governance/TAXONOMY_DEPTH_POLICY.md
- docs/governance/TAXONOMY_NAMING_CONVENTION.md
- docs/governance/TAXONOMY_QUALITY_CHECKLIST.md

Uso recomendado:

- Cargar solo cuando la tarea activa decisiones de taxonomía.

--------------------------------------------------
5. REGLAS OPERATIVAS ESPECIALIZADAS (NIVEL 4)
--------------------------------------------------

Reglas para procesos concretos:

- docs/governance/MVET_LAYER2_RULES.md

Uso recomendado:

- Cargar solo en escenarios de validación layer2 u homólogos.

--------------------------------------------------
6. EXCLUSIONES
--------------------------------------------------

No deben tratarse como RULES canónicas:

- Archivos en docs/context/*
- Checklists operativos como fuente normativa primaria
- Notas de release y reportes históricos

--------------------------------------------------
7. REGLA DE CARGA RECOMENDADA
--------------------------------------------------

Para sesión nueva de "prompt que genera prompt":

- cargar AI_PROMPT_SYSTEM_RULES.md
- sumar GLOBAL_RULES.md solo si hay decisiones transversales
- sumar SYSTEM_CONTRACT.md solo si hay impacto de comportamiento sistémico
- no cargar reglas de taxonomía si el objetivo es genérico de prompt

--------------------------------------------------
FIN DEL DOCUMENTO
