# GPA Tracker

GPA Tracker is an offline tool that allows students to manage their academic records and calculate semester GPA, cumulative GPA (CGPA), completed credits, and what-if predictions. It supports built-in and custom grading tables.

**Status:** In development (P6 — Input Prompts)

## Implemented

### P0 — Project Setup
- Python package and project configuration.
- Development environment and test setup.

### P1 — Grading Tables
- Four preset grading tables with decimal grade-point values.
- Custom grading table creation and validation.
- Grade normalization.
- Grade-point lookup and passing-grade checks.
- Unit tests for grading tables, custom table validation, and normalization.

### P2 — Models and Validation
- `Course`: validated course data, credit hours, status, and normalized grades.
- `Semester`: course management, name validation, and duplicate-course prevention.
- `Student`: student profile, semester and course management, and grading-table validation.
- `ValidationError`: consistent validation errors.
- Unit tests for model validation, data integrity, and atomic mutations.

### P3 — Calculator
- Exact `Decimal` arithmetic for quality points, semester GPA, and cumulative GPA (CGPA).
- Excludes in-progress courses from actual calculations.
- Counts failed courses in GPA calculations but excludes their credits from completed credits.
- Calculates best and lowest semesters using unrounded GPAs, preserving the earliest semester in ties.
- Rounds displayed GPA values to two decimal places using `ROUND_HALF_UP`.
- Frozen result dataclasses for semester and academic results.
- Unit tests for calculation rules, rounding, retakes, ties, and model immutability.

### P4 — Prediction
- What-if predictions for in-progress courses in one selected semester.
- Keeps actual semester results and actual CGPA alongside predicted values.
- Validates expected grades against the active grading table; expected grades remain in memory only.
- Calculates predicted semester GPA, completed credits, and CGPA using exact `Decimal` arithmetic without rounding.
- Reports missing expected grades and withholds predicted values until all selected-semester in-progress courses have expectations.
- Includes failing expected grades in GPA calculations but excludes their credits from predicted completed credits.
- Unit tests for W8, W9, W15, validation, case-insensitive course-code matching, and non-mutation.

### P5 — Storage
- Saves student profiles to JSON and restores them from saved files.
- Preserves student information, semesters, courses, course statuses, grades, and grading-table configuration.
- Supports all four preset grading tables and custom grading tables.
- Uses a versioned JSON schema to validate persisted data.
- Rejects malformed JSON, unsupported schema versions, unknown fields, invalid values, and inconsistent course data.
- Uses atomic file replacement when saving to protect existing data from failed writes.
- Leaves invalid data files unchanged when loading fails.
- Provides `apply_and_save` to persist a change and roll back in-memory state if the change or save fails.
- Includes tests for round-trip persistence, validation, failed writes, and rollback.

### P6 — Input Prompts
- Added reusable input helpers for text, whole numbers, menu choices, course status, grades, deletion confirmation, yes/no questions, and custom grading entries.
- Retries empty or invalid answers with specific messages; supports case-insensitive `/cancel` without treating Back (`0`) as cancellation.
- Supports injectable input/output functions for deterministic tests.
- Uses existing grade normalization, grading-table validation, and `CourseStatus` values.
- Includes acceptance tests for validation, retries, cancellation, and injected I/O.

## Install

Python 3.10 or newer is required.

Create and activate a virtual environment, then install the project with its development dependencies.

### Windows (PowerShell)

```powershell
py -3 -m venv .venv
.venv\Scripts\activate
python -m pip install -e ".[dev]"
```

### Linux or macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
```

## Run

```bash
python -m gpa_tracker
```

The command-line interface is still a placeholder. Interactive GPA tracking and integration of storage operations into the CLI have not been implemented yet.

## Tests

Run the test suite with:

```bash
python -m pytest
```

## Data location

The default storage path provided by the storage module is:

```text
~/.gpa_tracker/data.json
```

This resolves to a `.gpa_tracker` directory inside the current user's home directory. The storage module creates the parent directory when saving to a path that requires it.

Storage operations currently require calling the storage functions programmatically. The CLI does not yet provide interactive loading or saving.

## Known limits

- The interactive command-line interface is not implemented.
- Prediction expectations remain in memory and are not persisted.
- Retakes count as separate attempts; the tool does not replace an earlier grade with a newer one.
- The JSON storage schema is currently version 1.

See [the project specification](docs/SPEC.md) for the intended scope and requirements.