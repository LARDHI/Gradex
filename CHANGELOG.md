# Changelog

## [Unreleased]

## [1.0.0] - 2026-10-29

### Added
- Complete interactive command-line flow for summaries, semesters, courses, GPA predictions, and profile settings, including first-run setup.
- Automatic JSON persistence after every successful change, with validated loading, atomic writes, and rollback when a change or save fails.
- `--file PATH` to choose the data file; the default is `~/.gpa_tracker/data.json`.
- What-if prediction with expected grades held in memory only, including `/skip` for a missing grade and `/cancel` to abandon the prediction.
- Four built-in grading tables and validated custom grading tables.
- Exact `Decimal` calculations and plain-text output with two-decimal rounding.
- P9 verification report with the manual checklist and traceability in `docs/verification.md`.

### Known limits
- Target-GPA planning, retake policies beyond counting every attempt, fractional credits, saving predictions, GUI or web, multiple profiles per file, other languages, converting grades between systems.
