"""
Module 19 — Float Numbers: Practice Task Solutions
--------------------------------------------------

This file contains clean, beginner-friendly and professional solutions
for all float practice tasks from Float_Tasks.py.

Multiple solutions are always possible. These versions focus on:
- clear naming,
- type hints,
- simple, readable logic,
- and behaviour that makes sense in real programs.

IMPORTANT:
I should only read these solutions AFTER I honestly tried the tasks
on my own in Float_Tasks.py.
"""

from __future__ import annotations

import math


# ---------------------------------------------------------------------------
# Rank 1 — Beginner
# Very small, direct operations with float values.
# ---------------------------------------------------------------------------


def task_1_add_two_floats(a: float, b: float) -> float:
    """Return the sum of two floating-point numbers."""
    return a + b


def task_2_subtract_discount(price: float, discount: float) -> float:
    """
    Subtract a discount from a price.

    Example:
        price = 100.0, discount = 15.0  ->  85.0
    """
    return price - discount


def task_3_celsius_to_fahrenheit(celsius: float) -> float:
    """
    Convert Celsius to Fahrenheit using the standard formula:

        F = C * 9/5 + 32
    """
    return celsius * 9.0 / 5.0 + 32.0


def task_4_circle_area(radius: float) -> float:
    """
    Compute the area of a circle using:

        area = π * r²
    """
    return math.pi * radius**2


# ---------------------------------------------------------------------------
# Rank 2 — Easy
# Still simple, but combining 2–3 ideas in each function.
# ---------------------------------------------------------------------------


def task_5_average_of_three(a: float, b: float, c: float) -> float:
    """Return the arithmetic mean of three floating-point numbers."""
    return (a + b + c) / 3.0


def task_6_safe_divide(numerator: float, denominator: float) -> float | None:
    """
    Divide two floats safely.

    - If denominator is 0, return None (instead of raising an error).
    - Otherwise, return the division result.
    """
    if denominator == 0.0:
        return None
    return numerator / denominator


def task_7_percentage(part: float, whole: float) -> float | None:
    """
    Calculate the percentage (0–100) that 'part' represents of 'whole'.

        percentage = (part / whole) * 100

    Returns None if whole is 0 to avoid division by zero.
    """
    if whole == 0.0:
        return None
    return (part / whole) * 100.0


def task_8_round_two_decimals(value: float) -> float:
    """
    Round a float to 2 decimal places.

    This is very common when working with money or measurements.
    """
    return round(value, 2)


# ---------------------------------------------------------------------------
# Rank 3 — Intermediate
# Working with lists of floats and simple calculations.
# ---------------------------------------------------------------------------


def task_9_list_average(values: list[float]) -> float | None:
    """
    Return the average of a list of floats.

    If the list is empty, return None to signal "no data".
    """
    if not values:
        return None
    return sum(values) / len(values)


def task_10_find_max_float(values: list[float]) -> float | None:
    """
    Return the maximum float in a list.

    If the list is empty, return None.
    """
    if not values:
        return None

    current_max = values[0]
    for value in values[1:]:
        if value > current_max:
            current_max = value
    return current_max


def task_11_normalize_to_0_1(values: list[float]) -> list[float]:
    """
    Normalize a list of floats so that all values are in the range [0, 1].

    The formula used is:
        normalized_value = value / max_value

    If the list is empty or the maximum is 0, return a list of zeros
    with the same length (to avoid division by zero).
    """
    if not values:
        return []

    max_value = max(values)
    if max_value == 0.0:
        return [0.0 for _ in values]

    normalized = []
    for value in values:
        normalized.append(value / max_value)
    return normalized


# ---------------------------------------------------------------------------
# Rank 4 — Advanced
# More realistic patterns: comparisons, parsing, and accumulation.
# ---------------------------------------------------------------------------


def task_12_almost_equal(a: float, b: float, tolerance: float = 1e-9) -> bool:
    """
    Compare two floats with a tolerance, instead of strict equality.

    This helps avoid issues caused by binary floating-point precision.
    """
    return abs(a - b) <= tolerance


