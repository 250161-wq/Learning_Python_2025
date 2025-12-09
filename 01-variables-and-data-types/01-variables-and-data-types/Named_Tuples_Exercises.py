"""
Module 27 — Named Tuples: Practice Exercises
Comprehensive practice with Python named tuples, from beginner to
more professional, production-style usage.

In this module I:
- Practice how to create and use named tuples.
- Start from very simple examples (Rank 1) and move toward
  more realistic, professional patterns (Rank 5).
- Use both collections.namedtuple and typing.NamedTuple.
- Focus only on named tuples here. Data classes come in the next module.

Ranking system:
- Rank 1  -> Beginner: very basic syntax and concepts.
- Rank 2  -> Easy: still simple, but combining two or more concepts.
- Rank 3  -> Intermediate: more operations in a single example.
- Rank 4  -> Advanced: closer to how named tuples are used in real projects.
- Rank 5  -> Professional: clean, reusable, and readable patterns.

Author: Peyman Miyandashti
Date of Birth: 11/11/1983
ID Number: 250161
Year: 2025
"""

from collections import namedtuple
from typing import NamedTuple, List


# ===========================================================
# Rank 1 — Beginner
# Simple namedtuple creation and basic attribute access
# ===========================================================

print("Rank 1 — Beginner")

# Define a simple namedtuple type
Point = namedtuple("Point", ["x", "y"])

# Create an instance
origin = Point(0, 0)
point_a = Point(5, 10)

print("Origin:", origin)
print("Point A x:", point_a.x)
print("Point A y:", point_a.y)

# You can still access by index (like a normal tuple)
print("Point A (index 0):", point_a[0])
print("Point A (index 1):", point_a[1])
print("-" * 50)


# ===========================================================
# Rank 2 — Easy
# Multiple fields, unpacking, and simple calculations
# ===========================================================

print("Rank 2 — Easy")

# A namedtuple for a rectangle
Rectangle = namedtuple("Rectangle", ["width", "height"])

rect = Rectangle(width=4, height=7)

# Unpack into variables
w, h = rect

area = w * h
perimeter = 2 * (w + h)

print("Rectangle:", rect)
print("Width:", w)
print("Height:", h)
print("Area:", area)
print("Perimeter:", perimeter)
print("-" * 50)


# ===========================================================
# Rank 3 — Intermediate
# Using _replace, defaults via a factory function, and validation
# ===========================================================

print("Rank 3 — Intermediate")

# A namedtuple for a network device
NetworkDevice = namedtuple("NetworkDevice", ["name", "ip", "enabled"])

def make_device(name: str, ip: str, enabled: bool = True) -> NetworkDevice:
    """
    Factory function to create a NetworkDevice.

    This shows how to combine namedtuple with a simple function to
    simulate default values and basic validation.
    """
    if not ip or "." not in ip:
        raise ValueError(f"Invalid IP address: {ip!r}")
    return NetworkDevice(name=name, ip=ip, enabled=enabled)


device1 = make_device("router-1", "192.168.0.1")
device2 = make_device("switch-1", "192.168.0.2", enabled=False)

# Use _replace to create a modified copy (remember: namedtuples are immutable)
device2_enabled = device2._replace(enabled=True)

print("Device 1:", device1)
print("Device 2 (original):", device2)
print("Device 2 (enabled):", device2_enabled)
print("-" * 50)


# ===========================================================
# Rank 4 — Advanced
# Using typing.NamedTuple with type hints and methods
# ===========================================================

print("Rank 4 — Advanced")


class Student(NamedTuple):
    """
    Example of using typing.NamedTuple with type hints
    and a small method-like helper.
    """
    name: str
    group: str
    math_score: float
    physics_score: float

    def average(self) -> float:
        """Return the average score of the student."""
        return (self.math_score + self.physics_score) / 2


student_1 = Student(
    name="Peyman Miyandashti",
    group="1A",
    math_score=9.5,
    physics_score=8.7,
)

print("Student:", student_1)
print("Name:", student_1.name)
print("Group:", student_1.group)
print("Average score:", student_1.average())
print("-" * 50)


# ===========================================================
# Rank 5 — Professional
# Using named tuples in collections and utility functions
# ===========================================================

print("Rank 5 — Professional")


class Lesson(NamedTuple):
    """
    Represents a scheduled lesson in a school timetable.

    This is closer to real-world usage: a small, immutable data
    structure used in lists, filtering, and sorting.
    """
    subject: str
    teacher: str
    room: str
    start_time: str  # "08:00"
    end_time: str    # "08:50"


def build_daily_timetable() -> List[Lesson]:
    """Create a sample daily timetable using Lesson named tuples."""
    return [
        Lesson("Matemáticas", "Prof. Peyman", "A1", "08:00", "08:50"),
        Lesson("Física", "Prof. Peyman", "A1", "08:50", "09:40"),
        Lesson("Inglés", "Miss Arlette", "B2", "09:50", "10:40"),
        Lesson("Formación Cívica", "Prof. López", "A1", "10:50", "11:40"),
    ]


def print_timetable(lessons: List[Lesson]) -> None:
    """Nicely formatted timetable printout using attributes."""
    print("Daily Timetable")
    print("================")
    for lesson in lessons:
        print(
            f"{lesson.start_time}–{lesson.end_time} | "
            f"{lesson.subject:18} | "
            f"{lesson.teacher:15} | "
            f"Room {lesson.room}"
        )


def find_lessons_by_teacher(
    lessons: List[Lesson],
    teacher_name: str,
) -> List[Lesson]:
    """Return only the lessons taught by the given teacher."""
    return [lesson for lesson in lessons if lesson.teacher == teacher_name]


timetable = build_daily_timetable()
print_timetable(timetable)

pey_man_lessons = find_lessons_by_teacher(timetable, "Prof. Peyman")
print("\nLessons taught by Prof. Peyman:")
for lesson in pey_man_lessons:
    print(f"- {lesson.subject} in room {lesson.room} ({lesson.start_time})")

print("-" * 50)
