"""
Module 34 — Class & Static Methods: Practice Exercises
Comprehensive practice with @classmethod and @staticmethod, from beginner
to more professional, production-style usage.

In this module I:
- Compare instance methods, class methods, and static methods.
- Use class methods as alternative constructors.
- Use static methods as utility helpers that do not depend on instance state.
- Build small realistic models (students, configuration, and factories).

Ranking system:
- Rank 1  -> Beginner: basic instance vs class vs static methods.
- Rank 2  -> Easy: alternative constructors with @classmethod.
- Rank 3  -> Intermediate: validation and parsing helpers.
- Rank 4  -> Advanced: factory patterns and shared registries.
- Rank 5  -> Professional: mini "school system" using class & static methods.

Author: Peyman Miyandashti
Date of Birth: 11/11/1983
ID Number: 250161
Year: 2025
"""

from __future__ import annotations
from typing import List, Dict, Any

# ===========================================================
# Rank 1 — Beginner
# Instance vs class vs static methods
# ===========================================================

print("Rank 1 — Beginner")


class Counter:
    total_counters_created: int = 0  # class attribute

    def __init__(self, name: str) -> None:
        self.name = name
        self.value = 0
        Counter.total_counters_created += 1

    # Instance method: works with one specific object (self)
    def increment(self) -> None:
        self.value += 1
        print(f"[{self.name}] value is now {self.value}")

    # Class method: works with the class itself (cls)
    @classmethod
    def how_many_created(cls) -> int:
        return cls.total_counters_created

    # Static method: utility; does not touch class or instance state
    @staticmethod
    def is_valid_start_value(value: int) -> bool:
        return value >= 0


c1 = Counter("Lesson views")
c2 = Counter("Quiz attempts")

c1.increment()
c1.increment()
c2.increment()

print("Total counters created:", Counter.how_many_created())
print("Is -5 a valid start value?", Counter.is_valid_start_value(-5))
print("Is 10 a valid start value?", Counter.is_valid_start_value(10))
print("-" * 50)


# ===========================================================
# Rank 2 — Easy
# Class methods as alternative constructors
# ===========================================================

print("Rank 2 — Easy")


class Student:
    def __init__(self, name: str, age: int, country: str) -> None:
        self.name = name
        self.age = age
        self.country = country

    def __repr__(self) -> str:
        return f"Student(name={self.name!r}, age={self.age}, country={self.country!r})"

    @classmethod
    def from_string(cls, text: str) -> "Student":
        """
        Alternative constructor.
        Example: 'Peyman, 41, Mexico'
        """
        parts = [item.strip() for item in text.split(",")]
        if len(parts) != 3:
            raise ValueError(f"Cannot parse student string: {text!r}")
        name = parts[0]
        age = int(parts[1])
        country = parts[2]
        return cls(name, age, country)

    @classmethod
    def default_mexican(cls, name: str, age: int) -> "Student":
        """
        Another alternative constructor with default country.
        """
        return cls(name, age, "Mexico")


s1 = Student("Ana", 20, "Mexico")
s2 = Student.from_string("Peyman, 41, Mexico")
s3 = Student.default_mexican("Luis", 19)

print("Student 1:", s1)
print("Student 2:", s2)
print("Student 3:", s3)
print("-" * 50)


# ===========================================================
# Rank 3 — Intermediate
# Static methods for validation and small utilities
# ===========================================================

print("Rank 3 — Intermediate")


class GradeUtils:
    """
    Utility class to group static helper methods related to grades.
    """

    @staticmethod
    def is_passing(grade: float) -> bool:
        return grade >= 60.0

    @staticmethod
    def to_letter(grade: float) -> str:
        if grade >= 90:
            return "A"
        if grade >= 80:
            return "B"
        if grade >= 70:
            return "C"
        if grade >= 60:
            return "D"
        return "F"

    @staticmethod
    def clamp_grade(grade: float) -> float:
        """
        Clamp grade between 0 and 100.
        """
        return max(0.0, min(100.0, grade))


