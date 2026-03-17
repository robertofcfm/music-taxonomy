# ESTRATEGIA DE VALIDACIÓN DEL ÁRBOL MAESTRO
Sistema de Taxonomía de Géneros Musicales

--------------------------------------------------
METADATOS DEL DOCUMENTO
--------------------------------------------------

Nombre del proceso:

Marco de Validación de Entrada Taxonómica (MVET)

Alcance:

Definir y gobernar la estrategia de validación del archivo
maestro de taxonomía antes de cualquier uso operativo.

Archivo objetivo:

taxonomy/genre_tree_master.md

Archivo de implementación:

scripts/validate_tree.py

Responsable:

Propietario del proyecto

Estado:

v0.6 — Capa 2 implementada (stub con contrato de prompt y validación de respuesta).

Última actualización:

2026-03-15

--------------------------------------------------
PROPÓSITO
--------------------------------------------------

Este documento define la estrategia completa para validar
el archivo maestro de taxonomía.

El objetivo es proteger la calidad de la taxonomía maestra
en el tiempo para evitar que su integridad disminuya a medida
que evoluciona.

Este documento es una referencia estratégica viva.

En cada iteración se leerá, actualizará y refinará hasta que
la implementación alcance su estado definitivo.

--------------------------------------------------
PRINCIPIO FUNDAMENTAL
--------------------------------------------------

Las reglas de gobernanza definidas en el proyecto son LEY.

Toda regla derivada de documentos de gobernanza que aplique
a este proceso debe cumplirse sin excepción.

Cualquier violación causa ERROR FATAL.

Un error fatal:

- detiene el proceso inmediatamente
- genera un reporte de error detallado
- bloquea cualquier uso posterior del archivo validado
- requiere corrección humana antes de reanudar

No existen advertencias para violaciones de gobernanza.
Una regla se cumple o el proceso falla.

Excepción explícita:

Hallazgos etiquetados como WARNING o SUGGESTION solo aplican
a recomendaciones de calidad o semántica que no constituyen
incumplimiento de una obligación normativa.

--------------------------------------------------
ENFOQUE DE VALIDACIÓN
--------------------------------------------------

Este proceso usa un modelo de validación híbrido.

Operan dos capas en secuencia.

CAPA 1 — VALIDACIÓN ESTRUCTURAL DETERMINISTA

Ejecutada por:

scripts/validate_tree.py

Responsabilidad:

Aplicar validaciones objetivas basadas en reglas,
algorítmicamente evaluables y sin juicio musical subjetivo.

Comportamiento ante falla:

Cualquier violación en esta capa causa error fatal.
La Capa 2 puede ejecutarse de forma independiente para analisis semantico,
pero sus resultados no anulan ni compensan fallas fatales detectadas en Capa 1.

CAPA 2 — VALIDACIÓN MUSICAL SEMÁNTICA

Ejecutada por:

Prompt de IA con contexto fijo y estricto.

Responsabilidad:

Evaluar coherencia musical, distinción entre géneros hermanos,
riesgos de cohesión de playlists, redundancia y oportunidades
estructurales de mejora.

Comportamiento ante falla:

Los hallazgos se clasifican por severidad.
Los hallazgos de clase fatal detienen el proceso.
Los hallazgos no fatales generan reporte estructurado
para revisión humana.

PRINCIPIO COMPARTIDO:

Ninguna capa puede modificar la taxonomía maestra.
Ambas capas solo validan, reportan y recomiendan.

--------------------------------------------------
CUÁNDO CORRE ESTE PROCESO
--------------------------------------------------

Este proceso debe ejecutarse:

- Antes de cualquier corrida de clasificación.
- Antes de cualquier corrida de generación de árbol.
- Antes de cualquier release del proyecto.
- Después de cualquier cambio manual en la taxonomía maestra.

--------------------------------------------------
APLICABILIDAD DE DOCUMENTOS DE GOBERNANZA
--------------------------------------------------

Definiciones de clasificación:

