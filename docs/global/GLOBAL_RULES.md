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

RULE G001

The taxonomy defines the only valid genres
for classification.

--------------------------------------------------

RULE G002

The classifier must never invent genres.

--------------------------------------------------

RULE G003

If a required genre is missing the system
must produce a fatal error.

--------------------------------------------------

RULE G004

Fatal errors must stop the process and
report the cause.

--------------------------------------------------

RULE G005

A song may belong to multiple genres
if justified musically.

--------------------------------------------------

RULE G006

The classifier must normalize genre names.

--------------------------------------------------

RULE G007

Genre aliases must map to canonical
taxonomy genres.

--------------------------------------------------
END OF FILE