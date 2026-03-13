# PROJECT MEMORY
Music Genre Taxonomy System

--------------------------------------------------
1. PURPOSE
--------------------------------------------------

This document records the key design decisions of the project.

It exists to preserve the reasoning behind the system architecture,
taxonomy structure, and classification methodology.

The goal is to ensure that future work on the project remains
consistent with the original design philosophy.

--------------------------------------------------
2. PROJECT VISION
--------------------------------------------------

The system is designed to classify songs into meaningful musical
genres and organize them into a structured taxonomy.

The taxonomy is not only used for classification but also for
playlist navigation.

Users should be able to navigate the genre hierarchy to select
playlists that match a desired musical mood.

--------------------------------------------------
3. TAXONOMY-FIRST APPROACH
--------------------------------------------------

The project follows a taxonomy-first design.

This means:

• the taxonomy is designed before classification
• classification must follow the taxonomy
• the taxonomy defines valid genre targets

The classifier must never invent genres.

--------------------------------------------------
4. MANUAL TAXONOMY CONTROL
--------------------------------------------------

The taxonomy is controlled manually by the user.

The system must never modify the taxonomy automatically.

The system may only:

• suggest new genres
• suggest merges
• suggest relocations
• report inconsistencies

Final decisions always belong to the user.

--------------------------------------------------
5. PLAYLIST COHERENCE PRINCIPLE
--------------------------------------------------

The taxonomy is designed with playlist coherence in mind.

Genres must be structured so that each node produces
a coherent playlist.

If a genre produces inconsistent playlists,
the taxonomy should be revised.

--------------------------------------------------
6. GENRE ASSIGNMENT PHILOSOPHY
--------------------------------------------------

A genre should only be assigned to a song when the
song clearly belongs to that genre.

Minor stylistic influence must not count.

Example:

A song that contains a short rap section should
not automatically be classified as rap.

Genres must represent dominant musical identity.

--------------------------------------------------
7. MULTI-GENRE SUPPORT
--------------------------------------------------

Songs may belong to multiple genres.

If a song clearly contains characteristics of
multiple genres, all of them may be assigned.

There is no forced hierarchy between assigned genres.

--------------------------------------------------
8. LATIN BRANCH STRATEGY
--------------------------------------------------

Latin music is separated into its own branch.

The reason is that Latin styles often have
distinct musical characteristics even when they
share names with non-Latin genres.

Example:

Latin Rock vs Rock

This separation helps preserve playlist coherence.

--------------------------------------------------
9. GENERAL NODE STRATEGY
--------------------------------------------------

Some genres include fallback nodes.

Example:

Hard Rock (General)

These nodes exist to prevent forced classification
when a song belongs to the parent genre but not
to any defined subgenre.

--------------------------------------------------
10. DATASET-DRIVEN EVOLUTION
--------------------------------------------------

The taxonomy may evolve based on the dataset.

When many songs accumulate in a node, it may
become necessary to introduce subgenres.

The reference threshold used in the project is:

45 songs.

--------------------------------------------------
11. ATOMIC GENRE CONCEPT
--------------------------------------------------

Some genres should not be subdivided further.

These are called atomic genres.

Atomic genres represent styles that are already
specific enough.

Further subdivision would create artificial distinctions.

--------------------------------------------------
12. PROJECT PHASES
--------------------------------------------------

The project was designed in three phases.

Phase 1

Design the genre taxonomy.

Phase 2

Classify songs into genres.

Phase 3

Generate a dynamic genre tree based on the dataset.

--------------------------------------------------
13. DATA INTEGRITY PRINCIPLE
--------------------------------------------------

All project operations must rely on project files.

The system must not invent information.

If required data is missing, the system must report
the problem instead of making assumptions.

--------------------------------------------------
END PROJECT MEMORY