# VALIDATE MASTER STRATEGY
Music Genre Taxonomy System

--------------------------------------------------
METADATOS DEL DOCUMENTO
--------------------------------------------------

Process Name:

Marco de Validación de Entrada Taxonómica (MVET)

Alcance:

Define and govern the validación strategy for the
master taxonomía file before any operational use.

Archivo objetivo:

taxonomy/genre_tree_master.md

Archivo de implementación:

scripts/validate_tree.py

Responsable:

Propietario del proyecto

Estado:

v0.2 — Applicability matrix defined. Rule set pendiente.

Última actualización:

2026-03-15

--------------------------------------------------
PROPÓSITO
--------------------------------------------------

Este documento define the complete strategy for
validating the master taxonomía file.

El objetivo es protect the quality of the master
taxonomía over time so that its integrity does not
degrade as it evolves.

This document is a living strategy reference.

At each iteration it will be read, updated, and
refined until the implementation reaches its
definitive state.

--------------------------------------------------
PRINCIPIO FUNDAMENTAL
--------------------------------------------------

Governance reglas defined in the project are LAW.

Any rule derived from the gobernanza documents
that applies to this process debe be enforced
without exception.

Violations cause a ERROR FATAL.

A error fatal:

- stops the process immediately
- produces a detailed error report
- blocks any downstream use of the validated file
- requires human correction before resuming

There are no warnings for gobernanza rule violations.
A gobernanza rule is either satisfied or the process fails.

--------------------------------------------------
ENFOQUE DE VALIDACIÓN
--------------------------------------------------

This process uses a HYBRID validación model.

Two distinct validación layers operate in sequence.

LAYER 1 — DETERMINISTIC STRUCTURAL VALIDATION

Executed by:

scripts/validate_tree.py

Responsibility:

Enforce all objective, rule-based validacións
that can be evaluated algorithmically without
musical knowledge or subjective judgment.

Failure behavior:

Any violation at this layer causes a error fatal.
Layer 2 no debe execute if Layer 1 fails.

LAYER 2 — SEMANTIC MUSICAL VALIDATION

Executed by:

AI prompt with a strict fixed context.

Responsibility:

Evaluate musical coherence, sibling distinctiveness,
playlist cohesion risks, redundancy, and structural
improvement opportunities.

Failure behavior:

Findings at this layer are classified by severity.
Fatal-class findings stop the process.
Non-fatal findings produce a reporte estructurado
for human review.

SHARED PRINCIPLE:

Neither layer puede modify the master taxonomía.
Both layers only validate, report, and recommend.

--------------------------------------------------
WHEN THIS PROCESS RUNS
--------------------------------------------------

This process debe execute:

- Before any clasificación run.
- Before any tree generation run.
- Before any project release.
- After any manual change to the master taxonomía.

--------------------------------------------------
GOVERNANCE DOCUMENTS APPLICABILITY
--------------------------------------------------

Classification definitions:

  MANDATORY   — Defines reglas directly enforced by this
                process. Exclusion is not allowed.
                Rules derived from these documents are LAW.

  CONDITIONAL — Applies under specific execution scenarios
                (post-change run, pre-release run).
                Rules apply only when the scenario is active.

  REFERENTIAL — Provides system context only.
                Does not trigger mandatory validación checks.
                No reglas are derived from these documents.

  EXCLUDED    — Confirmed out of scope.
                Exclusion is justified with a
                non-interference proof.

Non-interference proof criteria (all four debe hold
for a document to be excluded):

  NI-1  Does not define structural reglas for the master tree.
  NI-2  Does not define naming or depth constraints.
  NI-3  Does not define cohesion or assignment restrictions
        applicable to the tree structure.
  NI-4  Does not impose a blocking condition for this process.

--------------------------------------------------

[ MANDATORY ]

docs/governance/GLOBAL_RULES.md

  Reason:
  Contains cross-subsystem reglas that directly govern the
  master taxonomía structure.
  Rules G001, G008, G009, G010, G011, G012, G013 impose
  enforceable structural, naming, and domain constraints
  on the master tree. None can be excluded.

