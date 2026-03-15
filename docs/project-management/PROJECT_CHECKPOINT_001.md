# Project Checkpoint 001
Architecture Completion Snapshot

This document captures the first stable reconstruction of the project
after extracting knowledge from the development conversation.

Purpose:
Preserve the architecture, rules, and project structure so the project
can be resumed later without losing context.

---

# Project Objective

The project builds a **music genre taxonomy system** capable of:

1. Defining a structured genre taxonomy.
2. Classifying songs into genres using that taxonomy.
3. Generating a dynamic genre tree based on real catalog content.

The system is divided into three phases.

---

# Phase 1 — Taxonomy Design

Status: COMPLETED

Goal:
Design the genre taxonomy and all structural rules before any automation.

Outputs:

taxonomy/genre_tree_master.md  
Editable taxonomy template.

taxonomy/genre_tree_operational.csv  
Operational representation used by scripts.

taxonomy/taxonomy_version.md  
Version control for taxonomy compatibility.

data/genre_alias.csv  
Alias mapping for genre normalization.

docs/governance/TAXONOMY_RULES.md  
Taxonomy rules.

docs/governance/TAXONOMY_NAMING_CONVENTION.md  
Genre naming rules.

docs/governance/TAXONOMY_CHANGE_POLICY.md  
Rules governing taxonomy evolution.

docs/governance/TAXONOMY_DEPTH_POLICY.md  
Rules for branch depth.

docs/governance/TAXONOMY_QUALITY_CHECKLIST.md  
Validation criteria for taxonomy.

docs/operations/PHASE1_FINAL_CHECKLIST.md  
Checklist confirming Phase 1 completion.

---

# Phase 2 — Song Genre Classification

Status: DESIGN COMPLETE / IMPLEMENTATION PENDING

Goal:
Assign genres to songs using the taxonomy.

Input:

catalog/songs_raw.csv

Output:

catalog/songs_with_genres.csv

Rules:

• Genres must be real musical genres.
• Songs can belong to multiple genres.
• Minor influences are ignored.
• Genres must match taxonomy leaves.

If no suitable genre exists:

A fatal error is raised and the taxonomy must be expanded.

---

# Phase 3 — Dynamic Genre Tree Generation

Status: DESIGN COMPLETE / IMPLEMENTATION PENDING

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
Standard taxonomy node.

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

Its genres must be selected from the Latin subtree.

This prevents mixing Latin and non-Latin genre contexts.

---

# Versioning Strategy

Each classification result stores:

taxonomy_version

If the taxonomy structure changes:

Previous classifications may become incompatible.

---

# Key Project Principle

The taxonomy template is **never modified automatically**.

Only the project owner edits:

taxonomy/genre_tree_master.md

Automation tools may only:

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

• The system architecture is preserved  
• The taxonomy rules are documented  
• The project can be resumed months later  

without losing context.