"""
Module 17 — Exceptions (try/except)
exceptions_solutions.py

This file contains the *solutions* for the practice tasks from exceptions_tasks.py.

Each function here shows one or more exception-handling patterns:
- Basic try/except
- Handling specific exception types
- Using else / finally
- Raising custom exceptions
- Defining a custom exception class

Author: Peyman Miyandashti
Year: 2025
"""


# ===========================================================
# Task 1 — Safe Division
# Goal:
#   Divide two numbers safely. If division by zero happens,
#   handle the error and return None.
# ===========================================================

def safe_divide(a: float, b: float) -> float | None:
    """
    Safely divide a by b.

    - Returns the result of a / b.
    - If b is 0, prints a message and returns None.
    """
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: You tried to divide by zero. Returning None instead.")
        return None


# Example usage (you can comment these out when importing):
if __name__ == "__main__":
    print("Task 1 — Safe Division")
    print("10 / 2 =", safe_divide(10, 2))
    print("10 / 0 =", safe_divide(10, 0))
    print("-" * 60)


# ===========================================================
# Task 2 — Convert Text to int Safely
# Goal:
#   Take a string and convert it to int.
#   If it is not a valid number, handle ValueError.
# ===========================================================

def to_int_safe(text: str) -> int | None:
    """
    Convert text to an integer safely.

    - On success: returns the integer.
    - On ValueError: prints an error and returns None.
    """
    try:
        value = int(text)
        return value
    except ValueError:
        print(f"Error: '{text}' is not a valid integer.")
        return None


if __name__ == "__main__":
    print("Task 2 — Convert Text to int Safely")
    print("Input '123'  ->", to_int_safe("123"))
    print("Input 'abc'  ->", to_int_safe("abc"))
    print("-" * 60)


# ===========================================================
# Task 3 — Safe List Access
# Goal:
#   Access an item by index safely.
#   Handle IndexError and TypeError.
# ===========================================================

def get_list_item_safe(items: list, index: int):
    """
    Return items[index] safely.

    - If index is out of range, print a message and return None.
    - If index is not an integer, print a message and return None.
    """
    try:
        value = items[index]
        return value
    except IndexError:
        print(f"Error: index {index} is out of range for list of length {len(items)}.")
        return None
    except TypeError:
        print(f"Error: index must be an integer, not {type(index).__name__}.")
        return None


if __name__ == "__main__":
    print("Task 3 — Safe List Access")
    sample = [10, 20, 30]
    print("items[1]  ->", get_list_item_safe(sample, 1))
    print("items[10] ->", get_list_item_safe(sample, 10))
    print("items['a'] ->", get_list_item_safe(sample, "a"))
    print("-" * 60)


# ===========================================================
# Task 4 — Calculate BMI with Validation
# Goal:
#   Use exceptions to validate weight and height.
#   Raise ValueError if invalid values are given.
#
#   Peyman's real data:
#   height = 187.3 cm  -> 1.873 m
#   weight = 72.5 kg
# ===========================================================

def calculate_bmi(weight_kg: float, height_cm: float) -> float:
    """
    Calculate Body Mass Index (BMI).

    - weight_kg must be > 0
    - height_cm must be > 0

    Raises:
        ValueError if weight or height is not valid.
    """
    if weight_kg <= 0:
        raise ValueError("Weight must be a positive number.")
    if height_cm <= 0:
        raise ValueError("Height must be a positive number.")

    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return bmi


if __name__ == "__main__":
    print("Task 4 — Calculate BMI with Validation")
    try:
        peyman_bmi = calculate_bmi(weight_kg=72.5, height_cm=187.3)
        print(f"Peyman's BMI is: {peyman_bmi:.2f}")
    except ValueError as e:
        print("Validation error:", e)

    # Example with invalid values
    try:
        bad_bmi = calculate_bmi(weight_kg=-50, height_cm=170)
        print("This should not be printed:", bad_bmi)
    except ValueError as e:
        print("Validation error (expected):", e)
    print("-" * 60)


# ===========================================================
# Task 5 — Open a File Safely
# Goal:
#   Try to open a file and read its content.
#   Handle FileNotFoundError and PermissionError.
# ===========================================================

