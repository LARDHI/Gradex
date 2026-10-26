"""Validated student, semester, and course models for GPA Tracker."""

from collections.abc import Iterable
from dataclasses import dataclass, field
from enum import Enum

from .grading import GradingError, GradingTable, normalize_grade


class ValidationError(ValueError):
    """Raised when model data violates a validation rule."""


class CourseStatus(Enum):
    """The state of a course's final grade."""

    COMPLETED = "completed"
    IN_PROGRESS = "in_progress"


def _trim_required_text(value: object, field_name: str, max_length: int | None = None) -> str:
    if not isinstance(value, str):
        raise ValidationError(
            f"Invalid {field_name} {value!r}: expected a string."
        )
    cleaned = value.strip()
    if not cleaned:
        raise ValidationError(
            f"Invalid {field_name} {value!r}: value cannot be empty or whitespace-only."
        )
    if max_length is not None and len(cleaned) > max_length:
        raise ValidationError(
            f"Invalid {field_name} {value!r}: maximum length is {max_length} characters after cleaning."
        )
    return cleaned


def _clean_semester_name(value: object) -> str:
    if not isinstance(value, str):
        raise ValidationError(f"Invalid semester name {value!r}: expected a string.")
    cleaned = " ".join(value.split())
    if not cleaned:
        raise ValidationError(
            f"Invalid semester name {value!r}: value cannot be empty or whitespace-only."
        )
    if len(cleaned) > 50:
        raise ValidationError(
            f"Invalid semester name {value!r}: maximum length is 50 characters after cleaning."
        )
    return cleaned


def _clean_course_code(value: object) -> str:
    if not isinstance(value, str):
        raise ValidationError(f"Invalid course code {value!r}: expected a string.")
    cleaned = value.strip()
    if not cleaned:
        raise ValidationError(
            f"Invalid course code {value!r}: code cannot be empty or whitespace-only."
        )
    return cleaned


def _course_code_key(value: object) -> str:
    return _clean_course_code(value).casefold()


def _semester_name_key(value: object) -> str:
    return _clean_semester_name(value).casefold()


@dataclass(frozen=True)
class Course:
    """An immutable course record whose status and grade are consistent."""

    code: str
    name: str
    credits: int
    status: CourseStatus
    grade: str | None

    def __post_init__(self) -> None:
        code = _clean_course_code(self.code)
        name = _trim_required_text(self.name, "course name", 100)

        if isinstance(self.credits, bool) or not isinstance(self.credits, int):
            raise ValidationError(
                f"Invalid course credits {self.credits!r}: credits must be an integer from 1 to 9, not a boolean or another type."
            )
        if not 1 <= self.credits <= 9:
            raise ValidationError(
                f"Invalid course credits {self.credits!r}: credits must be from 1 to 9 inclusive."
            )
        if not isinstance(self.status, CourseStatus):
            raise ValidationError(
                f"Invalid course status {self.status!r}: status must be a CourseStatus member."
            )

        if self.status is CourseStatus.COMPLETED:
            if self.grade is None:
                raise ValidationError(
                    "Invalid course grade None for status COMPLETED: a completed course must have a grade."
                )
            try:
                normalized_grade = normalize_grade(self.grade)
            except GradingError as exc:
                raise ValidationError(f"Invalid course grade {self.grade!r}: {exc}") from exc
            object.__setattr__(self, "grade", normalized_grade)
        else:
            if self.grade is not None:
                raise ValidationError(
                    f"Invalid course grade {self.grade!r} for status IN_PROGRESS: an in-progress course must have grade None."
                )

        object.__setattr__(self, "code", code)
        object.__setattr__(self, "name", name)


@dataclass
class Semester:
    """A named semester containing courses in insertion order."""

    name: str
    courses: list[Course] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.name = _clean_semester_name(self.name)
        if not isinstance(self.courses, list):
            raise ValidationError(
                f"Invalid semester courses {self.courses!r}: courses must be a list of Course objects."
            )
        self._validate_course_collection(self.courses)

    @staticmethod
    def _validate_course_collection(courses: list[Course]) -> None:
        seen_codes: set[str] = set()
        for course in courses:
            if not isinstance(course, Course):
                raise ValidationError(
                    f"Invalid semester course {course!r}: each entry must be a Course object."
                )
            key = _course_code_key(course.code)
            if key in seen_codes:
                raise ValidationError(
                    f"Duplicate course code {course.code!r}: course codes must be unique within a semester ignoring case."
                )
            seen_codes.add(key)

    def add_course(self, course: Course) -> None:
        if not isinstance(course, Course):
            raise ValidationError(
                f"Invalid course {course!r}: add_course requires a Course object."
            )
        key = _course_code_key(course.code)
        if any(_course_code_key(existing.code) == key for existing in self.courses):
            raise ValidationError(
                f"Duplicate course code {course.code!r}: course codes must be unique within a semester ignoring case."
            )
        self.courses.append(course)

    def replace_course(self, code: str, new_course: Course) -> None:
        target_key = _course_code_key(code)
        index = next(
            (i for i, course in enumerate(self.courses) if _course_code_key(course.code) == target_key),
            None,
        )
        if index is None:
            raise ValidationError(
                f"Course code {code!r} was not found in semester {self.name!r}."
            )
        if not isinstance(new_course, Course):
            raise ValidationError(
                f"Invalid replacement course {new_course!r}: expected a Course object."
            )
        new_key = _course_code_key(new_course.code)
        for other_index, existing in enumerate(self.courses):
            if other_index != index and _course_code_key(existing.code) == new_key:
                raise ValidationError(
                    f"Duplicate replacement course code {new_course.code!r}: it matches another course in semester {self.name!r} ignoring case."
                )
        self.courses[index] = new_course

    def delete_course(self, code: str) -> None:
        target_key = _course_code_key(code)
        index = next(
            (i for i, course in enumerate(self.courses) if _course_code_key(course.code) == target_key),
            None,
        )
        if index is None:
            raise ValidationError(
                f"Course code {code!r} was not found in semester {self.name!r}."
            )
        del self.courses[index]

    def find_course(self, code: str) -> Course:
        target_key = _course_code_key(code)
        for course in self.courses:
            if _course_code_key(course.code) == target_key:
                return course
        raise ValidationError(
            f"Course code {code!r} was not found in semester {self.name!r}."
        )


