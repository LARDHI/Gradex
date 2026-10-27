# GPA Tracker

GPA Tracker is an offline tool where a student records semesters and courses once and can view their GPA, cumulative GPA (CGPA), completed credits, and what-if predictions using either a built-in grading table or a custom grading table.

**Status:** In development (P4 — Prediction)

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
- Pure what-if predictions for in-progress courses in one selected semester.
- Keeps actual semester results and actual CGPA alongside predicted values.
- Validates expected grades against the active grading table; expected grades remain in memory only.
- Calculates predicted semester GPA, completed credits, and CGPA using exact `Decimal` arithmetic without rounding.
- Reports missing expected grades and withholds predicted values until all selected-semester in-progress courses have expectations.
- Includes failing expected grades in GPA calculations but excludes their credits from predicted completed credits.
- Unit tests for W8, W9, W15, validation, case-insensitive course-code matching, and non-mutation.

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

The command-line interface is still a placeholder; interactive GPA tracking has not been implemented yet.

## Tests

Run the test suite with:

```bash
python -m pytest
```

## Data location

To be written.

## Known limits

Persistence and interactive menus have not been implemented yet.

Retakes count as separate attempts; this tool does not replace an earlier grade with a newer one.

See [the project specification](docs/SPEC.md) for the intended scope and requirements.
