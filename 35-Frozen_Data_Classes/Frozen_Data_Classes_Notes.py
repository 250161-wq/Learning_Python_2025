"""
Frozen_Data_Classes_Notes.py
Module 35 — Frozen Data Classes
Author: Peyman Miyandashti
Year: 2025

This module explains frozen data classes in Python.
Frozen data classes are immutable after creation.
"""

from dataclasses import dataclass, replace

# ---------------------------------------------------------------------------
# 1. What Is a Frozen Data Class?
# ---------------------------------------------------------------------------
# A frozen data class is created by setting frozen=True.
# This prevents modification of attributes after initialization.


# ---------------------------------------------------------------------------
# 2. Creating a Frozen Data Class
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Point:
    x: int
    y: int

p1 = Point(10, 20)
print(p1)


# ---------------------------------------------------------------------------
# 3. Attempting to Modify a Frozen Object
# ---------------------------------------------------------------------------
# This will raise FrozenInstanceError.

# p1.x = 15


# ---------------------------------------------------------------------------
# 4. Equality and Hashing
# ---------------------------------------------------------------------------
# Frozen data classes are hashable by default
# if all fields are hashable.

p2 = Point(10, 20)
print(p1 == p2)
print(hash(p1))


# ---------------------------------------------------------------------------
# 5. Using Frozen Objects as Dictionary Keys
# ---------------------------------------------------------------------------

points = {
    Point(0, 0): "origin",
    Point(1, 1): "unit"
}

print(points[Point(0, 0)])


# ---------------------------------------------------------------------------
# 6. Creating Modified Copies with replace()
# ---------------------------------------------------------------------------
# replace() creates a new instance with updated values.

p3 = replace(p1, x=30)
print(p3)


# ---------------------------------------------------------------------------
# 7. Frozen Does Not Mean Deeply Immutable
# ---------------------------------------------------------------------------
# If a field contains a mutable object, that object can still change.

@dataclass(frozen=True)
class Box:
    items: list

box = Box([1, 2, 3])
box.items.append(4)
print(box.items)


# ---------------------------------------------------------------------------
# 8. When to Use Frozen Data Classes
# ---------------------------------------------------------------------------
# Use frozen data classes when:
# - data represents a value object
# - changes should be prevented
# - hashability is needed
# - thread safety matters


# ---------------------------------------------------------------------------
# 9. Frozen vs Named Tuples
# ---------------------------------------------------------------------------
# Frozen data classes:
# - support methods
# - use type hints
# - more flexible
#
# Named tuples:
# - lighter
# - simpler
# - less extensible


# ---------------------------------------------------------------------------
# 10. Best Practices
# ---------------------------------------------------------------------------
# - Prefer frozen=True for value objects
# - Avoid mutable fields inside frozen classes
# - Use replace() for updates
# - Keep frozen classes small and focused


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# Frozen data classes enforce immutability by design.
# They help prevent bugs and improve code reliability.
#
# Next Step:
# Continue with Frozen_Data_Classes_Examples.py
