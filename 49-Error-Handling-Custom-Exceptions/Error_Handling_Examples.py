"""
Error_Handling_Examples.py
Module 49 — Error Handling & Custom Exceptions
Author: Peyman Miyandashti
Year: 2025

This file contains clear and practical examples
demonstrating professional error handling patterns in Python.
"""

# ---------------------------------------------------------------------------
# Example 1: Raising Built-in Exceptions Intentionally
# ---------------------------------------------------------------------------

def divide(a: int, b: int) -> float:
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b

try:
    divide(10, 0)
except ZeroDivisionError as e:
    print("Error:", e)


# ---------------------------------------------------------------------------
# Example 2: Custom Exception Classes
# ---------------------------------------------------------------------------

class ValidationError(Exception):
    pass


class NegativeValueError(ValidationError):
    pass


def validate_positive(value: int) -> None:
    if value < 0:
        raise NegativeValueError("Value must be positive")

try:
    validate_positive(-5)
except ValidationError as e:
    print("Validation error:", e)


# ---------------------------------------------------------------------------
# Example 3: Catching Specific Exceptions
# ---------------------------------------------------------------------------

try:
    int("abc")
except ValueError:
    print("Invalid integer conversion")


# ---------------------------------------------------------------------------
# Example 4: Exception Propagation
# ---------------------------------------------------------------------------

def load_config(value: str) -> int:
    return int(value)

def start_app(config_value: str) -> int:
    return load_config(config_value)

try:
    start_app("xyz")
except ValueError as e:
    print("Application failed:", e)


# ---------------------------------------------------------------------------
# Example 5: Exception Chaining
# ---------------------------------------------------------------------------

def parse_int(value: str) -> int:
    try:
        return int(value)
    except ValueError as exc:
        raise ValueError("Failed to parse integer") from exc

try:
    parse_int("not_a_number")
except ValueError as e:
    print("Error:", e)


# ---------------------------------------------------------------------------
# Example 6: finally Block for Cleanup
# ---------------------------------------------------------------------------

try:
    print("Opening resource")
    raise RuntimeError("Unexpected failure")
finally:
    print("Closing resource")


# ---------------------------------------------------------------------------
# Example 7: Avoiding Bare except
# ---------------------------------------------------------------------------

try:
    numbers = [1, 2, 3]
    print(numbers[10])
except IndexError:
    print("Index out of range")


# ---------------------------------------------------------------------------
# Example 8: Re-Raising Exceptions
# ---------------------------------------------------------------------------

def read_value(value: str) -> int:
    try:
        return int(value)
    except ValueError:
        print("Logging invalid input")
        raise

try:
    read_value("abc")
except ValueError:
    print("Handled at higher level")


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# These examples demonstrate:
# - intentional error raising
# - custom exception usage
# - exception propagation and chaining
# - clean cleanup logic
#
# Next Step:
# Continue with Error_Handling_Tasks.py
