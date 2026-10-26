"""Acceptance tests for GPA Tracker's validated data models."""

from decimal import Decimal

import pytest

from gpa_tracker.grading import GradingError, GradingTable, build_custom_table, preset_table
from gpa_tracker.models import Course, CourseStatus, Semester, Student, ValidationError


def course(code="CS101", name="Intro to Programming", credits=3,
           status=CourseStatus.COMPLETED, grade="A"):
    return Course(code=code, name=name, credits=credits, status=status, grade=grade)


def profile(table_id="4.0-plus-only", name="Student"):
    return Student(name=name, table=preset_table(table_id))


def snapshot(student):
    return (
        student.name,
        student.table,
        tuple(
            (semester.name, tuple(semester.courses))
            for semester in student.semesters
        ),
    )


@pytest.mark.parametrize("credits", [1, 9])
def test_course_accepts_credit_boundaries(credits):
    assert course(credits=credits).credits == credits


@pytest.mark.parametrize("credits", [0, 10, 3.0, 3.5, "3", True])
def test_course_rejects_invalid_credits_with_value(credits):
    with pytest.raises(ValidationError) as exc_info:
        course(credits=credits)
    assert repr(credits) in str(exc_info.value)
    assert "credits" in str(exc_info.value).lower()


def test_course_trims_code_and_name_without_rewriting_internal_name_spaces():
    item = course(code=" CS102 ", name=" A  B ")
    assert item.code == "CS102"
    assert item.name == "A  B"


@pytest.mark.parametrize("field", ["code", "name"])
@pytest.mark.parametrize("value", ["", "   "])
def test_course_rejects_empty_code_or_name(field, value):
    kwargs = {field: value}
    with pytest.raises(ValidationError) as exc_info:
        course(**kwargs)
    assert field in str(exc_info.value).lower()
    assert repr(value) in str(exc_info.value)


def test_course_code_and_name_must_be_strings():
    with pytest.raises(ValidationError, match="course code"):
        course(code=123)
    with pytest.raises(ValidationError, match="course name"):
        course(name=None)


def test_course_name_length_boundaries():
    assert len(course(name="x" * 100).name) == 100
    with pytest.raises(ValidationError, match="100"):
        course(name="x" * 101)


def test_course_rejects_non_enum_status():
    with pytest.raises(ValidationError) as exc_info:
        course(status="completed")
    assert "status" in str(exc_info.value).lower()
    assert "'completed'" in str(exc_info.value)


def test_course_completed_requires_grade():
    with pytest.raises(ValidationError, match="COMPLETED"):
        course(status=CourseStatus.COMPLETED, grade=None)


def test_course_in_progress_requires_no_grade():
    with pytest.raises(ValidationError, match="IN_PROGRESS"):
        course(status=CourseStatus.IN_PROGRESS, grade="A")


def test_course_normalizes_grade_and_does_not_check_table_membership():
    assert course(grade=" b+ ").grade == "B+"
    assert course(grade="Z").grade == "Z"


def test_course_completed_grade_must_be_string():
    with pytest.raises(ValidationError) as exc_info:
        course(grade=4)
    assert "grade" in str(exc_info.value).lower()
    assert "4" in str(exc_info.value)
    assert "string" in str(exc_info.value).lower()


def test_semester_cleans_name_and_keeps_capitalization():
    assert Semester("  Fall   2026 ").name == "Fall 2026"


@pytest.mark.parametrize("name", ["", "   "])
def test_semester_rejects_empty_name(name):
    with pytest.raises(ValidationError) as exc_info:
        Semester(name)
    assert "semester name" in str(exc_info.value).lower()
    assert repr(name) in str(exc_info.value)


def test_semester_name_length_boundaries():
    assert len(Semester("x" * 50).name) == 50
    with pytest.raises(ValidationError, match="50"):
        Semester("x" * 51)


def test_semester_rejects_non_string_name():
    with pytest.raises(ValidationError, match="semester name"):
        Semester(42)


def test_semester_rejects_duplicate_course_codes_ignoring_case():
    semester = Semester("Fall")
    semester.add_course(course(code="CS101"))
    with pytest.raises(ValidationError, match="Duplicate"):
        semester.add_course(course(code="cs101"))
    assert len(semester.courses) == 1


def test_same_course_code_is_allowed_in_different_semesters():
    first, second = Semester("Fall"), Semester("Spring")
    first.add_course(course(code="CS101"))
    second.add_course(course(code="cs101"))
    assert len(first.courses) == len(second.courses) == 1


def test_semester_replace_can_keep_its_code():
    semester = Semester("Fall", [course(code="CS101")])
    replacement = course(code="cs101", name="Updated", grade="B")
    semester.replace_course("CS101", replacement)
    assert semester.courses == [replacement]


def test_semester_replace_rejects_code_of_another_course_atomically():
    semester = Semester("Fall", [course(code="CS101"), course(code="CS102", grade="B")])
    before = tuple(semester.courses)
    with pytest.raises(ValidationError, match="Duplicate"):
        semester.replace_course("CS101", course(code="cs102", grade="C"))
    assert tuple(semester.courses) == before


