"""Acceptance tests for P5 JSON persistence."""

import copy
import json
from pathlib import Path

import pytest

from gpa_tracker.grading import build_custom_table, preset_table
from gpa_tracker.models import Course, CourseStatus, Student, ValidationError
from gpa_tracker import storage
from gpa_tracker.storage import (
    MissingFileError,
    StorageError,
    apply_and_save,
    default_data_path,
    from_dict,
    load_student,
    save_student,
    to_dict,
)


def sample_student(table_id="4.0-plus-minus"):
    student = Student("Example Student", preset_table(table_id))
    student.add_semester("Fall 2026")
    student.add_course(
        "Fall 2026", Course("CS101", "Intro", 3, CourseStatus.COMPLETED, "B+")
    )
    student.add_course(
        "Fall 2026", Course("CS102", "Data Structures", 3, CourseStatus.IN_PROGRESS, None)
    )
    student.add_semester("Spring 2027")
    student.add_course(
        "Spring 2027", Course("CS201", "Algorithms", 4, CourseStatus.COMPLETED, "A")
    )
    return student


def profile_snapshot(student):
    return (
        student.name,
        student.table.table_id,
        tuple(
            (semester.name, tuple(semester.courses))
            for semester in student.semesters
        ),
    )


def test_round_trip_preserves_profile_and_courses(tmp_path):
    original = sample_student()
    path = tmp_path / "nested" / "data.json"
    save_student(original, path)
    loaded = load_student(path)
    assert profile_snapshot(loaded) == profile_snapshot(original)


def test_custom_table_round_trip_and_points_are_strings(tmp_path):
    student = Student(
        "Custom Student",
        build_custom_table([("A", "4.00"), ("B", "3.00"), ("F", "0.00")]),
    )
    student.add_semester("Fall")
    student.add_course("Fall", Course("CS1", "Course", 3, CourseStatus.COMPLETED, "A"))
    path = tmp_path / "data.json"
    save_student(student, path)
    raw = json.loads(path.read_text(encoding="utf-8"))
    assert raw["student"]["grading"]["type"] == "custom"
    assert raw["student"]["grading"]["entries"] == [
        {"letter": "A", "points": "4.00"},
        {"letter": "B", "points": "3.00"},
        {"letter": "F", "points": "0.00"},
    ]
    assert load_student(path).table.table_id == "custom"


@pytest.mark.parametrize(
    ("table_id", "scale", "system"),
    [
        ("4.0-plus-only", "4.0", "plus_only"),
        ("4.0-plus-minus", "4.0", "plus_minus"),
        ("5.0-plus-only", "5.0", "plus_only"),
        ("5.0-plus-minus", "5.0", "plus_minus"),
    ],
)
def test_all_preset_mappings_round_trip(tmp_path, table_id, scale, system):
    student = Student("Student", preset_table(table_id))
    path = tmp_path / "data.json"
    save_student(student, path)
    assert json.loads(path.read_text(encoding="utf-8"))["student"]["grading"] == {
        "type": "preset", "scale": scale, "system": system
    }
    assert load_student(path).table.table_id == table_id


def test_schema_version_and_no_computed_values_are_saved(tmp_path):
    student = sample_student()
    path = tmp_path / "data.json"
    save_student(student, path)
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["schema_version"] == 1
    forbidden = {"gpa", "cgpa", "quality_points", "predicted", "expected", "completed_credits"}
    def walk(value):
        if isinstance(value, dict):
            assert forbidden.isdisjoint(value)
            for child in value.values():
                walk(child)
        elif isinstance(value, list):
            for child in value:
                walk(child)
    walk(data)
    data["schema_version"] = 2
    path.write_text(json.dumps(data), encoding="utf-8")
    with pytest.raises(StorageError, match="schema_version"):
        load_student(path)


def test_invalid_json_reports_line_and_does_not_modify_file(tmp_path):
    path = tmp_path / "data.json"
    original = b'{\n  "schema_version": 1\n  "student": {}\n}'
    path.write_bytes(original)
    with pytest.raises(StorageError, match=r"line 3"):
        load_student(path)
    assert path.read_bytes() == original


def test_invalid_grade_does_not_modify_file(tmp_path):
    path = tmp_path / "data.json"
    data = to_dict(sample_student())
    data["semesters"][0]["courses"][0]["grade"] = "Z"
    original = json.dumps(data).encode()
    path.write_bytes(original)
    with pytest.raises(StorageError):
        load_student(path)
    assert path.read_bytes() == original


