from decimal import Decimal

from gpa_tracker.calculator import (
    academic_result,
    semester_result,
)
from gpa_tracker.formatting import (
    format_academic_summary,
    format_course_list,
    format_course_status,
    format_gpa,
    format_points,
    format_prediction,
    format_semester_summary,
    format_summary_screen,
)
from gpa_tracker.grading import preset_table
from gpa_tracker.models import Course, CourseStatus, Semester, Student
from gpa_tracker.prediction import predict_semester


def make_course(code, grade=None, credits=3, status=CourseStatus.COMPLETED, name=None):
    return Course(
        code=code,
        name=name if name is not None else f"Course {code}",
        credits=credits,
        status=status,
        grade=grade,
    )


def make_semester(name, courses=()):
    return Semester(name=name, courses=list(courses))


def make_student(semesters, table_id="4.0-plus-minus"):
    return Student(
        name="Test Student",
        table=preset_table(table_id),
        semesters=list(semesters),
    )


def test_format_gpa_rounding_and_missing_value():
    assert format_gpa(Decimal("3.125")) == "3.13"
    assert format_gpa(Decimal("2.875")) == "2.88"
    assert format_gpa(Decimal("3")) == "3.00"
    assert format_gpa(None) == "N/A"


def test_format_points():
    assert format_points(Decimal("9.99")) == "9.99"
    assert format_points(Decimal("17.25")) == "17.25"


def test_course_list_uses_exact_course_line_layout():
    semester = make_semester("Fall", [
        make_course("CS101", "B+", 3, name="Programming"),
        make_course("CS102", None, 3, CourseStatus.IN_PROGRESS, "Data Structures"),
    ])
    expected = (
        "Fall\n"
        f"{'CS101':<8}{'Programming':<26}{3:>3} cr  {'Completed':<12}{'B+'}\n"
        f"{'CS102':<8}{'Data Structures':<26}{3:>3} cr  {'In Progress':<12}{'-'}\n"
    )
    assert format_course_list(semester) == expected


def test_course_list_truncates_names_to_26_characters():
    name = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234"
    semester = make_semester("Fall", [
        make_course("CS101", "A", 3, name=name),
    ])
    expected_line = f"{'CS101':<8}{name[:26]:<26}{3:>3} cr  {'Completed':<12}{'A'}"
    assert format_course_list(semester) == f"Fall\n{expected_line}\n"
    assert name[:26] in format_course_list(semester)
    assert name[26:] not in format_course_list(semester)


def test_empty_course_list():
    assert format_course_list(make_semester("Summer")) == (
        "Summer\n"
        "  No courses yet.\n"
    )


def test_course_status_and_grade_labels():
    completed = make_course("CS101", "B+")
    in_progress = make_course("CS102", None, status=CourseStatus.IN_PROGRESS)
    assert format_course_status(completed) == "Completed"
    assert format_course_status(in_progress) == "In Progress"
    completed_line = format_course_list(make_semester("Fall", [completed])).splitlines()[1]
    in_progress_line = format_course_list(make_semester("Fall", [in_progress])).splitlines()[1]
    assert completed_line.endswith("B+")
    assert in_progress_line.endswith("-")


def test_semester_summary_with_completed_and_in_progress_courses():
    semester = make_semester("Fall", [
        make_course("CS101", "B+", 3),
        make_course("CS102", None, 3, CourseStatus.IN_PROGRESS),
    ])
    result = semester_result(semester, preset_table("4.0-plus-minus"))
    output = format_semester_summary(result)
    assert output == (
        "Semester: Fall\n"
        "  Courses:            2\n"
        "  Graded credits:     3\n"
        "  Quality points:     9.99\n"
        "  Semester GPA:       3.33\n"
        "  In progress:        1 course(s), excluded from GPA\n"
    )


def test_semester_summary_without_completed_courses():
    semester = make_semester("Fall", [
        make_course("CS101", None, 3, CourseStatus.IN_PROGRESS),
    ])
    result = semester_result(semester, preset_table("4.0-plus-minus"))
    output = format_semester_summary(result)
    assert "  Graded credits:     0\n" in output
    assert "  Quality points:     0.00\n" in output
    assert "  Semester GPA:       N/A\n" in output


def test_academic_summary_uses_calculator_best_and_lowest():
    profile = make_student([
        make_semester("Sem 1", [make_course("A", "A+", 1)]),
        make_semester("Sem 2", [make_course("B", "B", 5)]),
    ], "4.0-plus-only")
    result = academic_result(profile)
    output = format_academic_summary(result)
    assert "  CGPA:               3.17\n" in output
    assert f"  Best semester:      {result.best_semester}\n" in output
    assert f"  Lowest semester:    {result.lowest_semester}\n" in output


