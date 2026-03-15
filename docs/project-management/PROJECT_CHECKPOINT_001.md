# Project Checkpoint 001
Architecture Completion Snapshot

This document captures the first stable reconstruction of the project
after extracting knowledge from the development conversation.

Propósito:
Preserve the architecture, reglas, and project structure so the project
can be resumed later without losing context.

---

# Project Objective

The project builds a **music genre taxonomía system** capable of:

1. Defining a structured genre taxonomía.
2. Classifying songs into genres using that taxonomía.
3. Generating a dynamic genre tree based on real catalog content.

El sistema is divided into three phases.

---

# Phase 1 — Taxonomy Design

Estado: COMPLETED

Goal:
Design the genre taxonomía and all structural reglas before any automation.

Outputs:

taxonomy/genre_tree_master.md  
Editable taxonomía template.

taxonomy/genre_tree_operational.csv  
Operational representation used by scripts.

taxonomy/taxonomy_version.md  
Version control for taxonomía compatibility.

data/genre_alias.csv  
Alias mapping for genre normalization.

docs/governance/TAXONOMY_RULES.md  
Taxonomy reglas.

docs/governance/TAXONOMY_NAMING_CONVENTION.md  
Genre naming reglas.

docs/governance/TAXONOMY_CHANGE_POLICY.md  
Rules governing taxonomía evolution.

docs/governance/TAXONOMY_DEPTH_POLICY.md  
Rules for branch depth.

docs/governance/TAXONOMY_QUALITY_CHECKLIST.md  
Validation criteria for taxonomía.

docs/operations/PHASE1_FINAL_CHECKLIST.md  
Checklist confirming Phase 1 completion.

---

# Phase 2 — Song Genre Classification

Estado: DESIGN COMPLETE / IMPLEMENTATION PENDIENTE

Goal:
Assign genres to songs using the taxonomía.

Input:

catalog/songs_raw.csv

Output:

catalog/songs_with_genres.csv

Rules:

• Genres debe be real musical genres.
• Songs can belong to multiple genres.
• Minor influences are ignored.
• Genres debe match taxonomía leaves.

If no suitable genre exists:

A error fatal is raised and the taxonomía debe be expanded.

---

# Phase 3 — Dynamic Genre Tree Generation

Estado: DESIGN COMPLETE / IMPLEMENTATION PENDIENTE

Goal:
Generate a genre tree based on catalog data.

Rule:

A node becomes expandable when it contains more than:

45 songs

At that point:

• The node becomes a parent
• Songs are redistributed into subgenres

This process builds the final listening tree.

---

# Node Types

NORMAL  
Standard taxonomía node.

CLONE  
Portal node pointing to another canonical node.

GENERAL  
Fallback node for songs that belong to a parent genre but not to any defined subgenre.

ATOMIC  
Terminal node that should not be expanded further.

---

# Latin Genre Strategy

Latin music is handled as a separate branch.

If a song is Latin:

Its genres debe be selected from the Latin subtree.

This prevents mixing Latin and non-Latin genre contexts.

---

# Versioning Strategy

Each clasificación result stores:

taxonomy_version

If the taxonomía structure changes:

Previous clasificacións puede become incompatible.

---

# Key Project Principle

The taxonomía template is **never modified automatically**.

Only the project owner edits:

taxonomy/genre_tree_master.md

Automation tools puede only:

• analyze
• validate
• suggest changes

---

# Current Repository Structure

music-taxonomy/

data/  
taxonomy/  
catalog/  
scripts/  
reports/  
docs/

---

# Checkpoint Purpose

This checkpoint ensures that:

• El sistema architecture is preserved  
• The taxonomía reglas are documented  
• The project can be resumed months later  

without losing context.

