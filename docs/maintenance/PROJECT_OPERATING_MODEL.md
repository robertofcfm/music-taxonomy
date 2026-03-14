# PROJECT OPERATING MODEL
Music Genre Taxonomy System

--------------------------------------------------
1. PURPOSE
--------------------------------------------------

This document defines the operational model of the
Music Genre Taxonomy System.

The project operates through three distinct activities.

Each activity manipulates a different type of data
and must follow specific rules.

Understanding this separation is critical for
maintaining the integrity of the system.

--------------------------------------------------
2. CORE PRINCIPLE
--------------------------------------------------

The system separates three concerns:

1. Taxonomy definition
2. Song genre identification
3. Dataset-driven genre tree generation

Each activity interacts with different files and
must not modify data belonging to another activity.

--------------------------------------------------
3. ACTIVITY 1 — TAXONOMY TEMPLATE MANAGEMENT
--------------------------------------------------

Purpose:

Define and maintain the master genre taxonomy.

The taxonomy acts as the authoritative genre
definition used by the entire system.

Key characteristics:

• manually maintained
• defines valid genre leaves
• defines hierarchical genre relationships
• contains no song data

Primary file:

taxonomy/genre_tree_master.md

This file contains the human-editable taxonomy
structure using indentation.

--------------------------------------------------

Operational representation:

taxonomy/genre_tree_operational.csv

This file is generated from the master taxonomy
and is used by scripts and classification tools.

--------------------------------------------------

Important rule:

The taxonomy template is never modified automatically.

Automation tools may only:

• validate
• analyze
• suggest improvements

Only the project owner modifies the master taxonomy.

--------------------------------------------------
4. ACTIVITY 2 — SONG GENRE IDENTIFICATION
--------------------------------------------------

Purpose:

Determine which genres a song belongs to.

This process analyzes songs and assigns genres
based on the taxonomy.

Input file:

catalog/songs_raw.csv

This file contains the list of songs to classify.

Output file:

catalog/songs_with_genres.csv

This file stores classification results.

--------------------------------------------------

Classification rules:

• Genres must exist in the taxonomy
• Genres must correspond to taxonomy leaf nodes
• Songs may belong to multiple genres
• Minor stylistic influences must not be considered

Example:

A song containing a brief rap section should not
be classified as Rap unless rap is structurally
part of the song.

--------------------------------------------------

Missing genre handling:

If a suitable genre cannot be found in the taxonomy,
the classification process must stop and report
a fatal error.

The taxonomy must then be expanded manually.

--------------------------------------------------
5. ACTIVITY 3 — DYNAMIC GENRE TREE GENERATION
--------------------------------------------------

Purpose:

Generate a listening tree based on the actual
music catalog.

This tree is derived from the taxonomy and the
classified song dataset.

The resulting structure can be used to generate
genre-based playlists.

--------------------------------------------------

Expansion rule:

A node becomes expandable when the number of songs
assigned to that node exceeds:

45 songs

When this happens:

• the node becomes a parent
• songs are redistributed into subgenres

This allows the tree to grow organically according
to the real catalog.

--------------------------------------------------
6. LATIN GENRE STRATEGY
--------------------------------------------------

Latin music is treated as a separate branch.

If a song is identified as Latin music,
its genres must be selected from the Latin subtree.

This prevents mixing Latin and non-Latin genre
contexts which often represent different musical
traditions.

--------------------------------------------------
7. SPECIAL NODE TYPES
--------------------------------------------------

The taxonomy supports several special node types.

NORMAL

Standard genre node.

CLONE

A node that references another canonical node.
Clone nodes act as navigation portals and
do not duplicate the subtree.

GENERAL

Fallback node used when a song belongs to a parent
genre but does not match any defined subgenre.

Example:

Hard Rock
  Glam Metal
  Arena Rock
  Hard Rock (General)

ATOMIC

A terminal genre that should not be subdivided
because it already represents a specific style.

--------------------------------------------------
8. VERSIONING
--------------------------------------------------

The taxonomy version is stored in:

taxonomy/taxonomy_version.md

Classification results store the taxonomy version
used during classification.

If the taxonomy structure changes,
previous classifications may become incompatible.

--------------------------------------------------
9. PROJECT NAVIGATION MODEL
--------------------------------------------------

The taxonomy also functions as a playlist navigation
structure.

Users should be able to move up or down the genre
hierarchy to find playlists matching a desired
musical mood.

Each node may correspond to a playlist.

--------------------------------------------------
END DOCUMENT