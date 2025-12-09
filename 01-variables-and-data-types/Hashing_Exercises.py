"""
Module 41 — Hashing: Practice Exercises
Comprehensive practice with Python hashing, from beginner
to more professional, production-style usage.

In this module I:
- Use the built-in hash() function on different objects.
- Understand which types are hashable (can be used as dict keys / set elements).
- Implement __hash__ and __eq__ correctly for custom classes.
- See why mutability and hashing can be dangerous together.
- Build a small realistic "registry" that uses hashing behind the scenes.

Ranking system:
- Rank 1  -> Beginner: basic hash() on built-in types.
- Rank 2  -> Easy: using hashable objects in dicts and sets.
- Rank 3  -> Intermediate: custom value objects with __eq__ and __hash__.
- Rank 4  -> Advanced: mutability pitfalls with hashed objects.
- Rank 5  -> Professional: small "student registry" keyed by value objects.

Author: Peyman Miyandashti
Date of Birth: 11/11/1983
ID Number: 250161
Year: 2025
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, Set, Tuple


# ===========================================================
# Rank 1 — Beginner
# Basic hash() on built-in types
# ===========================================================

print("Rank 1 — Beginner")

# Hashing simple immutable built-in types
x_int = 42
x_str = "Python"
x_tuple = (1, 2, 3)

print("hash(42):        ", hash(x_int))
print("hash('Python'):  ", hash(x_str))
print("hash((1,2,3)):   ", hash(x_tuple))

# Lists and dicts are mutable -> NOT hashable
values = [1, 2, 3]
mapping = {"a": 1}

print("\nAre these hashable?")
for obj in [x_int, x_str, x_tuple, values, mapping]:
    try:
        h = hash(obj)
    except TypeError as e:
        print(f"  {type(obj).__name__}: NOT hashable -> {e}")
    else:
        print(f"  {type(obj).__name__}: hashable, hash={h}")

print("-" * 50)


# ===========================================================
# Rank 2 — Easy
# Using hashable objects in dicts and sets
# ===========================================================

print("Rank 2 — Easy")

# Dict keys must be hashable
student_ages: Dict[str, int] = {
    "Peyman": 41,
    "Ana": 20,
    "Luis": 19,
}

print("student_ages:", student_ages)
print("Age of Peyman:", student_ages["Peyman"])

# Using tuples (immutable) as keys to represent coordinates
classroom_seats: Dict[Tuple[int, int], str] = {
    (0, 0): "Ana",
    (0, 1): "Luis",
    (1, 0): "Maria",
}

print("\nStudent in seat (0, 1):", classroom_seats[(0, 1)])

# Sets also use hashing for membership and uniqueness
visited_ids: Set[int] = set()
for sid in [1001, 1002, 1001, 1003, 1002]:
    visited_ids.add(sid)

print("\nUnique student IDs seen:", visited_ids)
print("Is 1001 in visited_ids?", 1001 in visited_ids)
print("Is 9999 in visited_ids?", 9999 in visited_ids)

print("-" * 50)


# ===========================================================
# Rank 3 — Intermediate
# Custom value objects with __eq__ and __hash__
# ===========================================================

print("Rank 3 — Intermediate")


@dataclass(frozen=True)
class StudentID:
    """
    Small value object representing a student identity.

    Using dataclass(frozen=True) automatically gives:
    - __eq__ based on fields
    - __hash__ based on fields (because it is frozen / immutable)
    """

    school_code: str
    number: int


sid1 = StudentID("SEC-12", 1001)
sid2 = StudentID("SEC-12", 1001)
sid3 = StudentID("SEC-12", 1002)

print("sid1:", sid1)
print("sid2:", sid2)
print("sid3:", sid3)

print("sid1 == sid2?", sid1 == sid2)
print("sid1 == sid3?", sid1 == sid3)

print("hash(sid1):", hash(sid1))
print("hash(sid2):", hash(sid2), "(same as sid1 because they are equal)")
print("hash(sid3):", hash(sid3))

# Use StudentID as dictionary keys
student_names: Dict[StudentID, str] = {
    sid1: "Peyman",
    sid3: "Ana",
}

print("\nstudent_names dictionary:")
for key, value in student_names.items():
    print("  ", key, "->", value)

print("Lookup with new object equal to sid1:", student_names[StudentID("SEC-12", 1001)])

print("-" * 50)


# ===========================================================
# Rank 4 — Advanced
# Mutability pitfalls with hashed objects
# ===========================================================

print("Rank 4 — Advanced")


class MutableStudent:
    """
    Example of a BAD design for hashing:
    - The hash depends on a mutable field (grade).
    - If the field changes after we add the object to a set/dict,
      behavior becomes confusing and buggy.
    """

    def __init__(self, name: str, grade: int) -> None:
        self.name = name
        self.grade = grade

    def __hash__(self) -> int:
        # BAD: hash uses grade, which can change
        return hash((self.name, self.grade))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, MutableStudent):
            return NotImplemented
        return (self.name, self.grade) == (other.name, other.grade)

    def __repr__(self) -> str:
        return f"MutableStudent({self.name!r}, grade={self.grade})"


ms = MutableStudent("Luis", 80)
students_set: Set[MutableStudent] = {ms}

print("Initial set:", students_set)
print("Is 'ms' in set?", ms in students_set)

# Now we change the grade (which affects the hash)
print("\nChanging ms.grade from 80 to 90...")
ms.grade = 90

print("After change, ms:", ms)
print("Is 'ms' still in set?", ms in students_set)

print("Current set contents:", students_set)
print("Trying to remove ms from set...")
try:
    students_set.remove(ms)
except KeyError as e:
    print("  Failed to remove:", e)

print(
    """
