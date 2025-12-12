"""
Enumerations_Notes.py
Module 32 — Enumerations
Author: Peyman Miyandashti
Year: 2025

This module explains enumerations (Enum) in Python.
Enums are used to define fixed sets of named values.
"""

# ---------------------------------------------------------------------------
# 1. What Is an Enumeration?
# ---------------------------------------------------------------------------
# An enumeration is a collection of symbolic names bound to constant values.
# Enums improve readability and prevent invalid values.

# Example use cases:
# - status codes
# - modes
# - categories
# - states


# ---------------------------------------------------------------------------
# 2. Importing Enum
# ---------------------------------------------------------------------------

from enum import Enum


# ---------------------------------------------------------------------------
# 3. Creating a Basic Enum
# ---------------------------------------------------------------------------

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


# ---------------------------------------------------------------------------
# 4. Accessing Enum Members
# ---------------------------------------------------------------------------

print(Color.RED)
print(Color.RED.name)
print(Color.RED.value)


# ---------------------------------------------------------------------------
# 5. Iterating Over an Enum
# ---------------------------------------------------------------------------

for color in Color:
    print(color)


# ---------------------------------------------------------------------------
# 6. Comparing Enum Members
# ---------------------------------------------------------------------------
# Enum members are compared by identity, not by raw value.

print(Color.RED == Color.RED)
print(Color.RED == Color.GREEN)


# ---------------------------------------------------------------------------
# 7. Enums in Conditions
# ---------------------------------------------------------------------------

current_color = Color.RED

if current_color == Color.RED:
    print("The color is red")


# ---------------------------------------------------------------------------
# 8. Why Not Use Plain Constants?
# ---------------------------------------------------------------------------
# Plain constants allow invalid values.
# Enums restrict values to a known, controlled set.


# ---------------------------------------------------------------------------
# 9. Using auto() for Values
# ---------------------------------------------------------------------------

from enum import auto

class Status(Enum):
    STARTED = auto()
    RUNNING = auto()
    FINISHED = auto()


for status in Status:
    print(status.name, status.value)


# ---------------------------------------------------------------------------
# 10. IntEnum
# ---------------------------------------------------------------------------
# IntEnum allows comparison with integers.

from enum import IntEnum

class Priority(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

print(Priority.HIGH > Priority.MEDIUM)


# ---------------------------------------------------------------------------
# 11. Best Practices
# ---------------------------------------------------------------------------
# - Use enums for fixed sets of values
# - Compare enum members, not raw values
# - Avoid mixing enums and plain integers
# - Use meaningful enum names


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# Enumerations make code safer and more expressive.
# They help prevent bugs caused by invalid or unclear values.
#
# Next Step:
# Continue with Enumerations_Examples.py
