
# GPA Tracker

GPA Tracker is an offline tool where a student records semesters and courses once and can view their GPA, cumulative GPA (CGPA), and what-if predictions using either a built-in grading table or their own grading table.

**Status:** In development (P1 — Grading Tables)

## Implemented

- Four preset grading tables with decimal grade-point values.
- Custom grading table creation and validation.
- Grade normalization.
- Grade-point lookup and passing-grade checks.
- Unit tests for grading tables, custom table validation, and normalization.

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

## Data location

To be written.

## Known limits

GPA calculation, semester and course models, prediction, persistence, and interactive menus have not been implemented yet.

See [the project specification](docs/SPEC.md) for the intended scope and requirements.