"""
Module 36 — Exceptions: Practice Exercises
Comprehensive practice with Python exceptions, from beginner
to more professional, production-style usage.

In this module I:
- Understand try / except / else / finally blocks.
- Handle common errors such as ValueError, TypeError, and ZeroDivisionError.
- Create and use custom exception classes with clear error messages.
- Re-raise and chain exceptions to keep context from lower levels.
- Build a small realistic "student loader" example with robust error handling.

Ranking system:
- Rank 1  -> Beginner: basic try/except around risky operations.
- Rank 2  -> Easy: multiple except blocks, else, and finally.
- Rank 3  -> Intermediate: custom exceptions and validation logic.
- Rank 4  -> Advanced: exception chaining and wrapping low-level errors.
- Rank 5  -> Professional: mini "student file loader" with detailed errors.

Author: Peyman Miyandashti
Date of Birth: 11/11/1983
ID Number: 250161
Year: 2025
"""

from __future__ import annotations
from typing import List, Dict, Any, Optional


# ===========================================================
# Rank 1 — Beginner
# Basic try/except around risky operations
# ===========================================================

print("Rank 1 — Beginner")


def safe_divide(a: Any, b: Any) -> Optional[float]:
    """
    Safely divide a by b.

    - Returns the result if possible.
    - Prints an error message and returns None if something goes wrong.
    """
    try:
        result = a / b
    except ZeroDivisionError:
        print(f"Cannot divide by zero: a={a!r}, b={b!r}")
        return None
    except TypeError:
        print(f"Incompatible types for division: a={type(a)}, b={type(b)}")
        return None
    else:
        # Only executed if there was NO exception
        print(f"Division succeeded: {a!r} / {b!r} = {result}")
        return float(result)


safe_divide(10, 2)
safe_divide(5, 0)
safe_divide("10", 2)
print("-" * 50)


# ===========================================================
# Rank 2 — Easy
# Multiple except blocks, else, and finally
# ===========================================================

print("Rank 2 — Easy")


def parse_int_list(values: List[str]) -> List[int]:
    """
    Parse a list of strings into integers.

    Demonstrates:
    - Multiple except blocks
    - else (runs only if try succeeds)
    - finally (runs always)
    """
    parsed: List[int] = []
    for text in values:
        print(f"Trying to parse: {text!r}")
        try:
            number = int(text)
        except ValueError:
            print(f"  ValueError: {text!r} is not a valid integer")
        except TypeError:
            print(f"  TypeError: cannot parse value of type {type(text)}")
        else:
            print(f"  Success: parsed {text!r} -> {number}")
            parsed.append(number)
        finally:
            # This always runs, even if there was an exception
            print("  Finished attempt for:", text)
    return parsed


raw_values = ["10", "abc", "42", None, "7"]
parsed_values = parse_int_list(raw_values)
print("Parsed values:", parsed_values)
print("-" * 50)


# ===========================================================
# Rank 3 — Intermediate
# Custom exceptions and validation logic
# ===========================================================

print("Rank 3 — Intermediate")


class InvalidGradeError(Exception):
    """
    Custom exception for invalid grades.
    """

    def __init__(self, grade: Any, message: str = "Invalid grade") -> None:
        self.grade = grade
        self.message = message
        super().__init__(f"{message}: {grade!r}")


def validate_grade(grade: Any) -> float:
    """
    Validate that grade is a number between 0 and 100.
    Raises InvalidGradeError on problems.
    """
    if not isinstance(grade, (int, float)):
        raise InvalidGradeError(grade, "Grade must be a number")
    if grade < 0 or grade > 100:
        raise InvalidGradeError(grade, "Grade must be between 0 and 100")
    return float(grade)


def add_grade(grades: List[float], grade: Any) -> None:
    """
    Add a grade to the list, using validate_grade.
    If the grade is invalid, prints an error and does not add it.
    """
    try:
        valid = validate_grade(grade)
    except InvalidGradeError as e:
        print("Failed to add grade:", e)
    else:
        grades.append(valid)
        print(f"Added valid grade: {valid}")


grades_list: List[float] = []
add_grade(grades_list, 95)
add_grade(grades_list, 120)    # invalid
add_grade(grades_list, "bad")  # invalid
add_grade(grades_list, 60.5)
print("Final grades:", grades_list)
print("-" * 50)


# ===========================================================
# Rank 4 — Advanced
# Exception chaining and wrapping low-level errors
# ===========================================================

print("Rank 4 — Advanced")


class ConfigError(Exception):
    """
    High-level configuration error.

    Used to wrap lower-level exceptions with more context.
    """


