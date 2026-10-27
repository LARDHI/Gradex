"""Acceptance tests for pure what-if GPA prediction."""

from copy import deepcopy
from dataclasses import FrozenInstanceError
from decimal import Decimal

import pytest

from gpa_tracker.calculator import academic_result, best_and_lowest, semester_result
from gpa_tracker.grading import preset_table
from gpa_tracker.models import Course, CourseStatus, Semester, Student, ValidationError
from gpa_tracker.prediction import PredictionResult, clear_expected, predict_semester


def course(code, grade=None, credits=3, status=CourseStatus.COMPLETED):
    return Course(
        code=code,
        name=f"Course {code}",
        credits=credits,
        status=status,
        grade=grade,
    )


def make_student(semesters, table_id="4.0-plus-only"):
    return Student("Test Student", preset_table(table_id), semesters)


def in_progress(code, credits=3):
    return course(code, None, credits, CourseStatus.IN_PROGRESS)


def test_w8_predicts_semester_gpa_for_completed_and_in_progress_courses():
    student = make_student([
        Semester("Semester A", [course("DONE", "A", 3), in_progress("NOW", 3)])
    ])

    result = predict_semester(student, "Semester A", {"now": "b+"})

    assert result.predicted_gpa == Decimal("21.75") / Decimal("6")
    assert result.predicted_gpa == Decimal("3.625")
    assert result.predicted_completed_credits == 6
    assert result.actual.gpa == Decimal("11.25") / Decimal("3")
    assert result.missing_codes == ()


def test_w9_predicted_cgpa_uses_other_completed_semesters():
    student = make_student([
        Semester("Sem 1", [course("OLD", "B", 3)]),
        Semester("Sem 2", [course("DONE", "A", 3), in_progress("NOW", 3)]),
    ])

    result = predict_semester(student, "Sem 2", {"NOW": "B+"})

    assert result.actual_cgpa == Decimal("20.25") / Decimal("6")
    assert result.actual_cgpa == Decimal("3.375")
    assert result.predicted_cgpa == Decimal("30.75") / Decimal("9")
    assert result.predicted_cgpa == Decimal("30.75") / Decimal("9")


def test_w15_clear_expected_removes_only_requested_code_and_returns_copy():
    expected = {"CS101": "A", "CS102": "B+"}
    before = expected.copy()

    cleared = clear_expected(expected, "cs101")

    assert cleared == {"CS102": "B+"}
    assert cleared is not expected
    assert expected == before


def test_expected_f_counts_in_gpa_denominator_but_not_completed_credits():
    student = make_student([
        Semester("Fall", [course("DONE", "A", 3), in_progress("NOW", 3)])
    ])

    result = predict_semester(student, "Fall", {"NOW": "F"})

    assert result.predicted_gpa == Decimal("11.25") / Decimal("6")
    assert result.predicted_completed_credits == 3


def test_missing_expected_grade_returns_none_prediction_values_in_course_order():
    student = make_student([
        Semester("Fall", [in_progress("CS101"), in_progress("CS102"), in_progress("CS103")])
    ])

    result = predict_semester(student, "Fall", {"cs102": "B"})

    assert result.missing_codes == ("CS101", "CS103")
    assert result.predicted_gpa is None
    assert result.predicted_completed_credits is None
    assert result.predicted_cgpa is None
    assert result.actual_cgpa is None


@pytest.mark.parametrize("semester_name", ["Missing", " "])
def test_unknown_semester_raises_validation_error(semester_name):
    student = make_student([Semester("Fall", [in_progress("NOW")])])
    with pytest.raises(ValidationError):
        predict_semester(student, semester_name, {"NOW": "A"})


def test_semester_without_in_progress_courses_raises_validation_error():
    student = make_student([Semester("Fall", [course("DONE", "A")])])
    with pytest.raises(ValidationError, match="no in-progress"):
        predict_semester(student, "Fall", {})


