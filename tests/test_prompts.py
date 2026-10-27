"""Acceptance tests for P6 reusable input prompts."""

import builtins
import re
from decimal import Decimal

import pytest

from gpa_tracker.grading import build_custom_table, preset_table
from gpa_tracker.models import CourseStatus
from gpa_tracker.prompts import (
    ask_choice,
    ask_confirm_delete,
    ask_custom_entry,
    ask_grade,
    ask_number,
    ask_status,
    ask_text,
    ask_yes_no,
)


class Script:
    def __init__(self, answers):
        self.answers = iter(answers)
        self.prompts = []
        self.output = []

    def input(self, prompt):
        self.prompts.append(prompt)
        return next(self.answers)

    def print(self, line):
        self.output.append(line)


def kwargs(script):
    return {"input_func": script.input, "output_func": script.print}


def test_ask_text_returns_trimmed_text_without_collapsing_internal_spaces():
    script = Script(["  Fall   2026  "])
    assert ask_text("Semester: ", 50, **kwargs(script)) == "Fall   2026"


@pytest.mark.parametrize("invalid", ["", "   ", "x" * 51])
def test_ask_text_rejects_empty_whitespace_and_overlength(invalid):
    script = Script([invalid, "valid"])
    assert ask_text("Name: ", 50, **kwargs(script)) == "valid"
    assert len(script.output) == 1
    assert any(term in script.output[0].lower() for term in ("empty", "long", "length"))


@pytest.mark.parametrize("cancel", ["/cancel", " /CANCEL "])
def test_ask_text_cancel_is_none(cancel):
    script = Script([cancel])
    assert ask_text("Name: ", 50, **kwargs(script)) is None


@pytest.mark.parametrize("invalid", ["3.0", "3.5", "-1", "abc", "", "10"])
def test_ask_number_retries_invalid_answers(invalid):
    script = Script([invalid, "3"])
    assert ask_number("Credits: ", 1, 9, **kwargs(script)) == 3
    assert len(script.output) == 1
    assert invalid in script.output[0] or any(
        word in script.output[0].lower() for word in ("empty", "whole", "range")
    )


def test_ask_number_accepts_integer_digits():
    script = Script(["3"])
    assert ask_number("Number: ", 1, 9, **kwargs(script)) == 3


@pytest.mark.parametrize(("answer", "expected"), [("0", 0), ("2", 2)])
def test_ask_choice_accepts_back_and_last_choice(answer, expected):
    script = Script([answer])
    assert ask_choice(2, "Choice: ", **kwargs(script)) == expected


def test_ask_choice_retries_out_of_range_and_supports_cancel():
    script = Script(["3", "1"])
    assert ask_choice(2, "Choice: ", **kwargs(script)) == 1
    script = Script(["/cancel"])
    assert ask_choice(2, "Choice: ", **kwargs(script)) is None


def test_ask_status_prints_exact_menu_and_returns_completed():
    script = Script(["1"])
    assert ask_status(**kwargs(script)) is CourseStatus.COMPLETED
    assert script.output == [
        "Course status:  1. Completed (final grade is known)  2. In Progress (no final grade yet)",
        "",
    ]


def test_ask_status_returns_in_progress():
    script = Script(["2"])
    assert ask_status(**kwargs(script)) is CourseStatus.IN_PROGRESS


def test_ask_status_retries_invalid_answers():
    script = Script(["3", "completed", "1"])
    assert ask_status(**kwargs(script)) is CourseStatus.COMPLETED
    assert len(script.output) == 4  # menu, blank line, and two rejection messages
    assert "'3'" in script.output[2]
    assert "'completed'" in script.output[3]


def test_ask_grade_normalizes_valid_grade():
    script = Script([" b+ "])
    assert ask_grade(preset_table("4.0-plus-only"), **kwargs(script)) == "B+"


def test_ask_grade_rejects_grade_not_in_table_and_lists_ordered_letters():
    script = Script(["A-", "B+"])
    assert ask_grade(preset_table("4.0-plus-only"), **kwargs(script)) == "B+"
    message = script.output[0]
    assert "A-" in message
    assert "A+, A, B+, B, C+, C, D+, D, F" in message


def test_ask_grade_accepts_minus_grade_when_table_contains_it():
    script = Script(["A-"])
    assert ask_grade(preset_table("4.0-plus-minus"), **kwargs(script)) == "A-"


def test_ask_grade_cancel_returns_none():
    script = Script(["/cancel"])
    assert ask_grade(preset_table("4.0-plus-minus"), **kwargs(script)) is None


@pytest.mark.parametrize(("answer", "expected"), [("yes", True), (" YES ", True), ("y", False), ("no", False)])
def test_ask_confirm_delete(answer, expected):
    script = Script([answer])
    assert ask_confirm_delete("Delete? ", **kwargs(script)) is expected
    if expected is False:
        assert any("not deleted" in line.lower() for line in script.output)


