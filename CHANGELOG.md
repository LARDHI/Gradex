
# Changelog

## [Unreleased]

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