def read_file_safe(path: str) -> str | None:
    """
    Safely open and read a text file.

    - On success: return the file content as a string.
    - If file is not found: print a message and return None.
    - If permission is denied: print a message and return None.
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        return content
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return None
    except PermissionError:
        print(f"Error: Permission denied for file '{path}'.")
        return None
    except OSError as e:
        # Generic OS error (e.g., path too long, etc.)
        print(f"OS error while reading '{path}': {e}")
        return None


if __name__ == "__main__":
    print("Task 5 — Open a File Safely")
    print("Trying to read 'not_existing_file.txt' ...")
    content = read_file_safe("not_existing_file.txt")
    print("Result:", content)
    print("-" * 60)


# ===========================================================
# Task 6 — Custom Exception: InvalidGradeError
# Goal:
#   Create a custom exception for invalid grades and use it.
# ===========================================================

class InvalidGradeError(Exception):
    """Custom exception raised when a grade is not between 0 and 100."""
    pass


def validate_grade(grade: float) -> None:
    """
    Validate that grade is between 0 and 100 (inclusive).

    Raises:
        InvalidGradeError: if the grade is out of this range.
        TypeError: if grade is not a number.
    """
    if not isinstance(grade, (int, float)):
        raise TypeError(f"Grade must be a number, not {type(grade).__name__}.")

    if grade < 0 or grade > 100:
        raise InvalidGradeError(f"Grade {grade} is invalid. Must be between 0 and 100.")


def print_grade_status(student_name: str, grade: float) -> None:
    """
    Use validate_grade and handle exceptions.

    - On valid grade: print pass/fail.
    - On InvalidGradeError: print a custom message.
    - On TypeError: print a message about wrong type.
    """
    try:
        validate_grade(grade)
        status = "PASSED ✅" if grade >= 60 else "FAILED ❌"
        print(f"{student_name} -> Grade: {grade} | Status: {status}")
    except InvalidGradeError as e:
        print(f"[InvalidGradeError] {e}")
    except TypeError as e:
        print(f"[TypeError] {e}")


if __name__ == "__main__":
    print("Task 6 — Custom Exception: InvalidGradeError")
    print_grade_status("Peyman", 95)
    print_grade_status("Arlette", 120)  # invalid
    print_grade_status("Student X", -5)  # invalid
    print_grade_status("Student Y", "A+")  # wrong type
    print("-" * 60)


# ===========================================================
# Task 7 — try/except/else/finally Demo
# Goal:
#   Show how all four blocks work together.
# ===========================================================

def process_number(text: str) -> int | None:
    """
    Try to convert 'text' to an integer and show the flow of
    try / except / else / finally.

    Returns:
        int on success, None on error.
    """
    print(f"\nProcessing text: {text!r}")

    try:
        number = int(text)
    except ValueError:
        print("except: Could not convert to int.")
        number = None
    else:
        print("else: Conversion succeeded.")
    finally:
        print("finally: This always runs (cleanup, logging, etc.).")

    return number


if __name__ == "__main__":
    print("Task 7 — try/except/else/finally Demo")
    n1 = process_number("250161")
    print("Result:", n1)

    n2 = process_number("warcraft")
    print("Result:", n2)
    print("-" * 60)


# ===========================================================
# Task 8 — Exception Handling in a Simple "Profile" Function
# Goal:
#   Use a dict with Peyman's info and handle missing keys.
#
#   We use a dictionary that *should* contain keys like:
#   - 'name'
#   - 'age'
#   - 'city'
#   - 'country'
#
#   We print a profile, but handle KeyError if something is missing.
# ===========================================================

def print_profile_safe(profile: dict) -> None:
    """
    Print a small profile safely.

    Expected keys:
        'name', 'age', 'city', 'country'

    If any key is missing, catch KeyError and print a message.
    """
    try:
        name = profile["name"]
        age = profile["age"]
        city = profile["city"]
        country = profile["country"]

        print(f"{name} is {age} years old and lives in {city}, {country}.")
    except KeyError as e:
        missing_key = e.args[0]
        print(f"Error: Missing key '{missing_key}' in profile dictionary.")


if __name__ == "__main__":
    print("Task 8 — Exception Handling in a Simple 'Profile' Function")

    # A correct profile using Peyman's info:
    peyman_profile = {
        "name": "Peyman Miyandashti",
        "age": 43,
        "city": "Mexicali",
        "country": "Mexico",
    }
    print_profile_safe(peyman_profile)

    # An incomplete profile to trigger KeyError:
    broken_profile = {
        "name": "Arlette Chong",
        "age": 47,
        # "city" is missing on purpose
        "country": "Mexico",
    }
    print_profile_safe(broken_profile)
    print("-" * 60)
