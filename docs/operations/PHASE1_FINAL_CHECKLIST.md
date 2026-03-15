# Phase 1 Final Checklist
Validation checklist for closing Phase 1: Taxonomy Definition.

---

## Document Metadata

Scope:

Phase 1 exit criteria and validation checks for
taxonomy definition readiness.

Owner:

Project Owner

Last Updated:

2026-03-15

---

## Purpose

Phase 1 objective:
Define the complete genre taxonomy structure and the rules governing it
before implementing classification and tree generation processes.

This checklist ensures the taxonomy template is consistent, stable,
and ready for use by the classifier and tree generator.

---

# 1. Taxonomy Structure

[ ] The file `taxonomy/genre_tree_master.md` exists.

[ ] The tree contains a **single root node**.

[ ] Hierarchy is defined exclusively by **indentation**.

[ ] All genres are uniquely named.

[ ] All leaf nodes represent **actual musical genres**.

[ ] No leaf nodes contain vague labels such as:
- "Latin rhythms"
- "Various"
- "Other"

Genres must be musically meaningful.

---

# 2. Minimum Depth Rule

Each branch of the taxonomy must satisfy:

Minimum depth = **3 levels whenever musically meaningful**

Example:

Music
  Rock
    Alternative Rock
      Grunge

Shallow branches are acceptable only if:

- the genre is **atomic**
- no meaningful subgenres exist

---

# 3. Parent–Child Musical Rule

A parent genre must **contain** the musical characteristics of its children.

Correct:

Rock
  Hard Rock

Incorrect:

Rock
  Jazz

Rule:

Child genres must be **subsets** of the parent genre.

---

# 4. Genre Independence Rule

Sibling genres must be **musically distinguishable**.

If two sibling genres:

- share most characteristics
- are difficult to distinguish in classification

Then one of the following actions must be taken:

- merge the genres
- restructure the taxonomy

---

# 5. Node Types

Operational tree supports the following node types:

NORMAL  
Standard genre node.

CLONE  
A mirror of another node used to place the same genre
in multiple branches without duplicating the subtree.

GENERAL  
Fallback node used when a track belongs to the parent
but not to any defined subgenre.

Example:

Hard Rock
  Glam Metal
  Arena Rock
  Hard Rock (General)

---

# 6. Clone Node Rules

Clone nodes:

- cannot have children
- act as **portals** to the canonical node
- share the same tracks as the canonical node

Canonical node rules:

- holds the real subtree
- clone nodes only reference it

---

# 7. General Node Rules

A `(General)` node is allowed when:

- a parent has multiple defined subgenres
- some tracks belong to the parent
- but do not clearly belong to any subgenre

Rules:

- must be explicitly defined in the template
- cannot be created automatically
- should be used sparingly

---

# 8. Latin Music Rule

Latin music is handled as a **separate branch**.

If a track is identified as Latin:

Its genre classification must be restricted
to nodes within the **Latin branch**.

Example:

Latin
  Regional Mexicano
  Cumbia
  Vallenato

This avoids mixing Latin and non-Latin genre contexts.

---

# 9. Alias Support

The file:

data/genre_alias.csv

Stores alternative names for genres.

Example:

alt rock → Alternative Rock  
synthpop → Synth Pop

This helps the classifier normalize genre names.

---

# 10. Taxonomy Versioning

The taxonomy version is stored in:

taxonomy/taxonomy_version.md

Each classification output must include the taxonomy version used.

If the taxonomy structure changes:

- previous classifications may become obsolete
- full reclassification may be required

---

# 11. Template vs Operational Tree

Two representations exist:

Editable template
taxonomy/genre_tree_master.md

Operational tree
taxonomy/genre_tree_operational.csv

The operational version is generated from the template
and includes:

- numeric codes
- parent relationships
- node type

The template must **never contain codes**.

---

# 12. Template Editing Rule

The taxonomy template is **only modified manually by the project owner**.

Automation tools may:

- analyze
- validate
- suggest changes

But **never modify the template automatically**.

---

# 13. Quality Validation

Each time the taxonomy changes, validation must check:

- duplicate genre names
- ambiguous sibling genres
- shallow branches
- missing `(General)` nodes
- incorrect hierarchy relationships

Issues must be documented in:

reports/taxonomy_issues.csv

---

# 14. Phase 1 Completion Criteria

Phase 1 is considered complete when:

✔ Genre tree template exists  
✔ Taxonomy rules documented  
✔ Naming conventions defined  
✔ Structural validation rules defined  
✔ Versioning defined  
✔ Alias system defined  

At this point the system is ready to begin:

Phase 2 — Song Genre Classification