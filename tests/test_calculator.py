from copy import deepcopy
from dataclasses import FrozenInstanceError
from decimal import Decimal

import pytest

from gpa_tracker.calculator import (
    AcademicResult,
    SemesterResult,
    academic_result,
    best_and_lowest,
    quality_points,
    round_half_up,
    semester_result,
)
from gpa_tracker.grading import build_custom_table, preset_table
from gpa_tracker.models import Course, CourseStatus, Semester, Student


def course(code, grade, credits=3, status=CourseStatus.COMPLETED):
    return Course(code=code, name=f"Course {code}", grade=grade, credits=credits, status=status)


def semester(name, courses):
    return Semester(name=name, courses=list(courses))


def student(table, semesters):
    return Student(name="Test Student", table=table, semesters=list(semesters))


def test_w1_quality_points_plus_only_b_plus():
    assert quality_points(course("CS1", "B+", 3), preset_table("4.0-plus-only")) == Decimal("10.50")


def test_w2_quality_points_plus_minus_b_plus():
    assert quality_points(course("CS1", "B+", 3), preset_table("4.0-plus-minus")) == Decimal("9.99")


def test_w3_semester_gpa_and_quality_points():
    result = semester_result(semester("Fall", [course("A", "A", 3), course("B", "B", 4)]), preset_table("4.0-plus-only"))
    assert result.quality_points == Decimal("23.25")
    assert result.graded_credits == 7
    assert round_half_up(result.gpa) == Decimal("3.32")


def test_w4_cgpa_is_credit_weighted():
    profile = student(preset_table("4.0-plus-only"), [
        semester("Sem 1", [course("A", "A+", 1)]),
        semester("Sem 2", [course("B", "B", 5)]),
    ])
    result = academic_result(profile)
    assert result.cgpa == Decimal(19) / Decimal(6)
    assert round_half_up(result.cgpa) == Decimal("3.17")


def test_w5_half_up_gpa():
    result = semester_result(semester("Fall", [course("A", "A", 4), course("C", "C+", 4)]), preset_table("4.0-plus-only"))
    assert result.gpa == Decimal("3.125")
    assert round_half_up(result.gpa) == Decimal("3.13")


def test_w6_f_counts_in_gpa_but_not_completed_credits():
    result = semester_result(semester("Fall", [course("F", "F", 3), course("A", "A", 3)]), preset_table("5.0-plus-only"))
    assert result.quality_points == Decimal("17.25")
    assert result.gpa == Decimal("2.875")
    assert round_half_up(result.gpa) == Decimal("2.88")
    assert result.completed_credits == 3


def test_w7_in_progress_excluded_from_every_calculation():
    result = semester_result(semester("Fall", [
        course("A", "A", 3),
        course("IP", None, 3, CourseStatus.IN_PROGRESS),
    ]), preset_table("4.0-plus-only"))
    assert result.gpa == Decimal("3.75")
    assert result.completed_credits == 3
    assert result.graded_credits == 3
    assert result.quality_points == Decimal("11.25")


@pytest.mark.parametrize(("value", "expected"), [
    ("3.125", "3.13"),
    ("2.875", "2.88"),
    ("3.124", "3.12"),
    ("3.1249", "3.12"),
    ("0.005", "0.01"),
])
def test_round_half_up(value, expected):
    assert round_half_up(Decimal(value)) == Decimal(expected)


def test_quality_points_rejects_in_progress():
    with pytest.raises(ValueError):
        quality_points(course("IP", None, 3, CourseStatus.IN_PROGRESS), preset_table("4.0-plus-only"))


def test_semester_only_in_progress_has_no_gpa():
    result = semester_result(semester("Summer", [
        course("IP1", None, 3, CourseStatus.IN_PROGRESS),
        course("IP2", None, 4, CourseStatus.IN_PROGRESS),
    ]), preset_table("4.0-plus-only"))
    assert result.gpa is None
    assert result.in_progress_count == result.course_count == 2
    assert result.completed_count == result.graded_credits == 0


def test_w10_tie_keeps_earliest_semester_for_best_and_lowest():
    results = [
        SemesterResult("First", 1, 1, 0, 3, 3, Decimal("9"), Decimal("3")),
        SemesterResult("Second", 1, 1, 0, 3, 3, Decimal("9"), Decimal("3")),
    ]
    assert best_and_lowest(results) == ("First", "First")


