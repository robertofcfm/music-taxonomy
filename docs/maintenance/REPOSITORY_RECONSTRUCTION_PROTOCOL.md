# PROJECT RECONSTRUCTION PROTOCOL
Music Genre Taxonomy System

--------------------------------------------------
1. PURPOSE
--------------------------------------------------

This document defines the official protocol used to reconstruct,
validate, and recover project knowledge extracted from the
development conversation.

The purpose of this protocol is to guarantee that:

• no rules are lost during reconstruction  
• no information from the conversation disappears  
• project documentation remains consistent  
• each document contains only the information that belongs to it  

This protocol must be followed when reviewing project files.

--------------------------------------------------
2. WHEN THIS PROTOCOL IS USED
--------------------------------------------------

This protocol is used during the knowledge reconstruction phase.

The goal of this phase is to recover all relevant information
from the development conversation and integrate it into the
project documentation.

This process continues until all project files have been
validated and completed.

--------------------------------------------------
3. SOURCE OF TRUTH
--------------------------------------------------

During reconstruction there are two sources of information:

1. The project repository (ZIP structure)
2. The development conversation

The conversation must be scanned in every iteration to recover
knowledge that may not yet exist in the project files.

--------------------------------------------------
4. ZIP LOADING RULE
--------------------------------------------------

The project ZIP file is only reloaded when the previous iteration
introduced changes to any file.

If the previous iteration produced no modifications,
the same ZIP state must be reused.

This prevents unnecessary reloads and ensures consistency
during file analysis.

--------------------------------------------------
5. FILE SELECTION RULE
--------------------------------------------------

Each iteration processes exactly one source file.

A file may be selected if:

• it has not been processed yet
• it previously required modification
• it contains incomplete documentation

Files already marked as completed must be skipped.

--------------------------------------------------
6. ITERATION PROCEDURE
--------------------------------------------------

Every iteration must follow the exact procedure below.

STEP 1 — Load ZIP structure

Read the project directory structure to identify all files.

STEP 2 — Select source file

Choose a file that has not yet been finalized.

STEP 3 — Read file contents

Load the complete content of the source file without modifying it.

STEP 4 — Validate misplaced content

Check if the file contains rules, definitions,
or documentation that belong to another file.

STEP 5 — Identify destination file

If misplaced content is detected:

• identify the correct destination file
• verify whether the rule already exists there

STEP 6 — Destination verification

Two outcomes are possible.

CASE A — Rule already exists in destination

Action:

• remove the rule from the source file
• do not modify the destination file

CASE B — Rule missing from destination

Action:

• remove the rule from the source file
• add the rule to the destination file

Both the corrected source and destination files must be shown.

STEP 7 — Conversation scan

The entire development conversation must be scanned to detect
information relevant to the source file.

This includes:

• architectural decisions
• system strategies
• design explanations
• rules previously described but not documented
• project philosophies

If relevant information is found, it must be added to the file.

STEP 8 — Incomplete document validation

If the file lacks information necessary for its purpose,
missing content must be reconstructed using conversation context.

STEP 9 — Generate final file

The full corrected version of the file must be displayed.

Partial patches are not allowed.

The entire file must be shown.

STEP 10 — Update processing state

Two outcomes are possible.

CASE A — File modified

The file returns to the end of the processing queue.

CASE B — File unchanged

The file is marked as completed.

--------------------------------------------------
7. PROCESSING QUEUE RULE
--------------------------------------------------

The reconstruction process operates using a queue.

Rules:

• files modified during an iteration move to the end of the queue
• completed files are removed from the queue
• the process continues until all files are completed

--------------------------------------------------
8. CONVERSATION KNOWLEDGE RECOVERY
--------------------------------------------------

The conversation may contain critical knowledge not yet stored
in project files.

Examples include:

• taxonomy design reasoning
• playlist coherence philosophy
• Latin branch strategy
• node type definitions
• classification criteria
• system design decisions

This knowledge must be extracted and integrated
into the appropriate documentation.

--------------------------------------------------
9. INFORMATION LOSS PREVENTION
--------------------------------------------------

Before removing any rule from a file,
the protocol must verify that the rule already exists
in the correct destination file.

This guarantees that no rules are lost during cleanup.

--------------------------------------------------
10. FINALIZATION CRITERIA
--------------------------------------------------

The reconstruction phase is complete when:

• every project file has been processed
• no misplaced rules remain
• all documentation is complete
• the taxonomy rules are fully preserved

At that point the repository represents a
stable checkpoint of the project knowledge.

--------------------------------------------------
END DOCUMENT