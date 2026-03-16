# ÍNDICE DE ARCHIVOS DEL PROYECTO
Sistema de Taxonomía de Géneros Musicales

--------------------------------------------------
1. PROPÓSITO
--------------------------------------------------

Este documento define el rol de cada archivo dentro del repositorio.

Su propósito es:

• explicar la estructura del repositorio
• definir dónde vive cada tipo de documentación
• prevenir deriva documental
• guiar reconstrucción y mantenimiento

Toda la documentación del proyecto debe seguir la estructura
establecida en este índice.

--------------------------------------------------
2. ESTRUCTURA DEL REPOSITORIO
--------------------------------------------------

El repositorio está organizado en áreas lógicas:

catalog/
data/
taxonomy/
scripts/
reports/
docs/

Cada directorio contiene un tipo específico de datos
o documentación.

--------------------------------------------------
3. ARCHIVOS DE CATÁLOGO
--------------------------------------------------

catalog/songs_raw.csv

Catálogo de entrada con canciones a clasificar.

Campos típicos:

title
artist

--------------------------------------------------

catalog/songs_with_genres.csv

Archivo de salida generado por el sistema de clasificación.

Almacena géneros asignados a cada canción.

--------------------------------------------------
4. ARCHIVOS DE DATOS
--------------------------------------------------

data/genre_alias.csv

Mapa de alias para normalizar nombres de género.

Permite que el clasificador resuelva etiquetas alternas
hacia géneros canónicos.

--------------------------------------------------
5. ARCHIVOS DE TAXONOMÍA
--------------------------------------------------

taxonomy/genre_tree_master.md

Plantilla de taxonomía editable por humanos.

Define la jerarquía de géneros con indentación.

Solo el propietario del proyecto modifica este archivo.

--------------------------------------------------

taxonomy/genre_tree_operational.csv

Representación machine-readable de la taxonomía.

Se genera desde la taxonomía maestra y la usan scripts
y herramientas de clasificación.

--------------------------------------------------

taxonomy/taxonomy_version.md

Almacena la versión vigente de la taxonomía.

Se usa para verificar compatibilidad entre:

• estructura taxonómica
• resultados de clasificación
• árboles de género generados

--------------------------------------------------
6. ARCHIVOS DE SCRIPTS
--------------------------------------------------

scripts/build_tree.py

Genera el árbol dinámico de escucha a partir
de canciones clasificadas.

--------------------------------------------------

scripts/classify_songs.py

Realiza clasificación de género en canciones.

Lee:

catalog/songs_raw.csv

Escribe:

catalog/songs_with_genres.csv

--------------------------------------------------

scripts/validate_tree.py

Valida la estructura taxonómica y detecta
issues estructurales.

--------------------------------------------------
7. ARCHIVOS DE REPORTES
--------------------------------------------------

reports/taxonomy_improvement_report.csv

Contiene sugerencias para mejorar la taxonomía.

--------------------------------------------------

reports/taxonomy_issues.csv

Almacena problemas detectados de taxonomía, como:

• nodos ambiguos
• géneros faltantes
• conflictos de clasificación

--------------------------------------------------
8. ESTRUCTURA DE DOCUMENTACIÓN
--------------------------------------------------

Toda la documentación se organiza bajo docs/.

docs/

governance/
architecture/
operations/
project-management/
releases/

La documentación se agrupa por función.
Cada carpeta cumple un propósito operativo específico.

Los documentos de gobernanza y operaciones usan una
plantilla de encabezado común con:

• Propósito
• Alcance
• Responsable
• Última actualización

--------------------------------------------------
9. DOCUMENTACIÓN DE GOBERNANZA GLOBAL
--------------------------------------------------

docs/governance/GLOBAL_RULES.md

Define reglas transversales que aplican a múltiples
componentes del repositorio.

Este archivo es la ubicación canónica para reglas
que afectan más de un subsistema.

Ejemplos de reglas de alcance global:

• comportamiento taxonómico
• lógica de clasificación
• procedimientos de validación
• restricciones de repositorio

--------------------------------------------------

PRINCIPIO DE UBICACIÓN DE REGLAS

Si una regla aplica a un solo archivo o subsistema,
debe vivir en ese archivo específico.

Si una regla aplica a múltiples archivos o subsistemas,
debe ubicarse en:

docs/governance/GLOBAL_RULES.md

Otros documentos pueden referenciar la regla,
pero no deben duplicarla.

--------------------------------------------------

PRINCIPIO DE CARGA DE REGLAS

Cuando se evalúen reglas del repositorio
(por ejemplo durante reconstrucción o validación),
siempre deben cargarse:

1. docs/governance/GLOBAL_RULES.md
2. docs/governance/SYSTEM_CONTRACT.md