def read_config_raw(text: str) -> Dict[str, str]:
    """
    Very small 'config parser'.

    Expects lines like:
      key=value

    Raises:
    - ValueError on bad lines.
    """
    config: Dict[str, str] = {}
    for line_no, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue  # skip empty lines and comments
        if "=" not in stripped:
            raise ValueError(f"Line {line_no}: missing '=' in {stripped!r}")
        key, value = stripped.split("=", 1)
        config[key.strip()] = value.strip()
    return config


def load_config(text: str) -> Dict[str, str]:
    """
    Higher-level function that wraps low-level errors
    into a ConfigError, using exception chaining.
    """
    try:
        return read_config_raw(text)
    except Exception as e:
        # Wrap any exception into ConfigError with extra context.
        raise ConfigError("Failed to load configuration") from e


# Correct configuration
config_text_ok = """
# Sample configuration
host = localhost
port = 8080
"""

print("Loading valid config:")
try:
    config_ok = load_config(config_text_ok)
    print("Config loaded:", config_ok)
except ConfigError as e:
    print("ConfigError:", e)
    print("Original cause:", repr(e.__cause__))

print()

# Incorrect configuration (missing '=')
config_text_bad = """
host localhost
"""

print("Loading invalid config:")
try:
    config_bad = load_config(config_text_bad)
    print("Config loaded:", config_bad)
except ConfigError as e:
    print("ConfigError:", e)
    print("Original cause:", repr(e.__cause__))
print("-" * 50)


# ===========================================================
# Rank 5 — Professional
# Mini "student file loader" with robust error handling
# ===========================================================

print("Rank 5 — Professional")


class StudentDataError(Exception):
    """Base class for student data errors."""


class MissingFieldError(StudentDataError):
    """Raised when a required field is missing."""

    def __init__(self, line_no: int, field_name: str) -> None:
        super().__init__(f"Line {line_no}: missing required field {field_name!r}")
        self.line_no = line_no
        self.field_name = field_name


class StudentParseError(StudentDataError):
    """Raised when a field cannot be parsed."""

    def __init__(self, line_no: int, field_name: str, value: str, reason: str) -> None:
        message = f"Line {line_no}: cannot parse field {field_name!r}={value!r}: {reason}"
        super().__init__(message)
        self.line_no = line_no
        self.field_name = field_name
        self.value = value
        self.reason = reason


class StudentEntry:
    """
    Simple representation of a student entry loaded from text.

    Expected CSV format:
      name,age,grade

    - name: string
    - age: integer
    - grade: float (0–100)
    """

    def __init__(self, name: str, age: int, grade: float) -> None:
        self.name = name
        self.age = age
        self.grade = grade

    def __repr__(self) -> str:
        return f"StudentEntry({self.name!r}, age={self.age}, grade={self.grade:.1f})"


def parse_student_line(line_no: int, line: str) -> StudentEntry:
    parts = [p.strip() for p in line.split(",")]
    if len(parts) != 3:
        raise StudentDataError(
            f"Line {line_no}: expected 3 fields (name, age, grade), got {len(parts)}"
        )

    name, age_text, grade_text = parts

    if not name:
        raise MissingFieldError(line_no, "name")

    try:
        age = int(age_text)
    except ValueError as exc:
        raise StudentParseError(line_no, "age", age_text, "must be an integer") from exc

    try:
        grade = float(grade_text)
    except ValueError as exc:
        raise StudentParseError(line_no, "grade", grade_text, "must be a number") from exc

    try:
        grade = validate_grade(grade)  # reuse validate_grade from Rank 3
    except InvalidGradeError as exc:
        # Wrap InvalidGradeError into StudentParseError with extra context
        raise StudentParseError(line_no, "grade", grade_text, str(exc)) from exc

    return StudentEntry(name, age, grade)


def load_students_from_text(text: str) -> List[StudentEntry]:
    """
    Load students from a CSV-like text.

    Returns a list of StudentEntry objects.

    - Skips empty lines and comment lines starting with '#'.
    - Collects all errors and prints them, but continues processing.
    """
    students: List[StudentEntry] = []
    errors: List[StudentDataError] = []

    for line_no, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        try:
            student = parse_student_line(line_no, stripped)
        except StudentDataError as e:
            errors.append(e)
        else:
            students.append(student)

    # Report errors after processing all lines
    if errors:
        print("Some lines could not be loaded:")
        for err in errors:
            print("  -", err)
    else:
        print("All lines loaded successfully, no errors.")

    return students


students_text = """
# name,age,grade
Peyman,41,95
Ana,20,88.5
Luis,19,105        # invalid grade
Maria,17,abc       # invalid grade text
,18,75             # missing name
Carlos,17,72
"""

students = load_students_from_text(students_text)

print("\nLoaded students:")
for s in students:
    print(" ", s)

if students:
    avg_grade = sum(s.grade for s in students) / len(students)
    print(f"\nAverage grade of loaded students: {avg_grade:.2f}")
else:
    print("\nNo valid students were loaded.")

print("-" * 50)
