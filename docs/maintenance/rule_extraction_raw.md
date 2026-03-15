# RAW RULE EXTRACTION SNAPSHOT

Rules extracted from the conversation. They are intentionally not classified or deduplicated.


---
RULE 001

The taxonomy must never be modified automatically by the system.

---
RULE 002

Only the project owner may modify the taxonomy template.

---
RULE 003

The taxonomy template (genre_tree_master.md) is the authoritative editable source.

---
RULE 004

The operational taxonomy must be generated from the template.

---
RULE 005

The operational taxonomy must contain numeric node codes.

---
RULE 006

The template version and operational version must always match.

---
RULE 007

If taxonomy versions do not match the operational file must be regenerated.

---
RULE 008

The classifier must read the taxonomy before classification.

---
RULE 013

The taxonomy must be hierarchical.

---
RULE 014

Sibling genres must be musically distinguishable.

---
RULE 015

Genres must produce coherent playlists.

---
RULE 016

The taxonomy must prioritize musical coherence.

---
RULE 017

Genres must represent musical styles rather than vague descriptors.

---
RULE 019

Minor stylistic influence must not trigger genre assignment.

---
RULE 020

The taxonomy must guide playlist generation.

---
RULE 021

Playlist structure must follow the taxonomy hierarchy.

---
RULE 022

The project has three phases: taxonomy design, song classification, tree generation.

---
RULE 023

The taxonomy must be human editable.

---
RULE 024

The operational tree must be machine readable.

---
RULE 027

The system must support Latin music separation logic.

---
RULE 028

Latin songs must only use genres within the Latin branch.

---
RULE 029

Non‑Latin songs must not use genres from the Latin branch.

---
RULE 030

The Latin branch acts as an independent classification universe.

---
RULE 031

The taxonomy must support genre clones.

---
RULE 032

A clone node references a canonical node elsewhere in the tree.

---
RULE 033

Clone nodes must not have children.

---
RULE 034

Clone nodes must behave as portals to canonical nodes.

---
RULE 035

Songs belong to the canonical node, not the clone node.

---
RULE 036

Clone nodes allow navigation but do not duplicate structure.

---
RULE 037

Canonical nodes may have children.

---
RULE 038

The system must allow hybrid genres.

---
RULE 039

Hybrid genres may appear in multiple conceptual branches.

---
RULE 040

When hybrid genres appear in multiple branches clones may be used.

---
RULE 041

The system must detect missing genres during classification.

---
RULE 042

Missing genre detection must trigger a fatal error.

---
RULE 043

The system must record detailed error diagnostics.

---
RULE 044

The system must support multiple genre assignment per song.

---
RULE 045

The classifier must ignore trivial stylistic references.

---
RULE 046

Genres must be musically meaningful.

---
RULE 047

Generic labels must not be used as genres.

---
RULE 048

The taxonomy must evolve through controlled changes.

---
RULE 049

Taxonomy changes must be deliberate and documented.

---
RULE 050

The taxonomy owner evaluates new genre proposals.

---
RULE 051

The classifier may suggest new genres but never add them automatically.

---
RULE 052

The taxonomy may include general fallback nodes.

---
RULE 053

A fallback node represents songs that do not match existing subgenres.

---
RULE 054

Fallback nodes must be explicitly defined in the taxonomy.

---
RULE 055

Fallback nodes must not be automatically created.

---
RULE 056

Fallback nodes must be used as last resort classification.

---
RULE 057

The taxonomy must support expansion based on dataset size.

---
RULE 058

A node becomes expandable when song count exceeds threshold.

---
RULE 059

The expansion threshold was defined as approximately 45 songs.

---
RULE 060

When expansion occurs songs must be reevaluated for subgenres.

---
RULE 061

Only affected songs should be reevaluated.

---
RULE 062

The system must not unnecessarily reclassify unaffected songs.

---
RULE 063

The system must store genre assignments separately from tree structure.

---
RULE 064

The playlist tree must be generated dynamically from classified songs.

---
RULE 065

The generated tree must follow the taxonomy structure.

---
RULE 066

The generated tree must not modify the taxonomy.

---
RULE 067

The generated tree may activate nodes as songs appear.

---
RULE 068

Inactive nodes represent unused taxonomy branches.

---
RULE 069

The project must maintain separation between taxonomy and dataset.

---
RULE 070

The dataset must not modify taxonomy automatically.

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

Unclassified songs must remain in the queue.

---
RULE 075

Batch execution must stop if too many errors occur.

---
RULE 076

The system must maintain versioning of taxonomy and rules.

---
RULE 077

Classification results must record the taxonomy version used.

---
RULE 078

If taxonomy changes results may require reclassification.

---
RULE 079

The repository must be reconstructable without the conversation.

---
RULE 080

Documentation must preserve design decisions.

---
RULE 081

The repository must include a reconstruction protocol.

---
RULE 082

The reconstruction protocol must read files from the repository.

---
RULE 083

If file content is not read the iteration is invalid.

---
RULE 084

Misplaced rules must be moved to their correct documents.

---
RULE 085

If destination already contains the rule duplication must not occur.

---
RULE 086

If a file is modified the full file must be shown.

---
RULE 087

If a file requires no modification it must be marked complete.

---
RULE 088

Completed files must not be processed again.

---
RULE 089

Modified files return to the end of the processing queue.

---
RULE 090

Reconstruction progress must be reported.

---
RULE 091

The repository must remain consistent with its documentation.

---
RULE 092

Extracted rule candidate (deduplicated canonical form):
System behavior must remain consistent with taxonomy, classification, and playlist design principles.

---
DUPLICATE COLLAPSE NOTE

Former RULES 093–271 were semantic duplicates of RULE 092
(same rule text; only conversation context counter changed).
