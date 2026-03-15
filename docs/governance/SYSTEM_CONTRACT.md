# SYSTEM CONTRACT
Music Genre Taxonomy System

This document defines the mandatory rules governing the system.

These rules cannot be violated by any component of the project.

--------------------------------------------------
1. TAXONOMY GOVERNANCE
--------------------------------------------------

The taxonomy is controlled manually by the user.

The system must never:

- add genres
- move genres
- merge genres
- rename genres

The system may only:

- suggest improvements
- report inconsistencies

All structural modifications must be approved by the user.

--------------------------------------------------
2. TAXONOMY STRUCTURE
--------------------------------------------------

The taxonomy must follow these rules:

- Single root node
- Hierarchy defined by indentation
- Only leaf nodes may receive song assignments

Genres must represent real musical styles.

Genres must never be vague categories such as:

- "Latin rhythms"
- "Latin music"
- "World music"
- "Misc"

Leaf nodes must represent specific musical genres.

--------------------------------------------------
3. NODE TYPES
--------------------------------------------------

The system supports four node types.

NORMAL NODE

Standard taxonomy node.

CLONE NODE

A portal node referencing a canonical node.

Clone nodes:

- have no children
- contain no songs
- act only as navigation portals

GENERAL NODE

Fallback node used when songs fit the parent genre
but not any existing subgenre.

Example:

Hard Rock
  Glam Metal
  Arena Rock
  Hard Rock (General)

Rules for General nodes:

- they must be explicitly defined in the taxonomy
- the classifier must try other genres before using them
- they must not be abused as a default category

ATOMIC NODE

A genre that must not be subdivided further.

Atomic nodes represent genres where further subdivision
would create artificial or meaningless categories.

--------------------------------------------------
4. LATIN BRANCH RULE
--------------------------------------------------

Latin music exists inside a dedicated Latin branch.

If a song is Latin:

Genres must be selected only within the Latin branch.

If a song is not Latin:

Genres must not be selected within the Latin branch.

This rule prevents mixing Latin and non-Latin styles
that share the same genre name but produce different
playlist cohesion.

--------------------------------------------------
5. GENRE ASSIGNMENT RULE
--------------------------------------------------

A genre may be assigned only when its defining musical
characteristics are clearly present in the song.

Minor stylistic influence must not count.

Example:

A song with a short rap section must not be classified as rap.

Songs may have multiple genres if the defining characteristics
of each genre are clearly present.

There is no hierarchy or priority between genres.

If a song clearly belongs to multiple genres,
all of them must be assigned.

--------------------------------------------------
6. GENRE VALIDITY RULE
--------------------------------------------------

Genres must represent real musical styles.

The classifier must avoid vague labels such as:

- latin rhythms
- latin style
- latin music
- fusion style

Leaf nodes must correspond to clearly recognized genres.

--------------------------------------------------
7. CLASSIFICATION PIPELINE
--------------------------------------------------

The classifier must load the taxonomy before classifying songs.

Two execution modes exist.

TEST MODE

Batch size: 5 songs.

Purpose:

- debugging
- classifier validation
- rule verification

Logs must be highly detailed.

PRODUCTION MODE

Batch size: 100 songs.

Logs must confirm:

- taxonomy was loaded
- system rules were loaded
- classifier version

Batch processing is mandatory.

Batch continuity rules:

- batch classification must support partial results
- successful classifications must be appended to output
- unclassified songs must remain queued
- batch execution must stop when the error threshold is exceeded

--------------------------------------------------
8. NODE MISSING RULE
--------------------------------------------------

If a song requires a genre that does not exist
in the taxonomy, the system must stop classification.

The system must generate a report suggesting
a new genre node.

Batch rule:

A batch may generate a maximum of 5 missing-node reports.

If more than 5 appear, the execution must stop.

--------------------------------------------------
9. ERROR HANDLING
--------------------------------------------------

Fatal errors stop processing immediately.

Examples:

- genre missing from taxonomy
- ambiguous classification
- invalid taxonomy node
- invalid taxonomy structure

Error reports must contain:

- song title
- artist
- description of the problem
- suggested solution

Error diagnostics must be detailed enough to support
root-cause analysis and corrective action.

--------------------------------------------------
10. TAXONOMY VALIDATION
--------------------------------------------------

Before every release the taxonomy must be validated.

Validation must detect:

- sibling genre similarity
- playlist cohesion violations
- redundant nodes
- atomic node candidates
- possible merges

A release cannot proceed until validation issues
are resolved.

--------------------------------------------------
11. VERSION CONTROL
--------------------------------------------------

Taxonomy versions must be tracked.

Example:

taxonomy_version = 1.0

Classification outputs must include:

- taxonomy_version
- classifier_version
- rules_version

This allows resuming classification or detecting
incompatibilities.

--------------------------------------------------
12. COMPATIBILITY RULE
--------------------------------------------------

If the taxonomy changes in a way that breaks compatibility,
previous classification outputs become obsolete.

In that case:

All songs must be reclassified.

If the taxonomy changes without breaking compatibility:

- only affected songs should be reevaluated
- unaffected songs must not be reclassified unnecessarily

--------------------------------------------------
END SYSTEM CONTRACT