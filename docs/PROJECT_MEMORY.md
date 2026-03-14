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
4. DESIGN PRINCIPLE: PLAYLIST NAVIGATION
--------------------------------------------------

The taxonomy is intended not only as a classification system,
but also as a navigation structure for music listening.

Users should be able to move up or down the taxonomy tree
to find playlists that match a desired musical mood.

--------------------------------------------------
5. DESIGN PRINCIPLE: DATASET-AWARE EVOLUTION
--------------------------------------------------

The taxonomy may evolve as the dataset grows.

As the catalog expands, certain genres may accumulate
enough songs to justify further subdivision.

The taxonomy design must remain flexible enough to
accommodate this evolution while preserving musical coherence.

--------------------------------------------------
END PROJECT MEMORY