"""
Module 35 — Properties: Practice Exercises
Comprehensive practice with Python @property, from beginner
to more professional, production-style usage.

In this module I:
- Use @property to create "smart attributes" with simple syntax.
- Create read-only computed properties.
- Add validation and transformation with property setters.
- Use properties to keep related values in sync.
- Build a small realistic grading model for a school system.

Ranking system:
- Rank 1  -> Beginner: basic @property for computed attributes.
- Rank 2  -> Easy: read-only properties and formatting helpers.
- Rank 3  -> Intermediate: property setters with validation.
- Rank 4  -> Advanced: multiple related properties that stay in sync.
- Rank 5  -> Professional: mini "gradebook" model using properties.

Author: Peyman Miyandashti
Date of Birth: 11/11/1983
ID Number: 250161
Year: 2025
"""

from __future__ import annotations
from typing import List, Dict, Optional


# ===========================================================
# Rank 1 — Beginner
# Basic @property: computed attributes
# ===========================================================

print("Rank 1 — Beginner")


class LessonDuration:
    """
    Simple example: store duration in minutes,
    and expose hours as a computed property.
    """

    def __init__(self, title: str, minutes: int) -> None:
        self.title = title
        self.minutes = minutes

    @property
    def hours(self) -> float:
        """
        Computed attribute: number of hours (float).
        """
        return self.minutes / 60.0

    def __repr__(self) -> str:
        return f"LessonDuration(title={self.title!r}, minutes={self.minutes})"


python_lesson = LessonDuration("Python Intro", 90)
physics_lesson = LessonDuration("Physics Basics", 120)

print(python_lesson)
print("Python lesson hours:", python_lesson.hours)
print(physics_lesson)
print("Physics lesson hours:", physics_lesson.hours)
print("-" * 50)


# ===========================================================
# Rank 2 — Easy
# Read-only properties and formatting helpers
# ===========================================================

print("Rank 2 — Easy")


class StudentName:
    """
    Read-only properties for full name and display name.
    """

    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name.strip()
        self.last_name = last_name.strip()

    @property
    def full_name(self) -> str:
        """
        Read-only combination of first and last name.
        """
        return f"{self.first_name} {self.last_name}"

    @property
    def display_name(self) -> str:
        """
        Read-only "Last, First" style for reports.
        """
        return f"{self.last_name}, {self.first_name}"

    def __repr__(self) -> str:
        return f"StudentName({self.first_name!r}, {self.last_name!r})"


s1 = StudentName("Peyman", "Miyandashti")
s2 = StudentName("Ana", "Lopez")

print("Student 1:", s1)
print("  full_name:", s1.full_name)
print("  display_name:", s1.display_name)

print("Student 2:", s2)
print("  full_name:", s2.full_name)
print("  display_name:", s2.display_name)

# The following would be an error (there is no setter):
# s1.full_name = "Something else"
print("-" * 50)


# ===========================================================
# Rank 3 — Intermediate
# Property setters with validation
# ===========================================================

print("Rank 3 — Intermediate")


class Grade:
    """
    Store a numeric grade between 0 and 100.

    - grade: main numeric value (float)
    - Uses property to enforce valid range.
    """

    def __init__(self, value: float) -> None:
        self._grade: float = 0.0
        self.grade = value  # will use the setter with validation

    @property
    def grade(self) -> float:
        return self._grade

    @grade.setter
    def grade(self, value: float) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError(f"Grade must be a number, got {type(value)!r}")
        if value < 0 or value > 100:
            raise ValueError(f"Grade must be between 0 and 100, got {value}")
        self._grade = float(value)

    @property
    def is_passing(self) -> bool:
        """
        Read-only property that depends on grade.
        """
        return self.grade >= 60.0

    def __repr__(self) -> str:
        status = "PASS" if self.is_passing else "FAIL"
        return f"Grade({self.grade:.1f}, {status})"


g1 = Grade(95)
g2 = Grade(58)

print("g1:", g1)
print("g2:", g2)

print("Changing g2.grade to 75...")
g2.grade = 75
print("g2:", g2)

# Uncomment to see validation errors:
# Grade(-5)       # ValueError
# Grade("bad")    # TypeError

print("-" * 50)


# ===========================================================
# Rank 4 — Advanced
# Keeping related attributes in sync with properties
# ===========================================================

print("Rank 4 — Advanced")


