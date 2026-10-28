"""Tests for GPA Tracker's interactive CLI."""

import json

import pytest

from gpa_tracker import cli, storage
from gpa_tracker.grading import preset_table
from gpa_tracker.models import (
    Course,
    CourseStatus,
    Student,
)


def make_student(*, with_semester=False, with_courses=False):
    student = Student("Test Student", preset_table("4.0-plus-only"))

    if with_semester or with_courses:
        semester = student.add_semester("Fall 2026")
    if with_courses:
        student.add_course(
            semester.name,
            Course(
                code="CS101",
                name="Programming",
                credits=3,
                status=CourseStatus.COMPLETED,
                grade="A",
            ),
        )
    return student


def run_with_answers(path, answers):
    """Run the CLI with deterministic answers and collect displayed output."""
    remaining = iter(answers)
    output = []

    def fake_input(prompt=""):
        output.append(prompt)
        try:
            return next(remaining)
        except StopIteration:
            raise EOFError from None

    def fake_output(message=""):
        output.append(str(message))

    exit_code = cli.run(
        path,
        input_func=fake_input,
        output_func=fake_output,
    )
    return exit_code, "\n".join(output)


def create_file(path, student=None):
    if student is None:
        student = make_student()
    storage.save_student(student, path)
    return student


def test_first_run_creates_profile_and_data_file(tmp_path):
    path = tmp_path / "student.json"

    code, output = run_with_answers(
        path,
        [
            "Alex",
            "1",  # 4.0 Plus Only
            "0",  # Exit
        ],
    )

    assert code == 0
    assert path.exists()
    loaded = storage.load_student(path)
    assert loaded.name == "Alex"
    assert loaded.table.table_id == "4.0-plus-only"
    assert "Main menu:" in output


def test_first_run_cancel_does_not_create_data_file(tmp_path):
    path = tmp_path / "student.json"

    code, _ = run_with_answers(path, ["/cancel"])

    assert code == 0
    assert not path.exists()


def test_invalid_data_file_is_not_overwritten(tmp_path):
    path = tmp_path / "student.json"
    original = b'{"not": "valid GPA Tracker data"}\n'
    path.write_bytes(original)

    code, output = run_with_answers(path, ["0"])

    assert code == 1
    assert path.read_bytes() == original
    assert "not changed" in output.lower()


def test_existing_profile_can_exit_without_changing_file(tmp_path):
    path = tmp_path / "student.json"
    create_file(path)
    original = path.read_bytes()

    code, _ = run_with_answers(path, ["0"])

    assert code == 0
    assert path.read_bytes() == original


def test_add_semester_persists_successful_change(tmp_path):
    path = tmp_path / "student.json"
    create_file(path)

    code, _ = run_with_answers(
        path,
        [
            "2",          # Semesters
            "1",          # Add semester
            "Spring 2027",
            "0",          # Back
            "0",          # Exit
        ],
    )

    assert code == 0
    loaded = storage.load_student(path)
    assert [s.name for s in loaded.semesters] == ["Spring 2027"]


def test_cancel_add_semester_keeps_file_byte_identical(tmp_path):
    path = tmp_path / "student.json"
    create_file(path)
    original = path.read_bytes()

    run_with_answers(
        path,
        [
            "2",          # Semesters
            "1",          # Add semester
            "/cancel",
            "0",          # Back
            "0",          # Exit
        ],
    )

    assert path.read_bytes() == original


def test_duplicate_semester_is_rejected_without_changing_file(tmp_path):
    path = tmp_path / "student.json"
    student = make_student(with_semester=True)
    storage.save_student(student, path)
    original = path.read_bytes()

    _, output = run_with_answers(
        path,
        [
            "2",
            "1",
            " fall  2026 ",
            "0",
            "0",
        ],
    )

    assert path.read_bytes() == original
    assert "duplicate" in output.lower()


def test_delete_semester_requires_exact_yes_confirmation(tmp_path):
    path = tmp_path / "student.json"
    create_file(path, make_student(with_semester=True))
    original = path.read_bytes()

    run_with_answers(
        path,
        [
            "2", "3", "1", "y", "0", "0",
        ],
    )

    assert path.read_bytes() == original
    assert storage.load_student(path).semesters[0].name == "Fall 2026"


def test_delete_semester_after_confirmation(tmp_path):
    path = tmp_path / "student.json"
    create_file(path, make_student(with_courses=True))

    code, _ = run_with_answers(
        path,
        [
            "2", "3", "1", "yes",
            "0", "0",
        ],
    )

    assert code == 0
    assert storage.load_student(path).semesters == []


def test_add_course_asks_status_first_and_saves_course(tmp_path):
    path = tmp_path / "student.json"
    create_file(path, make_student(with_semester=True))

    code, output = run_with_answers(
        path,
        [
            "3",       # Courses
            "1",       # Semester
            "1",       # Add course
            "1",       # Completed — status must be first
            "B+",      # Grade
            "CS102",   # Code
            "Algorithms",
            "4",       # Credits
            "0",       # Course menu
            "0",       # Semester selection
            "0",       # Main menu
        ],
    )

    assert code == 0
    loaded = storage.load_student(path)
    course = loaded.find_semester("Fall 2026").courses[0]
    assert course.code == "CS102"
    assert course.name == "Algorithms"
    assert course.credits == 4
    assert course.status is CourseStatus.COMPLETED
    assert course.grade == "B+"
    assert output.index("Course status:") < output.index("Enter grade:")


def test_add_in_progress_course_has_no_grade(tmp_path):
    path = tmp_path / "student.json"
    create_file(path, make_student(with_semester=True))

    run_with_answers(
        path,
        [
            "3", "1", "1",
            "2",             # In Progress
            "CS103",
            "Databases",
            "3",
            "0", "0", "0",
        ],
    )

    loaded = storage.load_student(path)
    course = loaded.find_semester("Fall 2026").courses[0]
    assert course.status is CourseStatus.IN_PROGRESS
    assert course.grade is None


