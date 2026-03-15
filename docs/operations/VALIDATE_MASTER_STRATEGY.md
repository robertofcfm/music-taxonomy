# ESTRATEGIA DE VALIDACIÓN DEL ÁRBOL MAESTRO
Sistema de Taxonomía de Géneros Musicales

--------------------------------------------------
METADATOS DEL DOCUMENTO
--------------------------------------------------

Nombre del proceso:

Marco de Validación de Entrada Taxonómica (MVET)

Alcance:

Definir y gobernar la estrategia de validación para
el archivo taxonómico maestro antes de cualquier uso
operativo.

Archivo objetivo:

taxonomy/genre_tree_master.md

Archivo de implementación:

scripts/validate_tree.py

Responsable:

Propietario del proyecto

Estado:

v0.2 — Matriz de aplicabilidad definida. Set de reglas pendiente.

Última actualización:

2026-03-15

--------------------------------------------------
PROPÓSITO
--------------------------------------------------

Este documento define la estrategia completa para
validar el archivo taxonómico maestro.

El objetivo es proteger la calidad de la taxonomía
maestra en el tiempo para evitar que su integridad
degrade a medida que evoluciona.

Este documento es una referencia estratégica viva.

En cada iteración se leerá, actualizará y
refinará hasta que la implementación alcance
su estado definitivo.

--------------------------------------------------
PRINCIPIO FUNDAMENTAL
--------------------------------------------------

Las reglas de gobernanza definidas en el proyecto son LEY.

Cualquier regla derivada de los documentos de gobernanza
que aplique a este proceso debe cumplirse
sin excepción.

Las violaciones causan ERROR FATAL.

Un error fatal:

- detiene el proceso inmediatamente
- genera un reporte de error detallado
- bloquea cualquier uso posterior del archivo validado
- requiere corrección humana antes de reanudar

No existen warnings para violaciones de reglas de gobernanza.
Una regla de gobernanza se cumple o el proceso falla.

--------------------------------------------------
ENFOQUE DE VALIDACIÓN
--------------------------------------------------

Este proceso usa un modelo de validación HÍBRIDO.

Dos capas de validación distintas operan en secuencia.

CAPA 1 — VALIDACIÓN ESTRUCTURAL DETERMINISTA

Ejecutada por:

scripts/validate_tree.py

Responsabilidad:

Aplicar todas las validaciones objetivas basadas en reglas
que puedan evaluarse algorítmicamente sin
conocimiento musical ni juicio subjetivo.

Comportamiento ante falla:

Cualquier violación en esta capa causa error fatal.
La Capa 2 no debe ejecutarse si falla la Capa 1.

CAPA 2 — VALIDACIÓN MUSICAL SEMÁNTICA

Ejecutada por:

Prompt de IA con contexto fijo y estricto.

Responsabilidad:

Evaluar coherencia musical, diferenciación entre
géneros hermanos, riesgos de cohesión de playlists,
redundancia y oportunidades de mejora estructural.

Comportamiento ante falla:

Los hallazgos de esta capa se clasifican por severidad.
Los hallazgos de clase fatal detienen el proceso.
Los hallazgos no fatales generan un reporte estructurado
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

  MANDATORY   — Define reglas aplicadas directamente por
                este proceso. No se permite exclusión.
                Las reglas derivadas de estos documentos son LEY.

  CONDITIONAL — Aplica bajo escenarios específicos de ejecución
                (post-cambio, pre-release).
                Sus reglas aplican solo cuando el escenario está activo.

  REFERENTIAL — Proporciona solo contexto del sistema.
                No gatilla checks obligatorios de validación.
                No se derivan reglas de estos documentos.

  EXCLUDED    — Confirmado fuera de alcance.
                La exclusión se justifica con
                prueba de no injerencia.

Criterios de prueba de no injerencia (los cuatro deben cumplirse
para excluir un documento):

    NI-1  No define reglas estructurales para el árbol maestro.
    NI-2  No define restricciones de nombrado o profundidad.
    NI-3  No define restricciones de cohesión o asignación
      aplicables a la estructura del árbol.
    NI-4  No impone condición de bloqueo para este proceso.

--------------------------------------------------

[ MANDATORY ]

docs/governance/GLOBAL_RULES.md

  Razón:
  Contiene reglas transversales que gobiernan directamente
  la estructura taxonómica maestra.
  Rules G001, G008, G009, G010, G011, G012, G013 impose
  enforceable structural, naming, and domain constraints
  sobre el árbol maestro. Ninguna puede excluirse.

--------------------------------------------------

