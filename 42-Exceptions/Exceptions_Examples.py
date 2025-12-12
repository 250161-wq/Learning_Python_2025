"""
Exceptions_Examples.py
Module 42 — Exceptions
Author: Peyman Miyandashti
Year: 2025

This file contains clear and practical examples
showing how exceptions are handled in Python.
"""

# ---------------------------------------------------------------------------
# Example 1: Basic try / except
# ---------------------------------------------------------------------------

try:
    number = int("abc")
except ValueError:
    print("Could not convert to integer")


# ---------------------------------------------------------------------------
# Example 2: Handling Division Errors
# ---------------------------------------------------------------------------

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Division by zero is not allowed")


# ---------------------------------------------------------------------------
# Example 3: Multiple except Blocks
# ---------------------------------------------------------------------------

try:
    value = int("abc")
    result = 10 / value
except ValueError:
    print("Invalid number format")
except ZeroDivisionError:
    print("Cannot divide by zero")


# ---------------------------------------------------------------------------
# Example 4: Using else
# ---------------------------------------------------------------------------

try:
    number = int("25")
except ValueError:
    print("Invalid input")
else:
    print("Valid number:", number)


# ---------------------------------------------------------------------------
# Example 5: Using finally
# ---------------------------------------------------------------------------

try:
    file = open("sample.txt", "w")
    file.write("Hello, file!")
except IOError:
    print("File error occurred")
finally:
    file.close()
    print("File closed")


# ---------------------------------------------------------------------------
# Example 6: Raising an Exception
# ---------------------------------------------------------------------------

def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount


try:
    print(withdraw(100, 150))
except ValueError as e:
    print("Error:", e)


# ---------------------------------------------------------------------------
# Example 7: Custom Exception
# ---------------------------------------------------------------------------

class InvalidAgeError(Exception):
    pass


def set_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative")
    return age


try:
    set_age(-5)
except InvalidAgeError as e:
    print("Custom error:", e)


# ---------------------------------------------------------------------------
# Example 8: Catching Exception Object
# ---------------------------------------------------------------------------

try:
    int("xyz")
except ValueError as e:
    print("Error message:", e)


# ---------------------------------------------------------------------------
# Example 9: Avoiding Bare except
# ---------------------------------------------------------------------------

try:
    numbers = [1, 2, 3]
    print(numbers[5])
except IndexError:
    print("Index out of range")


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# These examples demonstrate:
# - safe error handling
# - clear exception types
# - controlled program flow
#
# Next Step:
# Continue with Exceptions_Tasks.py
