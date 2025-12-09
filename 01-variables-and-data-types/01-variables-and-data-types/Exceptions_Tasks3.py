# ===========================================================
# File: exceptions_tasks.py
# Module 17 — Exceptions (try/except): Practice Tasks
# Author: Peyman Miyandashti
# Year: 2025
# ===========================================================

"""
Module 17 — Exceptions (try/except): Practice Tasks

In this module I:
- Practice how to handle errors with try/except.
- Learn how to catch specific errors like ValueError, ZeroDivisionError,
  IndexError, KeyError, FileNotFoundError, etc.
- Learn how to raise my own exceptions for invalid data.

Ranking system:
- Rank 1  -> Beginner: very basic try/except.
- Rank 2  -> Easy: catch specific errors (ValueError, ZeroDivisionError).
- Rank 3  -> Intermediate: work with dicts and lists using try/except.
- Rank 4  -> Advanced: files, JSON, else/finally blocks.
- Rank 5  -> Professional: custom exception class and re-usable patterns.

Context info I will use:
- Name: Peyman Miyandashti
- Age: 43
- From: Tabriz, Iran — now living in Mexicali, Baja California, Mexico
- Studies: Information Technology Engineering and Digital Innovation (UPBC)
- Favorite number: 11
- Wife: Arlette Chong (47, teacher)
"""

from __future__ import annotations

import json
from typing import Any


# ===========================================================
# Rank 1 — Beginner
# Very simple try/except
# ===========================================================

def parse_int(value: str) -> int | None:
    """
    Task 1 (Rank 1)

    Convert a string to an integer.

    Requirements:
    - Use try/except.
    - Try to convert `value` to int.
    - If it works, return the integer.
    - If it fails (ValueError), return None.

    Example:
        parse_int("11")   -> 11
        parse_int("Peyman") -> None
    """
    # TODO: implement using try/except ValueError
    pass


def get_item_or_none(items: list[Any], index: int) -> Any | None:
    """
    Task 2 (Rank 1)

    Safely get an item from a list.

    Requirements:
    - Use try/except.
    - Try to return items[index].
    - If index is out of range (IndexError), return None.

    Example:
        get_item_or_none([10, 20, 30], 1) -> 20
        get_item_or_none([10, 20, 30], 5) -> None
    """
    # TODO: implement using try/except IndexError
    pass


# ===========================================================
# Rank 2 — Easy
# Specific exceptions and safe operations
# ===========================================================

def safe_divide(a: float, b: float) -> float | None:
    """
    Task 3 (Rank 2)

    Safely divide two numbers.

    Requirements:
    - Use try/except.
    - Try to return a / b.
    - If there is a ZeroDivisionError, print a short message and return None.

    Example:
        safe_divide(10, 2) -> 5.0
        safe_divide(10, 0) -> None  (and prints a message)
    """
    # TODO: implement using try/except ZeroDivisionError
    pass


def int_from_user_input(user_input: str) -> int:
    """
    Task 4 (Rank 2)

    Convert user input to int, but give a friendly error.

    Requirements:
    - Use try/except.
    - Try to convert `user_input` to int.
    - If it fails (ValueError), print:
        "Input must be a whole number, received: <user_input>"
      and then re-raise the ValueError with `raise`.

    Example:
        int_from_user_input("43") -> 43
        int_from_user_input("hello") -> prints message and raises ValueError
    """
    # TODO: implement using try/except ValueError and re-raise
    pass


# ===========================================================
# Rank 3 — Intermediate
# Dicts, KeyError, and validation
# ===========================================================

def get_age(person: dict[str, Any]) -> int:
    """
    Task 5 (Rank 3)

    Get the age from a person dictionary.

    The dictionary might look like:
        {
            "name": "Peyman Miyandashti",
            "age": 43,
            "city": "Mexicali"
        }

    Requirements:
    - Use try/except.
    - Try to read person["age"].
    - If the key "age" is missing (KeyError), raise a ValueError with
      the message: "Missing 'age' in person data".

    Example:
        get_age({"name": "Peyman", "age": 43}) -> 43
        get_age({"name": "Peyman"})           -> raises ValueError
    """
    # TODO: implement using try/except KeyError and raise ValueError
    pass


def describe_person(person: dict[str, Any]) -> str:
    """
    Task 6 (Rank 3)

    Build a description string for a person.

    Example person:
        {
            "name": "Peyman Miyandashti",
            "age": 43,
            "city": "Mexicali",
            "favorite_number": 11,
        }

    Requirements:
    - Use try/except.
    - Try to read "name" and "age" keys.
    - If either key is missing, return the string:
        "Invalid person data"
    - If everything is OK, return something like:
        "Peyman Miyandashti is 43 years old."

    Hint:
    - You can catch KeyError for the missing keys.
    """
    # TODO: implement using try/except KeyError
    pass


# ===========================================================
# Rank 4 — Advanced
# Files, JSON, and else/finally
# ===========================================================

def load_config(path: str) -> dict[str, Any]:
    """
    Task 7 (Rank 4)

    Load a JSON config file for Peyman's study plan.

    Requirements:
    - Use try/except/else/finally.
    - In the try block:
        * Open the file at `path` in read mode.
        * Use json.load(file) to load a dict.
    - Catch:
        * FileNotFoundError -> print a message and return {} (empty dict)
        * json.JSONDecodeError -> print a message and return {}
    - Use `else` to return the loaded config if everything was OK.
    - Use `finally` to print:
        f"Finished trying to read config from: {path}"

    Example:
        load_config("config.json") -> dict or {}
    """
    # TODO: implement using try/except/else/finally
    pass


def calculate_bmi(weight_kg: float, height_m: float) -> float | None:
    """
    Task 8 (Rank 4)

    Calculate BMI (Body Mass Index) for Peyman or Arlette.

    Formula:
        BMI = weight_kg / (height_m ** 2)

    Requirements:
    - Use try/except.
    - Handle two problems:
        * ZeroDivisionError (if height_m is 0)
        * TypeError (if the types are wrong, e.g. strings)
    - If an error happens, print a short message and return None.
    - If all is OK, return the BMI as a float.

    Example:
        calculate_bmi(72.5, 1.873) -> some float
        calculate_bmi(72.5, 0)     -> None (and message)
    """
    # TODO: implement using try/except for ZeroDivisionError and TypeError
    pass


# ===========================================================
# Rank 5 — Professional
# Custom exception and more realistic pattern
# ===========================================================

class InvalidGradeError(Exception):
    """
    Task 9 (Rank 5)

    Custom exception for invalid grades.