class Temperature:
    """
    Represent a temperature and keep Celsius and Fahrenheit
    values synchronized using properties.

    Internally store the temperature in Celsius.
    """

    def __init__(self, celsius: float) -> None:
        self._celsius: float = 0.0
        self.celsius = celsius  # use setter for validation

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        # Basic validation: Earth classroom realistic range
        if value < -50 or value > 80:
            raise ValueError(f"Unrealistic classroom temperature: {value} °C")
        self._celsius = float(value)

    @property
    def fahrenheit(self) -> float:
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value: float) -> None:
        # Set Fahrenheit, store in Celsius internally
        celsius_value = (value - 32) * 5 / 9
        self.celsius = celsius_value  # reuse validation

    def __repr__(self) -> str:
        return f"Temperature({self.celsius:.1f} °C / {self.fahrenheit:.1f} °F)"


temp = Temperature(25.0)
print("Initial:", temp)

print("Set temp.fahrenheit = 68...")
temp.fahrenheit = 68
print("Now:", temp)

print("Set temp.celsius = 30...")
temp.celsius = 30
print("Now:", temp)

print("-" * 50)


# ===========================================================
# Rank 5 — Professional
# Mini gradebook model using properties
# ===========================================================

print("Rank 5 — Professional")


class StudentRecord:
    """
    Represents a student's record in one course.

    Properties:
    - numeric_grade: main numeric score (0–100) with validation.
    - letter_grade: read-only mapping from numeric_grade to A/B/C/D/F.
    - is_passing: read-only True/False based on numeric_grade.
    - status: read-only text summary.

    Demonstrates how properties can:
    - enforce rules
    - compute values on the fly
    - keep everything in sync with simple attribute syntax
    """

    def __init__(self, name: str, numeric_grade: float) -> None:
        self.name = name
        self._numeric_grade: float = 0.0
        self.numeric_grade = numeric_grade  # use setter

    @property
    def numeric_grade(self) -> float:
        return self._numeric_grade

    @numeric_grade.setter
    def numeric_grade(self, value: float) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("numeric_grade must be a number")
        if value < 0 or value > 100:
            raise ValueError("numeric_grade must be between 0 and 100")
        self._numeric_grade = float(value)

    @property
    def letter_grade(self) -> str:
        g = self.numeric_grade
        if g >= 90:
            return "A"
        if g >= 80:
            return "B"
        if g >= 70:
            return "C"
        if g >= 60:
            return "D"
        return "F"

    @property
    def is_passing(self) -> bool:
        return self.numeric_grade >= 60.0

    @property
    def status(self) -> str:
        return f"{self.letter_grade} ({'PASS' if self.is_passing else 'FAIL'})"

    def __repr__(self) -> str:
        return f"StudentRecord({self.name!r}, {self.numeric_grade:.1f}, {self.status})"


class CourseGradebook:
    """
    A simple gradebook for one course.

    - Uses StudentRecord objects.
    - Provides properties for:
      * average_grade
      * passing_rate
      * best_student
      * worst_student
    """

    def __init__(self, course_name: str) -> None:
        self.course_name = course_name
        self._records: List[StudentRecord] = []

    def add_record(self, record: StudentRecord) -> None:
        self._records.append(record)

    @property
    def records(self) -> List[StudentRecord]:
        """
        Read-only view (you still could modify the list contents,
        but not replace the list itself).
        """
        return self._records

    @property
    def average_grade(self) -> float:
        if not self._records:
            return 0.0
        total = sum(r.numeric_grade for r in self._records)
        return total / len(self._records)

    @property
    def passing_rate(self) -> float:
        """
        Percentage of students who are passing (0.0 to 100.0).
        """
        if not self._records:
            return 0.0
        passing = sum(1 for r in self._records if r.is_passing)
        return passing * 100.0 / len(self._records)

    @property
    def best_student(self) -> Optional[StudentRecord]:
        if not self._records:
            return None
        return max(self._records, key=lambda r: r.numeric_grade)

    @property
    def worst_student(self) -> Optional[StudentRecord]:
        if not self._records:
            return None
        return min(self._records, key=lambda r: r.numeric_grade)

    def __repr__(self) -> str:
        return f"CourseGradebook({self.course_name!r}, {len(self._records)} records)"


gradebook = CourseGradebook("Python Programming 2025")

gradebook.add_record(StudentRecord("Peyman", 92))
gradebook.add_record(StudentRecord("Ana", 78))
gradebook.add_record(StudentRecord("Luis", 55))
gradebook.add_record(StudentRecord("Maria", 88))

print(gradebook)
print("Average grade:", gradebook.average_grade)
print("Passing rate:", f"{gradebook.passing_rate:.1f}%")

print("Best student:", gradebook.best_student)
print("Worst student:", gradebook.worst_student)

print("\nDetailed records:")
for record in gradebook.records:
    print(f"- {record.name:10s} | numeric={record.numeric_grade:5.1f} | status={record.status}")

print("-" * 50)