This demonstrates why:
- Objects used as dict keys or set elements should usually be IMMUTABLE
  (or at least the parts used for hashing must not change).
"""
)

print("-" * 50)


# ===========================================================
# Rank 5 — Professional
# Small "student registry" keyed by value objects
# ===========================================================

print("Rank 5 — Professional")


@dataclass(frozen=True)
class StudentKey:
    """
    Stable, immutable key for a student in the registry.

    Key is composed of:
    - school_code
    - enrollment_year
    - sequential_number
    """

    school_code: str
    enrollment_year: int
    sequential_number: int


@dataclass
class StudentInfo:
    """
    Information about a student that might change over time.
    (This object itself does not need to be hashable.)
    """

    full_name: str
    grade_level: int
    average_score: float = 0.0


class StudentRegistry:
    """
    Registry of students, using StudentKey as the dictionary key.

    Demonstrates:
    - Hashing of composite keys.
    - Using value objects for stable identity.
    """

    def __init__(self) -> None:
        self._data: Dict[StudentKey, StudentInfo] = {}

    def register(self, key: StudentKey, info: StudentInfo) -> None:
        if key in self._data:
            raise KeyError(f"Student {key} already registered")
        self._data[key] = info

    def get(self, key: StudentKey) -> StudentInfo:
        return self._data[key]

    def update_score(self, key: StudentKey, new_score: float) -> None:
        info = self._data[key]
        info.average_score = new_score

    def __contains__(self, key: StudentKey) -> bool:
        return key in self._data

    def __len__(self) -> int:
        return len(self._data)

    def __repr__(self) -> str:
        return f"StudentRegistry({len(self._data)} students)"


registry = StudentRegistry()

k1 = StudentKey("SEC-12", 2025, 1)
k2 = StudentKey("SEC-12", 2025, 2)

registry.register(k1, StudentInfo(full_name="Peyman Miyandashti", grade_level=3))
registry.register(k2, StudentInfo(full_name="Ana Lopez", grade_level=2))

print("Registry:", registry)
print("Is k1 in registry?", k1 in registry)
print("Is k2 in registry?", k2 in registry)

print("\nStudent for k1:", registry.get(k1))
print("Student for k2:", registry.get(k2))

print("\nUpdating Ana's average score...")
registry.update_score(k2, 89.5)
print("Student for k2 after update:", registry.get(k2))

print(
    """
Notice:
- StudentKey is immutable and hashable -> safe to use as dict key.
- StudentInfo is mutable, but it is the VALUE in the dict, not the KEY.
- This pattern is common in real applications for registries and caches.
"""
)

print("-" * 50)
