"""JSON persistence for one GPA Tracker student profile."""

from __future__ import annotations

import copy
import json
import os
import tempfile
from pathlib import Path
from typing import Callable, TypeVar

from .grading import GradingError, build_custom_table, preset_table
from .models import Course, CourseStatus, Semester, Student, ValidationError


SCHEMA_VERSION = 1
_PRESET_IDS = {
    ("4.0", "plus_only"): "4.0-plus-only",
    ("4.0", "plus_minus"): "4.0-plus-minus",
    ("5.0", "plus_only"): "5.0-plus-only",
    ("5.0", "plus_minus"): "5.0-plus-minus",
}
_PRESET_SETTINGS = {value: key for key, value in _PRESET_IDS.items()}
_T = TypeVar("_T")


class StorageError(Exception):
    """A persistence or persisted-data validation failure."""


class MissingFileError(StorageError):
    """The requested student data file does not exist."""


def default_data_path() -> Path:
    """Return the default data file path under the current user's home folder."""
    return Path.home() / ".gpa_tracker" / "data.json"


def to_dict(student: Student) -> dict:
    """Convert a Student to the versioned JSON structure, storing raw facts only."""
    if not isinstance(student, Student):
        raise TypeError("to_dict requires a Student instance.")

    table = student.table
    if table.table_id == "custom":
        grading = {
            "type": "custom",
            "entries": [
                {"letter": letter, "points": format(table.points[letter], ".2f")}
                for letter in table.letters
            ],
        }
    else:
        try:
            scale, system = _PRESET_SETTINGS[table.table_id]
        except KeyError as exc:
            raise StorageError(
                f"Cannot save student data: unsupported grading table {table.table_id!r}."
            ) from exc
        grading = {"type": "preset", "scale": scale, "system": system}

    return {
        "schema_version": SCHEMA_VERSION,
        "student": {"name": student.name, "grading": grading},
        "semesters": [
            {
                "name": semester.name,
                "courses": [
                    {
                        "code": course.code,
                        "name": course.name,
                        "credits": course.credits,
                        "status": course.status.value,
                        "grade": course.grade,
                    }
                    for course in semester.courses
                ],
            }
            for semester in student.semesters
        ],
    }


def _expect_object(value: object, where: str, keys: set[str]) -> dict:
    if not isinstance(value, dict):
        raise StorageError(f"Invalid {where}: expected an object.")
    actual = set(value)
    unknown = actual - keys
    missing = keys - actual
    if unknown:
        raise StorageError(f"Invalid {where}: unknown key(s): {', '.join(sorted(map(str, unknown)))}.")
    if missing:
        raise StorageError(f"Invalid {where}: missing key(s): {', '.join(sorted(missing))}.")
    return value


def from_dict(data: object) -> Student:
    """Validate decoded JSON and construct a Student using the domain models."""
    root = _expect_object(data, "top-level data", {"schema_version", "student", "semesters"})
    if type(root["schema_version"]) is not int or root["schema_version"] != SCHEMA_VERSION:
        raise StorageError(
            f"Unsupported or invalid schema_version {root['schema_version']!r}; expected {SCHEMA_VERSION}."
        )

    student_data = _expect_object(root["student"], "student", {"name", "grading"})
    grading_data = student_data["grading"]
    if not isinstance(grading_data, dict):
        raise StorageError("Invalid student.grading: expected an object.")
    grading_type = grading_data.get("type")
    if grading_type == "preset":
        grading_data = _expect_object(
            grading_data, "student.grading", {"type", "scale", "system"}
        )
        scale, system = grading_data["scale"], grading_data["system"]
        if not isinstance(scale, str) or not isinstance(system, str):
            raise StorageError("Invalid preset grading: scale and system must be strings.")
        table_id = _PRESET_IDS.get((scale, system))
        if table_id is None:
            raise StorageError(
                f"Invalid preset grading combination: scale={scale!r}, system={system!r}."
            )
        table = preset_table(table_id)
    elif grading_type == "custom":
        grading_data = _expect_object(
            grading_data, "student.grading", {"type", "entries"}
        )
        entries_data = grading_data["entries"]
        if not isinstance(entries_data, list):
            raise StorageError("Invalid custom grading entries: expected a list.")
        entries = []
        for index, entry in enumerate(entries_data):
            item = _expect_object(entry, f"student.grading.entries[{index}]", {"letter", "points"})
            if not isinstance(item["letter"], str):
                raise StorageError(f"Invalid custom grading letter at entry {index}: expected a string.")
            if not isinstance(item["points"], str):
                raise StorageError(f"Invalid custom grading points at entry {index}: expected a string.")
            entries.append((item["letter"], item["points"]))
        table = build_custom_table(entries)
    else:
        raise StorageError(f"Invalid student.grading.type {grading_type!r}.")

    semesters_data = root["semesters"]
    if not isinstance(semesters_data, list):
        raise StorageError("Invalid semesters: expected a list.")
    semesters = []
    for semester_index, raw_semester in enumerate(semesters_data):
        semester_data = _expect_object(
            raw_semester, f"semesters[{semester_index}]", {"name", "courses"}
        )
        if not isinstance(semester_data["name"], str):
            raise StorageError(f"Invalid semesters[{semester_index}].name: expected a string.")
        courses_data = semester_data["courses"]
        if not isinstance(courses_data, list):
            raise StorageError(f"Invalid semesters[{semester_index}].courses: expected a list.")
        courses = []
        for course_index, raw_course in enumerate(courses_data):
            where = f"semesters[{semester_index}].courses[{course_index}]"
            course_data = _expect_object(
                raw_course, where, {"code", "name", "credits", "status", "grade"}
            )
            for field in ("code", "name", "status"):
                if not isinstance(course_data[field], str):
                    raise StorageError(f"Invalid {where}.{field}: expected a string.")
            if type(course_data["credits"]) is not int:
                raise StorageError(f"Invalid {where}.credits: expected an integer.")
            if course_data["grade"] is not None and not isinstance(course_data["grade"], str):
                raise StorageError(f"Invalid {where}.grade: expected a string or null.")
            try:
                status = CourseStatus(course_data["status"])
            except ValueError as exc:
                raise StorageError(
                    f"Invalid {where}.status {course_data['status']!r}."
                ) from exc
            courses.append(
                Course(
                    code=course_data["code"],
                    name=course_data["name"],
                    credits=course_data["credits"],
                    status=status,
                    grade=course_data["grade"],
                )
            )
        semesters.append(Semester(semester_data["name"], courses))

    return Student(student_data["name"], table, semesters)