grades = [55.2, 89.5, 100.1, -5, 72.3]
for g in grades:
    g_clamped = GradeUtils.clamp_grade(g)
    print(
        f"Original: {g:6.1f} | Clamped: {g_clamped:6.1f} | "
        f"Passing: {GradeUtils.is_passing(g_clamped)} | Letter: {GradeUtils.to_letter(g_clamped)}"
    )

print("-" * 50)


# ===========================================================
# Rank 4 — Advanced
# Factory patterns and shared registries via class methods
# ===========================================================

print("Rank 4 — Advanced")


class Lesson:
    _registry: Dict[str, "Lesson"] = {}

    def __init__(self, code: str, title: str, duration_minutes: int) -> None:
        self.code = code
        self.title = title
        self.duration_minutes = duration_minutes
        # Automatically register
        Lesson._registry[code] = self

    def __repr__(self) -> str:
        return f"Lesson({self.code!r}, {self.title!r}, {self.duration_minutes} min)"

    @classmethod
    def create_python_intro(cls) -> "Lesson":
        return cls("PY101", "Introduction to Python", 90)

    @classmethod
    def create_math_review(cls) -> "Lesson":
        return cls("MATH101", "Algebra Review", 60)

    @classmethod
    def get_by_code(cls, code: str) -> "Lesson":
        if code not in cls._registry:
            raise KeyError(f"No lesson with code {code!r}")
        return cls._registry[code]

    @classmethod
    def all_lessons(cls) -> List["Lesson"]:
        return list(cls._registry.values())


# Using the factory class methods
python_lesson = Lesson.create_python_intro()
math_lesson = Lesson.create_math_review()
custom_lesson = Lesson("SCI101", "Basic Physics", 75)

print("All registered lessons:")
for lesson in Lesson.all_lessons():
    print("  ", lesson)

print("Get lesson by code 'PY101':", Lesson.get_by_code("PY101"))
print("-" * 50)


# ===========================================================
# Rank 5 — Professional
# Small "school system" using class & static methods
# ===========================================================

print("Rank 5 — Professional")


class Course:
    """
    Represents a course with a code, name, and enrolled students.
    Uses class methods to create pre-configured courses and static methods
    for small helpers.
    """

    _catalog: Dict[str, "Course"] = {}

    def __init__(self, code: str, name: str) -> None:
        self.code = code
        self.name = name
        self.students: List[Student] = []
        Course._catalog[code] = self

    def enroll(self, student: Student) -> None:
        self.students.append(student)
        print(f"Enrolled {student.name} into {self.code} – {self.name}")

    def average_age(self) -> float:
        if not self.students:
            return 0.0
        total = sum(s.age for s in self.students)
        return total / len(self.students)

    @classmethod
    def create_python_course(cls) -> "Course":
        return cls("PY-2025", "Python for Beginners")

    @classmethod
    def create_physics_course(cls) -> "Course":
        return cls("PHYS-2025", "Physics for Secondary School")

    @classmethod
    def get_course(cls, code: str) -> "Course":
        if code not in cls._catalog:
            raise KeyError(f"Course {code!r} not found")
        return cls._catalog[code]

    @classmethod
    def list_courses(cls) -> List["Course"]:
        return list(cls._catalog.values())

    @staticmethod
    def describe_student(student: Student) -> str:
        """
        Static helper to describe a student in one line.
        """
        return f"{student.name} ({student.age}, {student.country})"


# Create some students (reusing Student class from Rank 2)
pey = Student.default_mexican("Peyman", 41)
ana = Student("Ana", 20, "Mexico")
luis = Student("Luis", 19, "Mexico")

# Create and use courses via class methods
python_course = Course.create_python_course()
physics_course = Course.create_physics_course()

python_course.enroll(pey)
python_course.enroll(ana)
physics_course.enroll(luis)

print()
print("Course catalog:")
for course in Course.list_courses():
    print(f"- {course.code}: {course.name} (students: {len(course.students)})")

print()
print("Python course average age:", python_course.average_age())
print("Physics course average age:", physics_course.average_age())

print()
print("Student descriptions:")
for student in [pey, ana, luis]:
    print(" ", Course.describe_student(student))

print("-" * 50)
