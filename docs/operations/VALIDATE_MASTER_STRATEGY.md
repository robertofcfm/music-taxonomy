# VALIDATE MASTER STRATEGY
Music Genre Taxonomy System

--------------------------------------------------
DOCUMENT METADATA
--------------------------------------------------

Process Name:

Marco de Validación de Entrada Taxonómica (MVET)

Scope:

Define and govern the validation strategy for the
master taxonomy file before any operational use.

Target File:

taxonomy/genre_tree_master.md

Implementation File:

scripts/validate_tree.py

Owner:

Project Owner

Status:

v0.2 — Applicability matrix defined. Rule set pending.

Last Updated:

2026-03-15

--------------------------------------------------
PURPOSE
--------------------------------------------------

This document defines the complete strategy for
validating the master taxonomy file.

The goal is to protect the quality of the master
taxonomy over time so that its integrity does not
degrade as it evolves.

This document is a living strategy reference.

At each iteration it will be read, updated, and
refined until the implementation reaches its
definitive state.

--------------------------------------------------
FUNDAMENTAL PRINCIPLE
--------------------------------------------------

Governance rules defined in the project are LAW.

Any rule derived from the governance documents
that applies to this process must be enforced
without exception.

Violations cause a FATAL ERROR.

A fatal error:

- stops the process immediately
- produces a detailed error report
- blocks any downstream use of the validated file
- requires human correction before resuming

There are no warnings for governance rule violations.
A governance rule is either satisfied or the process fails.

--------------------------------------------------
VALIDATION APPROACH
--------------------------------------------------

This process uses a HYBRID validation model.

Two distinct validation layers operate in sequence.

LAYER 1 — DETERMINISTIC STRUCTURAL VALIDATION

Executed by:

scripts/validate_tree.py

Responsibility:

Enforce all objective, rule-based validations
that can be evaluated algorithmically without
musical knowledge or subjective judgment.

Failure behavior:

Any violation at this layer causes a fatal error.
Layer 2 must not execute if Layer 1 fails.

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
Non-fatal findings produce a structured report
for human review.

SHARED PRINCIPLE:

Neither layer may modify the master taxonomy.
Both layers only validate, report, and recommend.

--------------------------------------------------
WHEN THIS PROCESS RUNS
--------------------------------------------------

This process must execute:

- Before any classification run.
- Before any tree generation run.
- Before any project release.
- After any manual change to the master taxonomy.

--------------------------------------------------
GOVERNANCE DOCUMENTS APPLICABILITY
--------------------------------------------------

Classification definitions:

  MANDATORY   — Defines rules directly enforced by this
                process. Exclusion is not allowed.
                Rules derived from these documents are LAW.

  CONDITIONAL — Applies under specific execution scenarios
                (post-change run, pre-release run).
                Rules apply only when the scenario is active.

  REFERENTIAL — Provides system context only.
                Does not trigger mandatory validation checks.
                No rules are derived from these documents.

  EXCLUDED    — Confirmed out of scope.
                Exclusion is justified with a
                non-interference proof.

Non-interference proof criteria (all four must hold
for a document to be excluded):

  NI-1  Does not define structural rules for the master tree.
  NI-2  Does not define naming or depth constraints.
  NI-3  Does not define cohesion or assignment restrictions
        applicable to the tree structure.
  NI-4  Does not impose a blocking condition for this process.

--------------------------------------------------

[ MANDATORY ]

docs/governance/GLOBAL_RULES.md

  Reason:
  Contains cross-subsystem rules that directly govern the
  master taxonomy structure.
  Rules G001, G008, G009, G010, G011, G012, G013 impose
  enforceable structural, naming, and domain constraints
  on the master tree. None can be excluded.

--------------------------------------------------

docs/governance/SYSTEM_CONTRACT.md

  Reason:
  Section 2 defines mandatory taxonomy structure constraints.
  Section 3 defines valid node types (Normal, Clone, General, Atomic).
  Section 4 defines the Latin branch isolation rule.
  Section 10 explicitly defines taxonomy validation requirements.
  This document is a primary source of validation rules.

--------------------------------------------------

docs/governance/TAXONOMY_RULES.md

  Reason:
  The definitive structural rule document for the taxonomy.
  Covers root structure, hierarchy definition, leaf node rule,
  sibling distinction, playlist cohesion, depth, expansion,
  general node policy, atomic rule, Latin branch, naming,
  clone and hybrid policy.
  Every section contains directly enforceable rules.

--------------------------------------------------

docs/governance/TAXONOMY_DEPTH_POLICY.md

  Reason:
  Defines explicit depth constraints (min 3 levels, recommended
  3–5, excessive depth triggers review) and balance rules.
  These are objectively checkable structural constraints
  applicable to the master tree on every validation run.

--------------------------------------------------

docs/governance/TAXONOMY_NAMING_CONVENTION.md

  Reason:
  Defines the complete naming standard for taxonomy nodes:
  uniqueness, language rule, Title Case, General node pattern,
  Clone node naming, prohibition of ambiguous labels, length.
  All rules are directly verifiable on the master tree.

--------------------------------------------------

docs/governance/TAXONOMY_QUALITY_CHECKLIST.md

  Reason:
  This document IS the quality validation checklist for the
  taxonomy. Defines checks for root structure, sibling
  distinction, redundancy, expansion review, atomic review,
  general node usage, depth balance, over-fragmentation,
  Latin branch, naming consistency, and release gate.
  Maps directly to both Layer 1 and Layer 2 responsibilities.