MANDATORY:
Define reglas aplicadas directamente por este proceso.
No se permite exclusión.
Las reglas derivadas de estos documentos son LEY.

CONDITIONAL:
Aplica bajo escenarios específicos (post-cambio, pre-release).
Sus reglas aplican solo cuando el escenario está activo.

REFERENTIAL:
Proporciona solo contexto del sistema.
No gatilla checks obligatorios de validación.
No se derivan reglas de estos documentos.

EXCLUDED:
Confirmado fuera de alcance.
La exclusión debe justificarse con prueba de no injerencia.

Criterios de no injerencia (deben cumplirse todos):

- NI-1 No define reglas estructurales del árbol maestro.
- NI-2 No define restricciones de nombrado o profundidad.
- NI-3 No define restricciones de cohesión o asignación aplicables al árbol.
- NI-4 No impone condición de bloqueo para este proceso.

--------------------------------------------------

MANDATORY

- docs/governance/GLOBAL_RULES.md
  Razón: contiene reglas transversales con impacto directo en estructura,
  nombrado y dominio de la taxonomía maestra.

- docs/governance/SYSTEM_CONTRACT.md
  Razón: define restricciones obligatorias de estructura, tipos de nodo,
  aislamiento Latin y requerimientos explícitos de validación.

- docs/governance/TAXONOMY_RULES.md
  Razón: documento estructural principal para raíz, jerarquía, hojas,
  distinción de hermanos, cohesión, profundidad, nodos General/Atomic,
  rama Latin y política clone/híbridos.

- docs/governance/TAXONOMY_DEPTH_POLICY.md
  Razón: define límites y balance de profundidad verificables.

- docs/governance/TAXONOMY_NAMING_CONVENTION.md
  Razón: define estándar de nombrado verificable directamente.

- docs/governance/TAXONOMY_QUALITY_CHECKLIST.md
  Razón: define checks de calidad que mapean a Capa 1 y Capa 2.

CONDITIONAL

- docs/governance/TAXONOMY_CHANGE_POLICY.md
  Aplica en corridas post-cambio y pre-release.
  No aplica en checks rutinarios sin cambios recientes.

REFERENTIAL

- docs/context/PROJECT_CONTEXT.md
- docs/context/PROJECT_OPERATING_MODEL.md
- docs/context/SYSTEM_OVERVIEW.md

Razón general: aportan contexto de sistema;
no son fuente primaria de reglas obligatorias en este proceso.

EXCLUDED

- Ninguno.

Resumen de matriz:

- MANDATORY: 6 documentos
- CONDITIONAL: 1 documento
- REFERENTIAL: 3 documentos
- EXCLUDED: 0 documentos

Alcance de derivación de reglas:

Las reglas del set de validación deben derivarse exclusivamente
de los 6 documentos MANDATORY y del documento CONDITIONAL
cuando su escenario esté activo.

Los documentos REFERENTIAL no deben usarse como fuente de reglas.

--------------------------------------------------
CONJUNTO DE REGLAS DE VALIDACIÓN
--------------------------------------------------

ESTADO: DEFINIDO

Formato obligatorio de regla:

- RULE_ID
- LAYER (1 o 2)
- SEVERITY (FATAL o WARNING)
- DESCRIPTION
- CHECK

Convención de asignación por capa:

- `MVET-L1-*`: se implementa y ejecuta en Capa 1 (determinista).
- `MVET-L2-*`: se implementa y ejecuta en Capa 2 (semántica IA).
- `MVET-C-*`: reglas condicionales (activación por escenario).

Modelo de trazabilidad:

- La gobernanza se usa como base de conocimiento normativa.
- La trazabilidad se gestiona por archivo fuente, no por regla individual.
- Cada regla MVET referencia un bloque funcional del proceso.

Bloques funcionales y trazabilidad por archivo:

- FB-01 Estructura base del árbol
  Archivos fuente:
  - docs/governance/SYSTEM_CONTRACT.md
  - docs/governance/TAXONOMY_RULES.md

