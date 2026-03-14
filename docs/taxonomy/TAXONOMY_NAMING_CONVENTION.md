# TAXONOMY NAMING CONVENTION
Music Genre Taxonomy System

--------------------------------------------------
1. PURPOSE
--------------------------------------------------

This document defines the rules used to name genres
within the taxonomy.

Consistent naming is critical for:

• classification accuracy
• taxonomy readability
• avoiding ambiguity
• maintaining structural clarity

--------------------------------------------------
2. UNIQUE GENRE NAMES
--------------------------------------------------

Each genre name must be unique across the taxonomy.

Two nodes must never share the same name unless one
of them is a Clone node referencing the canonical node.

This ensures that classification targets remain
unambiguous.

--------------------------------------------------
3. LANGUAGE RULE
--------------------------------------------------

Outside the Latin branch, genre names must be written
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

English may still be used inside the Latin branch
when the genre name is widely recognized in English.

--------------------------------------------------
4. AVOID AMBIGUOUS TERMS
--------------------------------------------------

Genre names must represent clearly identifiable
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

Genre names must follow Title Case formatting.

Examples:

Alternative Rock  
Synth Pop  
Progressive Rock  

This improves readability and consistency.

--------------------------------------------------
6. GENERAL NODE NAMING
--------------------------------------------------

Fallback nodes must follow a strict naming rule.

The name must be:

Parent Genre + "(General)"

Example:

Hard Rock (General)  
Latin Rock (General)

This ensures that fallback nodes are clearly identifiable.

--------------------------------------------------
7. CLONE NODE NAMING
--------------------------------------------------

Clone nodes must use the same genre name as their
canonical node.

However, internally they must reference the canonical node.

Clone nodes exist only for navigation and classification
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

Genre names used during classification must match
exactly the names defined in the taxonomy.

The classifier must not invent variations or
synonyms of genre names.

Aliases may be handled separately through the
genre alias system.

--------------------------------------------------
END TAXONOMY NAMING CONVENTION