--------------------------------------------------

[ CONDITIONAL ]

docs/governance/TAXONOMY_CHANGE_POLICY.md

  Applies when:
  - The process runs after a manual change to the master tree.
  - The process runs as part of a pre-release validation.

  Does not apply when:
  - The process runs as a routine pre-classification check
    with no recent changes to the master tree.

  Reason:
  Defines node merge policy, relocation policy, and the full
  change review process. These rules only become active when
  a structural change has occurred or a release is pending.
  When active, rules in this document are also LAW.

--------------------------------------------------

[ REFERENTIAL ]

docs/architecture/PROJECT_CONTEXT.md

  Non-interference proof:
  NI-1 PASS — No structural rules for the master tree.
  NI-2 PASS — No naming or depth constraints defined.
  NI-3 PASS — No cohesion or assignment restrictions.
  NI-4 PASS — Defines no blocking condition for this process.

  Reason:
  Defines project purpose, objectives, and taxonomy evolution
  philosophy. Provides essential background for understanding
  the system but contains no enforceable validation rules.

--------------------------------------------------

docs/architecture/PROJECT_OPERATING_MODEL.md

  Non-interference proof:
  NI-1 PASS — Node types referenced here are fully covered
               by SYSTEM_CONTRACT.md (MANDATORY).
  NI-2 PASS — No independent naming or depth rules.
  NI-3 PASS — Latin strategy referenced here is fully covered
               by SYSTEM_CONTRACT.md and TAXONOMY_RULES.md.
  NI-4 PASS — No blocking condition beyond what MANDATORY
               documents already impose.

  Reason:
  Describes the operational model and activity separation.
  All validation-relevant content it contains (node types,
  Latin separation, immutability) is redundantly and more
  precisely defined in MANDATORY documents. Using this document
  as a rule source would create duplicate rules with the same
  content.

--------------------------------------------------

docs/architecture/SYSTEM_OVERVIEW.md

  Non-interference proof:
  NI-1 PASS — No independent structural rules defined.
  NI-2 PASS — No naming or depth constraints.
  NI-3 PASS — No cohesion or assignment constraints.
  NI-4 PASS — Only points to other documents; defines no
               blocking condition on its own.

  Reason:
  Pure high-level overview. Its sole function is to describe
  the system and reference the actual governance documents.
  No rules are derived from this document.

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

  Rules for the validation rule set must be derived
  exclusively from the 6 MANDATORY documents, plus the
  1 CONDITIONAL document when its scenario is active.

  The 3 REFERENTIAL documents must not be used as rule sources.

--------------------------------------------------
VALIDATION RULE SET
--------------------------------------------------

STATUS: PENDING DEFINITION

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

No rule may be invented outside the governance
document corpus.

--------------------------------------------------
AI PROMPT REQUIREMENTS
--------------------------------------------------

STATUS: PENDING DEFINITION

The AI prompt for Layer 2 must include:

  - Fixed rigid context block:
    system purpose, taxonomy-first principle,
    immutability rule, domain separation rules.

  - Applicable governance rules extracted and
    prioritized from the MANDATORY document set.

  - Severity classification schema:
    FATAL / WARNING / SUGGESTION.

  - Strict JSON output schema:
    rule_id, severity, node_path,
    evidence, recommendation, confidence.

  - Explicit prohibition on suggesting
    automatic changes.

The prompt must be deterministic in structure.
Variable content is limited to the taxonomy input.

--------------------------------------------------
OUTPUT AND QUALITY GATE
--------------------------------------------------

STATUS: PENDING DEFINITION

The process produces a single validation report.

Quality gate decision:

  PASS             — No violations found.

  PASS WITH WARNINGS — No fatal violations.
                       Non-fatal findings documented.

  FAIL             — One or more fatal violations.
                     Process blocked. Correction required.

Report must record:

  - Taxonomy version validated.
  - Date and time of execution.
  - Documents applied (from applicability matrix).
  - Layer 1 result and findings.
  - Layer 2 result and findings.
  - Final quality gate decision.
  - Hash or checksum of the validated file.

--------------------------------------------------
TRACEABILITY
--------------------------------------------------

The master taxonomy must never be modified automatically.

Every validation run must produce a traceable record.

Validation history allows:

  - Comparing quality evolution over time.
  - Detecting regressions after taxonomy changes.
  - Auditing which rules were applied and when.

--------------------------------------------------
IMPLEMENTATION NOTES
--------------------------------------------------

scripts/validate_tree.py

Currently a placeholder.

This file will implement Layer 1 when the rule set
is finalized and the applicability matrix is complete.

Implementation must not begin until the validation
rule set is finalized in this document.

--------------------------------------------------
REVISION HISTORY
--------------------------------------------------

v0.2 — 2026-03-15
  Governance documents applicability matrix completed.
  6 MANDATORY, 1 CONDITIONAL, 3 REFERENTIAL, 0 EXCLUDED.
  Non-interference proofs documented for all REFERENTIAL docs.
  Rule derivation scope formally bounded.
  Implementation gate updated: blocked until rule set is defined.

v0.1 — 2026-03-15
  Initial abstract strategy draft.
  Process approach defined: hybrid (script + AI).
  Governance rules established as LAW with fatal enforcement.
  Pending sections identified for next iterations.

--------------------------------------------------
END DOCUMENT
