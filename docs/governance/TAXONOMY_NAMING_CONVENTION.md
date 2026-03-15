# TAXONOMY NAMING CONVENTION
Music Genre Taxonomy System

--------------------------------------------------
METADATOS DEL DOCUMENTO
--------------------------------------------------

Alcance:

Naming standards for taxonomía nodes, fallback nodes,
and clone naming consistency.

Responsable:

Propietario del proyecto

Última actualización:

2026-03-15

--------------------------------------------------
1. PROPÓSITO
--------------------------------------------------

Este documento define the reglas used to name genres
within the taxonomía.

Consistent naming is critical for:

• clasificación accuracy
• taxonomía readability
• avoiding ambiguity
• maintaining structural clarity

--------------------------------------------------
2. UNIQUE GENRE NAMES
--------------------------------------------------

Each genre name debe be unique across the taxonomía.

Two nodes debe never share the same name unless one
of them is a Clone node referencing the canonical node.

This ensures that clasificación targets remain
unambiguous.

--------------------------------------------------
3. LANGUAGE RULE
--------------------------------------------------

Outside the Latin branch, genre names debe be written
in English.

Examples:

Rock  
Alternative Rock  
Dream Pop  
Heavy Metal

Inside the Latin branch, Spanish names are allowed
when the genre originates from Latin musical traditions.

Examples:

Vallenato  
Norteño  
Banda  
Ranchero  

English puede still be used inside the Latin branch
when the genre name is widely recognized in English.

--------------------------------------------------
4. AVOID AMBIGUOUS TERMS
--------------------------------------------------

Genre names debe represent clearly identifiable
musical styles.

The following types of names are not allowed:

• vague stylistic descriptions  
• marketing labels  
• non-musical descriptors  

Examples of invalid names:

Latin Style  
Mixed Music  
Various Genres  
Latin Rhythms

--------------------------------------------------
5. TITLE CASE
--------------------------------------------------

Genre names debe follow Title Case formatting.

Examples:

Alternative Rock  
Synth Pop  
Progressive Rock  

This improves readability and consistency.

--------------------------------------------------
6. NODO GENERAL NAMING
--------------------------------------------------

Fallback nodes debe follow a strict naming rule.

The name debe be:

Parent Genre + "(General)"

Example:

Hard Rock (General)  
Latin Rock (General)

This ensures that fallback nodes are clearly identifiable.

--------------------------------------------------
7. NODO CLON NAMING
--------------------------------------------------

Clone nodes debe use the same genre name as their
canonical node.

However, internally they debe reference the canonical node.

Clone nodes exist only for navigation and clasificación
assistance.

They do not contain independent song assignments.

--------------------------------------------------
8. AVOID OVERLY LONG NAMES
--------------------------------------------------

Genre names should remain concise.

Avoid unnecessarily long labels that combine
multiple descriptors.

Example of bad naming:

Alternative Progressive Experimental Rock

Instead, prefer clearly established genre names.

--------------------------------------------------
9. DATASET CONSISTENCY
--------------------------------------------------

Genre names used during clasificación debe match
exactly the names defined in the taxonomía.

The classifier no debe invent variations or
synonyms of genre names.

Aliases puede be handled separately through the
genre alias system.

--------------------------------------------------
END TAXONOMY NAMING CONVENTION