def test_ask_confirm_delete_cancel_returns_none():
    script = Script(["/cancel"])
    assert ask_confirm_delete("Delete? ", **kwargs(script)) is None


@pytest.mark.parametrize(("answer", "expected"), [("y", True), ("YES", True), ("n", False), ("No", False)])
def test_ask_yes_no_accepts_supported_answers(answer, expected):
    script = Script([answer])
    assert ask_yes_no("Continue? ", **kwargs(script)) is expected


def test_ask_yes_no_rejects_other_answer_then_retries():
    script = Script(["maybe", "yes"])
    assert ask_yes_no("Continue? ", **kwargs(script)) is True
    assert "maybe" in script.output[0]


@pytest.mark.parametrize(
    ("answers", "expected"),
    [
        (["a", "4"], ("A", "4")),
        (["B+", "3.33"], ("B+", "3.33")),
    ],
)
def test_ask_custom_entry_valid_values(answers, expected):
    script = Script(answers)
    assert ask_custom_entry(**kwargs(script)) == expected


@pytest.mark.parametrize("bad_letter", ["ABCD", "A++", "1", ""])
def test_ask_custom_entry_rejects_invalid_letter_then_retries(bad_letter):
    script = Script([bad_letter, "A", "4"])
    assert ask_custom_entry(**kwargs(script)) == ("A", "4")
    assert len(script.output) == 1
    assert "letter" in script.output[0].lower()


@pytest.mark.parametrize("bad_points", ["5.01", "-0.5", "3.333", "abc", "1e2"])
def test_ask_custom_entry_rejects_invalid_points_then_retries(bad_points):
    script = Script(["A", bad_points, "4.00"])
    assert ask_custom_entry(**kwargs(script)) == ("A", "4.00")
    assert len(script.output) == 1
    assert bad_points in script.output[0]


@pytest.mark.parametrize("cancel_at", ["letter", "points"])
def test_ask_custom_entry_cancel_at_either_question(cancel_at):
    answers = ["/cancel"] if cancel_at == "letter" else ["A", "/cancel"]
    script = Script(answers)
    assert ask_custom_entry(**kwargs(script)) is None


def test_cancel_works_after_a_rejected_answer():
    script = Script(["bad", "/cancel"])
    assert ask_number("Number: ", 1, 9, **kwargs(script)) is None
    assert len(script.output) == 1


def test_custom_entry_validates_against_p1_custom_table_rules():
    script = Script(["abc", "4.00"])
    letter, points_text = ask_custom_entry(**kwargs(script))
    table = build_custom_table([(letter, points_text), ("F", "0.00")])
    assert table.points_for("ABC") == Decimal("4.00")


def test_ctrl_c_and_eof_propagate():
    def interrupt(_prompt):
        raise KeyboardInterrupt

    def eof(_prompt):
        raise EOFError

    with pytest.raises(KeyboardInterrupt):
        ask_text("Name: ", 50, input_func=interrupt, output_func=lambda _line: None)
    with pytest.raises(EOFError):
        ask_text("Name: ", 50, input_func=eof, output_func=lambda _line: None)


def test_all_helpers_use_injected_io_only(monkeypatch):
    def forbidden(*_args, **_kwargs):
        raise AssertionError("builtins input/print must not be called")

    monkeypatch.setattr(builtins, "input", forbidden)
    monkeypatch.setattr(builtins, "print", forbidden)
    table = preset_table("4.0-plus-minus")
    cases = [
        (lambda s: ask_text("Text: ", 10, **kwargs(s)), ["ok"]),
        (lambda s: ask_number("Number: ", 1, 9, **kwargs(s)), ["3"]),
        (lambda s: ask_choice(2, "Choice: ", **kwargs(s)), ["0"]),
        (lambda s: ask_status(**kwargs(s)), ["1"]),
        (lambda s: ask_grade(table, **kwargs(s)), ["A-"]),
        (lambda s: ask_confirm_delete("Delete: ", **kwargs(s)), ["yes"]),
        (lambda s: ask_yes_no("Continue: ", **kwargs(s)), ["no"]),
        (lambda s: ask_custom_entry(**kwargs(s)), ["A", "4"]),
    ]
    for helper, answers in cases:
        script = Script(answers)
        helper(script)


def test_no_float_token_in_prompt_source_except_comments_or_docstrings():
    from pathlib import Path
    import gpa_tracker.prompts as prompts_module

    source = Path(prompts_module.__file__).read_text(encoding="utf-8")
    # The module should contain no float conversion or float call at all.
    assert not any(re.match(r".*\bfloat\b.*", line) for line in source.splitlines())
