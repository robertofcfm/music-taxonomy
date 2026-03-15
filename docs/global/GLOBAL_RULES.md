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
END OF FILE