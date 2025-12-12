"""
Frozen_Data_Classes_Examples.py
Module 35 — Frozen Data Classes
Author: Peyman Miyandashti
Year: 2025

This file contains clear and practical examples
showing how frozen data classes behave in Python.
"""

from dataclasses import dataclass, replace

# ---------------------------------------------------------------------------
# Example 1: Basic Frozen Data Class
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class User:
    username: str
    role: str

user1 = User("peyman", "admin")
print(user1)


# ---------------------------------------------------------------------------
# Example 2: Immutability Enforcement
# ---------------------------------------------------------------------------
# The following line would raise FrozenInstanceError:
# user1.role = "editor"


# ---------------------------------------------------------------------------
# Example 3: Equality and Hashing
# ---------------------------------------------------------------------------

user2 = User("peyman", "admin")
print(user1 == user2)
print(hash(user1))


# ---------------------------------------------------------------------------
# Example 4: Using Frozen Data Classes as Dictionary Keys
# ---------------------------------------------------------------------------

permissions = {
    User("peyman", "admin"): "full access",
    User("guest", "viewer"): "read only"
}

print(permissions[User("peyman", "admin")])


# ---------------------------------------------------------------------------
# Example 5: Creating Modified Copies with replace()
# ---------------------------------------------------------------------------

user3 = replace(user1, role="editor")
print(user3)


# ---------------------------------------------------------------------------
# Example 6: Frozen Does Not Guarantee Deep Immutability
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Config:
    options: list

config = Config(["debug", "verbose"])
config.options.append("safe")
print(config.options)


# ---------------------------------------------------------------------------
# Example 7: Frozen Data Class with Methods
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Rectangle:
    width: float
    height: float

    def area(self):
        return self.width * self.height

rect = Rectangle(5, 6)
print(rect.area())


# ---------------------------------------------------------------------------
# Example 8: Comparing Frozen Data Classes to Named Tuples
# ---------------------------------------------------------------------------

from collections import namedtuple

PointNT = namedtuple("PointNT", ["x", "y"])

pt_nt = PointNT(3, 4)
pt_dc = Rectangle(3, 4)

print(pt_nt)
print(pt_dc)


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# These examples show that frozen data classes:
# - prevent attribute reassignment
# - support hashing and equality
# - remain flexible with methods
#
# Next Step:
# Continue with Frozen_Data_Classes_Tasks.py
