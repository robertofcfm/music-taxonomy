# TAXONOMY RULES
Music Genre Taxonomy System

--------------------------------------------------
METADATOS DEL DOCUMENTO
--------------------------------------------------

Alcance:

Structural taxonomía reglas used by validación,
clasificación, and playlist generation.

Responsable:

Propietario del proyecto

Última actualización:

2026-03-15

--------------------------------------------------
PROPÓSITO
--------------------------------------------------

Este documento define the structural reglas governing the genre taxonomía.

The taxonomía represents the musical knowledge base of the system and is
used by the classifier and playlist generation pipeline.

--------------------------------------------------
1. TAXONOMY PROPÓSITO
--------------------------------------------------

The taxonomía defines the structure used to organize musical genres.

The taxonomía debe remain human-editable.

Its purpose is to:

- represent relationships between genres
- guide song clasificación
- ensure playlist coherence

The taxonomía debe prioritize musical coherence over completeness.

Genres debe represent musically meaningful styles.
Generic or vague descriptors are not valid genre nodes.

--------------------------------------------------
2. ESTRUCTURA RAÍZ
--------------------------------------------------

The taxonomía debe have a nodo raíz único.

Example:

Music

All genres debe descend from this root.

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

Songs puede only be classified into leaf nodes.

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

are valid clasificación targets.

--------------------------------------------------
5. GÉNERO HERMANO RULE
--------------------------------------------------

Genres that share the same parent debe represent
musically distinguishable styles.

Sibling genres no debe be so similar that they
produce indistinguishable playlists.

If sibling genres cannot be clearly distinguished,
they should be merged.

--------------------------------------------------
6. COHESIÓN DE PLAYLIST RULE
--------------------------------------------------

The taxonomía debe prioritize playlist coherence.

If a node generates playlists that sound inconsistent,
the taxonomía debe be adjusted.

Possible actions:

- merge sibling genres
- move nodes to a different parent
- split genres when necessary

--------------------------------------------------
7. NODE DEPTH POLICY
--------------------------------------------------

The taxonomía should maintain a moderate depth.

Typical depth:

3–5 levels.

Overly deep hierarchies should be avoided unless
they represent meaningful musical distinctions.

--------------------------------------------------
8. EXPANSION RULE
--------------------------------------------------

A node puede be expanded when the number of songs
assigned to it exceeds the expansion threshold.

Expansion threshold:

45 songs.

When expansion occurs, the node becomes a parent
and its songs debe be redistributed among subgenres.

--------------------------------------------------
9. NODO GENERAL POLICY
--------------------------------------------------

A node puede contain a General subnode when
existing subgenres do not fully cover the parent genre.

General nodes act as explicit fallback nodes for songs
that do not fit known subgenres of that parent.

Example:

Hard Rock
  Glam Metal
  Arena Rock
  Hard Rock (General)

General nodes debe:

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
11. RAMA LATIN STRUCTURE
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

Songs classified as Latin debe use this branch.

--------------------------------------------------
12. GENRE NAMING RULE
--------------------------------------------------

Genre names debe follow these reglas:

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

Taxonomy modifications debe be made manually.

El sistema cannot automatically modify the taxonomía.

El sistema puede only:

- suggest new nodes
- report inconsistencies
- propose structural improvements

All changes debe be approved by the user.

--------------------------------------------------
14. VALIDACIÓN DE TAXONOMÍA
--------------------------------------------------

Antes de un release the taxonomía debe ser validada.

Validation checks include:

- sibling genre similarity
- redundant nodes
- overly deep hierarchies
- playlist cohesion problems

--------------------------------------------------
15. SOURCE AND OPERATIONAL REPRESENTATION
--------------------------------------------------

The authoritative editable taxonomía source is:

taxonomy/genre_tree_master.md

The master taxonomía debe stay directly editable by users.

The operational taxonomía debe be generated from
the master taxonomía template.

The operational representation debe be machine-readable
and debe include numeric node codes.

The playlist tree debe be generated dynamically from
classified songs using this taxonomía.

--------------------------------------------------
16. CLONE AND HYBRID GENRE POLICY
--------------------------------------------------

The taxonomía supports clone nodes.

Clone node reglas:

- a clone debe reference one canonical node
- clone nodes no debe have children
- clone nodes act as navigation portals
- clones exist to avoid structural duplication
- canonical nodes puede have children

The taxonomía supports hybrid genres.

Hybrid genre reglas:

- a hybrid puede appear in multiple conceptual branches
- when represented in multiple branches, clone nodes
  should be used to point to the canonical node

--------------------------------------------------
END TAXONOMY RULES

