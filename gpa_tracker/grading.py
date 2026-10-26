"""Grading tables, grade normalization, and custom-table validation."""

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
import re
from types import MappingProxyType


class GradingError(ValueError):
    """Raised when a grade or grading table is invalid."""


def normalize_grade(text: str) -> str:
    """Trim surrounding whitespace and uppercase a grade letter."""
    if not isinstance(text, str):
        raise GradingError(f"Invalid grade {text!r}: expected a string.")

    normalized = text.strip().upper()
    if not normalized:
        raise GradingError(f"Invalid grade {text!r}: grade cannot be empty.")
    return normalized


@dataclass(frozen=True)
class GradingTable:
    """A grading table with ordered letters and immutable point values."""

    table_id: str
    letters: tuple[str, ...]
    points: Mapping[str, Decimal]

    def __post_init__(self) -> None:
        object.__setattr__(self, "letters", tuple(self.letters))
        object.__setattr__(self, "points", MappingProxyType(dict(self.points)))

    def points_for(self, letter: str) -> Decimal:
        """Return the points for a normalized letter in this table."""
        normalized = normalize_grade(letter)
        try:
            return self.points[normalized]
        except KeyError as exc:
            raise GradingError(
                f"Grade {normalized!r} is not present in grading table {self.table_id!r}."
            ) from exc

    def is_passing(self, letter: str) -> bool:
        """Return whether a normalized letter passes; only F fails."""
        normalized = normalize_grade(letter)
        if normalized not in self.points:
            raise GradingError(
                f"Grade {normalized!r} is not present in grading table {self.table_id!r}."
            )
        return normalized != "F"


def _make_preset(table_id: str, values: tuple[tuple[str, str], ...]) -> GradingTable:
    points = {letter: Decimal(value) for letter, value in values}
    return GradingTable(table_id=table_id, letters=tuple(points), points=points)


PRESET_TABLES: Mapping[str, GradingTable] = MappingProxyType(
    {
        "4.0-plus-only": _make_preset(
            "4.0-plus-only",
            (
                ("A+", "4.00"), ("A", "3.75"), ("B+", "3.50"),
                ("B", "3.00"), ("C+", "2.50"), ("C", "2.00"),
                ("D+", "1.50"), ("D", "1.00"), ("F", "0.00"),
            ),
        ),
        "4.0-plus-minus": _make_preset(
            "4.0-plus-minus",
            (
                ("A+", "4.00"), ("A", "3.75"), ("A-", "3.67"),
                ("B+", "3.33"), ("B", "3.00"), ("B-", "2.67"),
                ("C+", "2.33"), ("C", "2.00"), ("C-", "1.67"),
                ("D+", "1.33"), ("D", "1.00"), ("D-", "0.67"),
                ("F", "0.00"),
            ),
        ),
        "5.0-plus-only": _make_preset(
            "5.0-plus-only",
            (
                ("A+", "5.00"), ("A", "4.75"), ("B+", "4.50"),
                ("B", "4.00"), ("C+", "3.50"), ("C", "3.00"),
                ("D+", "2.50"), ("D", "2.00"), ("F", "1.00"),
            ),
        ),
        "5.0-plus-minus": _make_preset(
            "5.0-plus-minus",
            (
                ("A+", "5.00"), ("A", "4.75"), ("A-", "4.50"),
                ("B+", "4.25"), ("B", "4.00"), ("B-", "3.75"),
                ("C+", "3.50"), ("C", "3.00"), ("C-", "2.75"),
                ("D+", "2.50"), ("D", "2.00"), ("D-", "1.75"),
                ("F", "1.00"),
            ),
        ),
    }
)


_CUSTOM_LETTER_PATTERN = re.compile(r"(?:[A-Z]{1,3}|[A-Z]{1,2}[+-])\Z")
_TWO_PLACES = Decimal("0.01")


def _custom_points(value: object, letter: str) -> Decimal:
    if isinstance(value, bool) or not isinstance(value, (Decimal, str)):
        raise GradingError(
            f"Invalid points {value!r} for grade {letter!r}: expected Decimal or string, not {type(value).__name__}."
        )

    try:
        points = value if isinstance(value, Decimal) else Decimal(value)
    except (InvalidOperation, ValueError):
        raise GradingError(
            f"Invalid points {value!r} for grade {letter!r}: value is not a decimal number."
        ) from None

    if not points.is_finite():
        raise GradingError(
            f"Invalid points {value!r} for grade {letter!r}: value must be finite."
        )
    if points < Decimal("0.00") or points > Decimal("5.00"):
        raise GradingError(
            f"Invalid points {value!r} for grade {letter!r}: value must be between 0.00 and 5.00 inclusive."
        )
    if points.as_tuple().exponent < -2:
        raise GradingError(
            f"Invalid points {value!r} for grade {letter!r}: at most two decimal places are allowed."
        )

    return points.quantize(_TWO_PLACES)


def build_custom_table(entries: Sequence[tuple[str, object]]) -> GradingTable:
    """Validate entries and build an immutable custom grading table."""
    if isinstance(entries, (str, bytes)) or not isinstance(entries, Sequence):
        raise GradingError(
            f"Invalid custom table entries {entries!r}: expected a sequence of letter/points pairs."
        )
    if not 1 <= len(entries) <= 20:
        raise GradingError(
            f"Invalid custom table entry count {len(entries)}: expected between 1 and 20 entries."
        )

    points: dict[str, Decimal] = {}
    for entry in entries:
        if isinstance(entry, (str, bytes)) or not isinstance(entry, Sequence) or len(entry) != 2:
            raise GradingError(
                f"Invalid custom table entry {entry!r}: expected a (letter, points) pair."
            )
        raw_letter, raw_points = entry
        letter = normalize_grade(raw_letter)
        if not _CUSTOM_LETTER_PATTERN.fullmatch(letter):
            raise GradingError(
                f"Invalid grade letter {raw_letter!r}: expected 1–3 letters, optionally with a trailing + or - (signs allowed only after one or two letters)."
            )
        if letter in points:
            raise GradingError(
                f"Duplicate grade letter {letter!r}: letters must be unique after normalization."
            )
        points[letter] = _custom_points(raw_points, letter)

    if "F" not in points:
        raise GradingError("Invalid custom table: required failing grade 'F' is missing.")

    return GradingTable(table_id="custom", letters=tuple(points), points=points)


def preset_table(table_id: str) -> GradingTable:
    """Return a built-in table by ID, or raise GradingError for an unknown ID."""
    if not isinstance(table_id, str) or table_id not in PRESET_TABLES:
        raise GradingError(f"Unknown preset grading table ID {table_id!r}.")
    return PRESET_TABLES[table_id]