@pytest.mark.parametrize(
    ("status", "grade"), [("completed", None), ("in_progress", "A")]
)
def test_status_grade_mismatch_is_rejected(tmp_path, status, grade):
    path = tmp_path / "data.json"
    data = to_dict(sample_student())
    data["semesters"][0]["courses"][0]["status"] = status
    data["semesters"][0]["courses"][0]["grade"] = grade
    original = json.dumps(data).encode()
    path.write_bytes(original)
    with pytest.raises(StorageError):
        load_student(path)
    assert path.read_bytes() == original


def test_unknown_keys_and_wrong_types_are_rejected(tmp_path):
    path = tmp_path / "data.json"
    data = to_dict(sample_student())
    data["semesters"][0]["courses"][0]["gpa"] = "3.5"
    original = json.dumps(data).encode()
    path.write_bytes(original)
    with pytest.raises(StorageError, match="unknown key"):
        load_student(path)
    assert path.read_bytes() == original

    data = to_dict(sample_student())
    data["semesters"][0]["courses"][0]["credits"] = "3"
    original = json.dumps(data).encode()
    path.write_bytes(original)
    with pytest.raises(StorageError, match="credits"):
        load_student(path)
    assert path.read_bytes() == original


def test_missing_file_does_not_create_parent_folder(tmp_path):
    path = tmp_path / "missing" / "data.json"
    with pytest.raises(MissingFileError):
        load_student(path)
    assert not path.parent.exists()


def test_save_creates_parent_folder(tmp_path):
    path = tmp_path / "nested" / "deeper" / "data.json"
    save_student(sample_student(), path)
    assert path.is_file()


def test_failed_replace_preserves_old_file_and_removes_temp_file(tmp_path, monkeypatch):
    path = tmp_path / "data.json"
    path.write_text("old bytes", encoding="utf-8")
    before = path.read_bytes()
    def fail_replace(source, destination):
        raise OSError("simulated replace failure")
    monkeypatch.setattr(storage.os, "replace", fail_replace)
    with pytest.raises(StorageError, match="data.json"):
        save_student(sample_student(), path)
    assert path.read_bytes() == before
    assert list(tmp_path.iterdir()) == [path]


def test_apply_and_save_success_persists_change(tmp_path):
    student = sample_student()
    path = tmp_path / "data.json"
    save_student(student, path)
    apply_and_save(student, path, lambda profile: profile.rename("Updated Student"))
    assert load_student(path).name == "Updated Student"


def test_apply_and_save_rolls_back_memory_on_save_failure(tmp_path, monkeypatch):
    student = sample_student()
    before = copy.deepcopy(profile_snapshot(student))
    path = tmp_path / "data.json"
    monkeypatch.setattr(storage.os, "replace", lambda *_: (_ for _ in ()).throw(OSError("disk error")))
    with pytest.raises(StorageError):
        apply_and_save(student, path, lambda profile: profile.rename("Changed"))
    assert profile_snapshot(student) == before


def test_apply_and_save_rolls_back_change_failure_and_file(tmp_path):
    student = sample_student()
    path = tmp_path / "data.json"
    save_student(student, path)
    file_before = path.read_bytes()
    state_before = profile_snapshot(student)
    def failed_change(profile):
        profile.rename("Temporary Name")
        raise ValidationError("intentional failure")
    with pytest.raises(ValidationError, match="intentional failure"):
        apply_and_save(student, path, failed_change)
    assert profile_snapshot(student) == state_before
    assert path.read_bytes() == file_before


def test_default_path_uses_path_home(monkeypatch, tmp_path):
    monkeypatch.setattr(Path, "home", lambda: tmp_path)
    assert default_data_path() == tmp_path / ".gpa_tracker" / "data.json"


def test_from_dict_rejects_non_object_and_missing_keys():
    with pytest.raises(StorageError):
        from_dict([])
    with pytest.raises(StorageError, match="missing key"):
        from_dict({"schema_version": 1, "student": {"name": "X", "grading": {}}})


def test_no_input_print_or_float_runtime_names_in_storage_module():
    import ast
    source_path = Path(storage.__file__)
    tree = ast.parse(source_path.read_text(encoding="utf-8"))
    calls = [
        node.func.id for node in ast.walk(tree)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
    ]
    assert "input" not in calls
    assert "print" not in calls
    assert not any(isinstance(node, ast.Name) and node.id == "float" for node in ast.walk(tree))
