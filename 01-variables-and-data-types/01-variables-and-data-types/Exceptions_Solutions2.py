# ===========================================================
# File: exceptions_solutions.py
# Module 17 — Exceptions (try/except): Solutions
# Author: Peyman Miyandashti
# Year: 2025
# ===========================================================

"""
Module 17 — Exceptions (try/except): Solutions

This file contains one possible set of solutions for the tasks in
exceptions_tasks.py.

You can:
- Compare your code with these solutions.
- Learn new patterns and ideas for handling exceptions.
"""

from __future__ import annotations

import json
from typing import Any


# ===========================================================
# Rank 1 — Beginner
# Very simple try/except
# ===========================================================

def parse_int(value: str) -> int | None:
    """See exceptions_tasks.py for full description."""
    try:
        return int(value)
    except ValueError:
        return None


def get_item_or_none(items: list[Any], index: int) -> Any | None:
    """See exceptions_tasks.py for full description."""
    try:
        return items[index]
    except IndexError:
        return None


# ===========================================================
# Rank 2 — Easy
# Specific exceptions and safe operations
# ===========================================================

def safe_divide(a: float, b: float) -> float | None:
    """See exceptions_tasks.py for full description."""
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero. Please choose a different denominator.")
        return None


def int_from_user_input(user_input: str) -> int:
    """See exceptions_tasks.py for full description."""
    try:
        return int(user_input)
    except ValueError:
        print(f"Input must be a whole number, received: {user_input!r}")
        # Re-raise so the caller knows something went wrong.
        raise


# ===========================================================
# Rank 3 — Intermediate
# Dicts, KeyError, and validation
# ===========================================================

def get_age(person: dict[str, Any]) -> int:
    """See exceptions_tasks.py for full description."""
    try:
        return int(person["age"])
    except KeyError:
        raise ValueError("Missing 'age' in person data") from None


def describe_person(person: dict[str, Any]) -> str:
    """See exceptions_tasks.py for full description."""
    try:
        name = person["name"]
        age = person["age"]
    except KeyError:
        return "Invalid person data"

    return f"{name} is {age} years old."


# ===========================================================
# Rank 4 — Advanced
# Files, JSON, and else/finally
# ===========================================================

def load_config(path: str) -> dict[str, Any]:
    """See exceptions_tasks.py for full description."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            config = json.load(f)
    except FileNotFoundError:
        print(f"Config file not found: {path}")
        return {}
    except json.JSONDecodeError:
        print(f"Config file is not valid JSON: {path}")
        return {}
    else:
        # Only runs if no exception was raised.
        return config
    finally:
        # Always runs.
        print(f"Finished trying to read config from: {path}")


def calculate_bmi(weight_kg: float, height_m: float) -> float | None:
    """See exceptions_tasks.py for full description."""
    try:
        bmi = weight_kg / (height_m ** 2)
    except ZeroDivisionError:
        print("Height cannot be zero when calculating BMI.")
        return None
    except TypeError:
        print("Weight and height must be numbers (int or float).")
        return None
    else:
        return bmi


# ===========================================================
# Rank 5 — Professional
# Custom exception and more realistic pattern
# ===========================================================

class InvalidGradeError(Exception):
    """Custom exception for invalid grades."""
    pass


def _validate_grades(grades: list[float]) -> None:
    """
    Internal helper to validate a list of grades.

    Raises InvalidGradeError if:
    - List is empty.
    - Any grade is outside [0, 100].
    """
    if not grades:
        raise InvalidGradeError("No grades provided")

    for grade in grades:
        if grade < 0 or grade > 100:
            raise InvalidGradeError(f"Invalid grade value: {grade}")


def calculate_final_grade(grades: list[float]) -> float:
    """See exceptions_tasks.py for full description."""
    # First validate with our helper.
    _validate_grades(grades)

    try:
        average = sum(grades) / len(grades)
    except InvalidGradeError:
        # If we ever raised it inside here, just re-raise.
        raise
    else:
        return average


# ===========================================================
# Manual demo
# ===========================================================

if __name__ == "__main__":
    print("Module 17 — Exceptions (try/except): SOLUTIONS DEMO")
    print("-" * 60)

    # Example data based on your real info
    peyman = {
        "name": "Peyman Miyandashti",
        "age": 43,
        "city": "Mexicali",
        "favorite_number": 11,
    }

    arlette = {
        "name": "Arlette Chong",
        "age": 47,
        "city": "Mexicali",
        "job": "Teacher",
    }

    # Rank 1 demo
    print("Rank 1 — parse_int")
    print("parse_int('11') ->", parse_int("11"))
    print("parse_int('hello') ->", parse_int("hello"))
    print()

    print("Rank 1 — get_item_or_none")
    cars = ["Kia Sportage 2024", "Hyundai Creta 2018"]
    print("cars:", cars)
    print("get_item_or_none(cars, 0) ->", get_item_or_none(cars, 0))
    print("get_item_or_none(cars, 10) ->", get_item_or_none(cars, 10))
    print("-" * 60)

    # Rank 2 demo
    print("Rank 2 — safe_divide")
    print("safe_divide(10, 2) ->", safe_divide(10, 2))
    print("safe_divide(10, 0) ->", safe_divide(10, 0))
    print("-" * 60)

    # Rank 3 demo
    print("Rank 3 — get_age / describe_person")
    print("get_age(peyman) ->", get_age(peyman))
    print("describe_person(peyman) ->", describe_person(peyman))
    print("describe_person({}) ->", describe_person({}))
    print("-" * 60)

    # Rank 4 demo
    print("Rank 4 — calculate_bmi")
    bmi_peyman = calculate_bmi(72.5, 1.873)
    print("Peyman's BMI ~", bmi_peyman)
    bmi_error = calculate_bmi(72.5, 0)
    print("BMI with height 0 ->", bmi_error)
    print("-" * 60)

    # Rank 5 demo
    print("Rank 5 — calculate_final_grade")
    good_grades = [95.0, 88.5, 100.0]
    print("Grades:", good_grades)
    print("Average grade ->", calculate_final_grade(good_grades))

    try:
        bad_grades = [120.0]  # invalid
        print("Average with bad grades ->", calculate_final_grade(bad_grades))
    except InvalidGradeError as e:
        print("Caught InvalidGradeError:", e)
    print("-" * 60)

    print("Demo finished. Now go back to exceptions_tasks.py and write your own code! 🚀")