--------------------------------------------------

docs/governance/SYSTEM_CONTRACT.md

  Reason:
  Section 2 defines mandatory taxonomía structure constraints.
  Section 3 defines valid node types (Normal, Clone, General, Atomic).
  Section 4 defines the Latin branch isolation rule.
  Section 10 explicitly defines taxonomía validación requirements.
  This document is a primary source of validación reglas.

--------------------------------------------------

docs/governance/TAXONOMY_RULES.md

  Reason:
  The definitive structural rule document for the taxonomía.
  Covers root structure, hierarchy definition, leaf node rule,
  sibling distinction, playlist cohesion, depth, expansion,
  general node policy, atomic rule, Latin branch, naming,
  clone and hybrid policy.
  Every section contains directly enforceable reglas.

--------------------------------------------------

docs/governance/TAXONOMY_DEPTH_POLICY.md

  Reason:
  Defines explicit depth constraints (min 3 levels, recommended
  3–5, excessive depth triggers review) and balance reglas.
  These are objectively checkable structural constraints
  applicable to the master tree on every validación run.

--------------------------------------------------

docs/governance/TAXONOMY_NAMING_CONVENTION.md

  Reason:
  Defines the complete naming standard for taxonomía nodes:
  uniqueness, language rule, Title Case, General node pattern,
  Clone node naming, prohibition of ambiguous labels, length.
  All reglas are directly verifiable on the master tree.

--------------------------------------------------

docs/governance/TAXONOMY_QUALITY_CHECKLIST.md

  Reason:
  This document IS the quality validación checklist for the
  taxonomía. Defines checks for root structure, sibling
  distinction, redundancy, expansion review, atomic review,
  general node usage, depth balance, over-fragmentation,
  Latin branch, naming consistency, and release gate.
  Maps directly to both Layer 1 and Layer 2 responsibilities.

--------------------------------------------------

[ CONDITIONAL ]

docs/governance/TAXONOMY_CHANGE_POLICY.md

  Applies when:
  - The process runs after a manual change to the master tree.
  - The process runs as part of a pre-release validación.

  Does not apply when:
  - The process runs as a routine pre-clasificación check
    with no recent changes to the master tree.

  Reason:
  Defines node merge policy, relocation policy, and the full
  change review process. These reglas only become active when
  a structural change has occurred or a release is pendiente.
  When active, reglas in this document are also LAW.

--------------------------------------------------

[ REFERENTIAL ]

docs/architecture/PROJECT_CONTEXT.md

  Non-interference proof:
  NI-1 PASS — No structural reglas for the master tree.
  NI-2 PASS — No naming or depth constraints defined.
  NI-3 PASS — No cohesion or assignment restrictions.
  NI-4 PASS — Defines no blocking condition for this process.

  Reason:
  Defines project purpose, objectives, and taxonomía evolution
  philosophy. Provides essential background for understanding
  the system but contains no enforceable validación reglas.

--------------------------------------------------

docs/architecture/PROJECT_OPERATING_MODEL.md

  Non-interference proof:
  NI-1 PASS — Node types referenced here are fully covered
               by SYSTEM_CONTRACT.md (MANDATORY).
  NI-2 PASS — No independent naming or depth reglas.
  NI-3 PASS — Latin strategy referenced here is fully covered
               by SYSTEM_CONTRACT.md and TAXONOMY_RULES.md.
  NI-4 PASS — No blocking condition beyond what MANDATORY
               documents already impose.

  Reason:
  Describes the operational model and activity separation.
  All validación-relevant content it contains (node types,
  Latin separation, immutability) is redundantly and more
  precisely defined in MANDATORY documents. Using this document
  as a rule source would create duplicate reglas with the same
  content.

--------------------------------------------------

