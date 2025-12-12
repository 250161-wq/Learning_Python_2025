"""
Data_Classes_Tasks.py
Module 34 — Data Classes
Author: Peyman Miyandashti
Year: 2025

This file contains practice exercises focused on data classes.
The exercises progress from beginner to professional level.
Do not check the solutions file until you have attempted all tasks.
"""

from dataclasses import dataclass, field

# ---------------------------------------------------------------------------
# Rank 1 — Beginner
# ---------------------------------------------------------------------------

# Task 1
# Create a data class called Person with fields:
# name (str) and age (int).
# Create an instance and print it.


# Task 2
# Create two Person objects with the same values
# and compare them using == .


# ---------------------------------------------------------------------------
# Rank 2 — Easy
# ---------------------------------------------------------------------------

# Task 3
# Create a data class called Product with fields:
# name (str), price (float), and in_stock (bool) with default True.


# Task 4
# Modify an attribute of a Product instance
# and print the updated object.


# ---------------------------------------------------------------------------
# Rank 3 — Intermediate
# ---------------------------------------------------------------------------

# Task 5
# Create a data class called Order with fields:
# id (int) and items (list).
# Use default_factory to avoid shared mutable defaults.


# Task 6
# Add an item to the Order and print the result.


# ---------------------------------------------------------------------------
# Rank 4 — Advanced
# ---------------------------------------------------------------------------

# Task 7
# Create a frozen data class called Point with fields:
# x (int) and y (int).
# Try modifying a value and observe what happens.


# Task 8
# Use dataclasses.replace() to create a new instance
# with one modified value.


# ---------------------------------------------------------------------------
# Rank 5 — Professional
# ---------------------------------------------------------------------------

# Task 9
# Create a data class called UserProfile with fields:
# username, email, and active.
# Add a method that deactivates the user.


# Task 10
# Use a data class as a return value from a function
# that simulates a success or failure result.


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# These tasks reinforce clean data modeling,
# immutability, and professional use of data classes.
#
# Next Step:
# Continue with Data_Classes_Tasks_Solutions.py
