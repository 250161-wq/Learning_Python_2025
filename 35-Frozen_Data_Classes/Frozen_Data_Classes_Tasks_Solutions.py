"""
Frozen_Data_Classes_Tasks_Solutions.py
Module 35 — Frozen Data Classes
Author: Peyman Miyandashti
Year: 2025

This file contains clean and professional solutions
for the frozen data class exercises in this module.
"""

from dataclasses import dataclass, replace

# ---------------------------------------------------------------------------
# Rank 1 — Beginner
# ---------------------------------------------------------------------------

# Task 1 Solution
@dataclass(frozen=True)
class Point:
    x: int
    y: int

point1 = Point(10, 20)
print(point1)


# Task 2 Solution
# The following line would raise FrozenInstanceError:
# point1.x = 15


# ---------------------------------------------------------------------------
# Rank 2 — Easy
# ---------------------------------------------------------------------------

# Task 3 Solution
point2 = Point(10, 20)
print(point1 == point2)


# Task 4 Solution
print(hash(point1))


# ---------------------------------------------------------------------------
# Rank 3 — Intermediate
# ---------------------------------------------------------------------------

# Task 5 Solution
points = {
    Point(0, 0): "origin",
    Point(1, 1): "unit"
}

print(points[Point(0, 0)])


# Task 6 Solution
point3 = replace(point1, y=30)
print(point3)


# ---------------------------------------------------------------------------
# Rank 4 — Advanced
# ---------------------------------------------------------------------------

# Task 7 Solution
@dataclass(frozen=True)
class Box:
    items: list

box = Box([1, 2, 3])
box.items.append(4)
print(box.items)


# Task 8 Solution
# Frozen data classes prevent reassignment of attributes,
# but they do not prevent mutation of mutable objects stored inside them.
# This is why frozen data classes are not deeply immutable.


# ---------------------------------------------------------------------------
# Rank 5 — Professional
# ---------------------------------------------------------------------------

# Task 9 Solution
@dataclass(frozen=True)
class AppConfig:
    debug: bool
    version: str

config = AppConfig(debug=False, version="1.0.0")
print(config)


# Task 10 Solution
def start_app(config: AppConfig):
    if config.debug:
        print("Starting app in debug mode")
    else:
        print("Starting app in production mode")

start_app(config)


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# These solutions demonstrate safe and professional use
# of frozen data classes for immutable data modeling.
#
# Next Step:
# Move on to the next module when ready.