def test_cancel_course_creation_does_not_change_file(tmp_path):
    path = tmp_path / "student.json"
    create_file(path, make_student(with_semester=True))
    original = path.read_bytes()

    run_with_answers(
        path,
        [
            "3", "1", "1",
            "1", "/cancel",
            "0", "0", "0",
        ],
    )

    assert path.read_bytes() == original


def test_edit_course_enter_keeps_existing_values(tmp_path):
    path = tmp_path / "student.json"
    create_file(path, make_student(with_courses=True))

    run_with_answers(
        path,
        [
            "3", "1", "2", "1",  # Select course to edit
            "1",                 # Completed
            "",                  # Keep grade A
            "",                  # Keep code CS101
            "",                  # Keep name Programming
            "",                  # Keep 3 credits
            "0", "0", "0",
        ],
    )

    loaded = storage.load_student(path)
    course = loaded.find_semester("Fall 2026").courses[0]
    assert (
        course.code,
        course.name,
        course.credits,
        course.status,
        course.grade,
    ) == (
        "CS101",
        "Programming",
        3,
        CourseStatus.COMPLETED,
        "A",
    )


def test_cancel_course_edit_keeps_file_byte_identical(tmp_path):
    path = tmp_path / "student.json"
    create_file(path, make_student(with_courses=True))
    original = path.read_bytes()

    run_with_answers(
        path,
        [
            "3", "1", "2", "1",
            "/cancel",
            "0", "0", "0",
        ],
    )

    assert path.read_bytes() == original


def test_delete_course_requires_yes(tmp_path):
    path = tmp_path / "student.json"
    create_file(path, make_student(with_courses=True))
    original = path.read_bytes()

    run_with_answers(
        path,
        [
            "3", "1", "3", "1",
            "no",
            "0", "0", "0",
        ],
    )

    assert path.read_bytes() == original


def test_delete_course_after_confirmation(tmp_path):
    path = tmp_path / "student.json"
    create_file(path, make_student(with_courses=True))

    run_with_answers(
        path,
        [
            "3", "1", "3", "1",
            "yes",
            "0", "0", "0",
        ],
    )

    loaded = storage.load_student(path)
    assert loaded.find_semester("Fall 2026").courses == []


def test_grading_table_is_locked_while_courses_exist(tmp_path):
    path = tmp_path / "student.json"
    create_file(path, make_student(with_courses=True))
    original = path.read_bytes()

    _, output = run_with_answers(
        path,
        [
            "5",  # Profile
            "2",  # Change grading table
            "0",  # Back
            "0",  # Exit
        ],
    )

    assert path.read_bytes() == original
    assert "locked" in output.lower()


def test_change_profile_name_is_persisted(tmp_path):
    path = tmp_path / "student.json"
    create_file(path)

    run_with_answers(
        path,
        [
            "5", "1", "New Name",
            "0", "0",
        ],
    )

    assert storage.load_student(path).name == "New Name"


def test_summary_screen_displays_no_semesters_safely(tmp_path):
    path = tmp_path / "student.json"
    create_file(path)

    _, output = run_with_answers(
        path,
        [
            "1",   # Summary
            "",    # Continue
            "0",   # Exit
        ],
    )

    assert "No semesters yet." in output
    assert "N/A" in output


def test_prediction_does_not_persist_expected_grades(tmp_path):
    path = tmp_path / "student.json"
    student = make_student(with_semester=True)
    student.add_course(
        "Fall 2026",
        Course(
            code="CS201",
            name="Operating Systems",
            credits=3,
            status=CourseStatus.COMPLETED,
            grade="A",
        ),
    )
    student.add_course(
        "Fall 2026",
        Course(
            code="CS202",
            name="Networks",
            credits=3,
            status=CourseStatus.IN_PROGRESS,
            grade=None,
        ),
    )
    storage.save_student(student, path)
    original = path.read_bytes()

    run_with_answers(
        path,
        [
            "4",      # Predict GPA
            "1",      # Choose semester
            "B+",     # Expected grade for CS202
            "0",      # Back from prediction
            "0",      # Exit
        ],
    )

    assert path.read_bytes() == original
    loaded = storage.load_student(path)
    course = loaded.find_semester("Fall 2026").courses[1]
    assert course.status is CourseStatus.IN_PROGRESS
    assert course.grade is None


def test_prediction_lists_when_no_courses_are_in_progress(tmp_path):
    path = tmp_path / "student.json"
    create_file(path, make_student(with_courses=True))

    _, output = run_with_answers(
        path,
        [
            "4",
            "0",
        ],
    )

    assert "No semester has in-progress courses." in output


def test_main_menu_reprompts_after_invalid_choice(tmp_path):
    path = tmp_path / "student.json"
    create_file(path)

    _, output = run_with_answers(path, ["abc", "9", "0"])

    assert "Invalid number" in output
    assert output.count("Main menu:") >= 3


def test_numbered_menu_accepts_cancel_command(tmp_path):
    path = tmp_path / "student.json"
    create_file(path)

    code, _ = run_with_answers(path, ["/cancel"])

    assert code == 0


def test_saved_file_contains_raw_facts_not_predictions(tmp_path):
    path = tmp_path / "student.json"
    create_file(path, make_student(with_courses=True))

    data = json.loads(path.read_text(encoding="utf-8"))
    assert set(data) == {"schema_version", "student", "semesters"}
    serialized = json.dumps(data).lower()
    assert "predicted_gpa" not in serialized
    assert "expected_grades" not in serialized