@dataclass
class Student:
    """A student profile with a grading table and ordered semesters."""

    name: str
    table: GradingTable
    semesters: list[Semester] = field(default_factory=list)

    def __init__(
        self,
        name: str,
        table: GradingTable,
        semesters: Iterable[Semester] = (),
    ) -> None:
        self.name = _trim_required_text(name, "student name", 100)
        if not isinstance(table, GradingTable):
            raise ValidationError(
                f"Invalid grading table {table!r}: table must be a GradingTable."
            )
        self.table = table
        if isinstance(semesters, (str, bytes)) or not isinstance(semesters, Iterable):
            raise ValidationError(
                f"Invalid initial semesters {semesters!r}: expected an iterable of Semester objects."
            )
        self.semesters = []
        for semester in semesters:
            self._validate_semester_for_profile(semester, self.semesters)
            self.semesters.append(semester)

    @property
    def has_courses(self) -> bool:
        return any(semester.courses for semester in self.semesters)

    def rename(self, new_name: str) -> None:
        cleaned = _trim_required_text(new_name, "student name", 100)
        self.name = cleaned

    def set_table(self, table: GradingTable) -> None:
        if not isinstance(table, GradingTable):
            raise ValidationError(
                f"Invalid grading table {table!r}: table must be a GradingTable."
            )
        if self.has_courses:
            raise ValidationError(
                f"Cannot set grading table {table.table_id!r}: the table cannot be changed while the student has courses; delete all courses first."
            )
        self.table = table

    def add_semester(self, name: str) -> Semester:
        cleaned = _clean_semester_name(name)
        key = cleaned.casefold()
        if any(_semester_name_key(semester.name) == key for semester in self.semesters):
            raise ValidationError(
                f"Duplicate semester name {name!r}: semester names must be unique ignoring case and repeated whitespace."
            )
        semester = Semester(cleaned)
        self.semesters.append(semester)
        return semester

    def rename_semester(self, old_name: str, new_name: str) -> None:
        semester = self.find_semester(old_name)
        cleaned = _clean_semester_name(new_name)
        new_key = cleaned.casefold()
        if any(
            other is not semester and _semester_name_key(other.name) == new_key
            for other in self.semesters
        ):
            raise ValidationError(
                f"Duplicate semester name {new_name!r}: a different semester already has that name ignoring case and repeated whitespace."
            )
        semester.name = cleaned

    def delete_semester(self, name: str) -> None:
        semester = self.find_semester(name)
        self.semesters.remove(semester)

    def add_course(self, semester_name: str, course: Course) -> None:
        semester = self.find_semester(semester_name)
        self._validate_course_grade(course)
        semester.add_course(course)

    def replace_course(self, semester_name: str, code: str, new_course: Course) -> None:
        semester = self.find_semester(semester_name)
        self._validate_course_grade(new_course)
        semester.replace_course(code, new_course)

    def delete_course(self, semester_name: str, code: str) -> None:
        semester = self.find_semester(semester_name)
        semester.delete_course(code)

    def find_semester(self, name: str) -> Semester:
        key = _semester_name_key(name)
        for semester in self.semesters:
            if _semester_name_key(semester.name) == key:
                return semester
        raise ValidationError(f"Semester {name!r} was not found in the student profile.")

    def _validate_course_grade(self, course: Course) -> None:
        if not isinstance(course, Course):
            raise ValidationError(
                f"Invalid course {course!r}: expected a Course object."
            )
        if course.status is CourseStatus.COMPLETED:
            try:
                self.table.points_for(course.grade)  # type: ignore[arg-type]
            except GradingError as exc:
                raise ValidationError(
                    f"Invalid course grade {course.grade!r} for grading table {self.table.table_id!r}: {exc}"
                ) from exc

    def _validate_semester_for_profile(
        self, semester: object, existing: list[Semester]
    ) -> None:
        if not isinstance(semester, Semester):
            raise ValidationError(
                f"Invalid initial semester {semester!r}: each entry must be a Semester object."
            )
        cleaned_name = _clean_semester_name(semester.name)
        if cleaned_name != semester.name:
            raise ValidationError(
                f"Invalid initial semester name {semester.name!r}: existing semester names must already be cleaned; expected {cleaned_name!r}."
            )
        name_key = cleaned_name.casefold()
        if any(_semester_name_key(other.name) == name_key for other in existing):
            raise ValidationError(
                f"Duplicate semester name {semester.name!r}: semester names must be unique ignoring case and repeated whitespace."
            )
        if not isinstance(semester.courses, list):
            raise ValidationError(
                f"Invalid courses in semester {semester.name!r}: expected a list of Course objects."
            )
        seen_codes: set[str] = set()
        for course in semester.courses:
            if not isinstance(course, Course):
                raise ValidationError(
                    f"Invalid course {course!r} in semester {semester.name!r}: expected a Course object."
                )
            code_key = _course_code_key(course.code)
            if code_key in seen_codes:
                raise ValidationError(
                    f"Duplicate course code {course.code!r} in semester {semester.name!r}: course codes must be unique ignoring case."
                )
            seen_codes.add(code_key)
            self._validate_course_grade(course)
