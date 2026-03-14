# REPOSITORY RECONSTRUCTION PROTOCOL
Music Genre Taxonomy System

--------------------------------------------------
PURPOSE
--------------------------------------------------

This protocol defines the procedure used to
reconstruct and reconcile project knowledge
with the current repository state.

The objective is to progressively integrate
rules extracted from development discussions
into their correct repository locations.

The reconstruction process ensures that:

• repository documentation remains consistent
• rules are placed in their correct files
• duplicated or misplaced rules are removed
• extracted rules are progressively integrated
• repository knowledge becomes canonical

The protocol operates iteratively.

--------------------------------------------------
CORE PRINCIPLE
--------------------------------------------------

The repository ZIP file is the single source
of truth for the project state.

Every iteration must begin by loading the ZIP.

No file content may be assumed from memory
or from previous iterations.

--------------------------------------------------
KEY FILES
--------------------------------------------------

The reconstruction process relies on three
primary reference files.

docs/project/PROJECT_FILE_INDEX.md

Defines the function and responsibility of
every file in the repository.

Used to determine the correct destination
for any rule.

--------------------------------------------------

docs/global/GLOBAL_RULES.md

Defines system-wide rules that affect
multiple components of the repository.

If a rule applies to more than one subsystem,
it must be placed here.

If the correct destination of a rule is
uncertain, the rule must temporarily be
placed in GLOBAL_RULES.md.

--------------------------------------------------

docs/maintenance/rule_extraction_raw.md

Contains rules extracted from development
conversations that have not yet been fully
integrated into the repository.

This file acts as a temporary rule backlog.

During reconstruction this file will
gradually shrink as rules are implemented.

--------------------------------------------------
GENERAL RULES
--------------------------------------------------

The following constraints are mandatory.

1. The ZIP must be loaded at the beginning
   of every iteration.

2. No file may be modified without first
   reading its content from the ZIP.

3. No repository content may be invented.

4. Rules must never be duplicated.

5. If a rule applies to multiple files,
   it must be placed in GLOBAL_RULES.md.

6. If a rule applies to only one file,
   it must be placed in that file.

7. If the correct destination is unclear,
   the rule must be placed in GLOBAL_RULES.md.

8. Each iteration may modify:

   • one source file
   • one destination file (if rules move)

9. If any file is modified, the next
   iteration must start by loading the ZIP again.

10. When a file is modified, the full file
    content must be shown.

--------------------------------------------------
INITIALIZATION
--------------------------------------------------

Before the first iteration begins:

1. Load the repository ZIP.

2. Read:

docs/project/PROJECT_FILE_INDEX.md

to understand repository structure.

3. Read:

docs/global/GLOBAL_RULES.md

to identify existing system rules.

4. Read:

docs/maintenance/rule_extraction_raw.md

to identify rules that still need to be
integrated into the repository.

--------------------------------------------------
FILE PROCESSING ORDER
--------------------------------------------------

To reduce complexity early in the process,
files should be processed from smallest
to largest whenever possible.

Recommended priority order:

1. Small data files
2. CSV files
3. Short documentation files
4. Medium documentation files
5. Scripts
6. Large documentation files

This approach allows simple files to be
verified quickly and reduces early complexity.

--------------------------------------------------
ITERATION STRUCTURE
--------------------------------------------------

Each iteration processes exactly one file.

--------------------------------------------------
STEP 1 — LOAD ZIP
--------------------------------------------------

Load the latest repository ZIP.

The ZIP represents the authoritative
repository state.

This step must occur at the start of
every iteration.

--------------------------------------------------
STEP 2 — SELECT TARGET FILE
--------------------------------------------------

Select a repository file to inspect.

Files should be selected according to the
FILE PROCESSING ORDER defined above.

Prefer the smallest files first.

If a file was modified in the previous
iteration, it must be moved to the end
of the processing queue.

--------------------------------------------------
STEP 3 — READ FILE CONTENT
--------------------------------------------------

Read the file content from the ZIP.

This content must be treated as the
authoritative version of the file.

The file content should only be shown
in the conversation if:

• the file will be modified
• misplaced rules are detected
• missing rules are identified

Otherwise a brief confirmation is sufficient.

--------------------------------------------------
STEP 4 — VALIDATE CONTENT LOCATION
--------------------------------------------------

Analyze whether the content in the file
belongs to that file according to
PROJECT_FILE_INDEX.md.

If rules appear that belong elsewhere:

• mark them as misplaced
• identify the correct destination file

The rule must not be moved yet.

--------------------------------------------------
STEP 5 — SCAN RAW RULES
--------------------------------------------------

Scan:

docs/maintenance/rule_extraction_raw.md

Identify rules that belong to the
currently inspected file.

A rule belongs to a file if:

• it describes behavior of that component
• it defines constraints of that file
• PROJECT_FILE_INDEX indicates that
  the file owns that responsibility

--------------------------------------------------
STEP 6 — DETERMINE ACTION
--------------------------------------------------

Four outcomes are possible.

--------------------------------------------------
CASE A — FILE IS CORRECT
--------------------------------------------------

The file contains correct information and
no missing rules.

Action:

Mark the file as verified.

--------------------------------------------------
CASE B — RULES ARE MISPLACED
--------------------------------------------------

Rules appear in the file that belong
to another file.

Action:

1. Remove rules from the source file.
2. Add rules to the correct destination file.

Both files must be shown in full.

--------------------------------------------------
CASE C — FILE IS INCOMPLETE
--------------------------------------------------

Relevant rules exist in
rule_extraction_raw.md
but are not present in the file.

Action:

Generate a full corrected version
of the file including the new rules.

--------------------------------------------------
CASE D — RULE ALREADY IMPLEMENTED
--------------------------------------------------

A rule in rule_extraction_raw.md
already exists in the correct file.

Action:

No modification required.

The rule may be removed from
rule_extraction_raw.md.

--------------------------------------------------
STEP 7 — UPDATE RULE BACKLOG
--------------------------------------------------

If rules were implemented or confirmed
as already implemented:

Generate an updated version of:

docs/maintenance/rule_extraction_raw.md

The updated version must:

• remove resolved rules
• retain unresolved rules
• preserve ordering where possible

The full updated file must be shown.

--------------------------------------------------
STEP 8 — UPDATE FILE STATUS
--------------------------------------------------

File state must be updated.

If the file changed:

move it to the end of the queue.

If the file did not change:

mark it as verified.

--------------------------------------------------
STEP 9 — PROGRESS REPORT
--------------------------------------------------

Display a compact progress summary.

Example:

Files processed: 5 / 38
Files verified: 3
Files modified: 2
Remaining files: 33

--------------------------------------------------
INVALID ITERATIONS
--------------------------------------------------

The following errors invalidate an iteration:

• ZIP not loaded
• file not read from ZIP
• rule destination not determined
• modified file not shown in full
• rule duplicated across files

If an iteration becomes invalid,
it must be repeated from STEP 1.

--------------------------------------------------
END OF PROTOCOL
--------------------------------------------------