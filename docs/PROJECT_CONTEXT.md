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

The system must prioritize musical coherence and
clear genre identity.

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

Defines the structure of musical genres.

Responsibilities:

• maintain the genre hierarchy  
• define valid leaf nodes for classification  
• ensure sibling genres are musically distinct  
• maintain playlist cohesion  

The taxonomy is manually controlled by the user.

The system may only suggest improvements.

--------------------------------------------------

SONG GENRE IDENTIFICATION (PHASE 2)

Determines which genres a song belongs to.

Responsibilities:

• analyze songs
• assign one or more genres
• ensure genre assignments follow system rules
• report missing genres if necessary

The classifier must follow strict genre validity rules.

--------------------------------------------------

DYNAMIC GENRE TREE GENERATION (PHASE 3)

Builds a dynamic tree of genres based on the songs
being processed.

Responsibilities:

• organize songs by genre
• expand nodes when thresholds are exceeded
• generate playlist structures
• maintain balanced hierarchy

This tree adapts to the dataset.

--------------------------------------------------
4. PLAYLIST NAVIGATION MODEL
--------------------------------------------------

The taxonomy is designed so that each node may
represent a playlist.

Users should be able to navigate:

• from broader genres to more specific ones
• from specific genres to broader moods

The taxonomy must maintain musical cohesion
at every level.

--------------------------------------------------
5. TAXONOMY DESIGN PRINCIPLES
--------------------------------------------------

The taxonomy follows these principles.

MUSICAL COHERENCE

Genres must produce coherent playlists.

GENRE CLARITY

Genres must represent clearly identifiable styles.

STRUCTURAL SIMPLICITY

The taxonomy should avoid unnecessary complexity.

EXPANDABILITY

New genres may be added when required.

--------------------------------------------------
6. USER CONTROL
--------------------------------------------------

The taxonomy is never modified automatically.

The system may:

• suggest new genres
• suggest merges
• suggest structural improvements

The final decision always belongs to the user.

--------------------------------------------------
7. PROJECT DATA FLOW
--------------------------------------------------

The typical workflow is:

1. Load the genre taxonomy
2. Load the song catalog
3. Classify songs into genres
4. Detect missing genres if required
5. Generate the dynamic genre tree
6. Produce playlists

--------------------------------------------------
8. VERSION MANAGEMENT
--------------------------------------------------

The project tracks versions of:

• taxonomy
• classifier rules
• classification outputs

Versioning ensures reproducibility and
detects incompatible changes.

--------------------------------------------------
END PROJECT CONTEXT