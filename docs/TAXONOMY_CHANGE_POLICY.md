# TAXONOMY CHANGE POLICY
Music Genre Taxonomy System

--------------------------------------------------
1. PURPOSE
--------------------------------------------------

This document defines the rules governing modifications
to the genre taxonomy.

The taxonomy represents the structural backbone of the system
and must remain stable and coherent.

Changes must always prioritize musical coherence.

--------------------------------------------------
2. MANUAL CONTROL
--------------------------------------------------

The taxonomy can only be modified manually by the user.

The system must never automatically:

• add new genres
• remove genres
• rename genres
• move genres
• merge genres

The system may only:

• suggest improvements
• report inconsistencies
• propose possible structural changes

Final decisions always belong to the user.

--------------------------------------------------
3. NODE EXPANSION RULE
--------------------------------------------------

A taxonomy node may require expansion when it contains
too many songs assigned to it.

Expansion threshold:

45 songs.

When this happens the node may become a parent node
and new subgenres may be introduced.

The system may suggest possible subgenres but cannot
create them automatically.

--------------------------------------------------
4. NODE MERGE RULE
--------------------------------------------------

Two sibling genres may require merging when:

• their musical identity overlaps heavily
• their playlists sound nearly identical
• the classifier frequently assigns songs to both

When this occurs the system may recommend merging them
into a single genre.

--------------------------------------------------
5. NODE RELOCATION RULE
--------------------------------------------------

A genre may require relocation when it fits better
under a different parent genre.

Example:

A genre placed under Rock may later be identified
as belonging under Metal.

The system may report this possibility but must not
move the node automatically.

--------------------------------------------------
6. ATOMIC GENRE IDENTIFICATION
--------------------------------------------------

Some genres should not be subdivided further.

These are called atomic genres.

A genre should be considered atomic when:

• further subdivision would create artificial categories
• no widely recognized subgenres exist
• subdivision would harm playlist cohesion

Atomic nodes may be marked to prevent future expansion.

--------------------------------------------------
7. GENERAL NODE POLICY
--------------------------------------------------

A parent genre may include a fallback node.

Example:

Hard Rock
  Glam Metal
  Arena Rock
  Hard Rock (General)

The General node is used when:

• a song clearly belongs to the parent genre
• but does not fit any defined subgenre

The system must attempt all existing subgenres
before assigning a song to the General node.

--------------------------------------------------
8. MISSING GENRE DETECTION
--------------------------------------------------

If a song cannot be classified using existing leaf nodes,
the system must generate a missing genre report.

The report must include:

• song title
• artist
• suggested genre
• explanation

This allows the taxonomy to evolve when new genres appear.

--------------------------------------------------
9. TAXONOMY REVIEW PROCESS
--------------------------------------------------

Whenever the taxonomy changes, the system must review
the entire structure to detect improvement opportunities.

This includes:

• detecting overly similar sibling genres
• detecting nodes that should be merged
• detecting nodes that should be expanded
• detecting atomic genre candidates

--------------------------------------------------
10. RELEASE VALIDATION
--------------------------------------------------

Before a new project release is created, the taxonomy
must be validated.

Validation ensures that:

• all reported issues have been reviewed
• no structural inconsistencies remain
• playlist coherence is preserved

If unresolved taxonomy issues exist,
the release must be postponed.

--------------------------------------------------
END TAXONOMY CHANGE POLICY