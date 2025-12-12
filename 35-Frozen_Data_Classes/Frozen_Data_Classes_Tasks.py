"""
Frozen_Data_Classes_Tasks.py
Module 35 — Frozen Data Classes
Author: Peyman Miyandashti
Year: 2025

This file contains practice exercises focused on frozen data classes.
The exercises progress from beginner to professional level.
Do not check the solutions file until you have attempted all tasks.
"""

from dataclasses import dataclass, replace

# ---------------------------------------------------------------------------
# Rank 1 — Beginner
# ---------------------------------------------------------------------------

# Task 1
# Create a frozen data class called Point with fields:
# x (int) and y (int).
# Create an instance and print it.


# Task 2
# Try to modify one of the attributes of Point.
# Observe and understand the error that occurs.


# ---------------------------------------------------------------------------
# Rank 2 — Easy
# ---------------------------------------------------------------------------

# Task 3
# Create two Point objects with the same values
# and compare them using == .


# Task 4
# Print the hash value of a Point instance.


# ---------------------------------------------------------------------------
# Rank 3 — Intermediate
# ---------------------------------------------------------------------------

# Task 5
# Use a frozen data class as a key in a dictionary
# and retrieve a value using a new instance with the same data.


# Task 6
# Use dataclasses.replace() to create a modified copy
# of a frozen Point object.


# ---------------------------------------------------------------------------
# Rank 4 — Advanced
# ---------------------------------------------------------------------------

# Task 7
# Create a frozen data class that contains a mutable field (like a list).
# Modify the contents of the list and observe what happens.


# Task 8
# Explain (in comments) why frozen data classes are not deeply immutable.


# ---------------------------------------------------------------------------
# Rank 5 — Professional
# ---------------------------------------------------------------------------

# Task 9
# Design a frozen data class to represent a configuration value object
# that should never be modified after creation.


# Task 10
# Use the frozen configuration data class in a function
# to control application behavior.


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# These tasks focus on immutability, safety, and professional
# design decisions using frozen data classes.
#
# Next Step:
# Continue with Frozen_Data_Classes_Tasks_Solutions.py