GLOBAL_RULES.md contiene reglas canónicas.

SYSTEM_CONTRACT.md contiene reglas obligatorias del sistema.

--------------------------------------------------

PRINCIPIO DE PRECEDENCIA GLOBAL

docs/governance/GLOBAL_RULES.md es la fuente canónica
para reglas transversales.

Si existe conflicto entre un documento local y GLOBAL_RULES.md
sobre una regla transversal, GLOBAL_RULES.md tiene precedencia.

Los archivos locales pueden especializar implementación,
pero no deben contradecir reglas globales.

--------------------------------------------------
10. DOCUMENTACIÓN DE CONTEXTO
--------------------------------------------------

docs/context/CONTEXT_REGISTRY.md

Registro canonico de archivos de contexto del proyecto,
clasificados por nivel de uso.

--------------------------------------------------

docs/context/README.md

Guia rapida de la carpeta context y referencia
al registro de contexto.

--------------------------------------------------

docs/context/SYSTEM_OVERVIEW.md

Descripción de alto nivel de la arquitectura del sistema.

--------------------------------------------------

docs/context/PROJECT_CONTEXT.md

Describe objetivos conceptuales y contexto del sistema.

--------------------------------------------------

docs/context/PROJECT_OPERATING_MODEL.md

Explica la separación operativa de actividades.

--------------------------------------------------

docs/context/AI_PROMPT_SYSTEM_CONTEXT.md

Contexto del sistema de plantillas de prompt para IA.
Explica el modelo abstracto/concreto, herencia, capas
y criterios de uso por escenario.

--------------------------------------------------
11. DOCUMENTACIÓN DE GOBERNANZA DE TAXONOMÍA
--------------------------------------------------

docs/governance/SYSTEM_CONTRACT.md

Define reglas obligatorias de comportamiento del sistema.

--------------------------------------------------

docs/governance/TAXONOMY_RULES.md

Define estructura y comportamiento de la taxonomía.

--------------------------------------------------

docs/governance/TAXONOMY_CHANGE_POLICY.md

Define reglas para modificar la taxonomía.

--------------------------------------------------

docs/governance/TAXONOMY_DEPTH_POLICY.md

Define reglas de profundidad y expansión taxonómica.

--------------------------------------------------

docs/governance/TAXONOMY_NAMING_CONVENTION.md

Define convenciones de nombrado para géneros.

--------------------------------------------------

docs/governance/TAXONOMY_QUALITY_CHECKLIST.md

Checklist para validar calidad taxonómica.

--------------------------------------------------
12. DOCUMENTACIÓN DE OPERACIONES
--------------------------------------------------

docs/operations/PROJECT_BOOTSTRAP.md

Define cómo inicializar una sesión nueva
con el contexto correcto del proyecto.

--------------------------------------------------

docs/operations/PHASE1_FINAL_CHECKLIST.md

Checklist de cierre de la Fase 1.

--------------------------------------------------

docs/governance/AI_PROMPT_SYSTEM_RULES.md

Reglas que gobiernan el uso y composición de plantillas
de prompt para IA. Contiene principios de composición,
regla de selección y protocolo de cierre de conversación.

--------------------------------------------------

docs/operations/AI_PROMPT_BASE_TEMPLATE.md

Plantilla base abstracta para prompts de IA.
Contiene solo IMPORTS a contexto y reglas,
más la definición estructural de la plantilla.

--------------------------------------------------

docs/operations/AI_PROMPT_BASE_TEMPLATE_TIPO_PROMPT.md

Especializa la plantilla base para instancias cuyo
objetivo sea producir un prompt final.

--------------------------------------------------

docs/operations/AI_PROMPT_BASE_TEMPLATE_TIPO_TAREA.md

Especializa la plantilla base para instancias cuyo
objetivo sea producir una tarea operativa específica.

--------------------------------------------------
13. DOCUMENTACIÓN DE GESTIÓN DEL PROYECTO
--------------------------------------------------

docs/project-management/PROJECT_STATE.md

Almacena el estado operativo actual del proyecto.

--------------------------------------------------

docs/project-management/PROJECT_MEMORY.md

Almacena decisiones de diseño y contexto histórico.

--------------------------------------------------

docs/project-management/PROJECT_FILE_INDEX.md

Define la estructura documental del repositorio.

--------------------------------------------------

docs/project-management/PROJECT_CHECKPOINT_001.md

Instantánea de la arquitectura reconstruida del proyecto.

--------------------------------------------------
14. DOCUMENTACIÓN DE RELEASES
--------------------------------------------------

docs/releases/RELEASE_NOTES_v1.0.md

Notas de release de la primera versión estable del repositorio.

--------------------------------------------------
FIN DEL DOCUMENTO