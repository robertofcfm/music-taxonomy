# REPOSITORY RECONSTRUCTION PROTOCOL
Music Genre Taxonomy System

--------------------------------------------------
PURPOSE
--------------------------------------------------

This protocol defines the strict procedure used to
reconstruct project knowledge from the development
conversation and reconcile it with the current
repository state.

The objective is to ensure that:

• no information from the conversation is lost  
• repository files contain the correct knowledge  
• misplaced rules are moved to their correct files  
• incomplete documentation is completed  

The protocol must be executed iteratively.

--------------------------------------------------
GENERAL PRINCIPLES
--------------------------------------------------

The following rules are mandatory during execution.

1. The repository ZIP must always be treated as the
single source of truth for file contents.

2. The conversation must only be used to recover
missing information.

3. No content may be invented.

4. The content of a file must always be read from
the ZIP before any analysis occurs.

5. If the file content is not read, the iteration
is considered invalid.

6. If a change is applied, the modified file must
be shown in full.

7. If no change is required, the file must be
marked as completed.

--------------------------------------------------
PREPARATION STEP
--------------------------------------------------

Before starting iterations:

1. Load the ZIP repository.
2. Read the file:

docs/project/PROJECT_FILE_INDEX.md

This file defines the function of every repository
file and must be used to determine valid destinations
for rules.

--------------------------------------------------
ITERATION PROCEDURE
--------------------------------------------------

Each iteration processes exactly one file.

--------------------------------------------------
STEP 1 — LOAD ZIP
--------------------------------------------------

Load the latest ZIP version of the repository.

The ZIP must contain the current state of the project.

--------------------------------------------------
STEP 2 — SELECT SOURCE FILE
--------------------------------------------------

Select a file that has not yet been marked as completed.

Completed files must be skipped.

If a file was modified in the previous iteration,
it must return to the end of the processing queue.

--------------------------------------------------
STEP 3 — READ FILE CONTENT
--------------------------------------------------

Read the exact content of the file from the ZIP.

The content must be treated as the authoritative version.

To reduce conversation size, the content should only be
shown if:

• the file will be modified  
• the file contains misplaced rules  
• the file appears incomplete  

Otherwise a short confirmation is sufficient.

Example:

File read successfully  
No structural issues detected

--------------------------------------------------
STEP 4 — VALIDATE CONTENT LOCATION
--------------------------------------------------

Analyze whether the content belongs to the file
according to PROJECT_FILE_INDEX.md.

If rules are found that belong to another file:

• mark them as misplaced
• identify the correct destination file

Do NOT move the rule yet.

--------------------------------------------------
STEP 5 — CONVERSATION SCAN
--------------------------------------------------

Search the conversation for information that belongs
to the file being processed.

Only include information that:

• clearly belongs to this file
• is missing from the current file

Do not duplicate information already present.

--------------------------------------------------
STEP 6 — DETERMINE ACTION
--------------------------------------------------

Three possible outcomes exist.

--------------------------------------------------
CASE A — NO CHANGES REQUIRED
--------------------------------------------------

If the file content is correct and complete:

Mark the file as completed.

Output should be minimal.

Example:

File verified  
No changes required

--------------------------------------------------
CASE B — CONTENT MUST BE MOVED
--------------------------------------------------

If rules are misplaced:

Show two files:

1) Source file (after removing misplaced rules)

2) Destination file (after adding the rules)

If the destination file already contains the rule:

• do not duplicate it
• only remove it from the source

--------------------------------------------------
CASE C — FILE INCOMPLETE
--------------------------------------------------

If the file lacks important information found in
the conversation:

Generate the full corrected version of the file.

The full content must be shown.

--------------------------------------------------
STEP 7 — UPDATE FILE STATUS
--------------------------------------------------

File status must be updated.

Rules:

If file unchanged → mark as completed  
If file modified → move to end of queue

--------------------------------------------------
STEP 8 — PROGRESS REPORT
--------------------------------------------------

To minimize conversation size, only display a
compact summary.

Example:

Files processed: 12 / 39  
Completed files: 7  
Files remaining: 32

--------------------------------------------------
IMPORTANT CONSTRAINTS
--------------------------------------------------

The following errors invalidate the iteration:

• not reading the file from the ZIP  
• generating content without verifying the file  
• moving rules without identifying the destination  
• failing to show the full file after modification  

If any of these occur, the iteration must be repeated.

--------------------------------------------------
END PROTOCOL
--------------------------------------------------