def test_invalid_expected_grade_raises_validation_error():
    student = make_student([Semester("Fall", [in_progress("NOW")])])
    with pytest.raises(ValidationError, match="A-"):
        predict_semester(student, "Fall", {"NOW": "A-"})


@pytest.mark.parametrize("unexpected_code", ["UNKNOWN", "DONE", "OTHER"])
def test_expected_code_must_be_in_progress_in_selected_semester(unexpected_code):
    student = make_student([
        Semester("Fall", [course("DONE", "A"), in_progress("NOW")]),
        Semester("Spring", [in_progress("OTHER")]),
    ])
    with pytest.raises(ValidationError, match="does not match"):
        predict_semester(student, "Fall", {unexpected_code: "B"})


def test_in_progress_courses_in_other_semesters_are_excluded_from_predicted_cgpa():
    student = make_student([
        Semester("Sem 1", [course("OLD", "B", 3), in_progress("OTHER", 9)]),
        Semester("Sem 2", [course("DONE", "A", 3), in_progress("NOW", 3)]),
    ])

    result = predict_semester(student, "Sem 2", {"NOW": "B+"})

    assert result.predicted_cgpa == Decimal("30.75") / Decimal("9")


def test_expected_course_code_matching_is_case_insensitive_and_trimmed():
    student = make_student([Semester("Fall", [in_progress("CS101")])])
    result = predict_semester(student, "fall", {" cs101 ": " a "})
    assert result.predicted_gpa == Decimal("3.75")


def test_prediction_does_not_change_best_or_lowest_semester():
    student = make_student([
        Semester("First", [course("A", "B", 3)]),
        Semester("Current", [in_progress("NOW", 3)]),
        Semester("Last", [course("C", "A", 3)]),
    ])
    before = academic_result(student)
    result = predict_semester(student, "Current", {"NOW": "A+"})
    after = academic_result(student)

    assert result.predicted_gpa == Decimal("4")
    assert (after.best_semester, after.lowest_semester) == (
        before.best_semester,
        before.lowest_semester,
    )


def test_prediction_does_not_mutate_student_or_expected_mapping():
    student = make_student([
        Semester("Sem 1", [course("OLD", "B", 3)]),
        Semester("Sem 2", [course("DONE", "A", 3), in_progress("NOW", 3)]),
    ])
    student_before = deepcopy(student, {id(student.table): student.table})
    expected = {"now": "b+"}
    expected_before = expected.copy()

    predict_semester(student, "Sem 2", expected)

    assert student == student_before
    assert expected == expected_before


def test_clear_expected_is_case_insensitive_and_does_not_mutate_input():
    expected = {"Cs101": "A", "CS102": "B", "CS103": "C"}
    before = expected.copy()
    cleared = clear_expected(expected, "CS102")
    assert cleared == {"Cs101": "A", "CS103": "C"}
    assert expected == before


def test_prediction_result_is_frozen():
    student = make_student([Semester("Fall", [in_progress("NOW")])])
    result = predict_semester(student, "Fall", {"NOW": "A"})
    with pytest.raises(FrozenInstanceError):
        result.semester_name = "Changed"


def test_actual_semester_result_is_not_replaced_by_predicted_values():
    student = make_student([Semester("Fall", [course("DONE", "A", 3), in_progress("NOW", 3)])])
    actual_before = semester_result(student.semesters[0], student.table)
    result = predict_semester(student, "Fall", {"NOW": "F"})
    assert result.actual == actual_before
    assert result.actual.gpa == Decimal("3.75")
    assert result.predicted_gpa == Decimal("11.25") / Decimal("6")


def test_duplicate_expected_keys_differing_only_by_case_are_rejected():
    student = make_student([Semester("Fall", [in_progress("NOW")])])
    with pytest.raises(ValidationError, match="Duplicate expected"):
        predict_semester(student, "Fall", {"NOW": "A", "now": "B"})


def test_clear_expected_does_not_remove_nonmatching_codes():
    expected = {"CS101": "A", "CS102": "B"}
    assert clear_expected(expected, "cs103") == expected