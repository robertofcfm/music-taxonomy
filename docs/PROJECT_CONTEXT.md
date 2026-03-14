# PROJECT CONTEXT
Music Genre Taxonomy System

--------------------------------------------------
1. PROJECT PURPOSE
--------------------------------------------------

This project builds a structured music genre taxonomy
and a classification system capable of assigning
accurate genres to songs.

The taxonomy is designed not only for classification
but also to generate coherent playlists based on
genre hierarchy.

The system must prioritize:

• musical coherence  
• clear genre identity  
• meaningful genre hierarchy  

The final goal is to allow navigation through genres
in a way that produces musically consistent playlists.

--------------------------------------------------
2. CORE OBJECTIVE
--------------------------------------------------

The objective of the project is to create a system that:

• classifies songs into precise musical genres  
• maintains a structured genre taxonomy  
• generates genre-based playlists with musical coherence  
• evolves the taxonomy when new genres are discovered  

The taxonomy represents the musical knowledge base
used by the system.

--------------------------------------------------
3. SYSTEM COMPONENTS
--------------------------------------------------

The system consists of three major components.

--------------------------------------------------
GENRE TAXONOMY (PHASE 1)
--------------------------------------------------

Defines the structure of musical genres.

Responsibilities:

• maintain the genre hierarchy  
• define valid leaf nodes for classification  
• ensure sibling genres are musically distinct  
• maintain playlist coherence  

The taxonomy is manually controlled by the project owner.

The system may only:

• analyze  
• validate  
• suggest improvements  

Automatic modification of the taxonomy is NOT allowed.

--------------------------------------------------
SONG GENRE IDENTIFICATION (PHASE 2)
--------------------------------------------------

Determines which genres a song belongs to.

Responsibilities:

• analyze songs  
• assign one or more genres  
• ensure assignments follow taxonomy rules  
• detect missing genres  

Rules:

A genre must only be assigned when the song truly
belongs to that genre.

Minor influences must NOT be considered.

Example:

If a song briefly includes rap elements but is not
structurally rap music, it must NOT be classified as rap.

Songs may belong to multiple genres when musically valid.

--------------------------------------------------
DYNAMIC GENRE TREE GENERATION (PHASE 3)
--------------------------------------------------

Builds a listening tree based on real catalog content.

Rule:

A genre node becomes expandable when it contains:

45 songs

When this happens:

• the node becomes a parent  
• songs are redistributed into subgenres  

This allows the tree to evolve organically based on
the real music catalog.

--------------------------------------------------
4. LATIN MUSIC STRATEGY
--------------------------------------------------

Latin music is handled as a separate branch.

When a song is identified as Latin:

its genres must be selected exclusively from the
Latin subtree.

This prevents mixing Latin and non-Latin genre contexts
that often have different musical characteristics.

Example:

Latin
  Regional Mexicano
  Cumbia
  Vallenato

--------------------------------------------------
5. SPECIAL NODE TYPES
--------------------------------------------------

The system supports special taxonomy nodes.

NORMAL

Standard genre node.

CLONE

A clone node references another canonical node.
It allows the same genre to appear in multiple
locations without duplicating the subtree.

Clone nodes:

• cannot have children  
• act as navigation portals  
• share the songs of the canonical node  

GENERAL

Fallback node used when a song belongs to a parent
genre but not to any defined subgenre.

Example:

Hard Rock
  Glam Metal
  Arena Rock
  Hard Rock (General)

ATOMIC

A terminal node that should not be expanded further
because the genre is already specific enough.

--------------------------------------------------
6. TAXONOMY EXPANSION
--------------------------------------------------

The taxonomy may evolve when new genres are discovered.

Expansion occurs when:

• a song cannot be assigned to an existing genre

The system must report this situation as a **fatal error**
and propose the missing genre.

Only the project owner decides whether to add it.

--------------------------------------------------
7. FATAL ERROR CONDITIONS
--------------------------------------------------

The system must stop execution when:

• a song cannot be assigned to any genre  
• a required genre does not exist in the taxonomy  
• taxonomy files are inconsistent  
• required system documents are missing  

Fatal errors must include detailed diagnostics.

--------------------------------------------------
8. TAXONOMY TEMPLATE PRINCIPLE
--------------------------------------------------

The taxonomy template is stored in:

taxonomy/genre_tree_master.md

This file contains the editable genre hierarchy.

It uses indentation to define the tree structure.

Numeric codes are generated automatically
in the operational representation.

The template must never contain codes.

--------------------------------------------------
9. OPERATIONAL TAXONOMY
--------------------------------------------------

The operational taxonomy used by scripts is stored in:

taxonomy/genre_tree_operational.csv

This file contains:

• genre codes  
• parent relationships  
• node type  
• canonical references  

It is generated from the master taxonomy.

--------------------------------------------------
10. PROJECT PHILOSOPHY
--------------------------------------------------

The system prioritizes musical clarity over automation.

Key principle:

The taxonomy represents musical knowledge
and must remain human-controlled.

Automation may help analyze and classify music,
but the taxonomy itself must remain curated.