def test_semester_find_and_delete_course_case_insensitively():
    semester = Semester("Fall", [course(code="CS101")])
    assert semester.find_course(" cs101 ").code == "CS101"
    semester.delete_course("cs101")
    assert semester.courses == []


def test_semester_failed_mutations_leave_courses_unchanged():
    semester = Semester("Fall", [course(code="CS101")])
    before = tuple(semester.courses)
    with pytest.raises(ValidationError):
        semester.add_course(course(code="cs101"))
    with pytest.raises(ValidationError):
        semester.replace_course("missing", course(code="CS102"))
    with pytest.raises(ValidationError):
        semester.delete_course("missing")
    assert tuple(semester.courses) == before


def test_student_name_rules_and_rename():
    student = profile(name="  Student Name  ")
    assert student.name == "Student Name"
    student.rename("  New Name  ")
    assert student.name == "New Name"
    with pytest.raises(ValidationError, match="student name"):
        student.rename("   ")
    with pytest.raises(ValidationError, match="100"):
        student.rename("x" * 101)


def test_student_name_length_boundaries_and_type():
    assert len(profile(name="x" * 100).name) == 100
    with pytest.raises(ValidationError, match="100"):
        profile(name="x" * 101)
    with pytest.raises(ValidationError, match="student name"):
        profile(name=None)


def test_student_requires_grading_table():
    with pytest.raises(ValidationError, match="GradingTable"):
        Student("Student", "4.0-plus-only")


def test_student_semester_names_are_unique_after_cleaning_and_casefolding():
    student = profile()
    student.add_semester(" Fall 2026 ")
    with pytest.raises(ValidationError, match="Duplicate semester"):
        student.add_semester("fall   2026")
    student.add_semester("Fall2026")
    assert [s.name for s in student.semesters] == ["Fall 2026", "Fall2026"]


def test_student_rename_semester_allows_own_name_different_capitalization():
    student = profile()
    student.add_semester("Fall 2026")
    student.rename_semester("fall 2026", "FALL 2026")
    assert student.semesters[0].name == "FALL 2026"


def test_student_rename_semester_rejects_another_semesters_name_atomically():
    student = profile()
    student.add_semester("Fall 2026")
    student.add_semester("Spring 2027")
    before = snapshot(student)
    with pytest.raises(ValidationError, match="Duplicate semester"):
        student.rename_semester("Fall 2026", " spring   2027 ")
    assert snapshot(student) == before


def test_student_semester_name_maximum_length():
    student = profile()
    student.add_semester("x" * 50)
    before = snapshot(student)
    with pytest.raises(ValidationError, match="50"):
        student.add_semester("x" * 51)
    assert snapshot(student) == before


def test_student_set_table_lock_and_unlock_after_all_courses_deleted():
    student = profile("4.0-plus-only")
    alternative = preset_table("4.0-plus-minus")
    student.set_table(alternative)
    semester = student.add_semester("Fall")
    student.add_course("Fall", course(grade="A"))
    before = snapshot(student)
    with pytest.raises(ValidationError, match="while the student has courses"):
        student.set_table(preset_table("5.0-plus-only"))
    assert snapshot(student) == before
    student.delete_course("Fall", "CS101")
    assert student.has_courses is False
    student.set_table(preset_table("5.0-plus-only"))
    assert student.table.table_id == "5.0-plus-only"
    assert semester.courses == []


def test_student_in_progress_course_does_not_require_grade_lookup():
    student = profile("4.0-plus-only")
    student.add_semester("Fall")
    item = course(status=CourseStatus.IN_PROGRESS, grade=None)
    student.add_course("Fall", item)
    assert student.find_semester("Fall").courses == [item]


def test_student_grade_membership_depends_on_active_table():
    student = profile("4.0-plus-minus")
    student.add_semester("Fall")
    student.add_course("Fall", course(grade="A-"))
    strict_student = profile("4.0-plus-only")
    strict_student.add_semester("Fall")
    before = snapshot(strict_student)
    with pytest.raises(ValidationError) as exc_info:
        strict_student.add_course("Fall", course(grade="A-"))
    assert "A-" in str(exc_info.value)
    assert "4.0-plus-only" in str(exc_info.value)
    assert snapshot(strict_student) == before


def test_student_custom_table_accepts_only_its_grades():
    custom = build_custom_table([("A", "4.00"), ("B", "3.00"), ("F", "0.00")])
    student = Student("Student", custom)
    student.add_semester("Fall")
    student.add_course("Fall", course(grade="a"))
    before = snapshot(student)
    with pytest.raises(ValidationError, match="C+"):
        student.add_course("Fall", course(code="CS102", grade="C+"))
    assert snapshot(student) == before


def test_student_constructor_validates_duplicate_semester_names():
    with pytest.raises(ValidationError, match="Duplicate semester"):
        Student("Student", preset_table("4.0-plus-only"), [Semester("Fall"), Semester(" fall ")])


def test_student_constructor_validates_duplicate_course_codes():
    semester = Semester("Fall")
    semester.courses.extend([course(code="CS101"), course(code="cs101", grade="B")])
    with pytest.raises(ValidationError, match="Duplicate course"):
        Student("Student", preset_table("4.0-plus-only"), [semester])