def task_13_parse_float_list(text: str) -> list[float]:
    """
    Parse a string containing numbers separated by commas or spaces
    and return a list of floats.

    Example:
        "1.5,  2.0  3.25" -> [1.5, 2.0, 3.25]
    """
    # Replace commas with spaces, then split on whitespace.
    cleaned = text.replace(",", " ")
    parts = cleaned.split()

    numbers: list[float] = []
    for part in parts:
        try:
            number = float(part)
        except ValueError:
            # Ignore values that cannot be parsed.
            continue
        numbers.append(number)

    return numbers


def task_14_total_with_tax(amounts: list[float], tax_rate: float) -> float:
    """
    Given a list of base amounts and a tax rate (e.g. 0.16 for 16%),
    compute the total including tax, rounded to 2 decimal places.
    """
    subtotal = sum(amounts)
    total = subtotal * (1.0 + tax_rate)
    return round(total, 2)


# ---------------------------------------------------------------------------
# Rank 5 — Professional
# Small, realistic helpers that look like code in real projects.
# ---------------------------------------------------------------------------


def task_15_stats_summary(values: list[float]) -> dict[str, float] | None:
    """
    Return a small stats summary for a list of floats.

    Structure:
        {
            "min": <minimum_value>,
            "max": <maximum_value>,
            "average": <average_value>,
        }

    Returns None if the list is empty.
    """
    if not values:
        return None

    minimum = min(values)
    maximum = max(values)
    average = sum(values) / len(values)

    return {
        "min": minimum,
        "max": maximum,
        "average": average,
    }


def task_16_format_currency(value: float, symbol: str = "$") -> str:
    """
    Format a float as a currency string, with 2 decimals.

    Example:
        value = 1234.5, symbol = "$"  ->  "$1,234.50"
    """
    # Use Python's formatted string with thousand separators and 2 decimals
    return f"{symbol}{value:,.2f}"


def task_17_apply_discount(price: float, discount_percent: float) -> float:
    """
    Apply a percentage discount to a price and return the final price
    rounded to 2 decimals.

    Example:
        price = 100.0, discount_percent = 20.0  ->  80.00
    """
    discount_amount = price * (discount_percent / 100.0)
    final_price = price - discount_amount
    return round(final_price, 2)


# ---------------------------------------------------------------------------
# Manual testing section
# (Optional) Run this file directly to see some example outputs.
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("Manual tests for Float_Tasks_Solutions.py\n")

    print("task_1_add_two_floats(1.5, 2.3) ->", task_1_add_two_floats(1.5, 2.3))
    print("task_3_celsius_to_fahrenheit(0.0) ->", task_3_celsius_to_fahrenheit(0.0))
    print("task_4_circle_area(1.0) ->", task_4_circle_area(1.0))

    print("task_6_safe_divide(10.0, 0.0) ->", task_6_safe_divide(10.0, 0.0))
    print("task_7_percentage(20.0, 80.0) ->", task_7_percentage(20.0, 80.0))
    print("task_8_round_two_decimals(3.14159) ->", task_8_round_two_decimals(3.14159))

    sample_values = [1.5, 2.0, 3.5, 0.5]
    print("task_9_list_average(sample_values) ->", task_9_list_average(sample_values))
    print("task_10_find_max_float(sample_values) ->", task_10_find_max_float(sample_values))
    print("task_11_normalize_to_0_1(sample_values) ->", task_11_normalize_to_0_1(sample_values))

    print('task_12_almost_equal(0.1 + 0.2, 0.3) ->', task_12_almost_equal(0.1 + 0.2, 0.3))
    print('task_13_parse_float_list("1.5, 2, 3.2 x 4") ->', task_13_parse_float_list("1.5, 2, 3.2 x 4"))
    print("task_14_total_with_tax([100.0, 50.0], 0.16) ->", task_14_total_with_tax([100.0, 50.0], 0.16))

    print("task_15_stats_summary(sample_values) ->", task_15_stats_summary(sample_values))
    print("task_16_format_currency(1234.5) ->", task_16_format_currency(1234.5))
    print("task_17_apply_discount(100.0, 15.0) ->", task_17_apply_discount(100.0, 15.0))
