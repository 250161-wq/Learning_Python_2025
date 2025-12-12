"""
Exceptions_Tasks_Solutions.py
Module 42 — Exceptions
Author: Peyman Miyandashti
Year: 2025

This file contains clean and professional solutions
for the exception handling exercises in this module.
"""

# ---------------------------------------------------------------------------
# Rank 1 — Beginner
# ---------------------------------------------------------------------------

# Task 1 & 2 Solution
try:
    value = int("abc")
except ValueError:
    print("Invalid input: cannot convert to integer")


# ---------------------------------------------------------------------------
# Rank 2 — Easy
# ---------------------------------------------------------------------------

# Task 3 Solution
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: division by zero")


# Task 4 Solution
try:
    value = int("abc")
    result = 10 / value
except ValueError:
    print("Invalid number format")
except ZeroDivisionError:
    print("Cannot divide by zero")


# ---------------------------------------------------------------------------
# Rank 3 — Intermediate
# ---------------------------------------------------------------------------

# Task 5 Solution
try:
    number = int("25")
except ValueError:
    print("Invalid input")
else:
    print("Valid number:", number)


# Task 6 Solution
try:
    file = open("example.txt", "w")
    file.write("Hello")
finally:
    file.close()
    print("File closed safely")


# ---------------------------------------------------------------------------
# Rank 4 — Advanced
# ---------------------------------------------------------------------------

# Task 7 Solution
def check_positive(n):
    if n < 0:
        raise ValueError("Number must be non-negative")
    return n

try:
    print(check_positive(-3))
except ValueError as e:
    print("Error:", e)


# Task 8 Solution
class InvalidScoreError(Exception):
    pass


def set_score(score):
    if score < 0 or score > 100:
        raise InvalidScoreError("Score must be between 0 and 100")
    return score

try:
    set_score(150)
except InvalidScoreError as e:
    print("Custom exception:", e)


# ---------------------------------------------------------------------------
# Rank 5 — Professional
# ---------------------------------------------------------------------------

# Task 9 Solution
def read_file_safe(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        print("File not found")
    except IOError:
        print("I/O error occurred")
    return None

print(read_file_safe("missing.txt"))


# Task 10 Solution
# Catching specific exceptions is better because:
# - it avoids hiding unexpected errors
# - it makes debugging easier
# - it documents what can go wrong
# - it prevents masking real bugs
#
# Bare except should be avoided because it catches everything,
# including system-exiting exceptions.


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# These solutions demonstrate:
# - structured error handling
# - safe cleanup with finally
# - correct use of custom exceptions
# - professional exception design
#
# Next Step:
# Move on to the next module when ready.
``
