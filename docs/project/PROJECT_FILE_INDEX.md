# PROJECT FILE INDEX
Music Genre Taxonomy System

--------------------------------------------------
1. PURPOSE
--------------------------------------------------

This document defines the role of every file in the
Music Genre Taxonomy System repository.

Its purpose is to:

• explain the repository structure  
• define where documentation belongs  
• prevent documentation drift  
• guide reconstruction and maintenance processes  

All project documentation must follow the structure
defined in this index.

--------------------------------------------------
2. REPOSITORY STRUCTURE
--------------------------------------------------

The repository is organized into several logical areas.

catalog/
data/
taxonomy/
scripts/
reports/
docs/

Each directory contains a specific type of data
or documentation.

--------------------------------------------------
3. CATALOG FILES
--------------------------------------------------

catalog/songs_raw.csv

Input catalog containing songs to classify.

Typical fields include:

title  
artist

--------------------------------------------------

catalog/songs_with_genres.csv

Output file produced by the classification system.

Stores the genres assigned to each song.

--------------------------------------------------
4. DATA FILES
--------------------------------------------------

data/genre_alias.csv

Alias mapping used to normalize genre names.

Allows the classifier to match alternate genre labels
to canonical taxonomy genres.

--------------------------------------------------
5. TAXONOMY FILES
--------------------------------------------------

taxonomy/genre_tree_master.md

Human-editable taxonomy template.

Defines the genre hierarchy using indentation.

Only the project owner modifies this file.

--------------------------------------------------

taxonomy/genre_tree_operational.csv

Machine-readable representation of the taxonomy.

Generated from the master taxonomy and used
by scripts and classification tools.

--------------------------------------------------

taxonomy/taxonomy_version.md

Stores the current taxonomy version.

Used to verify compatibility between:

• taxonomy structure  
• classification results  
• generated genre trees  

--------------------------------------------------
6. SCRIPT FILES
--------------------------------------------------

scripts/build_tree.py

Generates the dynamic listening tree
based on classified song data.

--------------------------------------------------

scripts/classify_songs.py

Performs song genre classification.

Reads:

catalog/songs_raw.csv

Writes:

catalog/songs_with_genres.csv

--------------------------------------------------

scripts/validate_tree.py

Validates taxonomy structure and checks
for structural issues.

--------------------------------------------------
7. REPORT FILES
--------------------------------------------------

reports/taxonomy_improvement_report.csv

Contains suggestions for improving the taxonomy.

--------------------------------------------------

reports/taxonomy_issues.csv

Stores detected taxonomy problems such as:

• ambiguous nodes  
• missing genres  
• classification conflicts  

--------------------------------------------------
8. DOCUMENTATION STRUCTURE
--------------------------------------------------

All documentation is organized under the docs directory.

docs/

system/  
taxonomy/  
project/  
maintenance/  
releases/

Each folder serves a specific documentation purpose.

--------------------------------------------------
9. SYSTEM DOCUMENTATION
--------------------------------------------------

docs/system/SYSTEM_OVERVIEW.md

High-level description of the system architecture.

--------------------------------------------------

docs/system/SYSTEM_CONTRACT.md

Defines mandatory rules governing system behavior.

--------------------------------------------------
10. TAXONOMY DOCUMENTATION
--------------------------------------------------

docs/taxonomy/TAXONOMY_RULES.md

Defines the structure and behavior of the taxonomy.

--------------------------------------------------

docs/taxonomy/TAXONOMY_CHANGE_POLICY.md

Defines the rules for modifying the taxonomy.

--------------------------------------------------

docs/taxonomy/TAXONOMY_DEPTH_POLICY.md

Defines rules governing taxonomy expansion.

--------------------------------------------------

docs/taxonomy/TAXONOMY_NAMING_CONVENTION.md

Defines naming conventions for genres.

--------------------------------------------------

docs/taxonomy/TAXONOMY_QUALITY_CHECKLIST.md

Checklist used to validate taxonomy quality.

--------------------------------------------------
11. PROJECT DOCUMENTATION
--------------------------------------------------

docs/project/PROJECT_CONTEXT.md

Describes the conceptual goals of the project.

--------------------------------------------------

docs/project/PROJECT_STATE.md

Stores the current operational state of the project.

--------------------------------------------------

docs/project/PROJECT_MEMORY.md

Stores design decisions and historical context.

--------------------------------------------------

docs/project/PROJECT_FILE_INDEX.md

Defines the documentation structure of the repository.

--------------------------------------------------
12. MAINTENANCE DOCUMENTATION
--------------------------------------------------

docs/maintenance/PROJECT_BOOTSTRAP.md

Defines how a new session should initialize
the project context.

--------------------------------------------------

docs/maintenance/REPOSITORY_RECONSTRUCTION_PROTOCOL.md

Defines the protocol used to reconstruct project
knowledge from the development conversation.

--------------------------------------------------

docs/maintenance/PROJECT_OPERATING_MODEL.md

Explains the operational model of the system and
the separation between taxonomy design,
song classification, and tree generation.

--------------------------------------------------

docs/maintenance/PROJECT_CHECKPOINT_001.md

Snapshot of the reconstructed project architecture.

--------------------------------------------------

docs/maintenance/PHASE1_FINAL_CHECKLIST.md

Checklist confirming Phase 1 completion.

--------------------------------------------------
13. RELEASE DOCUMENTATION
--------------------------------------------------

docs/releases/RELEASE_NOTES_v1.0.md

Release notes describing the first stable
version of the repository.

--------------------------------------------------
END DOCUMENT