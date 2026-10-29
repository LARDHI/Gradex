"""Acceptance tests for grading tables and custom-table validation."""

from decimal import Decimal

import pytest

from gpa_tracker.grading import (
    PRESET_TABLES,
    GradingError,
    build_custom_table,
    normalize_grade,
    preset_table,
)


PRESET_VALUES = [
    ("4.0-plus-only", "A+", "4.00"),
    ("4.0-plus-only", "A", "3.75"),
    ("4.0-plus-only", "B+", "3.50"),
    ("4.0-plus-only", "B", "3.00"),
    ("4.0-plus-only", "C+", "2.50"),
    ("4.0-plus-only", "C", "2.00"),
    ("4.0-plus-only", "D+", "1.50"),
    ("4.0-plus-only", "D", "1.00"),
    ("4.0-plus-only", "F", "0.00"),
    ("4.0-plus-minus", "A+", "4.00"),
    ("4.0-plus-minus", "A", "3.75"),
    ("4.0-plus-minus", "A-", "3.67"),
    ("4.0-plus-minus", "B+", "3.33"),
    ("4.0-plus-minus", "B", "3.00"),
    ("4.0-plus-minus", "B-", "2.67"),
    ("4.0-plus-minus", "C+", "2.33"),
    ("4.0-plus-minus", "C", "2.00"),
    ("4.0-plus-minus", "C-", "1.67"),
    ("4.0-plus-minus", "D+", "1.33"),
    ("4.0-plus-minus", "D", "1.00"),
    ("4.0-plus-minus", "D-", "0.67"),
    ("4.0-plus-minus", "F", "0.00"),
    ("5.0-plus-only", "A+", "5.00"),
    ("5.0-plus-only", "A", "4.75"),
    ("5.0-plus-only", "B+", "4.50"),
    ("5.0-plus-only", "B", "4.00"),
    ("5.0-plus-only", "C+", "3.50"),
    ("5.0-plus-only", "C", "3.00"),
    ("5.0-plus-only", "D+", "2.50"),
    ("5.0-plus-only", "D", "2.00"),
    ("5.0-plus-only", "F", "1.00"),
    ("5.0-plus-minus", "A+", "5.00"),
    ("5.0-plus-minus", "A", "4.75"),
    ("5.0-plus-minus", "A-", "4.50"),
    ("5.0-plus-minus", "B+", "4.25"),
    ("5.0-plus-minus", "B", "4.00"),
    ("5.0-plus-minus", "B-", "3.75"),
    ("5.0-plus-minus", "C+", "3.50"),
    ("5.0-plus-minus", "C", "3.00"),
    ("5.0-plus-minus", "C-", "2.75"),
    ("5.0-plus-minus", "D+", "2.50"),
    ("5.0-plus-minus", "D", "2.00"),
    ("5.0-plus-minus", "D-", "1.75"),
    ("5.0-plus-minus", "F", "1.00"),
]


@pytest.mark.parametrize("table_id, letter, expected", PRESET_VALUES)
def test_every_preset_value_is_exact_decimal(table_id, letter, expected):
    assert preset_table(table_id).points_for(letter) == Decimal(expected)


@pytest.mark.parametrize(
    "table_id, letter",
    [
        ("4.0-plus-only", "A-"),
        ("4.0-plus-only", "B-"),
        ("4.0-plus-only", "C-"),
        ("4.0-plus-only", "D-"),
        ("5.0-plus-only", "A-"),
        ("5.0-plus-only", "B-"),
        ("5.0-plus-only", "C-"),
        ("5.0-plus-only", "D-"),
    ],
)
def test_na_letters_are_rejected(table_id, letter):
    with pytest.raises(GradingError, match=letter.replace("+", r"\+").replace("-", r"\-")):
        preset_table(table_id).points_for(letter)


def test_preset_letter_counts():
    assert {table_id: len(table.letters) for table_id, table in PRESET_TABLES.items()} == {
        "4.0-plus-only": 9,
        "4.0-plus-minus": 13,
        "5.0-plus-only": 9,
        "5.0-plus-minus": 13,
    }


@pytest.mark.parametrize("table", list(PRESET_TABLES.values()))
def test_only_f_is_failing_in_each_preset(table):
    assert table.is_passing("F") is False
    for letter in table.letters:
        if letter != "F":
            assert table.is_passing(letter) is True


def test_normalization_and_invalid_grades():
    assert normalize_grade(" b+ ") == "B+"
    assert normalize_grade("a") == "A"
    with pytest.raises(GradingError):
        preset_table("4.0-plus-minus").points_for("B +")
    with pytest.raises(GradingError, match="empty"):
        normalize_grade("")
    with pytest.raises(GradingError, match="empty"):
        normalize_grade("   ")
    with pytest.raises(GradingError, match="string"):
        normalize_grade(None)


def test_normalize_grade_collapses_repeated_spaces():
    assert normalize_grade("  b   +  ") == "B +"
    assert normalize_grade("a\t\tb") == "A B"


def test_custom_table_builds_and_looks_up_valid_values():
    table = build_custom_table([("A", "4.00"), ("B", "3.00"), ("F", "0.00")])
    assert table.table_id == "custom"
    assert table.points_for("a") == Decimal("4.00")
    assert table.is_passing("F") is False
    assert table.is_passing("B") is True


def test_custom_table_requires_f():
    with pytest.raises(GradingError, match="F"):
        build_custom_table([("A", "4.00"), ("B", "3.00")])


@pytest.mark.parametrize("entries", [[], [("F", "0")] * 21])
def test_custom_table_entry_count_bounds(entries):
    with pytest.raises(GradingError, match="entry count"):
        build_custom_table(entries)


def test_custom_table_rejects_duplicate_letters_after_normalization():
    with pytest.raises(GradingError, match="A"):
        build_custom_table([("a", "4"), ("A", "3"), ("F", "0")])


@pytest.mark.parametrize("letter", ["ABCD", "A++", "1", ""])
def test_custom_table_rejects_invalid_letters_with_specific_message(letter):
    with pytest.raises(GradingError) as exc_info:
        build_custom_table([(letter, "4"), ("F", "0")])
    assert repr(letter) in str(exc_info.value)


@pytest.mark.parametrize(
    "value",
    [
        "-0.01",
        "5.01",
        "4.001",
        4.0,
        True,
        "not-a-number",
    ],
)
def test_custom_table_rejects_invalid_points_with_specific_message(value):
    with pytest.raises(GradingError) as exc_info:
        build_custom_table([("A", value), ("F", "0")])
    assert repr(value) in str(exc_info.value)


def test_custom_points_are_quantized_to_two_decimal_places():
    table = build_custom_table([("A", Decimal("4")), ("F", Decimal("0"))])
    assert table.points_for("A") == Decimal("4.00")
    assert table.points["A"].as_tuple().exponent == -2


def test_unknown_preset_id_raises_grading_error():
    with pytest.raises(GradingError, match="not-a-preset"):
        preset_table("not-a-preset")


def test_table_points_are_read_only():
    with pytest.raises(TypeError):
        PRESET_TABLES["4.0-plus-only"].points["A"] = Decimal("0.00")
    with pytest.raises(TypeError):
        PRESET_TABLES["new"] = PRESET_TABLES["4.0-plus-only"]