def test_w11_no_completed_courses_returns_none_values():
    profile = student(preset_table("4.0-plus-only"), [
        semester("Only", [course("IP", None, 3, CourseStatus.IN_PROGRESS)])
    ])
    sem_result = semester_result(profile.semesters[0], profile.table)
    result = academic_result(profile)
    assert sem_result.gpa is None
    assert result.cgpa is None
    assert result.best_semester is result.lowest_semester is None


def test_w12_custom_table_f_counts_but_not_completed_credits():
    table = build_custom_table([("A", "4.00"), ("F", "0.00")])
    result = semester_result(semester("Fall", [course("A", "A", 3), course("F", "F", 3)]), table)
    assert result.gpa == Decimal("2.00")
    assert result.completed_credits == 3


def test_w14_retake_attempts_across_semesters_both_count():
    profile = student(preset_table("4.0-plus-only"), [
        semester("Fall 2025", [course("CS101", "F", 3)]),
        semester("Spring 2026", [course("CS101", "B", 3)]),
    ])
    result = academic_result(profile)
    assert result.cgpa == Decimal("1.50")
    assert result.quality_points == Decimal("9.00")
    assert result.completed_credits == 3


def test_in_progress_does_not_change_academic_result():
    table = preset_table("4.0-plus-only")
    baseline = student(table, [
        semester("Sem 1", [course("A", "A+", 1)]),
        semester("Sem 2", [course("B", "B", 5)]),
    ])
    augmented = student(table, [
        semester("Sem 1", [course("A", "A+", 1), course("IP1", None, 3, CourseStatus.IN_PROGRESS)]),
        semester("Sem 2", [course("B", "B", 5), course("IP2", None, 4, CourseStatus.IN_PROGRESS)]),
    ])
    before = academic_result(baseline)
    after = academic_result(augmented)
    assert (after.cgpa, after.completed_credits, after.quality_points, after.best_semester, after.lowest_semester) == (
        before.cgpa, before.completed_credits, before.quality_points, before.best_semester, before.lowest_semester
    )


def test_lowest_tie_also_keeps_earliest():
    results = [
        SemesterResult("First", 1, 1, 0, 3, 3, Decimal("3"), Decimal("1")),
        SemesterResult("Middle", 1, 1, 0, 3, 3, Decimal("6"), Decimal("2")),
        SemesterResult("Last", 1, 1, 0, 3, 3, Decimal("3"), Decimal("1")),
    ]
    assert best_and_lowest(results) == ("Middle", "First")


def test_academic_result_repeatable_and_student_unchanged():
    profile = student(preset_table("4.0-plus-only"), [
        semester("Fall", [course("A", "A", 3)]),
        semester("Spring", [course("B", "B", 3)]),
    ])
    before = deepcopy(profile, {id(profile.table): profile.table})
    first = academic_result(profile)
    second = academic_result(profile)
    assert first == second
    assert profile == before


def test_unrounded_values_decide_best_semester():
    table = build_custom_table([("A", "3.13"), ("B", "3.12"), ("F", "0.00")])
    profile = student(table, [
        semester("Higher", [course("A", "A", 3), course("F1", "F", 497)]),
        semester("Lower", [course("B", "B", 3), course("F2", "F", 497)]),
    ])
    result = academic_result(profile)
    higher = semester_result(profile.semesters[0], table)
    lower = semester_result(profile.semesters[1], table)
    assert round_half_up(higher.gpa) == round_half_up(lower.gpa) == Decimal("0.02")
    assert higher.gpa > lower.gpa
    assert result.best_semester == "Higher"


def test_result_dataclasses_are_frozen():
    result = SemesterResult("Fall", 1, 1, 0, 3, 3, Decimal("9"), Decimal("3"))
    with pytest.raises(FrozenInstanceError):
        result.name = "Changed"


def test_semester_result_does_not_mutate_semester():
    sem = semester("Fall", [course("A", "A", 3)])
    before = deepcopy(sem)
    assert semester_result(sem, preset_table("4.0-plus-only")) == semester_result(sem, preset_table("4.0-plus-only"))
    assert sem == before
