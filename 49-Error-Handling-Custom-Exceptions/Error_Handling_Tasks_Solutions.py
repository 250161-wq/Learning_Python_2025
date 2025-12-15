"""
Error_Handling_Tasks_Solutions.py
Module 49 — Error Handling & Custom Exceptions
Author: Peyman Miyandashti
Year: 2025

This file contains clean and professional solutions
for the error handling and custom exception exercises in this module.
"""

# ---------------------------------------------------------------------------
# Rank 1 — Intermediate
# ---------------------------------------------------------------------------

# Task 1 Solution
def check_positive(number: int) -> None:
    if number < 0:
        raise ValueError("Number cannot be negative")


# Task 2 Solution
try:
    check_positive(-10)
except ValueError as e:
    print("Error:", e)


# ---------------------------------------------------------------------------
# Rank 2 — Easy-Advanced
# ---------------------------------------------------------------------------

# Task 3 Solution
class InvalidAgeError(Exception):
    """Raised when age is outside valid range"""
    pass


# Task 4 Solution
def validate_age(age: int) -> None:
    if age < 0 or age > 120:
        raise InvalidAgeError("Age must be between 0 and 120")


try:
    validate_age(150)
except InvalidAgeError as e:
    print("Invalid age:", e)


# ---------------------------------------------------------------------------
# Rank 3 — Intermediate-Advanced
# ---------------------------------------------------------------------------

# Task 5 Solution
def parse_integer(value: str) -> int:
    try:
        return int(value)
    except ValueError as exc:
        raise ValueError("Failed to convert string to integer") from exc


# Task 6 Solution
try:
    parse_integer("abc")
except ValueError as e:
    print("High-level error:", e)
    if e.__cause__:
        print("Original cause:", e.__cause__)


# ---------------------------------------------------------------------------
# Rank 4 — Advanced
# ---------------------------------------------------------------------------

# Task 7 Solution
class AppError(Exception):
    """Base exception for application-level errors"""
    pass


# Task 8 Solution
class ConfigurationError(AppError):
    pass


class DatabaseError(AppError):
    pass


# ---------------------------------------------------------------------------
# Rank 5 — Professional
# ---------------------------------------------------------------------------

# Task 9 Solution
def load_configuration(config: dict) -> str:
    if not config:
        raise ConfigurationError("Configuration is missing")
    if "host" not in config:
        raise ConfigurationError("Configuration missing 'host'")
    return config["host"]


try:
    load_configuration({})
except ConfigurationError as e:
    print("Configuration error:", e)


# Task 10 Solution
# Catch exceptions when:
# - you can recover
# - you can add context
# - you can translate errors for users
#
# Let exceptions propagate when:
# - you cannot handle them meaningfully
# - higher layers should decide how to respond
#
# Avoid bare except because:
# - it hides real bugs
# - it catches system-exiting exceptions
# - it makes debugging difficult


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# These solutions demonstrate:
# - intentional exception raising
# - clean custom exception hierarchies
# - exception chaining
# - professional error-handling philosophy
#
# Next Step:
# Move on to the next module when ready.
