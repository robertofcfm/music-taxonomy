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

v0.2 — Matriz de aplicabilidad definida. Conjunto de reglas pendiente.

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
La Capa 2 no debe ejecutarse si falla la Capa 1.

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

- docs/architecture/PROJECT_CONTEXT.md
- docs/architecture/PROJECT_OPERATING_MODEL.md
- docs/architecture/SYSTEM_OVERVIEW.md

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

ESTADO: DEFINICIÓN PENDIENTE

Cada regla deberá definirse con:

- RULE_ID
- SOURCE
- LAYER (1 o 2)
- SEVERITY (FATAL o WARNING)
- DESCRIPTION
- CHECK

No se permite inventar reglas fuera del corpus de gobernanza.

--------------------------------------------------
REQUISITOS DEL PROMPT DE IA
--------------------------------------------------

ESTADO: DEFINICIÓN PENDIENTE

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

--------------------------------------------------
SALIDA Y GATE DE CALIDAD
--------------------------------------------------

ESTADO: DEFINICIÓN PENDIENTE

El proceso genera un único reporte de validación.

Decisión de gate de calidad:

- PASS: sin violaciones.
- PASS WITH WARNINGS: sin violaciones fatales; hallazgos no fatales documentados.
- FAIL: una o más violaciones fatales; proceso bloqueado.

El reporte debe registrar:

- versión de taxonomía validada
- fecha y hora de ejecución
- documentos aplicados
- resultado y hallazgos de Capa 1
- resultado y hallazgos de Capa 2
- decisión final del gate de calidad
- hash o checksum del archivo validado

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

Actualmente es un marcador de posición.

Este archivo implementará la Capa 1 cuando el conjunto
de reglas esté finalizado y la matriz de aplicabilidad completa.

La implementación no debe iniciar hasta que el conjunto de reglas
quede finalizado en este documento.

--------------------------------------------------
HISTORIAL DE REVISIONES
--------------------------------------------------

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