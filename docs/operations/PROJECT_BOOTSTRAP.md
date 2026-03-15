# PROJECT BOOTSTRAP
Music Genre Taxonomy System

--------------------------------------------------
1. PURPOSE
--------------------------------------------------

This document defines how to initialize the project
when starting a new working session.

Its goal is to guarantee that the system loads
the correct project context and avoids inventing
information or operating with outdated taxonomy data.

--------------------------------------------------
2. REQUIRED DOCUMENTS
--------------------------------------------------

When starting a new session the following documents
must be loaded before performing any work.

SYSTEM RULES

docs/governance/SYSTEM_CONTRACT.md

TAXONOMY STRUCTURE RULES

docs/governance/TAXONOMY_RULES.md

PROJECT CONTEXT

docs/architecture/PROJECT_CONTEXT.md

TAXONOMY GOVERNANCE

docs/governance/TAXONOMY_CHANGE_POLICY.md
docs/governance/TAXONOMY_DEPTH_POLICY.md
docs/governance/TAXONOMY_NAMING_CONVENTION.md
docs/governance/TAXONOMY_QUALITY_CHECKLIST.md

--------------------------------------------------
3. TAXONOMY FILES
--------------------------------------------------

The editable taxonomy is stored in:

taxonomy/genre_tree_master.md

This file defines the genre hierarchy using indentation.

The operational representation used by scripts is:

taxonomy/genre_tree_operational.csv

Rules:

• The operational tree must always match the master tree  
• If versions do not match the operational file must be regenerated  

--------------------------------------------------
4. TAXONOMY VERSION CONTROL
--------------------------------------------------

Taxonomy version information is stored in:

taxonomy/taxonomy_version.md

This version guarantees compatibility between:

• taxonomy structure  
• classification results  
• generated trees  

--------------------------------------------------
5. PROJECT STATE DOCUMENTS
--------------------------------------------------

The following documents store project progress:

docs/project-management/PROJECT_STATE.md  
docs/project-management/PROJECT_MEMORY.md  
docs/project-management/PROJECT_FILE_INDEX.md  
docs/project-management/PROJECT_CHECKPOINT_*.md  

They help restore context if the project is resumed
after a long period.

--------------------------------------------------
6. CLASSIFICATION INPUT FILES
--------------------------------------------------

Song catalogs are stored in:

catalog/songs_raw.csv

After classification the output is written to:

catalog/songs_with_genres.csv

Only successfully classified songs are written.

--------------------------------------------------
END PROJECT BOOTSTRAP