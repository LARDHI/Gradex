"""Interactive command-line screens for GPA Tracker."""

from __future__ import annotations

import os
from collections.abc import Callable
from pathlib import Path

from . import storage
from .calculator import academic_result, semester_result
from .formatting import (
    format_course_list,
    format_prediction,
    format_summary_screen,
)
from .grading import GradingError, build_custom_table, preset_table
from .models import Course, CourseStatus, Student, ValidationError
from .prediction import predict_semester
from .prompts import (
    ask_choice,
    ask_confirm_delete,
    ask_custom_entry,
    ask_grade,
    ask_number,
    ask_status,
    ask_text,
    ask_yes_no,
)
from .storage import MissingFileError, StorageError

InputFunc = Callable[[str], str]
OutputFunc = Callable[[str], object]

_GRADING_OPTIONS = (
    ("4.0 Plus Only", "4.0-plus-only"),
    ("4.0 Plus/Minus", "4.0-plus-minus"),
    ("5.0 Plus Only", "5.0-plus-only"),
    ("5.0 Plus/Minus", "5.0-plus-minus"),
)


def _show_grading_menu(output_func: OutputFunc) -> None:
    output_func("Grading table:")
    for number, (label, _) in enumerate(_GRADING_OPTIONS, start=1):
        output_func(f"  {number}. {label}")
    output_func("  5. Enter my own table")


def _custom_table_flow(
    input_func: InputFunc, output_func: OutputFunc
):
    """Collect a custom table; invalid tables are not applied to the profile."""
    while True:
        entries: list[tuple[str, str]] = []

        while True:
            entry = ask_custom_entry(
                input_func=input_func,
                output_func=output_func,
            )
            if entry is None:
                return None

            entries.append(entry)
            more = ask_yes_no(
                "Add another entry? (y/n): ",
                input_func=input_func,
                output_func=output_func,
            )
            if more is None:
                return None
            if not more:
                break

        try:
            return build_custom_table(entries)
        except GradingError as exc:
            output_func(f"Invalid custom grading table: {exc}")
            retry = ask_yes_no(
                "Try creating the table again? (y/n): ",
                input_func=input_func,
                output_func=output_func,
            )
            if retry is not True:
                return None


def _choose_table(
    input_func: InputFunc, output_func: OutputFunc
):
    """Return a grading table, or None when cancelled."""
    while True:
        _show_grading_menu(output_func)
        choice = ask_choice(
            5,
            "Choose a grading table (0 to cancel): ",
            input_func=input_func,
            output_func=output_func,
        )
        if choice in (None, 0):
            return None
        if choice == 5:
            table = _custom_table_flow(input_func, output_func)
            if table is None:
                continue
            return table
        return preset_table(_GRADING_OPTIONS[choice - 1][1])


def _save_change(
    student: Student,
    path: str | os.PathLike[str],
    change: Callable[[Student], object],
    output_func: OutputFunc,
) -> bool:
    """Apply and persist one change, rolling back if validation or saving fails."""
    try:
        storage.apply_and_save(student, path, change)
    except StorageError:
        output_func(
            "Your change was not saved. Your data file was left as it was."
        )
        return False
    except ValidationError as exc:
        output_func(f"Change rejected: {exc}")
        return False
    return True


def _numbered_items(
    items, output_func: OutputFunc, *, empty_message: str
) -> bool:
    if not items:
        output_func(empty_message)
        return False
    for number, item in enumerate(items, start=1):
        output_func(f"  {number}. {item}")
    return True


def _summary_screen(
    student: Student,
    input_func: InputFunc,
    output_func: OutputFunc,
) -> None:
    academic = academic_result(student)
    semester_results = [
        semester_result(semester, student.table)
        for semester in student.semesters
    ]
    output_func(format_summary_screen(academic, semester_results))
    input_func("Press Enter to continue.")