- FB-02 Convenciones de nombrado
  Archivos fuente:
  - docs/governance/TAXONOMY_NAMING_CONVENTION.md

- FB-03 Profundidad y equilibrio
  Archivos fuente:
  - docs/governance/TAXONOMY_DEPTH_POLICY.md
  - docs/governance/TAXONOMY_RULES.md

- FB-04 Inmutabilidad y seguridad del maestro
  Archivos fuente:
  - docs/governance/GLOBAL_RULES.md
  - docs/governance/SYSTEM_CONTRACT.md

- FB-05 Calidad semántica musical
  Archivos fuente:
  - docs/governance/TAXONOMY_QUALITY_CHECKLIST.md
  - docs/governance/TAXONOMY_RULES.md

- FB-06 Gestión de cambio y release
  Archivos fuente:
  - docs/governance/TAXONOMY_CHANGE_POLICY.md
  - docs/governance/TAXONOMY_QUALITY_CHECKLIST.md

Regla de diseño del set:

- No se permite inventar reglas fuera del corpus de gobernanza.
- Toda violación de regla de gobernanza obligatoria es FATAL.
- WARNING/SUGGESTION solo pueden usarse para recomendaciones
  no normativas (de calidad o semántica), incluso si su fuente
  documental pertenece al corpus de gobernanza.

Catálogo inicial de reglas del proceso:

CAPA 1 — Reglas deterministas (script)

- MVET-L1-001
  FB: FB-01
  SEVERITY: FATAL
  DESCRIPTION: Debe existir un nodo raíz único.
  CHECK: Conteo de raíces = 1.

- MVET-L1-002
  FB: FB-01
  SEVERITY: FATAL
  DESCRIPTION: La jerarquía debe ser válida por indentación.
  CHECK: Parser de árbol sin saltos de nivel inválidos ni nodos huérfanos.

- MVET-L1-003
  FB: FB-02
  SEVERITY: FATAL
  DESCRIPTION: Nombres de género únicos (excepto clone permitido).
  CHECK: Duplicados bloqueados cuando no exista justificación clone.

- MVET-L1-004
  FB: FB-02
  SEVERITY: FATAL
  DESCRIPTION: Formato de nombrado válido (Title Case y patrón General).
  CHECK: Regex de formato y validación de sufijo "(General)".

- MVET-L1-005
  FB: FB-01
  SEVERITY: FATAL
  DESCRIPTION: Nodos General no autogenerados y correctamente definidos.
  CHECK: Presencia explícita y ubicación bajo padre correspondiente.

- MVET-L1-006
  FB: FB-01
  SEVERITY: FATAL
  DESCRIPTION: Restricciones de nodo clone.
  CHECK: Clone sin hijos y con referencia canónica válida.

- MVET-L1-007
  FB: FB-03
  SEVERITY: WARNING
  DESCRIPTION: Profundidad mínima estructural del árbol.
  CHECK: La profundidad mínima requerida es 3.
         Esta regla no evalúa semántica musical ni justificación atómica.

- MVET-L1-008
  FB: FB-04
  SEVERITY: FATAL
  DESCRIPTION: Inmutabilidad del archivo maestro.
  CHECK: El proceso no modifica taxonomy/genre_tree_master.md.

- MVET-L1-009
  FB: FB-02
  SEVERITY: FATAL
  DESCRIPTION: Términos ambiguos prohibidos en nombres de nodo.
  CHECK: Lista de prohibidos y variantes normalizadas.

- MVET-L1-010
  FB: FB-04
  SEVERITY: FATAL
  DESCRIPTION: Separación de dominio Latin en reglas estructurales declaradas.
  CHECK: Rama Latin presente y sin contradicciones de estructura base.

CAPA 2 — Reglas semánticas (IA)

- MVET-L2-001
  FB: FB-05
  SEVERITY: WARNING
  DESCRIPTION: Distinción musical entre géneros hermanos.
  CHECK: Evaluación comparativa y evidencia por par de hermanos conflictivos.