docs/architecture/SYSTEM_OVERVIEW.md

  Non-interference proof:
  NI-1 PASS — No independent structural reglas defined.
  NI-2 PASS — No naming or depth constraints.
  NI-3 PASS — No cohesion or assignment constraints.
  NI-4 PASS — Only points to other documents; defines no
               blocking condition on its own.

  Reason:
  Pure high-level overview. Its sole function is to describe
  the system and reference the actual gobernanza documents.
  No reglas are derived from this document.

--------------------------------------------------

[ EXCLUDED ]

  None.

  All candidate documents have been classified.
  No document was excluded without justification.

--------------------------------------------------

Applicability matrix summary:

  MANDATORY    6 documents
  CONDITIONAL  1 document
  REFERENTIAL  3 documents
  EXCLUDED     0 documents

Rule derivation scope:

  Rules for the validación rule set debe be derived
  exclusively from the 6 MANDATORY documents, plus the
  1 CONDITIONAL document when its scenario is active.

  The 3 REFERENTIAL documents no debe be used as rule sources.

--------------------------------------------------
VALIDATION RULE SET
--------------------------------------------------

STATUS: PENDIENTE DEFINITION

Rules will be derived exclusively from documents
classified as MANDATORY or CONDITIONAL in the
applicability matrix above.

Each rule will be tagged with:

  RULE_ID     — Unique identifier.
  SOURCE      — Document and section it derives from.
  LAYER       — 1 (deterministic) or 2 (semantic AI).
  SEVERITY    — FATAL or WARNING.
  DESCRIPTION — What is checked.
  CHECK       — How it is evaluated.

No rule puede be invented outside the gobernanza
document corpus.

--------------------------------------------------
AI PROMPT REQUIREMENTS
--------------------------------------------------

STATUS: PENDIENTE DEFINITION

The AI prompt for Layer 2 debe include:

  - Fixed rigid context block:
    system purpose, taxonomía-first principle,
    immutability rule, domain separation reglas.

  - Applicable gobernanza reglas extracted and
    prioritized from the MANDATORY document set.

  - Severity clasificación schema:
    FATAL / WARNING / SUGGESTION.

  - Strict JSON output schema:
    rule_id, severity, node_path,
    evidence, recommendation, confidence.

  - Explicit prohibition on suggesting
    automatic changes.

The prompt debe be deterministic in structure.
Variable content is limited to the taxonomía input.

--------------------------------------------------
OUTPUT AND QUALITY GATE
--------------------------------------------------

STATUS: PENDIENTE DEFINITION

The process produces a single validación report.

Quality gate decision:

  PASS             — No violations found.

  PASS WITH WARNINGS — No fatal violations.
                       Non-fatal findings documented.

  FAIL             — One or more fatal violations.
                     Process blocked. Correction required.

Report debe record:

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

The master taxonomía debe never be modified automatically.

Every validación run debe produce a traceable record.

Validation history allows:

  - Comparing quality evolution over time.
  - Detecting regressions after taxonomía changes.
  - Auditing which reglas were applied and when.

--------------------------------------------------
NOTAS DE IMPLEMENTACIÓN
--------------------------------------------------

scripts/validate_tree.py

Currently a placeholder.

This file will implement Layer 1 when the rule set
is finalized and the applicability matrix is complete.

Implementation no debe begin until the validación
rule set is finalized in this document.

--------------------------------------------------
HISTORIAL DE REVISIONES
--------------------------------------------------

v0.2 — 2026-03-15
  Governance documents applicability matrix completed.
  6 MANDATORY, 1 CONDITIONAL, 3 REFERENTIAL, 0 EXCLUDED.
  Non-interference proofs documented for all REFERENTIAL docs.
  Rule derivation scope formally bounded.
  Implementation gate updated: blocked until rule set is defined.

v0.1 — 2026-03-15
  Borrador inicial abstracto de la estrategia.
  Process approach defined: hybrid (script + AI).
  Governance reglas established as LAW with fatal enforcement.
  Pending sections identified for next iterations.

--------------------------------------------------
FIN DEL DOCUMENTO


