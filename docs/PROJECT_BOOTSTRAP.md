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

The bootstrap process ensures that:

• taxonomy rules are loaded  
• taxonomy files are validated  
• project state is restored  
• classification operates with the correct version  

--------------------------------------------------
2. REQUIRED DOCUMENTS
--------------------------------------------------

When starting a new session the following documents
must be loaded before performing any work.

SYSTEM RULES

docs/SYSTEM_CONTRACT.md

TAXONOMY STRUCTURE RULES

docs/TAXONOMY_RULES.md

PROJECT CONTEXT

docs/PROJECT_CONTEXT.md

TAXONOMY GOVERNANCE

docs/TAXONOMY_CHANGE_POLICY.md  
docs/TAXONOMY_DEPTH_POLICY.md  
docs/TAXONOMY_NAMING_CONVENTION.md  
docs/TAXONOMY_QUALITY_CHECKLIST.md  

These documents define how the system must behave.

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

This version is used to guarantee compatibility between:

• taxonomy structure
• classification results
• generated trees

If the taxonomy structure changes:

previous classifications may become obsolete.

--------------------------------------------------
5. PROJECT STATE DOCUMENTS
--------------------------------------------------

The following documents store project progress:

docs/PROJECT_STATE.md  
docs/PROJECT_MEMORY.md  
docs/PROJECT_FILE_INDEX.md  
docs/PROJECT_CHECKPOINT_*.md  

They help restore context if the project is resumed
after a long period.

--------------------------------------------------
6. CLASSIFICATION INPUT FILES
--------------------------------------------------

Song catalogs are stored in:

catalog/songs_raw.csv

This file contains the raw list of songs.

After classification the output is written to:

catalog/songs_with_genres.csv

Only successfully classified songs are written.

--------------------------------------------------
7. CLASSIFICATION RULES
--------------------------------------------------

Classification must follow strict rules.

• Genres must exist in the taxonomy  
• Genres must correspond to leaf nodes  
• Songs may have multiple genres  
• Minor influences must be ignored  

Example:

If a song briefly contains rap elements
but is not structurally rap music,
it must NOT be classified as rap.

--------------------------------------------------
8. FATAL ERROR CONDITIONS
--------------------------------------------------

The system must stop execution when:

• a song cannot be assigned to any genre
• a required genre does not exist in the taxonomy
• taxonomy files are inconsistent
• required documents are missing

Fatal errors must include detailed diagnostic
information explaining the cause.

--------------------------------------------------
9. CLASSIFICATION BATCH PROCESS
--------------------------------------------------

Song classification operates in batches.

Maximum batch size:

100 songs

However during system tuning a special mode is used.

TEST MODE

Batch size:

5 songs

This mode prints extremely detailed output to detect
classification problems.

--------------------------------------------------
10. DATA LOADING RULE
--------------------------------------------------

Before each batch the system must reload:

• taxonomy files  
• taxonomy rules  
• alias definitions  

This ensures the classifier does not rely on memory
or invent information.

--------------------------------------------------
11. ALIAS NORMALIZATION
--------------------------------------------------

Alias mappings are stored in:

data/genre_alias.csv

This file maps alternative genre names to
canonical taxonomy names.

Example:

alt rock → Alternative Rock  
synthpop → Synth Pop  

--------------------------------------------------
12. MASTER PRINCIPLE
--------------------------------------------------

The classifier must never invent genres.

All genre assignments must come from:

taxonomy/genre_tree_operational.csv

If a suitable genre cannot be found
the system must raise a fatal error
and request taxonomy expansion.

--------------------------------------------------
13. BOOTSTRAP COMPLETION
--------------------------------------------------

Bootstrap is complete when:

• system rules are loaded  
• taxonomy files are validated  
• project state documents are loaded  
• taxonomy version compatibility is confirmed  

After bootstrap the system may begin
taxonomy maintenance or song classification.