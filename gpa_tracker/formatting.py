"""Pure text formatting helpers for GPA Tracker."""

from collections.abc import Sequence
from decimal import Decimal

from .calculator import (
    AcademicResult,
    SemesterResult,
    round_half_up,
)
from .models import Course, CourseStatus, Semester
from .prediction import PredictionResult


def format_gpa(value: Decimal | None) -> str:
    """Format a GPA to two decimal places, or N/A when unavailable."""
    if value is None:
        return "N/A"
    return f"{round_half_up(value):.2f}"


def format_points(value: Decimal) -> str:
    """Format quality points to two decimal places."""
    return f"{round_half_up(value):.2f}"


def format_course_status(course: Course) -> str:
    """Return the display label for a course's status."""
    if course.status is CourseStatus.COMPLETED:
        return "Completed"
    return "In Progress"


def format_course_list(semester: Semester) -> str:
    """Format a semester title and its courses in stored order."""
    lines = [semester.name]

    if not semester.courses:
        lines.append("  No courses yet.")
        return "\n".join(lines) + "\n"

    for course in semester.courses:
        code = course.code
        name = course.name[:26]
        credits = course.credits
        status = format_course_status(course)
        grade = course.grade if course.status is CourseStatus.COMPLETED else "-"
        lines.append(
            f"{code:<8}{name:<26}{credits:>3} cr  {status:<12}{grade}"
        )

    return "\n".join(lines) + "\n"


def format_semester_summary(result: SemesterResult) -> str:
    """Format one semester's calculated summary."""
    return (
        f"Semester: {result.name}\n"
        f"  Courses:            {result.course_count}\n"
        f"  Graded credits:     {result.graded_credits}\n"
        f"  Quality points:     {format_points(result.quality_points)}\n"
        f"  Semester GPA:       {format_gpa(result.gpa)}\n"
        f"  In progress:        {result.in_progress_count} course(s), "
        "excluded from GPA\n"
    )


def format_academic_summary(result: AcademicResult) -> str:
    """Format academic totals and best/lowest semester names."""
    best_semester = result.best_semester or "N/A"
    lowest_semester = result.lowest_semester or "N/A"

    return (
        "Academic summary\n"
        f"  Semesters:          {result.semester_count}\n"
        f"  Completed credits:  {result.completed_credits}\n"
        f"  Quality points:     {format_points(result.quality_points)}\n"
        f"  CGPA:               {format_gpa(result.cgpa)}\n"
        f"  Best semester:      {best_semester}\n"
        f"  Lowest semester:    {lowest_semester}\n"
    )


def format_summary_screen(
    academic: AcademicResult,
    semesters: Sequence[SemesterResult],
) -> str:
    """Format semester summaries and then the academic summary."""
    academic_text = format_academic_summary(academic)

    if not semesters:
        return f"No semesters yet.\n{academic_text}"

    semester_text = "\n\n".join(
        format_semester_summary(semester).removesuffix("\n")
        for semester in semesters
    )
    return f"{semester_text}\n\n{academic_text}"


def format_prediction(result: PredictionResult) -> str:
    """Format an incomplete prediction or actual/predicted comparison."""
    if result.missing_codes:
        missing_codes = ", ".join(result.missing_codes)
        return (
            f"Prediction for {result.semester_name}: incomplete.\n"
            f"Expected grades still needed for: {missing_codes}\n"
        )

    actual_gpa = format_gpa(result.actual.gpa)
    predicted_gpa = format_gpa(result.predicted_gpa)
    actual_credits = str(result.actual.completed_credits)
    predicted_credits = (
        "N/A"
        if result.predicted_completed_credits is None
        else str(result.predicted_completed_credits)
    )
    actual_cgpa = format_gpa(result.actual_cgpa)
    predicted_cgpa = format_gpa(result.predicted_cgpa)

    return (
        f"Prediction for {result.semester_name}\n"
        "                       Actual     Predicted\n"
        f"Semester GPA           {actual_gpa:>8}   {predicted_gpa:>9}\n"
        f"Completed credits      {actual_credits:>8}   "
        f"{predicted_credits:>9}\n"
        f"CGPA                   {actual_cgpa:>8}   "
        f"{predicted_cgpa:>9}\n"
    )