def test_academic_summary_without_completed_courses():
    profile = make_student([
        make_semester("Only", [
            make_course("IP", None, 3, CourseStatus.IN_PROGRESS),
        ]),
    ], "4.0-plus-only")
    output = format_academic_summary(academic_result(profile))
    assert "  CGPA:               N/A\n" in output
    assert "  Best semester:      N/A\n" in output
    assert "  Lowest semester:    N/A\n" in output


def test_summary_screen_without_semesters():
    profile = make_student([], "4.0-plus-only")
    academic = academic_result(profile)
    assert format_summary_screen(academic, []) == (
        "No semesters yet.\n"
        f"{format_academic_summary(academic)}"
    )


def test_summary_screen_separates_semesters_and_academic_summary():
    profile = make_student([
        make_semester("Fall", [make_course("A", "A", 3)]),
        make_semester("Spring", [make_course("B", "B", 3)]),
    ])
    academic = academic_result(profile)
    summaries = [
        semester_result(semester, profile.table)
        for semester in profile.semesters
    ]
    output = format_summary_screen(academic, summaries)
    assert output == (
        f"{format_semester_summary(summaries[0]).removesuffix(chr(10))}\n\n"
        f"{format_semester_summary(summaries[1]).removesuffix(chr(10))}\n\n"
        f"{format_academic_summary(academic)}"
    )


def test_complete_prediction_layout_and_rounding():
    profile = make_student([
        make_semester("Semester A", [
            make_course("DONE", "A", 3),
            make_course("NOW", None, 3, CourseStatus.IN_PROGRESS),
        ]),
    ], "4.0-plus-only")
    result = predict_semester(profile, "Semester A", {"NOW": "B+"})
    output = format_prediction(result)
    assert output == (
        "Prediction for Semester A\n"
        "                       Actual     Predicted\n"
        "Semester GPA               3.75        3.63\n"
        "Completed credits             3           6\n"
        "CGPA                       3.75        3.63\n"
    )


def test_incomplete_prediction_lists_only_missing_codes_in_semester_order():
    profile = make_student([
        make_semester("Fall", [
            make_course("CS101", None, 3, CourseStatus.IN_PROGRESS),
            make_course("CS102", None, 3, CourseStatus.IN_PROGRESS),
        ]),
    ], "4.0-plus-only")
    result = predict_semester(profile, "Fall", {"CS101": "A"})
    assert format_prediction(result) == (
        "Prediction for Fall: incomplete.\n"
        "Expected grades still needed for: CS102\n"
    )


def test_prediction_displays_na_for_missing_actual_gpa():
    profile = make_student([
        make_semester("Fall", [
            make_course("CS101", None, 3, CourseStatus.IN_PROGRESS),
        ]),
    ], "4.0-plus-only")
    result = predict_semester(profile, "Fall", {"CS101": "B+"})
    output = format_prediction(result)
    assert "Semester GPA                N/A        3.50\n" in output
    assert "Completed credits             0           3\n" in output


def test_output_has_no_tabs_or_ansi_escapes():
    profile = make_student([
        make_semester("Fall", [
            make_course("CS101", "B+", 3),
            make_course("CS102", None, 3, CourseStatus.IN_PROGRESS),
        ]),
    ])
    sem_result = semester_result(profile.semesters[0], profile.table)
    academic = academic_result(profile)
    outputs = [
        format_course_list(profile.semesters[0]),
        format_semester_summary(sem_result),
        format_academic_summary(academic),
        format_summary_screen(academic, [sem_result]),
        format_prediction(predict_semester(profile, "Fall", {"CS102": "A"})),
    ]
    assert all("\t" not in output and "\x1b" not in output for output in outputs)


def test_formatting_functions_are_repeatable():
    profile = make_student([
        make_semester("Fall", [
            make_course("CS101", "B+", 3),
            make_course("CS102", None, 3, CourseStatus.IN_PROGRESS),
        ]),
    ])
    sem_result = semester_result(profile.semesters[0], profile.table)
    academic = academic_result(profile)
    prediction = predict_semester(profile, "Fall", {"CS102": "A"})
    calls = [
        (format_gpa, (Decimal("3.125"),)),
        (format_points, (Decimal("9.99"),)),
        (format_course_status, (profile.semesters[0].courses[0],)),
        (format_course_list, (profile.semesters[0],)),
        (format_semester_summary, (sem_result,)),
        (format_academic_summary, (academic,)),
        (format_summary_screen, (academic, [sem_result],)),
        (format_prediction, (prediction,)),
    ]
    for function, args in calls:
        assert function(*args) == function(*args)
