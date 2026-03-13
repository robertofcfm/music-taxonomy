# TAXONOMY DEPTH POLICY
Music Genre Taxonomy System

--------------------------------------------------
1. PURPOSE
--------------------------------------------------

This document defines how deep the genre taxonomy
is allowed to grow and how depth should be managed.

The goal is to maintain a structure that is:

• musically meaningful
• easy to navigate
• stable for classification
• suitable for playlist generation

--------------------------------------------------
2. MINIMUM STRUCTURAL DEPTH
--------------------------------------------------

The taxonomy should normally reach at least
three levels of depth.

Example:

Music
  Rock
    Alternative Rock
      Indie Rock

This allows classification to reach a level
of genre specificity that is useful for playlists.

--------------------------------------------------
3. RECOMMENDED DEPTH RANGE
--------------------------------------------------

The recommended taxonomy depth is:

3 to 5 levels.

This range usually allows enough specialization
without producing unnecessary complexity.

--------------------------------------------------
4. EXCESSIVE DEPTH
--------------------------------------------------

Very deep hierarchies should be avoided.

If a taxonomy branch becomes excessively deep,
it should be reviewed.

Possible corrective actions:

• merge subgenres
• simplify the hierarchy
• move nodes to a more appropriate parent

--------------------------------------------------
5. EXPANSION PRINCIPLE
--------------------------------------------------

Depth should grow only when musically justified.

A node should only be expanded when:

• enough songs exist to justify subdivision
• meaningful subgenres exist
• the subdivision improves playlist coherence

Artificial subdivisions must be avoided.

--------------------------------------------------
6. ATOMIC GENRE LIMIT
--------------------------------------------------

Some genres should not be subdivided further.

These genres are considered atomic.

Examples of conditions where a node becomes atomic:

• no widely recognized subgenres exist
• further subdivision would reduce playlist cohesion
• the genre already represents a specific style

Atomic nodes should be marked in the taxonomy.

--------------------------------------------------
7. GENERAL NODE INTERACTION
--------------------------------------------------

When a node is expanded, a General node may be used
to preserve songs that do not fit any subgenre.

Example:

Hard Rock
  Glam Metal
  Arena Rock
  Hard Rock (General)

This prevents forced classification into
incorrect subgenres.

--------------------------------------------------
8. DATASET-DRIVEN EXPANSION
--------------------------------------------------

Expansion may also be influenced by the dataset.

If many songs accumulate in a genre node,
subdivision may become necessary.

The system uses an expansion reference value:

45 songs.

This value indicates when a node may require
structural expansion.

--------------------------------------------------
9. BALANCE PRINCIPLE
--------------------------------------------------

The taxonomy should remain balanced.

Branches should not grow disproportionately deep
while other branches remain extremely shallow.

When imbalance appears, the taxonomy should
be reviewed.

--------------------------------------------------
END TAXONOMY DEPTH POLICY