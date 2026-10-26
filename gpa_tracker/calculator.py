"""Pure GPA calculation functions using exact Decimal arithmetic."""

from collections.abc import Sequence
from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP

from .grading import GradingTable
from .models import Course, CourseStatus, Semester, Student

_TWO_PLACES = Decimal("0.01")
_ZERO = Decimal("0")


def round_half_up(value: Decimal) -> Decimal:
    """Round a Decimal to two places using ROUND_HALF_UP."""
    return value.quantize(_TWO_PLACES, rounding=ROUND_HALF_UP)


def quality_points(course: Course, table: GradingTable) -> Decimal:
    """Return a completed course's grade points multiplied by its credits."""
    if course.status is CourseStatus.IN_PROGRESS:
        raise ValueError("Quality points are unavailable for an in-progress course.")
    return table.points_for(course.grade) * course.credits


@dataclass(frozen=True)
class SemesterResult:
    name: str
    course_count: int
    completed_count: int
    in_progress_count: int
    graded_credits: int
    completed_credits: int
    quality_points: Decimal
    gpa: Decimal | None


@dataclass(frozen=True)
class AcademicResult:
    semester_count: int
    completed_credits: int
    quality_points: Decimal
    cgpa: Decimal | None
    best_semester: str | None
    lowest_semester: str | None


def semester_result(semester: Semester, table: GradingTable) -> SemesterResult:
    """Calculate a semester result without mutating its model."""
    course_count = len(semester.courses)
    completed_count = 0
    in_progress_count = 0
    graded_credits = 0
    completed_credits = 0
    total_quality_points = _ZERO

    for course in semester.courses:
        if course.status is CourseStatus.IN_PROGRESS:
            in_progress_count += 1
            continue

        completed_count += 1
        graded_credits += course.credits
        total_quality_points += quality_points(course, table)
        if table.is_passing(course.grade):
            completed_credits += course.credits

    gpa = total_quality_points / graded_credits if graded_credits else None
    return SemesterResult(
        name=semester.name,
        course_count=course_count,
        completed_count=completed_count,
        in_progress_count=in_progress_count,
        graded_credits=graded_credits,
        completed_credits=completed_credits,
        quality_points=total_quality_points,
        gpa=gpa,
    )


def best_and_lowest(
    results: Sequence[SemesterResult],
) -> tuple[str | None, str | None]:
    """Return best and lowest GPA semester names; ties keep the earliest."""
    best: SemesterResult | None = None
    lowest: SemesterResult | None = None

    for result in results:
        if result.gpa is None:
            continue
        if best is None or result.gpa > best.gpa:
            best = result
        if lowest is None or result.gpa < lowest.gpa:
            lowest = result

    return (
        best.name if best is not None else None,
        lowest.name if lowest is not None else None,
    )


def academic_result(student: Student) -> AcademicResult:
    """Calculate profile totals and semester extrema without mutation."""
    results = [
        semester_result(semester, student.table)
        for semester in student.semesters
    ]
    total_quality_points = sum(
        (result.quality_points for result in results), _ZERO
    )
    total_graded_credits = sum(result.graded_credits for result in results)
    completed_credits = sum(result.completed_credits for result in results)
    cgpa = (
        total_quality_points / total_graded_credits
        if total_graded_credits
        else None
    )
    best_semester, lowest_semester = best_and_lowest(results)

    return AcademicResult(
        semester_count=len(student.semesters),
        completed_credits=completed_credits,
        quality_points=total_quality_points,
        cgpa=cgpa,
        best_semester=best_semester,
        lowest_semester=lowest_semester,
    )
