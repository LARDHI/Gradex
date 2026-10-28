# Changelog

## [Unreleased]

### In Progress — P8: Menus and Command-Line Flow

- Developing the interactive command-line flow for summaries, semesters,
  courses, GPA predictions, and profile settings.
- Integrating first-run setup, saved-profile loading, and configurable
  data-file paths through `--file PATH`.
- Implementing semester and course management with validation,
  cancellation, and deletion confirmation.
- Integrating persistence for successful changes while protecting saved
  data from failed or cancelled operations.
- Keeping GPA prediction expectations in memory without persisting them.
- Preparing acceptance tests for CLI navigation, persistence, validation,
  cancellation, and error handling.

P8 is not complete until the required acceptance cases and full test suite
have been verified.

### Added — P7: Text Formatting
- Added pure formatting helpers for GPA and quality points, course lists and statuses, semester and academic summaries, the combined summary screen, and prediction comparisons.
- Formatted GPA and quality-point values to two decimal places using `ROUND_HALF_UP`, with unavailable values displayed as `N/A`.
- Added consistent plain-text layouts, including course-name truncation, in-progress grade placeholders, blank-line separation between summaries, and incomplete-prediction reporting.
- Added acceptance tests for numeric formatting, exact output layouts, empty results, missing values, and repeatability.

### Added — P6: Input Prompts
- Added reusable validated prompts for text, whole numbers, menu choices, course status, grades, deletion confirmation, yes/no questions, and custom grading entries.
- Added retry messages for invalid input and support for case-insensitive `/cancel`; menu choice `0` remains the Back option.
- Added injectable input/output functions so prompt behavior can be tested without calling built-in I/O directly.
- Added acceptance tests for valid and invalid answers, retries, cancellation, custom-entry rules, and I/O injection.

### Added — P5: Storage
- Added JSON persistence for student profiles through `save_student` and `load_student`.
- Added `to_dict` and `from_dict` for serialization and validated reconstruction of student data.
- Added schema versioning using `SCHEMA_VERSION`.
- Added support for all four preset grading tables and custom grading-table definitions.
- Added `default_data_path`, which resolves to `~/.gpa_tracker/data.json`.
- Added `StorageError` and `MissingFileError` for persistence and missing-file failures.
- Added strict validation for JSON structure, required and unknown fields, schema versions, course data, and grading-table configuration.
- Added atomic file replacement to protect existing data when a save fails.
- Added `apply_and_save` to apply a change, persist it, and roll back in-memory state when the change or save fails.
- Added tests for profile round trips, grading-table persistence, invalid-data handling, file preservation, atomic writes, and rollback.

### Added — P4: Prediction
- Added frozen `PredictionResult` for actual semester results and optional predicted values.
- Added `predict_semester` to calculate predicted semester GPA, completed credits, and CGPA for one selected semester.
- Added validation for selected semesters, in-progress courses, and expected grades against the active grading table.
- Added missing-grade reporting; incomplete predictions return `None` for predicted values.
- Added `clear_expected` to remove a course's expected grade case-insensitively without mutating the input mapping.
- Kept predictions in memory only and preserved actual student data and best/lowest semester results.
- Added 21 tests covering W8, W9, W15, validation, Decimal calculations, and non-mutation.

### Added — P3: Calculator
- Added `round_half_up` for two-decimal rounding using `ROUND_HALF_UP`.
- Added `quality_points` for completed courses using exact `Decimal` arithmetic.
- Added frozen `SemesterResult` and `AcademicResult` dataclasses.
- Added semester GPA, quality points, graded credits, and passing completed credits calculations.
- Added credit-weighted CGPA and best/lowest semester selection, with unrounded comparisons and earliest-semester tie-breaking.
- Excluded in-progress courses from actual academic calculations.
- Added tests for acceptance cases W1–W7, W10–W12, W14, rounding, retakes, ties, and immutability.

### Added — P2: Models and Validation
- Added `ValidationError` for model validation failures.
- Added the `CourseStatus` enum and validated, immutable `Course` model.
- Added `Semester` with course management and duplicate-course validation.
- Added `Student` with semester and course management, grading-table validation, and profile validation.
- Added validation and atomicity tests for model operations.

### Added — P1: Grading Tables
- Four preset grading tables with decimal grade-point values.
- Custom grading table creation and validation.
- Grade normalization and grade-point lookup.
- Passing-grade checks.
- Unit tests for grading tables, custom table validation, and normalization.

### Added — P0: Project Setup
- Initial project skeleton and Python package configuration.
- Development and test setup.
