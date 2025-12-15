"""
Error_Handling_Tasks.py
Module 49 — Error Handling & Custom Exceptions
Author: Peyman Miyandashti
Year: 2025

This file contains practice exercises focused on
professional error handling and custom exception design.
The exercises progress from intermediate to professional level.
Do not check the solutions file until you have attempted all tasks.
"""

# ---------------------------------------------------------------------------
# Rank 1 — Intermediate
# ---------------------------------------------------------------------------

# Task 1
# Write a function that raises a ValueError
# if a number is negative.


# Task 2
# Call the function inside a try/except block
# and print a clear error message.


# ---------------------------------------------------------------------------
# Rank 2 — Easy-Advanced
# ---------------------------------------------------------------------------

# Task 3
# Create a custom exception called InvalidAgeError
# that inherits from Exception.


# Task 4
# Write a function that raises InvalidAgeError
# if age is less than 0 or greater than 120.


# ---------------------------------------------------------------------------
# Rank 3 — Intermediate-Advanced
# ---------------------------------------------------------------------------

# Task 5
# Write a function that converts a string to an integer.
# If conversion fails, raise a new ValueError
# using exception chaining (raise ... from ...).


# Task 6
# Catch the chained exception and print both messages.


# ---------------------------------------------------------------------------
# Rank 4 — Advanced
# ---------------------------------------------------------------------------

# Task 7
# Create a base exception class called AppError.


# Task 8
# Create two child exceptions:
# - ConfigurationError
# - DatabaseError
# Both should inherit from AppError.


# ---------------------------------------------------------------------------
# Rank 5 — Professional
# ---------------------------------------------------------------------------

# Task 9
# Write a function that simulates loading configuration data.
# Raise ConfigurationError if data is missing or invalid.


# Task 10
# Explain (in comments):
# - when to catch exceptions
# - when to let exceptions propagate
# - why bare except should be avoided


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# These tasks reinforce:
# - intentional error design
# - custom exception hierarchies
# - clean and maintainable error handling
#
# Next Step:
# Continue with Error_Handling_Tasks_Solutions.py