docs/governance/SYSTEM_CONTRACT.md

  Razón:
  La Sección 2 define restricciones obligatorias de estructura.
  Section 3 defines valid node types (Normal, Clone, General, Atomic).
  Section 4 defines the Latin branch isolation rule.
  Section 10 explicitly defines taxonomía validación requirements.
  Este documento es fuente primaria de reglas de validación.

--------------------------------------------------

docs/governance/TAXONOMY_RULES.md

  Razón:
  Es el documento definitivo de reglas estructurales de taxonomía.
  Covers root structure, hierarchy definition, leaf node rule,
  sibling distinction, playlist cohesion, depth, expansion,
  general node policy, atomic rule, Latin branch, naming,
  clone and hybrid policy.
  Cada sección contiene reglas aplicables de forma directa.

--------------------------------------------------

docs/governance/TAXONOMY_DEPTH_POLICY.md

  Razón:
  Defines explicit depth constraints (min 3 levels, recommended
  3–5, excessive depth triggers review) and balance reglas.
  These are objectively checkable structural constraints
  aplicables al árbol maestro en cada ejecución de validación.

--------------------------------------------------

docs/governance/TAXONOMY_NAMING_CONVENTION.md

  Razón:
  Define el estándar completo de nombrado para nodos taxonómicos:
  uniqueness, language rule, Title Case, General node pattern,
  Clone node naming, prohibition of ambiguous labels, length.
  Todas sus reglas son verificables directamente sobre el árbol maestro.

--------------------------------------------------

docs/governance/TAXONOMY_QUALITY_CHECKLIST.md

  Razón:
  Este documento ES el checklist de validación de calidad de la
  taxonomía. Define checks para estructura raíz, género hermano,
  distinction, redundancy, expansion review, atomic review,
  general node usage, depth balance, over-fragmentation,
  Latin branch, naming consistency, and release gate.
  Mapea directamente a responsabilidades de Capa 1 y Capa 2.

--------------------------------------------------

[ CONDITIONAL ]

docs/governance/TAXONOMY_CHANGE_POLICY.md

  Aplica cuando:
  - El proceso corre después de un cambio manual al árbol maestro.
  - El proceso corre como parte de una validación pre-release.

  No aplica cuando:
  - El proceso corre como check rutinario pre-clasificación
    sin cambios recientes en el árbol maestro.

  Razón:
  Define política de fusión, política de reubicación y el
  proceso completo de revisión de cambios. Estas reglas solo
  se activan cuando hubo cambio estructural o un release pendiente.
  Cuando están activas, estas reglas también son LEY.

--------------------------------------------------

[ REFERENTIAL ]

docs/architecture/PROJECT_CONTEXT.md

  Prueba de no injerencia:
  NI-1 PASS — No define reglas estructurales del árbol maestro.
  NI-2 PASS — No define restricciones de nombrado o profundidad.
  NI-3 PASS — No define restricciones de cohesión o asignación.
  NI-4 PASS — No define condición de bloqueo para este proceso.

  Razón:
  Define propósito, objetivos y filosofía de evolución taxonómica.
  Aporta contexto esencial, pero no contiene reglas de validación
  aplicables de forma obligatoria.

--------------------------------------------------

docs/architecture/PROJECT_OPERATING_MODEL.md

  Prueba de no injerencia:
  NI-1 PASS — Node types referenced here are fully covered
               by SYSTEM_CONTRACT.md (MANDATORY).
  NI-2 PASS — No contiene reglas independientes de nombrado o profundidad.
  NI-3 PASS — Latin strategy referenced here is fully covered
               by SYSTEM_CONTRACT.md and TAXONOMY_RULES.md.
  NI-4 PASS — No blocking condition beyond what MANDATORY
               documents already impose.

  Razón:
  Describes the operational model and activity separation.
  Todo su contenido relevante para validación (tipos de nodo,
  Latin separation, immutability) is redundantly and more
  precisely defined in MANDATORY documents. Using this document
  como fuente de reglas, crearía duplicidad de reglas con el mismo
  contenido.

--------------------------------------------------

docs/architecture/SYSTEM_OVERVIEW.md

  Prueba de no injerencia:
  NI-1 PASS — No define reglas estructurales independientes.
  NI-2 PASS — No naming or depth constraints.
  NI-3 PASS — No cohesion or assignment constraints.
  NI-4 PASS — Only points to other documents; defines no
               blocking condition on its own.

  Razón:
  Pure high-level overview. Its sole function is to describe
  el sistema y referenciar documentos de gobernanza.
  No se derivan reglas de este documento.

--------------------------------------------------

