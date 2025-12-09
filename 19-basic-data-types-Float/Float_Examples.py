"""
Module 19 — Float: Examples

This file contains small, focused examples that demonstrate how floats
work in real Python code. Each example is short, clear, and written to
be easy to run and modify.

How to use this file:
- Run it with:  python Float_Examples.py
- Compare the printed output with the code.
- Change values, recalculate, and observe how floats behave.
"""


# ---------------------------------------------------------
# Rank 1 — Basic Float Usage
# ---------------------------------------------------------


def example_1_create_basic_floats() -> None:
    """Create simple float values and print their types."""
    print("Example 1 — creating floats")

    temperature = 36.5
    speed = 12.0
    negative_value = -4.75

    print("Temperature:", temperature)
    print("Speed:", speed)
    print("Negative value:", negative_value)
    print("Type:", type(temperature))
    print()


def example_2_basic_arithmetic() -> None:
    """Show basic arithmetic operations using floats."""
    print("Example 2 — basic float arithmetic")

    a = 5.5
    b = 2.0

    print("a + b =", a + b)
    print("a - b =", a - b)
    print("a * b =", a * b)
    print("a / b =", a / b)
    print("a ** b =", a ** b)
    print()


# ---------------------------------------------------------
# Rank 2 — Formatting, Rounding, and Real Calculations
# ---------------------------------------------------------


def example_3_rounding_values() -> None:
    """Round float values to a specific number of decimal places."""
    print("Example 3 — rounding")

    value = 10 / 3
    print("Raw value:", value)
    print("Rounded (2 decimals):", round(value, 2))
    print("Rounded (4 decimals):", round(value, 4))
    print()


def example_4_formatting_floats() -> None:
    """Use f-strings to format floats for clean, readable output."""
    print("Example 4 — formatting with f-strings")

    price = 19.9999

    print(f"Default: {price}")
    print(f"Two decimals: {price:.2f}")
    print(f"Aligned (10 spaces): {price:10.2f}")
    print()


# ---------------------------------------------------------
# Rank 3 — Averages, Totals, and Percentages
# ---------------------------------------------------------


def example_5_average_of_list() -> None:
    """Compute the average of several float values."""
    print("Example 5 — computing an average")

    grades = [9.5, 7.0, 8.3, 10.0]
    total = sum(grades)
    average = total / len(grades)

    print("Grades:", grades)
    print("Total:", total)
    print("Average:", average)
    print(f"Average (formatted): {average:.2f}")
    print()


def example_6_percentage_calculation() -> None:
    """Compute a percentage from two values."""
    print("Example 6 — percentage calculation")

    correct = 17
    total = 20

    score = (correct / total) * 100

    print(f"Correct {correct}/{total}")
    print(f"Score: {score:.1f}%")
    print()


# ---------------------------------------------------------
# Rank 4 — Precision Issues and Safe Comparisons
# ---------------------------------------------------------

import math


def example_7_precision_problem() -> None:
    """Show why 0.1 + 0.2 is not exactly 0.3."""
    print("Example 7 — floating-point precision issue")

    a = 0.1 + 0.2
    b = 0.3

    print("a =", a)
    print("b =", b)
    print("a == b:", a == b)  # expected to be False
    print()


def example_8_safe_comparison() -> None:
    """Use math.isclose() to compare floats safely."""
    print("Example 8 — safe float comparison")

    a = 0.1 + 0.2
    b = 0.3

    print("math.isclose(a, b):", math.isclose(a, b, rel_tol=1e-9))
    print()


# ---------------------------------------------------------
# Rank 5 — Realistic Use Cases with Floats
# ---------------------------------------------------------


def example_9_invoice_calculation() -> None:
    """Create a small, realistic invoice using floats."""
    print("Example 9 — invoice calculation")

    price = 89.99
    quantity = 3
    tax_rate = 0.16  # 16%

    subtotal = price * quantity
    tax = subtotal * tax_rate
    total = subtotal + tax

    print(f"Price per item: ${price:.2f}")
    print("Quantity:", quantity)
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax (16%): ${tax:.2f}")
    print(f"Total: ${total:.2f}")
    print()


def example_10_weight_normalization() -> None:
    """Normalize weight values so they add up to 1 (100%)."""
    print("Example 10 — normalizing weights")

    weights = [2.0, 3.0, 5.0]
    total = sum(weights)

    normalized = [w / total for w in weights]

    print("Original weights:", weights)
    print("Normalized:", normalized)
    print("Sum of normalized:", sum(normalized))
    print()


# ---------------------------------------------------------
# Main entry point
# ---------------------------------------------------------


def main() -> None:
    """Run all float examples in order."""
    # Rank 1
    example_1_create_basic_floats()
    example_2_basic_arithmetic()

    # Rank 2
    example_3_rounding_values()
    example_4_formatting_floats()

    # Rank 3
    example_5_average_of_list()
    example_6_percentage_calculation()

    # Rank 4
    example_7_precision_problem()
    example_8_safe_comparison()

    # Rank 5
    example_9_invoice_calculation()
    example_10_weight_normalization()


if __name__ == "__main__":
    main()