- MVET-L2-002
  FB: FB-05
  SEVERITY: WARNING
  DESCRIPTION: Riesgos de cohesión de playlists por estructura.
  CHECK: Identificación de nodos con mezcla estilística potencial.

- MVET-L2-003
  FB: FB-05
  SEVERITY: WARNING
  DESCRIPTION: Redundancia entre nodos.
  CHECK: Detección de géneros potencialmente equivalentes,
         excluyendo nodos clone.

- MVET-L2-004
  FB: FB-05
  SEVERITY: WARNING
  DESCRIPTION: Sobre-fragmentación estructural.
  CHECK: Detección de subramas excesivas sin valor musical claro.

- MVET-L2-005
  FB: FB-05
  SEVERITY: WARNING
  DESCRIPTION: Criterio atómico para límite de profundidad máxima.
  CHECK: Nodos hoja donde subdividir más sería forzado o
         deterioraría coherencia musical.

- MVET-L2-006
  FB: FB-06
  SEVERITY: WARNING
  DESCRIPTION: Candidatos de reubicación estructural.
  CHECK: Propuesta de reubicación con evidencia musical.

- MVET-L2-007
  FB: FB-06
  SEVERITY: WARNING
  DESCRIPTION: Candidatos de fusión de nodos hermanos.
  CHECK: Evidencia de solapamiento alto entre hermanos.

- MVET-L2-008
  FB: FB-04
  SEVERITY: FATAL
  DESCRIPTION: Violación semántica de separación Latin y no-Latin.
  CHECK: Hallazgo explícito de mezcla de dominios incompatibles, excluyendo nodos clone.

Reglas condicionales (activas en post-cambio y pre-release):

- MVET-C-001
  FB: FB-06
  LAYER: 2
  SEVERITY: WARNING
  DESCRIPTION: Revisión global de cambios estructurales recientes.
  CHECK: Confirmación de revisión integral de efectos colaterales.

- MVET-C-002
  FB: FB-06
  LAYER: 1 y 2
  SEVERITY: FATAL
  DESCRIPTION: Bloqueo de release por issues estructurales no resueltos.
  CHECK: Cualquier issue abierto de severidad fatal bloquea el gate.

--------------------------------------------------
REQUISITOS DEL PROMPT DE IA
--------------------------------------------------

ESTADO: DEFINIDO

El prompt de IA para Capa 2 debe incluir:

- Bloque rígido de contexto (propósito del sistema, taxonomy-first,
  inmutabilidad, separación de dominio).
- Reglas de gobernanza aplicables extraídas del set MANDATORY.
- Esquema de severidad: FATAL / WARNING / SUGGESTION.
- Esquema estricto de salida JSON:
  rule_id, severity, node_path, evidence, recommendation, confidence.
- Prohibición explícita de sugerir cambios automáticos.

La estructura del prompt debe ser determinista.
El contenido variable se limita al input taxonómico.

Contrato de salida obligatorio de Capa 2:

- Formato JSON válido, sin texto fuera del JSON.
- Cada hallazgo debe incluir:
  - rule_id
  - severity (FATAL | WARNING | SUGGESTION)
  - node_path
  - evidence
  - recommendation
  - confidence (0.00-1.00)
- Debe incluir resumen final:
  - total_fatal
  - total_warning
  - total_suggestion
  - decision_recommendation (PASS | PASS_WITH_WARNINGS | FAIL)

Reglas de seguridad del prompt:

- Prohibido proponer edición automática del archivo maestro.
- Prohibido crear reglas no presentes en el corpus de gobernanza.
- Prohibido ocultar incertidumbre: debe reportarse en confidence.

--------------------------------------------------
SALIDA Y GATE DE CALIDAD
--------------------------------------------------

ESTADO: DEFINIDO

El proceso genera un único reporte de validación.

Decisión de gate de calidad:

- PASS: sin violaciones.
- PASS WITH WARNINGS: sin violaciones fatales; hallazgos no fatales documentados.
- FAIL: una o más violaciones fatales; proceso bloqueado.

Criterio de decisión automático:

- FAIL:
  - Si existe al menos 1 FATAL en Capa 1.
  - Si existe al menos 1 FATAL en Capa 2.

- PASS WITH WARNINGS:
  - Sin FATAL.
  - Al menos 1 WARNING o SUGGESTION.

- PASS:
  - Sin FATAL.
  - Sin WARNING.
  - Sin SUGGESTION crítica pendiente.

El reporte debe registrar:

- versión de taxonomía validada
- fecha y hora de ejecución
- documentos aplicados
- resultado y hallazgos de Capa 1
- resultado y hallazgos de Capa 2
- decisión final del gate de calidad
- hash o checksum del archivo validado

Artefactos de salida mínimos del proceso:

- reports/validate_master_report.json
- reports/validate_master_report.md
- reports/validate_master_run_metadata.json

--------------------------------------------------
TRAZABILIDAD
--------------------------------------------------

La taxonomía maestra nunca debe modificarse automáticamente.

Cada corrida de validación debe generar un registro trazable.

El historial de validación permite:

- comparar evolución de calidad en el tiempo
- detectar regresiones tras cambios taxonómicos
- auditar qué reglas se aplicaron y cuándo

--------------------------------------------------
NOTAS DE IMPLEMENTACIÓN
--------------------------------------------------

scripts/validate_tree.py

Implementa la Capa 1 determinista.
Ejecución: python scripts/validate_tree.py
Salida: reports/validate_master_report.json y .md

scripts/validate_tree_layer2.py

Implementa la Capa 2 semántica como stub operativo.

Modo generación de prompt:
  python scripts/validate_tree_layer2.py --print-prompt
  Salida: prompts/validate_master_layer2_prompt.txt
  Ese archivo debe enviarse a un modelo de lenguaje externo.

Modo aplicación de respuesta:
  python scripts/validate_tree_layer2.py --apply-response <respuesta.json>
  Valida el esquema JSON de la respuesta IA y genera reportes.
  Salida: reports/validate_master_layer2_report.json y .md

--------------------------------------------------
HISTORIAL DE REVISIONES
--------------------------------------------------

v0.6 — 2026-03-15
- scripts/validate_tree_layer2.py implementado como stub operativo de Capa 2.
- Modos --print-prompt y --apply-response funcionando.
- Contrato de respuesta JSON con validación de esquema.
- Pre-requisito de Capa 1 verificado antes de ejecutar Capa 2.

v0.5 — 2026-03-15
- MVET-L1-007 actualizado: profundidad mínima = 3.
- Se elimina tope máximo numérico fijo de profundidad.
- La profundidad máxima se define por criterio de género atómico.
- Se separa formalmente la evaluación: mínimo en Capa 1 y criterio atómico en Capa 2.

v0.4 — 2026-03-15
- Se cambió el modelo de trazabilidad: de SOURCE por regla a trazabilidad por archivo.
- Se definieron bloques funcionales (FB-01 a FB-06) como puente entre reglas y documentos.
- La gobernanza quedó explicitada como base de conocimiento normativa.

v0.3 — 2026-03-15
- Conjunto de reglas MVET definido (Capa 1, Capa 2 y condicionales).
- Contrato de prompt de IA definido con esquema de salida obligatorio.
- Gate de calidad definido con criterio automático de decisión.
- Artefactos de salida del proceso definidos.
- Implementación de Capa 1 desbloqueada.

v0.2 — 2026-03-15
- Matriz de aplicabilidad documental completada.
- 6 MANDATORY, 1 CONDITIONAL, 3 REFERENTIAL, 0 EXCLUDED.
- Alcance de derivación de reglas formalmente acotado.
- Gate de implementación bloqueado hasta definir conjunto de reglas.

v0.1 — 2026-03-15
- Borrador inicial abstracto de la estrategia.
- Enfoque de proceso definido: híbrido (script + IA).
- Reglas de gobernanza establecidas como LEY con cumplimiento fatal.

--------------------------------------------------
FIN DEL DOCUMENTO