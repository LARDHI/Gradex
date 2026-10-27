"""Reusable, validated input prompts for the GPA Tracker CLI."""

from __future__ import annotations

from decimal import Decimal, InvalidOperation
import re
from collections.abc import Callable

from .grading import GradingError, GradingTable, normalize_grade
from .models import CourseStatus

InputFunc = Callable[[str], str]
OutputFunc = Callable[[str], object]

_CANCEL = "/cancel"
_CUSTOM_LETTER_PATTERN = re.compile(r"(?:[A-Z]{1,3}|[A-Z]{1,2}[+-])\Z")


def _read_answer(label: str, input_func: InputFunc) -> str | None:
    """Read one answer; return None only for the cancellation command."""
    answer = input_func(label).strip()
    if answer.casefold() == _CANCEL:
        return None
    return answer


def ask_text(
    label: str,
    max_length: int,
    *,
    input_func: InputFunc = input,
    output_func: OutputFunc = print,
) -> str | None:
    """Ask for non-empty text within a maximum length, returning trimmed text."""
    while True:
        answer = _read_answer(label, input_func)
        if answer is None:
            return None
        if not answer:
            output_func("Input cannot be empty. Please enter a value.")
            continue
        if len(answer) > max_length:
            output_func(
                f"Input is too long ({len(answer)} characters). Maximum length is {max_length} characters."
            )
            continue
        return answer


def ask_number(
    label: str,
    minimum: int,
    maximum: int,
    *,
    input_func: InputFunc = input,
    output_func: OutputFunc = print,
) -> int | None:
    """Ask for whole decimal digits within an inclusive integer range."""
    while True:
        answer = _read_answer(label, input_func)
        if answer is None:
            return None
        if not answer:
            output_func("Input cannot be empty. Please enter a whole number.")
            continue
        if re.fullmatch(r"[0-9]+", answer) is None:
            output_func(
                f"Invalid number {answer!r}: enter whole decimal digits only, without a sign or decimal point."
            )
            continue
        try:
            number = int(answer)
        except ValueError:
            output_func(
                f"Number {answer!r} is too large to process. Enter a number from {minimum} to {maximum} inclusive."
            )
            continue
        if not minimum <= number <= maximum:
            output_func(
                f"Number {number} is out of range. Enter a number from {minimum} to {maximum} inclusive."
            )
            continue
        return number


def ask_choice(
    count: int,
    label: str,
    *,
    input_func: InputFunc = input,
    output_func: OutputFunc = print,
) -> int | None:
    """Ask for a menu choice from 0 through count; 0 means Back."""
    return ask_number(
        label, 0, count, input_func=input_func, output_func=output_func
    )


def ask_status(
    *,
    input_func: InputFunc = input,
    output_func: OutputFunc = print,
) -> CourseStatus | None:
    """Ask whether a course is completed or still in progress."""
    output_func(
        "Course status:  1. Completed (final grade is known)  "
        "2. In Progress (no final grade yet)"
    )
    output_func("")
    while True:
        answer = _read_answer("Choose 1 or 2: ", input_func)
        if answer is None:
            return None
        if not answer:
            output_func("Input cannot be empty. Enter 1 for Completed or 2 for In Progress.")
            continue
        if answer == "1":
            return CourseStatus.COMPLETED
        if answer == "2":
            return CourseStatus.IN_PROGRESS
        output_func(
            f"Invalid course status choice {answer!r}. Enter 1 for Completed or 2 for In Progress."
        )


def ask_grade(
    table: GradingTable,
    *,
    label: str = "Enter grade: ",
    input_func: InputFunc = input,
    output_func: OutputFunc = print,
) -> str | None:
    """Ask for a grade present in the selected grading table."""
    valid_letters = ", ".join(table.letters)
    while True:
        answer = _read_answer(label, input_func)
        if answer is None:
            return None
        if not answer:
            output_func("Grade cannot be empty. Enter one of the valid letters.")
            continue
        try:
            grade = normalize_grade(answer)
            table.points_for(grade)
        except GradingError:
            output_func(
                f"Invalid grade {answer!r}. Valid letters for this table, in order: {valid_letters}."
            )
            continue
        return grade


def ask_confirm_delete(
    label: str,
    *,
    input_func: InputFunc = input,
    output_func: OutputFunc = print,
) -> bool | None:
    """Require the exact word 'yes' to authorize deletion."""
    while True:
        answer = _read_answer(label, input_func)
        if answer is None:
            return None
        if not answer:
            output_func("Input cannot be empty. Type 'yes' to confirm deletion.")
            continue
        if answer.casefold() == "yes":
            return True
        output_func("The item was not deleted. Type 'yes' to confirm deletion.")
        return False


def ask_yes_no(
    label: str,
    *,
    input_func: InputFunc = input,
    output_func: OutputFunc = print,
) -> bool | None:
    """Ask for a yes/no answer, retrying anything other than y/yes/n/no."""
    while True:
        answer = _read_answer(label, input_func)
        if answer is None:
            return None
        if not answer:
            output_func("Input cannot be empty. Enter y/yes or n/no.")
            continue
        normalized = answer.casefold()
        if normalized in {"y", "yes"}:
            return True
        if normalized in {"n", "no"}:
            return False
        output_func(f"Invalid yes/no answer {answer!r}. Enter y/yes or n/no.")


def ask_custom_entry(
    *,
    letter_label: str = "Enter grade letter: ",
    points_label: str = "Enter grade points: ",
    input_func: InputFunc = input,
    output_func: OutputFunc = print,
) -> tuple[str, str] | None:
    """Ask for one custom grade letter and its points, without checking duplicates."""
    while True:
        raw_letter = _read_answer(letter_label, input_func)
        if raw_letter is None:
            return None
        if not raw_letter:
            output_func("Grade letter cannot be empty.")
            continue
        try:
            letter = normalize_grade(raw_letter)
        except GradingError:
            output_func(f"Invalid grade letter {raw_letter!r}: enter a non-empty letter pattern.")
            continue
        if _CUSTOM_LETTER_PATTERN.fullmatch(letter) is None:
            output_func(
                f"Invalid grade letter {raw_letter!r}: use 1–3 letters, or 1–2 letters followed by + or -."
            )
            continue
        break

    while True:
        points_text = _read_answer(points_label, input_func)
        if points_text is None:
            return None
        if not points_text:
            output_func("Grade points cannot be empty. Enter a decimal from 0.00 to 5.00.")
            continue
        try:
            points = Decimal(points_text)
        except (InvalidOperation, ValueError):
            output_func(
                f"Invalid points {points_text!r}: enter a decimal from 0.00 to 5.00 with at most 2 decimal places."
            )
            continue
        if not points.is_finite():
            output_func(f"Invalid points {points_text!r}: value must be a finite decimal number.")
            continue
        if points < Decimal("0.00") or points > Decimal("5.00"):
            output_func(f"Invalid points {points_text!r}: value must be from 0.00 to 5.00 inclusive.")
            continue
        if points.as_tuple().exponent < -2:
            output_func(f"Invalid points {points_text!r}: at most 2 decimal places are allowed.")
            continue
        return letter, points_text
