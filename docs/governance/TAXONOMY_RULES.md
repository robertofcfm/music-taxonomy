# TAXONOMY RULES
Music Genre Taxonomy System

--------------------------------------------------
DOCUMENT METADATA
--------------------------------------------------

Scope:

Structural taxonomy rules used by validation,
classification, and playlist generation.

Owner:

Project Owner

Last Updated:

2026-03-15

--------------------------------------------------
PURPOSE
--------------------------------------------------

This document defines the structural rules governing the genre taxonomy.

The taxonomy represents the musical knowledge base of the system and is
used by the classifier and playlist generation pipeline.

--------------------------------------------------
1. TAXONOMY PURPOSE
--------------------------------------------------

The taxonomy defines the structure used to organize musical genres.

The taxonomy must remain human-editable.

Its purpose is to:

- represent relationships between genres
- guide song classification
- ensure playlist coherence

The taxonomy must prioritize musical coherence over completeness.

Genres must represent musically meaningful styles.
Generic or vague descriptors are not valid genre nodes.

--------------------------------------------------
2. ROOT STRUCTURE
--------------------------------------------------

The taxonomy must have a single root node.

Example:

Music

All genres must descend from this root.

--------------------------------------------------
3. HIERARCHY DEFINITION
--------------------------------------------------

Hierarchy is defined by indentation.

Example:

Music
  Rock
    Alternative Rock
      Indie Rock
      Grunge

Each indentation level represents a deeper specialization.

--------------------------------------------------
4. LEAF NODE RULE
--------------------------------------------------

Songs may only be classified into leaf nodes.

Leaf nodes are nodes that do not have children.

Example:

Music
  Rock
    Alternative Rock
      Indie Rock
      Grunge

Only:

- Indie Rock
- Grunge

are valid classification targets.

--------------------------------------------------
5. SIBLING GENRE RULE
--------------------------------------------------

Genres that share the same parent must represent
musically distinguishable styles.

Sibling genres must not be so similar that they
produce indistinguishable playlists.

If sibling genres cannot be clearly distinguished,
they should be merged.

--------------------------------------------------
6. PLAYLIST COHESION RULE
--------------------------------------------------

The taxonomy must prioritize playlist coherence.

If a node generates playlists that sound inconsistent,
the taxonomy must be adjusted.

Possible actions:

- merge sibling genres
- move nodes to a different parent
- split genres when necessary

--------------------------------------------------
7. NODE DEPTH POLICY
--------------------------------------------------

The taxonomy should maintain a moderate depth.

Typical depth:

3–5 levels.

Overly deep hierarchies should be avoided unless
they represent meaningful musical distinctions.

--------------------------------------------------
8. EXPANSION RULE
--------------------------------------------------

A node may be expanded when the number of songs
assigned to it exceeds the expansion threshold.

Expansion threshold:

45 songs.

When expansion occurs, the node becomes a parent
and its songs must be redistributed among subgenres.

--------------------------------------------------
9. GENERAL NODE POLICY
--------------------------------------------------

A node may contain a General subnode when
existing subgenres do not fully cover the parent genre.

General nodes act as explicit fallback nodes for songs
that do not fit known subgenres of that parent.

Example:

Hard Rock
  Glam Metal
  Arena Rock
  Hard Rock (General)

General nodes must:

- be explicitly defined
- never be auto-created by the system
- not replace proper genre creation
- be used only when necessary

--------------------------------------------------
10. ATOMIC GENRE RULE
--------------------------------------------------

Some genres should not be subdivided further.

These genres are considered atomic.

Atomic genres represent styles where further
subdivision would create artificial distinctions.

--------------------------------------------------
11. LATIN BRANCH STRUCTURE
--------------------------------------------------

Latin music exists in a dedicated branch.

Example:

Music
  Latin
    Latin Rock
    Latin Pop
    Regional Latin

Genres under Latin represent styles belonging
to Latin musical traditions.

Songs classified as Latin must use this branch.

--------------------------------------------------
12. GENRE NAMING RULE
--------------------------------------------------

Genre names must follow these rules:

- Title Case
- Clear musical meaning
- No abbreviations unless widely accepted

Avoid vague or descriptive labels.

Example of invalid names:

- Latin Style
- Misc Genres
- Mixed Music

--------------------------------------------------
13. TAXONOMY MODIFICATION POLICY
--------------------------------------------------

Taxonomy modifications must be made manually.

The system cannot automatically modify the taxonomy.

The system may only:

- suggest new nodes
- report inconsistencies
- propose structural improvements

All changes must be approved by the user.

--------------------------------------------------
14. TAXONOMY VALIDATION
--------------------------------------------------

Before a release the taxonomy must be validated.

Validation checks include:

- sibling genre similarity
- redundant nodes
- overly deep hierarchies
- playlist cohesion problems

--------------------------------------------------
15. SOURCE AND OPERATIONAL REPRESENTATION
--------------------------------------------------

The authoritative editable taxonomy source is:

taxonomy/genre_tree_master.md

The master taxonomy must stay directly editable by users.

The operational taxonomy must be generated from
the master taxonomy template.

The operational representation must be machine-readable
and must include numeric node codes.

The playlist tree must be generated dynamically from
classified songs using this taxonomy.

--------------------------------------------------
16. CLONE AND HYBRID GENRE POLICY
--------------------------------------------------

The taxonomy supports clone nodes.

Clone node rules:

- a clone must reference one canonical node
- clone nodes must not have children
- clone nodes act as navigation portals
- clones exist to avoid structural duplication
- canonical nodes may have children

The taxonomy supports hybrid genres.

Hybrid genre rules:

- a hybrid may appear in multiple conceptual branches
- when represented in multiple branches, clone nodes
  should be used to point to the canonical node

--------------------------------------------------
END TAXONOMY RULES