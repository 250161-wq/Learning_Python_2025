"""
Typing_Advanced_Tasks.py
Module 47 — Typing & Type Hints (Advanced)
Author: Peyman Miyandashti
Year: 2025

This file contains practice exercises focused on advanced typing.
The exercises progress from beginner-advanced to professional level.
Do not check the solutions file until you have attempted all tasks.
"""

from typing import (
    List, Dict, Tuple,
    Union, Optional, Literal,
    Callable, TypeVar, Generic,
    Protocol, TypedDict
)

# ---------------------------------------------------------------------------
# Rank 1 — Beginner-Advanced
# ---------------------------------------------------------------------------

# Task 1
# Write a function that accepts either an int or a string
# and returns it converted to a string.
# Use Union in the type hint.


# Task 2
# Write a function that may return an integer or None.
# Use Optional in the return type.


# ---------------------------------------------------------------------------
# Rank 2 — Easy
# ---------------------------------------------------------------------------

# Task 3
# Write a function that accepts a mode argument
# restricted to "r", "w", or "a" using Literal.


# Task 4
# Annotate a list of integers, a dictionary of string to int,
# and a tuple of two integers.


# ---------------------------------------------------------------------------
# Rank 3 — Intermediate
# ---------------------------------------------------------------------------

# Task 5
# Create a generic function using TypeVar
# that returns the last element of a list.


# Task 6
# Create a generic class that stores a value
# and returns it using a method.


# ---------------------------------------------------------------------------
# Rank 4 — Advanced
# ---------------------------------------------------------------------------

# Task 7
# Define a Protocol that requires a method named process()
# returning a string.
# Write a function that accepts this protocol.


# Task 8
# Create a TypedDict representing user data
# with fields: id (int), name (str), active (bool).


# ---------------------------------------------------------------------------
# Rank 5 — Professional
# ---------------------------------------------------------------------------

# Task 9
# Write a function that accepts another function as an argument
# using Callable, applies it to two integers,
# and returns the result.


# Task 10
# Explain (in comments):
# - when advanced typing improves code quality
# - when it can be overkill


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# These tasks reinforce:
# - expressive type design
# - safe and readable APIs
# - professional-level Python typing
#
# Next Step:
# Continue with Typing_Advanced_Tasks_Solutions.py