def _semesters_screen(
    student: Student,
    path: str | os.PathLike[str],
    input_func: InputFunc,
    output_func: OutputFunc,
) -> None:
    while True:
        output_func("Semesters:")
        if not student.semesters:
            output_func("  No semesters yet.")
        else:
            _numbered_items(
                [semester.name for semester in student.semesters],
                output_func,
                empty_message="  No semesters yet.",
            )

        output_func("  1. Add semester")
        output_func("  2. Rename semester")
        output_func("  3. Delete semester")
        output_func("  0. Back")

        choice = ask_choice(
            3,
            "Choose an option: ",
            input_func=input_func,
            output_func=output_func,
        )
        if choice in (None, 0):
            return

        if choice == 1:
            name = ask_text(
                "Semester name: ",
                50,
                input_func=input_func,
                output_func=output_func,
            )
            if name is None:
                continue
            _save_change(
                student,
                path,
                lambda current: current.add_semester(name),
                output_func,
            )
            continue

        if not student.semesters:
            output_func("There are no semesters to select.")
            continue

        _numbered_items(
            [semester.name for semester in student.semesters],
            output_func,
            empty_message="There are no semesters to select.",
        )
        index = ask_choice(
            len(student.semesters),
            "Choose a semester (0 to cancel): ",
            input_func=input_func,
            output_func=output_func,
        )
        if index in (None, 0):
            continue

        semester_name = student.semesters[index - 1].name

        if choice == 2:
            new_name = ask_text(
                "New semester name: ",
                50,
                input_func=input_func,
                output_func=output_func,
            )
            if new_name is None:
                continue
            _save_change(
                student,
                path,
                lambda current: current.rename_semester(
                    semester_name, new_name
                ),
                output_func,
            )
            continue

        semester = student.find_semester(semester_name)
        output_func(
            f"Semester {semester.name!r} contains "
            f"{len(semester.courses)} course(s)."
        )
        confirmed = ask_confirm_delete(
            "Type yes to delete this semester and all its courses: ",
            input_func=input_func,
            output_func=output_func,
        )
        if confirmed is True:
            _save_change(
                student,
                path,
                lambda current: current.delete_semester(semester_name),
                output_func,
            )


def _edit_text(
    label: str,
    current: str,
    max_length: int,
    input_func: InputFunc,
    output_func: OutputFunc,
) -> str | None:
    """Enter keeps the current value; /cancel aborts the whole edit."""
    while True:
        answer = input_func(f"{label} [{current}]: ").strip()

        if answer.casefold() == "/cancel":
            return None
        if not answer:
            return current
        if len(answer) > max_length:
            output_func(
                f"Input is too long ({len(answer)} characters). "
                f"Maximum length is {max_length} characters."
            )
            continue
        return answer


def _edit_credits(
    current: int,
    input_func: InputFunc,
    output_func: OutputFunc,
) -> int | None:
    while True:
        answer = input_func(f"Credit hours [{current}]: ").strip()

        if answer.casefold() == "/cancel":
            return None
        if not answer:
            return current
        if not answer.isascii() or not answer.isdecimal():
            output_func(
                "Invalid credit hours. Enter whole decimal digits from 1 to 9."
            )
            continue

        credits = int(answer)
        if not 1 <= credits <= 9:
            output_func(
                f"Number {credits} is out of range. "
                "Enter a number from 1 to 9 inclusive."
            )
            continue
        return credits


def _edit_grade(
    student: Student,
    current_grade: str | None,
    input_func: InputFunc,
    output_func: OutputFunc,
) -> str | None:
    if current_grade is None:
        return ask_grade(
            student.table,
            input_func=input_func,
            output_func=output_func,
        )

    while True:
        answer = input_func(f"Grade [{current_grade}]: ").strip()

        if answer.casefold() == "/cancel":
            return None
        if not answer:
            return current_grade

        grade = answer.upper()
        try:
            student.table.points_for(grade)
        except GradingError:
            output_func(
                f"Invalid grade {answer!r}. Valid letters for this table, "
                f"in order: {', '.join(student.table.letters)}."
            )
            continue
        return grade


def _collect_course(
    student: Student,
    input_func: InputFunc,
    output_func: OutputFunc,
    *,
    existing: Course | None = None,
) -> Course | None:
    """Collect and validate the complete course before changing any data."""
    status = ask_status(
        input_func=input_func,
        output_func=output_func,
    )
    if status is None:
        return None

    if status is CourseStatus.COMPLETED:
        grade = _edit_grade(
            student, existing.grade, input_func, output_func
        ) if existing is not None else ask_grade(
            student.table,
            input_func=input_func,
            output_func=output_func,
        )
        if grade is None:
            return None
    else:
        grade = None

    if existing is None:
        code = ask_text(
            "Course code: ",
            100,
            input_func=input_func,
            output_func=output_func,
        )
        if code is None:
            return None

        name = ask_text(
            "Course name: ",
            100,
            input_func=input_func,
            output_func=output_func,
        )
        if name is None:
            return None

        credits = ask_number(
            "Credit hours (1-9): ",
            1,
            9,
            input_func=input_func,
            output_func=output_func,
        )
        if credits is None:
            return None
    else:
        code = _edit_text(
            "Course code",
            existing.code,
            100,
            input_func,
            output_func,
        )
        if code is None:
            return None

        name = _edit_text(
            "Course name",
            existing.name,
            100,
            input_func,
            output_func,
        )
        if name is None:
            return None

        credits = _edit_credits(
            existing.credits, input_func, output_func
        )
        if credits is None:
            return None

    try:
        return Course(
            code=code,
            name=name,
            credits=credits,
            status=status,
            grade=grade,
        )
    except ValidationError as exc:
        output_func(f"Invalid course: {exc}")
        return None


