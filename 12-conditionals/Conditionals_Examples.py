"""
Module 12 — Conditionals (if, elif, else)
Examples File

This file contains small, focused examples that demonstrate how to use
conditional statements in real Python code. Each example is clear,
professional, and designed for learning and experimentation.

Run this file directly to see the output:
    python Conditionals_Examples.py
"""


# ---------------------------------------------------------------------------
# Rank 1 — Very basic conditional statements
# ---------------------------------------------------------------------------

def example_1_basic_if() -> None:
    """Check if a number is positive."""
    number = 5
    print("Example 1 — Basic if statement")
    if number > 0:
        print(f"{number} is positive.")
    print()


def example_2_if_else() -> None:
    """Basic if/else decision."""
    age = 16
    print("Example 2 — if/else")
    if age >= 18:
        print("You are an adult.")
    else:
        print("You are a minor.")
    print()


def example_3_string_comparison() -> None:
    """Compare text values with a conditional."""
    name = "Peyman"
    print("Example 3 — String comparison")
    if name == "Peyman":
        print("Welcome, Peyman!")
    else:
        print("Unknown user.")
    print()


# ---------------------------------------------------------------------------
# Rank 2 — Multiple conditions with elif
# ---------------------------------------------------------------------------

def example_4_grade_evaluation() -> None:
    """Use elif to evaluate multiple ranges."""
    score = 78
    print("Example 4 — Using elif")
    if score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    else:
        print("Grade: D or below")
    print()


def example_5_temperature_check() -> None:
    """Demonstrate elif chain."""
    temperature = 15
    print("Example 5 — Temperature levels")
    if temperature < 0:
        print("Freezing!")
    elif temperature < 10:
        print("Very cold")
    elif temperature < 20:
        print("Cold")
    else:
        print("Warm")
    print()


# ---------------------------------------------------------------------------
# Rank 3 — Logical operators and combined conditions
# ---------------------------------------------------------------------------

def example_6_logical_and_or() -> None:
    """Combine conditions with and/or."""
    age = 22
    is_member = True
    print("Example 6 — Logical operators")

    if age >= 18 and is_member:
        print("Welcome to the club.")

    if age < 18 or not is_member:
        print("Access restricted.")

    print()


def example_7_login_system() -> None:
    """Simulate a simple login system."""
    username = "admin"
    password = "1234"
    print("Example 7 — Combined conditions in login")

    if username == "admin" and password == "1234":
        print("Login successful.")
    else:
        print("Invalid username or password.")
    print()


# ---------------------------------------------------------------------------
# Rank 4 — Nested conditionals
# ---------------------------------------------------------------------------

def example_8_nested_if() -> None:
    """Show nested conditional logic."""
    user_role = "teacher"
    active = True

    print("Example 8 — Nested if statements")

    if active:
        if user_role == "admin":
            print("Admin dashboard opened.")
        elif user_role == "teacher":
            print("Teacher dashboard opened.")
        else:
            print("Standard user panel opened.")
    else:
        print("Account is inactive.")

    print()


# ---------------------------------------------------------------------------
# Rank 5 — More realistic decision-making patterns
# ---------------------------------------------------------------------------

def example_9_billing_rules() -> None:
    """Simulate billing logic using multiple conditions."""
    total = 120
    is_vip = True

    print("Example 9 — Billing rules")

    if total >= 100:
        discount = 20
    elif total >= 50:
        discount = 10
    else:
        discount = 0

    if is_vip:
        discount += 5

    print(f"Total: {total}")
    print(f"Discount applied: {discount}")
    print()


def example_10_input_validation() -> None:
    """Validate simple user input using conditionals."""
    print("Example 10 — Input validation")

    number = -3

    if number < 0:
        print("Error: number cannot be negative.")
    elif number == 0:
        print("Number is zero.")
    else:
        print("Valid positive number.")

    print()


# ---------------------------------------------------------------------------
# Main Entry Point
# ---------------------------------------------------------------------------

def main() -> None:
    """Run all example functions in order."""

    # Rank 1
    example_1_basic_if()
    example_2_if_else()
    example_3_string_comparison()

    # Rank 2
    example_4_grade_evaluation()
    example_5_temperature_check()

    # Rank 3
    example_6_logical_and_or()
    example_7_login_system()

    # Rank 4
    example_8_nested_if()

    # Rank 5
    example_9_billing_rules()
    example_10_input_validation()


if __name__ == "__main__":
    main()
