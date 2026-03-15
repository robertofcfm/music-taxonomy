# SYSTEM OVERVIEW
Music Genre Taxonomy System

--------------------------------------------------
1. PURPOSE
--------------------------------------------------

This document provides a high-level overview of the
Music Genre Taxonomy System.

It explains how the main components of the project
interact and how the taxonomy, classifier, and
playlist generation pipeline operate together.

--------------------------------------------------
2. SYSTEM GOALS
--------------------------------------------------

The system has three main goals:

• classify songs into meaningful musical genres  
• maintain a coherent genre taxonomy  
• generate navigable genre-based playlists  

The taxonomy acts as the central knowledge structure
for the entire system.

--------------------------------------------------
3. CORE COMPONENTS
--------------------------------------------------

The project contains three main subsystems.

1. TAXONOMY DESIGN

The taxonomy defines the hierarchical structure of
musical genres.

It is manually maintained by the user.

Files involved:

taxonomy/genre_tree_master.md  
taxonomy/genre_tree_operational.csv  

--------------------------------------------------

2. SONG CLASSIFICATION

The classifier assigns genres to songs using the
taxonomy.

Input:

catalog/songs_raw.csv

Output:

catalog/songs_with_genres.csv

Classification follows strict rules defined in:

docs/governance/SYSTEM_CONTRACT.md

--------------------------------------------------

3. TREE GENERATION

After songs are classified, a dynamic genre tree
may be generated based on the dataset.

This process organizes songs into nodes that can
be used to generate playlists.

--------------------------------------------------
4. PROJECT PHASES
--------------------------------------------------

The project evolves through three phases.

PHASE 1

Taxonomy design and rule definition.

PHASE 2

Song classification using the taxonomy.

PHASE 3

Generation of the dataset-driven genre tree.

--------------------------------------------------
5. SYSTEM PRINCIPLES
--------------------------------------------------

The system follows several core principles.

• taxonomy-first design  
• manual taxonomy governance  
• playlist coherence  
• strict rule enforcement  
• dataset-aware taxonomy evolution  

--------------------------------------------------
6. SYSTEM DOCUMENTATION
--------------------------------------------------

Key documents that govern the system:

docs/governance/SYSTEM_CONTRACT.md  
docs/governance/TAXONOMY_RULES.md  
docs/governance/TAXONOMY_CHANGE_POLICY.md  
docs/governance/TAXONOMY_DEPTH_POLICY.md  
docs/governance/TAXONOMY_NAMING_CONVENTION.md  

These documents define the behavior and structure
of the system.

--------------------------------------------------
END SYSTEM OVERVIEW