[ EXCLUDED ]

  Ninguno.

  Todos los documentos candidatos fueron clasificados.
  Ningún documento fue excluido sin justificación.

--------------------------------------------------

Resumen de matriz de aplicabilidad:

  MANDATORY    6 documents
  CONDITIONAL  1 document
  REFERENTIAL  3 documents
  EXCLUDED     0 documents

Alcance de derivación de reglas:

  Las reglas del set de validación deben derivarse
  exclusivamente de los 6 documentos MANDATORY, más
  el documento CONDITIONAL cuando su escenario esté activo.

  Los 3 documentos REFERENTIAL no deben usarse como fuente de reglas.

--------------------------------------------------
SET DE REGLAS DE VALIDACIÓN
--------------------------------------------------

ESTADO: DEFINICIÓN PENDIENTE

Las reglas se derivarán exclusivamente de documentos
clasificados como MANDATORY o CONDITIONAL en la
matriz de aplicabilidad anterior.

Cada regla se etiquetará con:

  RULE_ID     — Identificador único.
  SOURCE      — Documento y sección de origen.
  LAYER       — 1 (determinista) o 2 (IA semántica).
  SEVERITY    — FATAL o WARNING.
  DESCRIPTION — Qué se verifica.
  CHECK       — Cómo se evalúa.

No se puede inventar ninguna regla fuera del
corpus documental de gobernanza.

--------------------------------------------------
REQUISITOS DEL PROMPT DE IA
--------------------------------------------------

ESTADO: DEFINICIÓN PENDIENTE

El prompt de IA para la Capa 2 debe incluir:

  - Bloque rígido de contexto:
    propósito del sistema, principio taxonomy-first,
    regla de inmutabilidad, reglas de separación de dominio.

  - Reglas de gobernanza aplicables extraídas y
    priorizadas del set documental MANDATORY.

  - Esquema de clasificación de severidad:
    FATAL / WARNING / SUGGESTION.

  - Esquema estricto de salida JSON:
    rule_id, severity, node_path,
    evidence, recommendation, confidence.

  - Prohibición explícita de sugerir
    cambios automáticos.

El prompt debe ser determinista en estructura.
El contenido variable se limita al input taxonómico.

--------------------------------------------------
SALIDA Y QUALITY GATE
--------------------------------------------------

ESTADO: DEFINICIÓN PENDIENTE

El proceso produce un único reporte de validación.

Decisión de quality gate:

  PASS             — Sin violaciones detectadas.

  PASS WITH WARNINGS — Sin violaciones fatales.
                       Hallazgos no fatales documentados.

  FAIL             — Una o más violaciones fatales.
                     Proceso bloqueado. Corrección requerida.

El reporte debe registrar:

  - Taxonomy version validated.
  - Date and time of execution.
  - Documents applied (from applicability matrix).
  - Layer 1 result and findings.
  - Layer 2 result and findings.
  - Final quality gate decision.
  - Hash or checksum of the validated file.

--------------------------------------------------
TRAZABILIDAD
--------------------------------------------------

La taxonomía maestra nunca debe modificarse automáticamente.

Cada corrida de validación debe producir un registro trazable.

El historial de validación permite:

  - Comparar evolución de calidad en el tiempo.
  - Detectar regresiones tras cambios taxonómicos.
  - Auditar qué reglas se aplicaron y cuándo.

--------------------------------------------------
NOTAS DE IMPLEMENTACIÓN
--------------------------------------------------

scripts/validate_tree.py

Actualmente es un placeholder.

Este archivo implementará la Capa 1 cuando el set
de reglas esté finalizado y la matriz de aplicabilidad completa.

La implementación no debe iniciar hasta que el set de
reglas de validación esté finalizado en este documento.

--------------------------------------------------
HISTORIAL DE REVISIONES
--------------------------------------------------

v0.2 — 2026-03-15
  Matriz de aplicabilidad documental completada.
  6 MANDATORY, 1 CONDITIONAL, 3 REFERENTIAL, 0 EXCLUDED.
  Pruebas de no injerencia documentadas para todos los docs REFERENTIAL.
  Alcance de derivación de reglas formalmente acotado.
  Gate de implementación actualizado: bloqueado hasta definir set de reglas.

v0.1 — 2026-03-15
  Borrador inicial abstracto de la estrategia.
  Enfoque de proceso definido: híbrido (script + IA).
  Reglas de gobernanza establecidas como LEY con enforcement fatal.
  Secciones pendientes identificadas para iteraciones siguientes.

--------------------------------------------------
FIN DEL DOCUMENTO