def save_student(student: Student, path: str | os.PathLike[str]) -> None:
    """Atomically save a profile; a failed pre-replace write leaves old data intact."""
    target = Path(path)
    temporary_path: Path | None = None
    try:
        payload = json.dumps(to_dict(student), ensure_ascii=False, indent=2) + "\n"
        target.parent.mkdir(parents=True, exist_ok=True)
        descriptor, temporary_name = tempfile.mkstemp(
            prefix=f".{target.name}.", suffix=".tmp", dir=target.parent
        )
        temporary_path = Path(temporary_name)
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary_path, target)
        temporary_path = None
    except Exception as exc:
        if temporary_path is not None:
            try:
                temporary_path.unlink(missing_ok=True)
            except OSError:
                pass
        if isinstance(exc, StorageError):
            reason = str(exc)
        else:
            reason = str(exc) or type(exc).__name__
        raise StorageError(f"Could not save student data at {str(target)!r}: {reason}") from exc


def load_student(path: str | os.PathLike[str]) -> Student:
    """Read and fully validate a profile without modifying its file."""
    target = Path(path)
    try:
        text = target.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise MissingFileError(f"Student data file not found at {str(target)!r}.") from exc
    except (OSError, UnicodeError) as exc:
        raise StorageError(
            f"Could not read student data at {str(target)!r}: {str(exc) or type(exc).__name__}"
        ) from exc

    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        raise StorageError(
            f"Invalid JSON in {str(target)!r} at line {exc.lineno}, column {exc.colno}: {exc.msg}."
        ) from exc
    except (ValueError, RecursionError) as exc:
        raise StorageError(f"Invalid JSON in {str(target)!r}: {exc}.") from exc

    try:
        return from_dict(data)
    except StorageError as exc:
        raise StorageError(f"Invalid student data in {str(target)!r}: {exc}") from exc
    except (ValidationError, GradingError, TypeError, ValueError, KeyError, RecursionError) as exc:
        raise StorageError(f"Invalid student data in {str(target)!r}: {exc}") from exc


def _restore_student(student: Student, snapshot: Student) -> None:
    """Restore state on the existing Student object to preserve its identity."""
    student.name = snapshot.name
    student.table = snapshot.table
    student.semesters = snapshot.semesters


def apply_and_save(
    student: Student,
    path: str | os.PathLike[str],
    change: Callable[[Student], _T],
) -> _T:
    """Apply one change, save it, and roll back in-memory state on any failure."""
    try:
        snapshot = copy.deepcopy(student)
    except (TypeError, ValueError):
        # GradingTable contains an immutable mapping proxy, which cannot be deep-copied.
        # Its table is immutable, so deep-copy the mutable semester/course state instead.
        snapshot = Student(student.name, student.table, copy.deepcopy(student.semesters))
    try:
        result = change(student)
    except BaseException:
        _restore_student(student, snapshot)
        raise
    try:
        save_student(student, path)
    except StorageError:
        _restore_student(student, snapshot)
        raise
    return result
