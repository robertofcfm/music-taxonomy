# PROJECT BOOTSTRAP
Music Genre Taxonomy System

--------------------------------------------------
1. PURPOSE
--------------------------------------------------

This document defines how to initialize the project
when starting a new working session.

The goal is to ensure that the system loads the
correct context and avoids inventing information.

The project relies on several documents that define
rules, taxonomy structure, and project architecture.

These documents must always be loaded before
performing any classification or taxonomy work.

--------------------------------------------------
2. REQUIRED DOCUMENTS
--------------------------------------------------

When starting a new session the following documents
must be loaded first.

Core system rules:

docs/SYSTEM_CONTRACT.md

Taxonomy structural rules:

docs/TAXONOMY_RULES.md

Project architecture and context:

docs/PROJECT_CONTEXT.md

Taxonomy governance policies:

docs/TAXONOMY_CHANGE_POLICY.md
docs/TAXONOMY_DEPTH_POLICY.md
docs/TAXONOMY_NAMING_CONVENTION.md
docs/TAXONOMY_QUALITY_CHECKLIST.md

These documents define the system behavior.

--------------------------------------------------
3. TAXONOMY FILES
--------------------------------------------------

The taxonomy itself is stored in:

taxonomy/genre_tree_master.md

This file represents the editable taxonomy.

A secondary operational representation may also exist:

taxonomy/genre_tree_operational.csv

The operational file is used by scripts
and classification tools.

--------------------------------------------------
4. PROJECT STATE DOCUMENTS
--------------------------------------------------

Additional project state documents may exist:

PROJECT_STATE.md
PROJECT_MEMORY.md
PROJECT_FILE_INDEX.md
PROJECT_CHECKPOINT_*.md

These files describe the current progress of the project
and may help restore context.

--------------------------------------------------
5. BOOTSTRAP PROCESS
--------------------------------------------------

When starting a new working session the following
steps must be executed.

Step 1

Load the SYSTEM_CONTRACT.

Step 2

Load all taxonomy governance documents.

Step 3

Load the project context.

Step 4

Load the current taxonomy structure.

Step 5

Verify taxonomy version.

Step 6

Confirm that all required files exist.

--------------------------------------------------
6. INFORMATION INTEGRITY RULE
--------------------------------------------------

The system must never assume information that has
not been loaded from the project files.

All decisions must rely on the content of the
project documents.

If required information is missing the system
must report the problem rather than invent
a solution.

--------------------------------------------------
7. SESSION RECOVERY
--------------------------------------------------

If a session is restarted or moved to a new environment
the bootstrap process must be repeated.

This ensures that the full system context is restored
before continuing work.

--------------------------------------------------
END PROJECT BOOTSTRAP