def _courses_screen(
    student: Student,
    path: str | os.PathLike[str],
    input_func: InputFunc,
    output_func: OutputFunc,
) -> None:
    while True:
        if not student.semesters:
            output_func("No semesters yet. Add a semester first.")
            return

        output_func("Choose a semester:")
        _numbered_items(
            [semester.name for semester in student.semesters],
            output_func,
            empty_message="No semesters yet.",
        )
        semester_index = ask_choice(
            len(student.semesters),
            "Choose a semester (0 to back): ",
            input_func=input_func,
            output_func=output_func,
        )
        if semester_index in (None, 0):
            return

        semester_name = student.semesters[semester_index - 1].name

        while True:
            try:
                semester = student.find_semester(semester_name)
            except ValidationError as exc:
                output_func(str(exc))
                break

            output_func(format_course_list(semester))
            output_func("Course menu:")
            output_func("  1. Add course")
            output_func("  2. Edit course")
            output_func("  3. Delete course")
            output_func("  0. Back")

            choice = ask_choice(
                3,
                "Choose an option: ",
                input_func=input_func,
                output_func=output_func,
            )
            if choice in (None, 0):
                break

            if choice == 1:
                course = _collect_course(
                    student, input_func, output_func
                )
                if course is None:
                    continue

                _save_change(
                    student,
                    path,
                    lambda current: current.add_course(
                        semester_name, course
                    ),
                    output_func,
                )
                continue

            if not semester.courses:
                output_func("There are no courses to select.")
                continue

            output_func("Choose a course:")
            _numbered_items(
                [
                    f"{course.code} — {course.name}"
                    for course in semester.courses
                ],
                output_func,
                empty_message="There are no courses to select.",
            )
            course_index = ask_choice(
                len(semester.courses),
                "Choose a course (0 to cancel): ",
                input_func=input_func,
                output_func=output_func,
            )
            if course_index in (None, 0):
                continue

            course = semester.courses[course_index - 1]

            if choice == 2:
                replacement = _collect_course(
                    student,
                    input_func,
                    output_func,
                    existing=course,
                )
                if replacement is None:
                    continue

                _save_change(
                    student,
                    path,
                    lambda current: current.replace_course(
                        semester_name, course.code, replacement
                    ),
                    output_func,
                )
                continue

            confirmed = ask_confirm_delete(
                f"Delete course {course.code!r}? Type yes to confirm: ",
                input_func=input_func,
                output_func=output_func,
            )
            if confirmed is True:
                _save_change(
                    student,
                    path,
                    lambda current: current.delete_course(
                        semester_name, course.code
                    ),
                    output_func,
                )


