
# GPA Tracker

GPA Tracker is an offline tool where a student records semesters and courses once and can view their GPA, cumulative GPA (CGPA), and what-if predictions using either a built-in grading table or their own grading table.

**Status:** In development (P0)

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

Expected output during P0:

```text
GPA Tracker: not yet implemented.
```

## Data location

To be written.

## Known limits

This is the initial project setup. GPA calculations, grading tables, semester and course models, persistence, and interactive menus have not been implemented.

See [the project specification, Section 1](SPEC.md#1) for the intended scope and requirements.
