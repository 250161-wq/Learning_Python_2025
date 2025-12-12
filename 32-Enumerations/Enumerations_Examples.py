"""
Enumerations_Examples.py
Module 32 — Enumerations
Author: Peyman Miyandashti
Year: 2025

This file contains clear and practical examples
showing how enumerations (Enum) work in Python.
"""

# ---------------------------------------------------------------------------
# Example 1: Basic Enum Definition
# ---------------------------------------------------------------------------

from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(Color.RED)
print(Color.RED.name)
print(Color.RED.value)


# ---------------------------------------------------------------------------
# Example 2: Iterating Over Enum Members
# ---------------------------------------------------------------------------

for color in Color:
    print(color)


# ---------------------------------------------------------------------------
# Example 3: Enum Comparison
# ---------------------------------------------------------------------------

if Color.RED == Color.RED:
    print("Same color")

if Color.RED != Color.GREEN:
    print("Different colors")


# ---------------------------------------------------------------------------
# Example 4: Using Enums in Conditions
# ---------------------------------------------------------------------------

current_color = Color.BLUE

if current_color == Color.BLUE:
    print("Blue selected")


# ---------------------------------------------------------------------------
# Example 5: Enum with auto() Values
# ---------------------------------------------------------------------------

from enum import auto

class Status(Enum):
    NEW = auto()
    IN_PROGRESS = auto()
    DONE = auto()

for status in Status:
    print(status.name, status.value)


# ---------------------------------------------------------------------------
# Example 6: IntEnum Comparison
# ---------------------------------------------------------------------------

from enum import IntEnum

class Priority(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

if Priority.HIGH > Priority.MEDIUM:
    print("High priority")


# ---------------------------------------------------------------------------
# Example 7: Enum from Value
# ---------------------------------------------------------------------------

color = Color(1)
print(color)


# ---------------------------------------------------------------------------
# Example 8: Preventing Invalid Values
# ---------------------------------------------------------------------------

def paint(color: Color):
    if not isinstance(color, Color):
        raise ValueError("Invalid color")
    print("Painting with", color.name)

paint(Color.GREEN)


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# These examples show how enums:
# - improve code readability
# - prevent invalid values
# - provide safer comparisons
#
# Next Step:
# Continue with Enumerations_Tasks.py
