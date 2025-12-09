"""
Module 28 — Data Classes: Practice Exercises
Comprehensive practice with Python data classes, from beginner to
more professional, production-style usage.

In this module I:
- Practice how to create and use data classes with @dataclass.
- Start from very simple examples (Rank 1) and move toward
  more realistic, professional patterns (Rank 5).
- Use type hints, default values, methods, and immutability.

Ranking system:
- Rank 1  -> Beginner: very basic syntax and concepts.
- Rank 2  -> Easy: still simple, but combining two or more concepts.
- Rank 3  -> Intermediate: more operations and logic in one class.
- Rank 4  -> Advanced: relationships between objects, lists, and helpers.
- Rank 5  -> Professional: patterns that feel like real application code.

Author: Peyman Miyandashti
Date of Birth: 11/11/1983
ID Number: 250161
Year: 2025
"""

from dataclasses import dataclass, field, asdict, replace
from typing import List


# ===========================================================
# Rank 1 — Beginner
# Simple data class with a few fields
# ===========================================================

print("Rank 1 — Beginner")


@dataclass
class SimpleStudent:
    name: str
    age: int


student = SimpleStudent(name="Peyman", age=41)

print("SimpleStudent instance:", student)
print("Name:", student.name)
print("Age:", student.age)
print("-" * 50)


# ===========================================================
# Rank 2 — Easy
# Default values, type hints, and equality
# ===========================================================

print("Rank 2 — Easy")


@dataclass
class Course:
    name: str
    credits: int = 6
    is_active: bool = True


course_math = Course(name="Matemáticas I")
course_physics = Course(name="Física I", credits=8)
course_math_copy = Course(name="Matemáticas I", credits=6)

print("Course (math):", course_math)
print("Course (physics):", course_physics)
print("Course (math copy):", course_math_copy)
print("Is math equal to math_copy?", course_math == course_math_copy)
print("-" * 50)


# ===========================================================
# Rank 3 — Intermediate
# Methods, __post_init__ for validation and normalization
# ===========================================================

print("Rank 3 — Intermediate")


@dataclass
class GradedStudent:
    name: str
    math_score: float
    physics_score: float
    group: str

    def __post_init__(self) -> None:
        # Normalize group and validate scores
        self.group = self.group.upper().strip()

        for field_name in ("math_score", "physics_score"):
            value = getattr(self, field_name)
            if not (0.0 <= value <= 10.0):
                raise ValueError(f"{field_name} must be between 0 and 10, got {value!r}")

    def average(self) -> float:
        return (self.math_score + self.physics_score) / 2

    def passed(self, min_avg: float = 6.0) -> bool:
        return self.average() >= min_avg


graded_student = GradedStudent(
    name="Peyman Miyandashti",
    math_score=9.2,
    physics_score=8.8,
    group=" 1a ",
)

print("GradedStudent:", graded_student)
print("Average:", graded_student.average())
print("Passed? ->", graded_student.passed())
print("-" * 50)


# ===========================================================
# Rank 4 — Advanced
# Data classes with list fields and helper functions
# ===========================================================

print("Rank 4 — Advanced")


@dataclass
class LessonDC:
    subject: str
    teacher: str
    room: str
    start_time: str
    end_time: str


@dataclass
class TimetableDC:
    group: str
    lessons: List[LessonDC] = field(default_factory=list)

    def add_lesson(self, lesson: LessonDC) -> None:
        self.lessons.append(lesson)

    def list_subjects(self) -> List[str]:
        return sorted({lesson.subject for lesson in self.lessons})

    def lessons_by_teacher(self, teacher: str) -> List[LessonDC]:
        return [lesson for lesson in self.lessons if lesson.teacher == teacher]


timetable_1a = TimetableDC(group="1A")

timetable_1a.add_lesson(
    LessonDC("Matemáticas", "Prof. Peyman", "A1", "08:00", "08:50")
)
timetable_1a.add_lesson(
    LessonDC("Física", "Prof. Peyman", "A1", "08:50", "09:40")
)
timetable_1a.add_lesson(
    LessonDC("Inglés", "Miss Arlette", "B2", "09:50", "10:40")
)

print("Timetable for group:", timetable_1a.group)
print("Subjects:", timetable_1a.list_subjects())

print("\nLessons by Prof. Peyman:")
for lesson in timetable_1a.lessons_by_teacher("Prof. Peyman"):
    print(f"- {lesson.subject} in room {lesson.room} ({lesson.start_time})")

print("-" * 50)


# ===========================================================
# Rank 5 — Professional
# Frozen (immutable) data class, configuration object, asdict, replace
# ===========================================================

print("Rank 5 — Professional")


@dataclass(frozen=True)
class AppConfig:
    """
    Example of a configuration object for an application.

    - frozen=True makes it immutable (like a namedtuple).
    - We use replace() to create modified copies.
    """
    app_name: str
    debug: bool
    version: str
    database_url: str
    max_connections: int = 10


config_default = AppConfig(
    app_name="SchoolManager",
    debug=True,
    version="1.0.0",
    database_url="sqlite:///school.db",
)

# Convert to dict for logging or serialization
config_dict = asdict(config_default)

# Create a modified copy for production (debug=False)
config_production = replace(
    config_default,
    debug=False,
    database_url="postgresql://user:password@localhost/school",
)

print("Default config:", config_default)
print("Config as dict:", config_dict)
print("Production config:", config_production)

print("-" * 50)
