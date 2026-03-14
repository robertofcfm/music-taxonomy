# PROJECT FILE INDEX
Music Genre Taxonomy System

This document describes every file used in the project
and its role within the system.

The goal is to provide a clear reference so that
rules and information are always placed in the correct
document.

--------------------------------------------------
PROJECT STRUCTURE
--------------------------------------------------

music-taxonomy/

data/        → normalization data  
taxonomy/    → taxonomy definition  
catalog/     → song catalog and classification results  
scripts/     → automation tools  
reports/     → validation reports  
docs/        → documentation and system rules  

--------------------------------------------------
DATA DIRECTORY
--------------------------------------------------

data/genre_alias.csv

Purpose

Stores alias mappings for genre normalization.

This file allows the classifier to convert alternative
genre names into the canonical taxonomy name.

Example

alt rock → Alternative Rock  
synthpop → Synth Pop  

Edited manually.

--------------------------------------------------
TAXONOMY DIRECTORY
--------------------------------------------------

taxonomy/genre_tree_master.md

Editable taxonomy template.

Characteristics

• hierarchy defined by indentation  
• no numeric codes  
• manually maintained  

This is the authoritative genre taxonomy.

IMPORTANT

This file must NEVER be modified automatically.

---

taxonomy/genre_tree_operational.csv

Operational representation of the taxonomy.

Contains

• genre codes  
• parent relationships  
• node types  
• canonical references  

Generated from the master taxonomy.

Used by scripts and classifiers.

---

taxonomy/taxonomy_version.md

Stores the current taxonomy version.

Purpose

Ensures compatibility between

• taxonomy structure  
• classification results  
• generated trees  

--------------------------------------------------
CATALOG DIRECTORY
--------------------------------------------------

catalog/songs_raw.csv

Input catalog.

Contains the list of songs that must be classified.

Structure

title,artist

Example

Bohemian Rhapsody,Queen

---

catalog/songs_with_genres.csv

Classification output.

Structure

title,artist,genres,taxonomy_version

Contains only successfully classified songs.

--------------------------------------------------
SCRIPTS DIRECTORY
--------------------------------------------------

scripts/classify_songs.py

Song classification engine.

Responsibilities

• read songs_raw.csv  
• classify songs using taxonomy  
• validate rules  
• produce songs_with_genres.csv  

---

scripts/build_tree.py

Builds the dynamic listening tree.

Used in Phase 3.

The tree expands when nodes exceed the threshold
number of songs.

---

scripts/validate_tree.py

Validates taxonomy structure.

Checks

• parent-child relationships  
• node types  
• taxonomy consistency  

--------------------------------------------------
REPORTS DIRECTORY
--------------------------------------------------

reports/taxonomy_issues.csv

Stores detected taxonomy problems.

Examples

• missing genres  
• ambiguous siblings  
• invalid hierarchy  

---

reports/taxonomy_improvement_report.csv

Stores recommendations for improving taxonomy.

Examples

• possible merges  
• missing subgenres  
• structural improvements  

--------------------------------------------------
DOCUMENTATION DIRECTORY
--------------------------------------------------

docs/PROJECT_CONTEXT.md

High level description of the project.

Explains

• system philosophy  
• system architecture  
• main concepts  

---

docs/PROJECT_BOOTSTRAP.md

Defines how the system must initialize a working
session.

Ensures that required documents and taxonomy files
are loaded before performing operations.

---

docs/PROJECT_FILE_INDEX.md

This document.

Defines the role of each file in the project.

Used during reconstruction to determine
the correct destination for rules.

---

docs/PROJECT_MEMORY.md

Records key design decisions made during the
development of the project.

Used to preserve reasoning behind architecture
choices.

---

docs/PROJECT_STATE.md

Stores the current operational status of the
project.

May include

• progress information  
• active taxonomy version  
• pending tasks  

---

docs/PROJECT_CHECKPOINT_*.md

Snapshots of the project state.

Used to restore context after long periods
without working on the project.

---

docs/PHASE1_FINAL_CHECKLIST.md

Checklist used to validate completion of
taxonomy design.

---

docs/SYSTEM_CONTRACT.md

Defines mandatory system rules that must always
be respected by all tools.

---

docs/TAXONOMY_RULES.md

Core rules governing taxonomy structure.

---

docs/TAXONOMY_CHANGE_POLICY.md

Defines how the taxonomy may evolve.

---

docs/TAXONOMY_DEPTH_POLICY.md

Defines minimum depth requirements for branches.

---

docs/TAXONOMY_NAMING_CONVENTION.md

Defines naming rules for genres.

---

docs/TAXONOMY_QUALITY_CHECKLIST.md

Checklist used to validate taxonomy quality.

--------------------------------------------------
FILE EDITING PRINCIPLE
--------------------------------------------------

Files fall into three categories

MANUAL FILES

Edited only by the project owner

• genre_tree_master.md  
• taxonomy rules documents  
• documentation  

GENERATED FILES

Created automatically by scripts

• genre_tree_operational.csv  
• classification results  

REPORT FILES

Generated by validation processes

• taxonomy_issues.csv  
• improvement reports  

--------------------------------------------------
MASTER RULE
--------------------------------------------------

Rules must always be stored in the document that
corresponds to their scope.

The PROJECT_FILE_INDEX must be consulted before
moving or adding rules to any document.