# RAW RULE EXTRACTION SNAPSHOT

Raw rules extracted from conversations. Not yet classified.

---
RULE 008

The classifier must load the taxonomy before classifying songs.

---
RULE 019

Minor stylistic influence must not trigger genre assignment.

---
RULE 022

The project has three phases: taxonomy design, song classification, and tree generation.

---
RULE 041

The system must detect missing genres during classification.

---
RULE 042

Missing genres must trigger a fatal error.

---
RULE 043

The system must log detailed error diagnostics.

---
RULE 044

The system must allow multiple genres per song.

---
RULE 045

The classifier must ignore trivial stylistic references.

---
RULE 057

The taxonomy must support dataset-driven expansion.

---
RULE 058

A node becomes expandable when song count exceeds a threshold.

---
RULE 059

The expansion threshold is approximately 45 songs.

---
RULE 060

After expansion, songs must be reevaluated for subgenres.

---
RULE 061

Only affected songs should be reevaluated.

---
RULE 062

Unaffected songs must not be reclassified unnecessarily.

---
RULE 067

The generated tree may activate nodes when songs appear.

---
RULE 068

Inactive nodes represent unused taxonomy branches.

---
RULE 071

The classifier must support batch processing.

---
RULE 072

Batch classification must support partial results.

---
RULE 073

Successful classifications must be appended to output.

---
RULE 074

Unclassified songs must remain queued.

---
RULE 075

Batch execution must stop when the error threshold is exceeded.

---
RULE 079

The repository must be reconstructable without conversation history.

---
RULE 080

Documentation must preserve design decisions.

---
RULE 081

The repository must include a reconstruction protocol.

---
RULE 082

The reconstruction protocol must read repository files.

---
RULE 083

If file content is not read, the iteration is invalid.

---
RULE 084

Misplaced rules must be moved to correct documents.

---
RULE 085

If a destination already contains a rule, do not duplicate it.

---
RULE 086

If a file changes, show the full file.

---
RULE 087

If a file needs no changes, mark it complete.

---
RULE 088

Completed files must not be processed again.

---
RULE 089

Modified files must return to the end of the queue.

---
RULE 090

Reconstruction progress must be reported.

---
DUPLICATE COLLAPSE NOTE

Former RULES 093â€“271 were semantic duplicates of RULE 092
(same text; only the context counter changed).

