# GPA Tracker

GPA Tracker is an offline command-line tool for students to record semesters and courses
and to calculate semester GPA, cumulative GPA (CGPA), completed credits, and what-if
predictions. It stores one student profile per JSON file and needs no network connection.

## Features

- Numbered text menus: 1 Summary, 2 Semesters, 3 Courses, 4 Predict GPA, 5 Profile, 0 Exit.
- First run creates the profile (name, then grading table). Later runs load the saved file
  automatically.
- Semesters: add, rename, and delete. Deleting a semester removes its courses after typing
  `yes` to confirm.
- Courses: add, edit, and delete. The status prompt comes first: Completed (a grade is
  required) or In Progress (no grade yet).
- Summaries show semester GPA, quality points, graded credits, in-progress course count,
  CGPA, and the best and lowest semester.
- What-if prediction for one semester: enter expected grades for its in-progress courses, or
  type `/skip` for a course to see which expected grades are still missing. `/cancel`
  abandons the prediction. Expected grades are held in memory only and are never saved.
- Four built-in grading tables and custom grading tables.
- Every successful change is saved immediately to JSON with an atomic replace. A damaged
  file is reported and never overwritten.
- Exact decimal arithmetic (no floats). GPA values display with two decimal places, rounded
  half up.
- Works on Windows, Linux, and macOS.

## Requirements

- Python 3.10 or newer.
- No other runtime dependencies. `pytest` is installed only for development.

## Install

Create and activate a virtual environment, then install the project with its development
dependencies.

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

Start the interactive menus with the default data file:

```bash
python -m gpa_tracker
```

Use a different data file:

```bash
python -m gpa_tracker --file PATH
```

On Windows, quote paths that contain spaces:

```powershell
python -m gpa_tracker --file "C:\Users\me\Documents\student.json"
```

Every successful change is saved as soon as it is made. Ctrl+C or end of input exits
cleanly.

## Data location

The default data file is:

```text
~/.gpa_tracker/data.json
```

On Windows this resolves to `C:\Users\<name>\.gpa_tracker\data.json`. The folder is created
when the first save happens. `--file PATH` overrides the default for that run.

The file stores raw facts only: the profile, the grading table, semesters, and courses
(code, name, credits, status, grade), with `"schema_version": 1`. GPA values and predictions
are never stored.

## Grading tables

The four built-in tables are 4.0 Plus Only, 4.0 Plus/Minus, 5.0 Plus Only, and
5.0 Plus/Minus.

**The four built-in tables are the owner's baseline and have NOT been verified against any
official university table. Users must check their own university's table.**

| Grade | 4.0 Plus Only | 4.0 Plus/Minus | 5.0 Plus Only | 5.0 Plus/Minus |
|---|---|---|---|---|
| A+ | 4.00 | 4.00 | 5.00 | 5.00 |
| A | 3.75 | 3.75 | 4.75 | 4.75 |
| A- | n/a | 3.67 | n/a | 4.50 |
| B+ | 3.50 | 3.33 | 4.50 | 4.25 |
| B | 3.00 | 3.00 | 4.00 | 4.00 |
| B- | n/a | 2.67 | n/a | 3.75 |
| C+ | 2.50 | 2.33 | 3.50 | 3.50 |
| C | 2.00 | 2.00 | 3.00 | 3.00 |
| C- | n/a | 1.67 | n/a | 2.75 |
| D+ | 1.50 | 1.33 | 2.50 | 2.50 |
| D | 1.00 | 1.00 | 2.00 | 2.00 |
| D- | n/a | 0.67 | n/a | 1.75 |
| F | 0.00 | 0.00 | 1.00 | 1.00 |

A custom table can be entered at first run or from the profile screen while the profile has
no courses. Rules: 1 to 20 entries; each letter is 1 to 3 characters using letters and an
optional `+` or `-`; points range from 0.00 to 5.00 with at most two decimal places; letters
are unique ignoring case; the letter `F` is required and is the only failing grade. The
grading table is locked once any course exists.

## Known limits

Out of scope for V1:

- Target-GPA planning, retake policies beyond counting every attempt, fractional credits,
  saving predictions, GUI or web, multiple profiles per file, other languages, converting
  grades between systems.

## Tests

Run the test suite with:

```bash
python -m pytest
```

The suite contains 301 tests. The manual checklist (C1-C22), the rule-to-test traceability
table, and the recorded gaps are in [docs/verification.md](docs/verification.md).
