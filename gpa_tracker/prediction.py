"""Pure what-if GPA predictions for one semester's in-progress courses."""

from collections.abc import Mapping
from dataclasses import dataclass
from decimal import Decimal

from .calculator import (
    SemesterResult,
    academic_result,
    quality_points,
    semester_result,
)
from .grading import GradingError, normalize_grade
from .models import CourseStatus, Student, ValidationError

_ZERO = Decimal("0")


def _code_key(code: object) -> str:
    """Normalize a course code for case-insensitive matching."""
    if not isinstance(code, str):
        raise ValidationError(
            f"Invalid course code {code!r}: expected a string."
        )
    cleaned = code.strip()
    if not cleaned:
        raise ValidationError(
            f"Invalid course code {code!r}: code cannot be empty or whitespace-only."
        )
    return cleaned.casefold()


def _expected_grade(value: object, student: Student, code: str) -> str:
    """Normalize and validate an expected grade against the active table."""
    try:
        grade = normalize_grade(value)  # type: ignore[arg-type]
        student.table.points_for(grade)
    except (GradingError, TypeError) as exc:
        raise ValidationError(
            f"Invalid expected grade {value!r} for course {code!r}: "
            f"{exc if isinstance(exc, Exception) else 'invalid grade' }"
        ) from exc
    return grade


@dataclass(frozen=True)
class PredictionResult:
    """Actual semester result alongside optional what-if values."""

    semester_name: str
    actual: SemesterResult
    missing_codes: tuple[str, ...]
    predicted_gpa: Decimal | None
    predicted_completed_credits: int | None
    actual_cgpa: Decimal | None
    predicted_cgpa: Decimal | None


def predict_semester(
    student: Student,
    semester_name: str,
    expected: Mapping[str, str],
) -> PredictionResult:
    """Predict semester GPA and CGPA without changing the student or inputs.

    Completed courses retain their actual grades. Expected grades are applied
    only to in-progress courses in the selected semester. If any such course
    has no expected grade, predicted GPA, completed credits, and CGPA are None.
    """
    semester = student.find_semester(semester_name)
    in_progress = [
        course for course in semester.courses
        if course.status is CourseStatus.IN_PROGRESS
    ]
    if not in_progress:
        raise ValidationError(
            f"Semester {semester.name!r} has no in-progress courses to predict."
        )

    courses_by_key = {_code_key(course.code): course for course in in_progress}
    normalized_expected: dict[str, str] = {}

    for raw_code, raw_grade in expected.items():
        key = _code_key(raw_code)
        course = courses_by_key.get(key)
        if course is None:
            raise ValidationError(
                f"Expected grade entry for course {raw_code!r} does not match "
                f"an in-progress course in semester {semester.name!r}."
            )
        if key in normalized_expected:
            raise ValidationError(
                f"Duplicate expected grade entries for course {course.code!r} "
                "are not allowed when course codes differ only by case."
            )
        normalized_expected[key] = _expected_grade(raw_grade, student, course.code)

    missing_codes = tuple(
        course.code for course in in_progress
        if _code_key(course.code) not in normalized_expected
    )
    actual = semester_result(semester, student.table)
    actual_cgpa = academic_result(student).cgpa

    if missing_codes:
        return PredictionResult(
            semester_name=semester.name,
            actual=actual,
            missing_codes=missing_codes,
            predicted_gpa=None,
            predicted_completed_credits=None,
            actual_cgpa=actual_cgpa,
            predicted_cgpa=None,
        )

    semester_quality_points = _ZERO
    semester_credits = 0
    predicted_completed_credits = 0

    for course in semester.courses:
        semester_credits += course.credits
        if course.status is CourseStatus.COMPLETED:
            semester_quality_points += quality_points(course, student.table)
            if student.table.is_passing(course.grade):
                predicted_completed_credits += course.credits
            continue

        grade = normalized_expected[_code_key(course.code)]
        semester_quality_points += student.table.points_for(grade) * course.credits
        if student.table.is_passing(grade):
            predicted_completed_credits += course.credits

    predicted_gpa = semester_quality_points / semester_credits

    other_quality_points = _ZERO
    other_graded_credits = 0
    for other_semester in student.semesters:
        if other_semester is semester:
            continue
        for course in other_semester.courses:
            if course.status is CourseStatus.IN_PROGRESS:
                continue
            other_quality_points += quality_points(course, student.table)
            other_graded_credits += course.credits

    predicted_cgpa_denominator = other_graded_credits + semester_credits
    predicted_cgpa = (
        (other_quality_points + semester_quality_points)
        / predicted_cgpa_denominator
        if predicted_cgpa_denominator
        else None
    )

    return PredictionResult(
        semester_name=semester.name,
        actual=actual,
        missing_codes=(),
        predicted_gpa=predicted_gpa,
        predicted_completed_credits=predicted_completed_credits,
        actual_cgpa=actual_cgpa,
        predicted_cgpa=predicted_cgpa,
    )