def test_student_constructor_validates_grade_membership():
    semester = Semester("Fall", [course(grade="Z")])
    with pytest.raises(ValidationError) as exc_info:
        Student("Student", preset_table("4.0-plus-only"), [semester])
    assert "Z" in str(exc_info.value)


def test_student_constructor_preserves_semester_order_and_validates_courses():
    first = Semester("Fall", [course(code="CS101", grade="A")])
    second = Semester("Spring", [course(code="CS101", grade="B")])
    student = Student("Student", preset_table("4.0-plus-only"), [first, second])
    assert student.semesters == [first, second]
    assert student.semesters[0].name == "Fall"
    assert student.semesters[1].name == "Spring"


def test_student_constructor_rejects_non_semester_initial_data():
    with pytest.raises(ValidationError, match="Semester"):
        Student("Student", preset_table("4.0-plus-only"), ["Fall"])


def test_student_find_semester_ignores_case_and_extra_whitespace():
    student = profile()
    added = student.add_semester("Fall 2026")
    assert student.find_semester("  fall   2026 ") is added
    with pytest.raises(ValidationError, match="was not found"):
        student.find_semester("Winter 2026")


def test_student_delete_semester_removes_it_and_its_courses():
    student = profile()
    student.add_semester("Fall")
    student.add_course("Fall", course())
    student.delete_semester(" fall ")
    assert student.semesters == []
    assert student.has_courses is False


def test_student_replace_course_validates_grade_and_replacement_rules_atomically():
    student = profile()
    student.add_semester("Fall")
    student.add_course("Fall", course())
    student.add_course("Fall", course(code="CS102", grade="B"))
    before = snapshot(student)
    with pytest.raises(ValidationError):
        student.replace_course("Fall", "CS101", course(code="CS101", grade="A-"))
    assert snapshot(student) == before
    with pytest.raises(ValidationError, match="Duplicate"):
        student.replace_course("Fall", "CS101", course(code="CS102", grade="B"))
    assert snapshot(student) == before


def test_student_successful_replace_delete_and_find_course():
    student = profile()
    student.add_semester("Fall")
    student.add_course("Fall", course())
    replacement = course(name="Revised", grade="B")
    student.replace_course("Fall", "cs101", replacement)
    assert student.find_semester("Fall").find_course("CS101") is replacement
    student.delete_course("Fall", "CS101")
    assert student.has_courses is False


def test_failed_student_mutations_leave_state_unchanged():
    student = profile()
    student.add_semester("Fall")
    student.add_semester("Spring")
    student.add_course("Fall", course())
    student.add_course("Fall", course(code="CS102", grade="B"))

    operations = [
        lambda: student.rename("   "),
        lambda: student.set_table(preset_table("5.0-plus-only")),
        lambda: student.add_semester("fall"),
        lambda: student.rename_semester("Fall", "   "),
        lambda: student.rename_semester("Fall", "Spring"),
        lambda: student.delete_semester("Missing"),
        lambda: student.add_course("Missing", course(code="CS102")),
        lambda: student.add_course("Fall", course(code="CS101")),
        lambda: student.add_course("Fall", course(code="CS102", grade="Z")),
        lambda: student.replace_course("Missing", "CS101", course(code="CS101")),
        lambda: student.replace_course("Fall", "Missing", course(code="CS102")),
        lambda: student.replace_course("Fall", "CS101", course(code="CS102", grade="B")),
        lambda: student.replace_course("Fall", "CS101", course(code="CS101", grade="Z")),
        lambda: student.delete_course("Missing", "CS101"),
        lambda: student.delete_course("Fall", "Missing"),
    ]
    for operation in operations:
        before = snapshot(student)
        with pytest.raises(ValidationError):
            operation()
        assert snapshot(student) == before


def test_grading_errors_are_converted_to_validation_errors_with_original_message():
    student = profile()
    student.add_semester("Fall")
    with pytest.raises(ValidationError) as exc_info:
        student.add_course("Fall", course(grade="A-"))
    assert "Grade 'A-' is not present in grading table '4.0-plus-only'." in str(exc_info.value)
    assert isinstance(exc_info.value.__cause__, GradingError)


def test_no_stateful_calculations_are_stored_on_models():
    student = profile()
    assert not hasattr(student, "gpa")
    assert not hasattr(student, "cgpa")
    assert not hasattr(student, "predictions")


def test_model_module_has_no_input_or_print_calls_and_no_float_usage():
    from pathlib import Path
    import ast

    source_path = Path(__file__).parents[1] / "gpa_tracker" / "models.py"
    source = source_path.read_text(encoding="utf-8")
    tree = ast.parse(source)
    calls = [
        node.func.id
        for node in ast.walk(tree)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
    ]
    assert "input" not in calls
    assert "print" not in calls
    # The word is allowed in documentation/messages, but not as a runtime symbol.
    assert not any(
        isinstance(node, ast.Name) and node.id == "float"
        for node in ast.walk(tree)
    )
