# GLOBAL RULES
Music Genre Taxonomy System

--------------------------------------------------
PURPOSE
--------------------------------------------------

This document defines rules that apply to
multiple subsystems of the project.

These rules affect system components such as:

• taxonomy
• classifier
• alias mapping
• system validation
• playlist generation

Rules that apply to more than one component
must be placed here.

--------------------------------------------------
GLOBAL RULES
--------------------------------------------------

G001 — TAXONOMY AUTHORITY

The taxonomy defines the only valid genres
for the classification system.

All genres assigned to songs must exist
in the taxonomy.

--------------------------------------------------

G002 — NO GENRE INVENTION

The classifier must never invent genres.

All assigned genres must correspond to
existing taxonomy nodes.

--------------------------------------------------

G003 — MISSING GENRE FAILURE

If a required genre is missing from the
taxonomy, the system must produce a fatal error.

--------------------------------------------------

G004 — FATAL ERROR POLICY

Fatal errors must stop execution and
report the cause of the failure.

--------------------------------------------------

G005 — MULTI-GENRE CLASSIFICATION

A song may belong to multiple genres
when musically justified.

--------------------------------------------------

G006 — GENRE NORMALIZATION

Genre names must be normalized before
classification.

--------------------------------------------------

G007 — ALIAS RESOLUTION

Genre aliases must resolve to canonical
taxonomy genres.

--------------------------------------------------

G008 — TAXONOMY IMMUTABILITY

The system must never modify the taxonomy automatically.

--------------------------------------------------

G009 — TAXONOMY EDIT AUTHORITY

Only the project owner may edit the taxonomy template.

--------------------------------------------------

G010 — TAXONOMY VERSION CONSISTENCY

Template and operational taxonomy versions must always match.
If versions differ, the operational taxonomy must be regenerated.

--------------------------------------------------

G011 — PLAYLIST CONSISTENCY

Taxonomy, classification, and playlist structure must remain musically coherent.
Playlist structure must follow taxonomy hierarchy.

--------------------------------------------------

G012 — LATIN DOMAIN SEPARATION

Latin and non-Latin classification domains are independent.
Latin songs must use Latin-branch genres only.
Non-Latin songs must not use Latin-branch genres.

--------------------------------------------------

G013 — CANONICAL ASSIGNMENT POLICY

Songs must be assigned to canonical taxonomy nodes, not clone nodes.

--------------------------------------------------

G014 — PROPOSAL NON-AUTOMATION

The classifier may suggest genres but must not add them automatically.

--------------------------------------------------

G015 — STRUCTURE VS ASSIGNMENT SEPARATION

Genre assignments must be stored separately from taxonomy structure.

--------------------------------------------------

G016 — GENERATED TREE CONSTRAINTS

The generated tree must follow taxonomy structure and must not alter taxonomy data.

--------------------------------------------------

G017 — DATASET/TAXONOMY SEPARATION

Dataset state must not modify taxonomy automatically.

--------------------------------------------------

G018 — VERSIONED CLASSIFICATION TRACEABILITY

The system must version taxonomy/rules, and classification results must record the taxonomy version used.

--------------------------------------------------

G019 — RECLASSIFICATION ON CHANGE

Taxonomy changes may require reclassification of affected results.

--------------------------------------------------

G020 — REPOSITORY/DOCUMENTATION CONSISTENCY

Repository content must remain consistent with documentation and design principles.

--------------------------------------------------

---
RULE 019

Minor stylistic influence must not trigger genre assignment.

---

END OF FILE