# TAXONOMY CHANGE POLICY
Music Genre Taxonomy System

--------------------------------------------------
DOCUMENT METADATA
--------------------------------------------------

Scope:

Governance rules for reviewing, approving, and
validating taxonomy changes.

Owner:

Project Owner

Last Updated:

2026-03-15

--------------------------------------------------
1. PURPOSE
--------------------------------------------------

This document defines the policy governing structural
changes to the genre taxonomy.

The taxonomy represents the structural backbone
of the system and must evolve carefully.

Changes must always prioritize musical coherence.

--------------------------------------------------
2. TAXONOMY CHANGE PRINCIPLE
--------------------------------------------------

The taxonomy evolves through controlled changes
approved by the user.

Every proposed change must be deliberate and
documented before approval.

The taxonomy owner is responsible for evaluating
new genre proposals.

The system may analyze the taxonomy and suggest
possible improvements but cannot apply them automatically.

--------------------------------------------------
3. NODE MERGE POLICY
--------------------------------------------------

Two sibling genres may require merging when:

• their musical identity overlaps heavily
• their playlists sound nearly identical
• the classifier frequently assigns songs to both

When this occurs the system may recommend merging them
into a single genre.

--------------------------------------------------
4. NODE RELOCATION POLICY
--------------------------------------------------

A genre may require relocation when it fits better
under a different parent genre.

Example:

A genre placed under Rock may later be identified
as belonging under Metal.

The system may report this possibility but must not
move the node automatically.

--------------------------------------------------
5. TAXONOMY REVIEW PROCESS
--------------------------------------------------

Whenever the taxonomy changes, the system should
review the entire structure to detect improvement
opportunities.

This includes:

• detecting overly similar sibling genres
• detecting nodes that should be merged
• detecting nodes that should be expanded
• detecting atomic genre candidates

--------------------------------------------------
6. RELEASE VALIDATION
--------------------------------------------------

Before a new project release is created,
the taxonomy must be validated.

Validation ensures that:

• all reported issues have been reviewed
• taxonomy structure remains coherent
• no unresolved structural problems remain