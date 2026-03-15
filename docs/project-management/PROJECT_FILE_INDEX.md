# PROJECT FILE INDEX
Music Genre Taxonomy System

--------------------------------------------------
1. PROPÓSITO
--------------------------------------------------

Este documento define the role of every file in the
Music Genre Taxonomy System repository.

Its purpose is to:

• explain the repository structure  
• define where documentation belongs  
• prevent documentation drift  
• guide reconstruction and maintenance processes  

All project documentation debe follow the structure
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

Output file produced by the clasificación system.

Stores the genres assigned to each song.

--------------------------------------------------
4. DATA FILES
--------------------------------------------------

data/genre_alias.csv

Alias mapping used to normalize genre names.

Allows the classifier to match alternate genre labels
to canonical taxonomía genres.

--------------------------------------------------
5. TAXONOMY FILES
--------------------------------------------------

taxonomy/genre_tree_master.md

Human-editable taxonomía template.

Defines the genre hierarchy using indentation.

Only the project owner modifies this file.

--------------------------------------------------

taxonomy/genre_tree_operational.csv

Machine-readable representation of the taxonomía.

Generated from the master taxonomía and used
by scripts and clasificación tools.

--------------------------------------------------

taxonomy/taxonomy_version.md

Stores the current taxonomía version.

Used to verify compatibility between:

• taxonomía structure  
• clasificación results  
• generated genre trees  

--------------------------------------------------
6. SCRIPT FILES
--------------------------------------------------

scripts/build_tree.py

Generates the dynamic listening tree
based on classified song data.

--------------------------------------------------

scripts/classify_songs.py

Performs song genre clasificación.

Reads:

catalog/songs_raw.csv

Writes:

catalog/songs_with_genres.csv

--------------------------------------------------

scripts/validate_tree.py

Validates taxonomía structure and checks
for structural issues.

--------------------------------------------------
7. REPORT FILES
--------------------------------------------------

reports/taxonomía_improvement_report.csv

Contains suggestions for improving the taxonomía.

--------------------------------------------------

reports/taxonomía_issues.csv

Stores detected taxonomía problems such as:

• ambiguous nodes  
• missing genres  
• clasificación conflicts  

--------------------------------------------------
8. DOCUMENTATION STRUCTURE
--------------------------------------------------

All documentation is organized under the docs directory.

docs/

gobernanza/  
architecture/  
operations/  
project-management/  
releases/

Documentation is grouped by function.

Each folder serves a specific operational purpose.

Governance and operations documents use a common
header template with:

• Purpose  
• Scope  
• Owner  
• Last Updated  

--------------------------------------------------
9. GLOBAL GOVERNANCE DOCUMENTATION
--------------------------------------------------

docs/governance/GLOBAL_RULES.md

Defines system-wide reglas that apply to multiple
components of the repository.

This file acts as the canonical location for reglas
that affect more than one subsystem.

Examples include reglas that affect:

• taxonomía behavior  
• clasificación logic  
• validación procedures  
• repository constraints  

--------------------------------------------------

RULE PLACEMENT PRINCIPLE

If a rule applies to only one file or subsystem,
it should be placed in that specific file.

If a rule applies to multiple files or subsystems,
it debe be placed in:

docs/governance/GLOBAL_RULES.md

Other documents puede reference the rule but should
not duplicate it.

--------------------------------------------------

RULE LOADING PRINCIPLE

Whenever repository reglas are evaluated
(for example during reconstruction or validación),
the following files debe always be loaded:

1. docs/governance/GLOBAL_RULES.md  
2. docs/governance/SYSTEM_CONTRACT.md  

GLOBAL_RULES.md contains canonical reglas.

SYSTEM_CONTRACT.md contains mandatory system reglas.

--------------------------------------------------

GLOBAL PRECEDENCE PRINCIPLE

docs/governance/GLOBAL_RULES.md is the canonical
cross-system rule source.

If a conflict exists between a local document
and GLOBAL_RULES.md for a cross-subsystem rule,
GLOBAL_RULES.md takes precedence.

Local files puede specialize implementation details
but no debe contradict global reglas.

--------------------------------------------------
10. ARCHITECTURE DOCUMENTATION
--------------------------------------------------

docs/architecture/SYSTEM_OVERVIEW.md

High-level description of the system architecture.

--------------------------------------------------

docs/architecture/PROJECT_CONTEXT.md

Describes conceptual goals and system context.

--------------------------------------------------

docs/architecture/PROJECT_OPERATING_MODEL.md

Explains the operational separation of activities.

--------------------------------------------------
11. GOBERNANZA DE TAXONOMÍA DOCUMENTATION
--------------------------------------------------

docs/governance/SYSTEM_CONTRACT.md

Defines mandatory reglas governing system behavior.

--------------------------------------------------

docs/governance/TAXONOMY_RULES.md

Defines the structure and behavior of the taxonomía.

--------------------------------------------------

docs/governance/TAXONOMY_CHANGE_POLICY.md

Defines the reglas for modifying the taxonomía.

--------------------------------------------------

docs/governance/TAXONOMY_DEPTH_POLICY.md

Defines reglas governing taxonomía expansion.

--------------------------------------------------

docs/governance/TAXONOMY_NAMING_CONVENTION.md

Defines naming conventions for genres.

--------------------------------------------------

docs/governance/TAXONOMY_QUALITY_CHECKLIST.md

Checklist used to validate taxonomía quality.

--------------------------------------------------
12. OPERATIONS DOCUMENTATION
--------------------------------------------------

docs/operations/PROJECT_BOOTSTRAP.md

Defines how a new session should initialize
the project context.

--------------------------------------------------

docs/operations/PHASE1_FINAL_CHECKLIST.md

Checklist confirming Phase 1 completion.

--------------------------------------------------
13. PROJECT MANAGEMENT DOCUMENTATION
--------------------------------------------------

docs/project-management/PROJECT_STATE.md

Stores the current operational state of the project.

--------------------------------------------------

docs/project-management/PROJECT_MEMORY.md

Stores design decisions and historical context.

--------------------------------------------------

docs/project-management/PROJECT_FILE_INDEX.md

Defines the documentation structure of the repository.

--------------------------------------------------

docs/project-management/PROJECT_CHECKPOINT_001.md

Snapshot of the reconstructed project architecture.

--------------------------------------------------
14. RELEASE DOCUMENTATION
--------------------------------------------------

docs/releases/RELEASE_NOTES_v1.0.md

Release notes describing the first stable
version of the repository.

--------------------------------------------------
FIN DEL DOCUMENTO

