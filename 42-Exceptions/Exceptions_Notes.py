"""
Exceptions_Notes.py
Module 42 — Exceptions
Author: Peyman Miyandashti
Year: 2025

This module explains exception handling in Python.
Exceptions allow programs to handle runtime errors safely.
"""

# ---------------------------------------------------------------------------
# 1. What Is an Exception?
# ---------------------------------------------------------------------------
# An exception is an error that occurs during program execution.
# Without handling, it stops the program.


# ---------------------------------------------------------------------------
# 2. Basic try / except
# ---------------------------------------------------------------------------

try:
    x = int("abc")
except ValueError:
    print("Conversion failed")


# ---------------------------------------------------------------------------
# 3. Catching Specific Exceptions
# ---------------------------------------------------------------------------

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")


# ---------------------------------------------------------------------------
# 4. Multiple except Blocks
# ---------------------------------------------------------------------------

try:
    value = int("abc")
    result = 10 / value
except ValueError:
    print("Invalid integer")
except ZeroDivisionError:
    print("Division by zero")


# ---------------------------------------------------------------------------
# 5. Using else
# ---------------------------------------------------------------------------
# else runs only if no exception occurs.

try:
    number = int("5")
except ValueError:
    print("Invalid input")
else:
    print("Number is valid:", number)


# ---------------------------------------------------------------------------
# 6. Using finally
# ---------------------------------------------------------------------------
# finally always runs, even if an exception occurs.

try:
    file = open("example.txt", "w")
    file.write("Hello")
finally:
    file.close()


# ---------------------------------------------------------------------------
# 7. Raising Exceptions
# ---------------------------------------------------------------------------

def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount


# ---------------------------------------------------------------------------
# 8. Custom Exceptions
# ---------------------------------------------------------------------------

class NegativeNumberError(Exception):
    pass


def check_positive(n):
    if n < 0:
        raise NegativeNumberError("Negative number not allowed")
    return n


# ---------------------------------------------------------------------------
# 9. Exception Hierarchy
# ---------------------------------------------------------------------------
# All exceptions inherit from BaseException.
# Most user-defined exceptions inherit from Exception.


# ---------------------------------------------------------------------------
# 10. Best Practices
# ---------------------------------------------------------------------------
# - Catch specific exceptions
# - Avoid bare except
# - Use exceptions for exceptional cases
# - Do not suppress errors silently
# - Keep error messages clear


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# Proper exception handling is essential for reliable software.
# It separates error logic from business logic.
#
# Next Step:
# Continue with Exceptions_Examples.py
