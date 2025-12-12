"""
Data_Classes_Examples.py
Module 34 — Data Classes
Author: Peyman Miyandashti
Year: 2025

This file contains clear and practical examples
showing how data classes are used in Python.
"""

from dataclasses import dataclass, field, replace

# ---------------------------------------------------------------------------
# Example 1: Basic Data Class
# ---------------------------------------------------------------------------

@dataclass
class User:
    username: str
    email: str
    active: bool = True

user1 = User("peyman", "peyman@example.com")
print(user1)


# ---------------------------------------------------------------------------
# Example 2: Equality Comparison
# ---------------------------------------------------------------------------

user2 = User("peyman", "peyman@example.com")
print(user1 == user2)


# ---------------------------------------------------------------------------
# Example 3: Mutable Fields with default_factory
# ---------------------------------------------------------------------------

@dataclass
class Cart:
    items: list = field(default_factory=list)

cart = Cart()
cart.items.append("Book")
cart.items.append("Pen")
print(cart)


# ---------------------------------------------------------------------------
# Example 4: Adding Behavior (Methods)
# ---------------------------------------------------------------------------

@dataclass
class Rectangle:
    width: float
    height: float

    def area(self):
        return self.width * self.height

rect = Rectangle(6, 4)
print(rect.area())


# ---------------------------------------------------------------------------
# Example 5: Frozen Data Class
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Point:
    x: int
    y: int

pt = Point(3, 7)
print(pt)


# ---------------------------------------------------------------------------
# Example 6: Updating Data with replace()
# ---------------------------------------------------------------------------
# replace() creates a new instance with updated values.

user3 = replace(user1, active=False)
print(user3)


# ---------------------------------------------------------------------------
# Example 7: Using Data Classes as Return Values
# ---------------------------------------------------------------------------

@dataclass
class Result:
    success: bool
    message: str

def process_data(ok: bool):
    if ok:
        return Result(True, "Processing completed")
    return Result(False, "Processing failed")

print(process_data(True))


# ---------------------------------------------------------------------------
# Example 8: Comparison with Named Tuples
# ---------------------------------------------------------------------------

from collections import namedtuple

PointNT = namedtuple("PointNT", ["x", "y"])

p_nt = PointNT(3, 7)
print(p_nt == pt)  # Different types


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# These examples show how data classes:
# - reduce boilerplate
# - improve readability
# - support behavior and structure
#
# Next Step:
# Continue with Data_Classes_Tasks.py