def _prediction_screen(
    student: Student,
    input_func: InputFunc,
    output_func: OutputFunc,
) -> None:
    while True:
        available = [
            semester
            for semester in student.semesters
            if any(
                course.status is CourseStatus.IN_PROGRESS
                for course in semester.courses
            )
        ]
        if not available:
            output_func("No semester has in-progress courses.")
            return

        output_func("Choose a semester to predict:")
        _numbered_items(
            [semester.name for semester in available],
            output_func,
            empty_message="No semester has in-progress courses.",
        )
        index = ask_choice(
            len(available),
            "Choose a semester (0 to back): ",
            input_func=input_func,
            output_func=output_func,
        )
        if index in (None, 0):
            return

        semester = available[index - 1]
        in_progress = [
            course
            for course in semester.courses
            if course.status is CourseStatus.IN_PROGRESS
        ]

        def ask_expected(course: Course) -> tuple[str | None, bool]:
            """Ask for an expected grade; /skip omits it, /cancel aborts."""
            valid_letters = ", ".join(student.table.letters)
            while True:
                answer = input_func(
                    f"Expected grade for {course.code} (or /skip): "
                ).strip()
                if answer.casefold() == "/cancel":
                    return None, True
                if answer.casefold() == "/skip":
                    return None, False
                if not answer:
                    output_func(
                        "Grade cannot be empty. Enter one of the valid letters."
                    )
                    continue
                grade = answer.upper()
                try:
                    student.table.points_for(grade)
                except GradingError:
                    output_func(
                        f"Invalid grade {answer!r}. Valid letters for this table, "
                        f"in order: {valid_letters}."
                    )
                    continue
                return grade, False

        # Expectations are local to this selected-semester session.
        expected: dict[str, str] = {}
        cancelled = False
        for course in in_progress:
            grade, cancel_requested = ask_expected(course)
            if cancel_requested:
                cancelled = True
                break
            if grade is not None:
                expected[course.code] = grade

        if cancelled:
            continue

        while True:
            result = predict_semester(
                student, semester.name, expected
            )
            output_func(format_prediction(result))
            output_func("Prediction menu:")
            output_func("  1. Change an expected grade")
            output_func("  2. Choose another semester")
            output_func("  0. Back")

            choice = ask_choice(
                2,
                "Choose an option: ",
                input_func=input_func,
                output_func=output_func,
            )
            if choice in (None, 0):
                return
            if choice == 2:
                break

            output_func("Choose a course:")
            _numbered_items(
                [course.code for course in in_progress],
                output_func,
                empty_message="No in-progress courses.",
            )
            course_index = ask_choice(
                len(in_progress),
                "Choose a course (0 to cancel): ",
                input_func=input_func,
                output_func=output_func,
            )
            if course_index in (None, 0):
                continue

            course = in_progress[course_index - 1]
            grade, cancel_requested = ask_expected(course)
            if cancel_requested:
                continue
            if grade is None:
                expected.pop(course.code, None)
            else:
                expected[course.code] = grade


def _profile_screen(
    student: Student,
    path: str | os.PathLike[str],
    input_func: InputFunc,
    output_func: OutputFunc,
) -> None:
    while True:
        output_func("Profile")
        output_func("  1. Change name")
        output_func("  2. Change grading table")
        output_func("  0. Back")

        choice = ask_choice(
            2,
            "Choose an option: ",
            input_func=input_func,
            output_func=output_func,
        )
        if choice in (None, 0):
            return

        if choice == 1:
            name = ask_text(
                "New student name: ",
                100,
                input_func=input_func,
                output_func=output_func,
            )
            if name is None:
                continue

            _save_change(
                student,
                path,
                lambda current: current.rename(name),
                output_func,
            )
            continue

        if student.has_courses:
            output_func(
                "Your profile has courses, so the grading table is locked. "
                "Delete all courses first to change it."
            )
            continue

        table = _choose_table(input_func, output_func)
        if table is None:
            continue

        _save_change(
            student,
            path,
            lambda current: current.set_table(table),
            output_func,
        )


def run(
    path: str | os.PathLike[str],
    *,
    input_func: InputFunc = input,
    output_func: OutputFunc = print,
) -> int:
    """Run GPA Tracker with injectable I/O; return a process exit code."""
    try:
        try:
            student = storage.load_student(path)
        except MissingFileError:
            output_func("No data file found. Let's create your profile.")

            name = ask_text(
                "Student name: ",
                100,
                input_func=input_func,
                output_func=output_func,
            )
            if name is None:
                return 0

            table = _choose_table(input_func, output_func)
            if table is None:
                return 0

            student = Student(name, table)
            try:
                storage.save_student(student, path)
            except StorageError:
                output_func(
                    "Your profile could not be saved. "
                    "The data file was not changed."
                )
                return 1
        except StorageError as exc:
            output_func(f"Could not load student data: {exc}")
            output_func("The file was not changed.")
            return 1

        while True:
            output_func("Main menu:")
            output_func("  1. Summary")
            output_func("  2. Semesters")
            output_func("  3. Courses")
            output_func("  4. Predict GPA")
            output_func("  5. Profile")
            output_func("  0. Exit")

            choice = ask_choice(
                5,
                "Choose an option: ",
                input_func=input_func,
                output_func=output_func,
            )
            if choice in (None, 0):
                return 0

            if choice == 1:
                _summary_screen(student, input_func, output_func)
            elif choice == 2:
                _semesters_screen(
                    student, path, input_func, output_func
                )
            elif choice == 3:
                _courses_screen(
                    student, path, input_func, output_func
                )
            elif choice == 4:
                _prediction_screen(
                    student, input_func, output_func
                )
            elif choice == 5:
                _profile_screen(
                    student, path, input_func, output_func
                )

    except (KeyboardInterrupt, EOFError):
        output_func("Exiting. Your data is saved.")
        return 0