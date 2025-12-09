"""
Module 17 — Exceptions (try/except): Practice Exercises
Comprehensive practice with Python exceptions, from beginner to
more professional, production-style usage.

In this module I:
- Practice how to use try/except to catch and handle errors.
- Learn how to work with specific exception types (ValueError, ZeroDivisionError, etc.).
- Use else and finally blocks for more precise control.
- Build small, reusable functions that validate and handle errors cleanly.

Ranking system:
- Rank 1  -> Beginner: very basic try/except usage.
- Rank 2  -> Easy: input conversion and simple error messages.
- Rank 3  -> Intermediate: multiple exceptions and simple validation.
- Rank 4  -> Advanced: functions, else/finally, and cleaner structure.
- Rank 5  -> Professional: reusable validation + exception handling patterns.

Author: Peyman Miyandashti
Date of Birth: 11/11/1983
ID Number: 250161
Year: 2025
"""

# Base data about Peyman that we can reuse in examples
peyman_age = 43
peyman_height_cm = int(187.3)  # 187
peyman_weight_kg = int(72.5)   # 72
favorite_number = 11


# ===========================================================
# Rank 1 — Beginner
# Simple try/except with ZeroDivisionError
# ===========================================================

print("Rank 1 — Beginner")

# Here we intentionally do a dangerous operation: division by zero.
# We use try/except so the program does not crash.
try:
    result = peyman_age / 0
    print("Result:", result)
except ZeroDivisionError:
    print("Oops! You tried to divide by zero. This is not allowed in math.")

print("-" * 50)


# ===========================================================
# Rank 2 — Easy
# Converting strings to integers with ValueError handling
# ===========================================================

print("Rank 2 — Easy")

# Imagine Peyman is reading user input as strings from the keyboard or a file.
# We simulate this with hard-coded strings.

age_input = "43"        # valid integer string
height_input = "187.3"  # invalid integer string (float, not int)

def safe_int_convert(text: str) -> int | None:
    """Convert text to int safely. Return None if it fails."""
    try:
        value = int(text)
        return value
    except ValueError:
        print(f"Cannot convert '{text}' to an integer.")
        return None

peyman_age_int = safe_int_convert(age_input)
peyman_height_int = safe_int_convert(height_input)

print("Converted age:", peyman_age_int)
print("Converted height (should fail):", peyman_height_int)

print("-" * 50)


# ===========================================================
# Rank 3 — Intermediate
# Handling multiple exceptions and validating data
# ===========================================================

print("Rank 3 — Intermediate")

# Scenario:
# Peyman wants to calculate BMI = weight_kg / (height_m ** 2)
# Possible problems:
# - ValueError if conversion fails
# - ZeroDivisionError if height is 0 (invalid data)

def calculate_bmi(height_cm_str: str, weight_kg_str: str) -> float | None:
    try:
        height_cm = float(height_cm_str)
        weight_kg = float(weight_kg_str)

        if height_cm <= 0:
            raise ValueError("Height must be greater than zero.")

        height_m = height_cm / 100
        bmi = weight_kg / (height_m ** 2)
        return bmi

    except ValueError as e:
        print("Value error while calculating BMI:", e)
        return None
    except ZeroDivisionError:
        print("Zero division error: height cannot be zero.")
        return None

# Valid data from Peyman
bmi_valid = calculate_bmi("187.3", "72.5")
print("BMI with valid data:", bmi_valid)

# Invalid height data: zero
bmi_invalid_height = calculate_bmi("0", "72.5")
print("BMI with invalid height:", bmi_invalid_height)

# Invalid weight data: not a number
bmi_invalid_weight = calculate_bmi("187.3", "seventy-two")
print("BMI with invalid weight:", bmi_invalid_weight)

print("-" * 50)


# ===========================================================
# Rank 4 — Advanced
# Using else and finally with try/except
# ===========================================================

print("Rank 4 — Advanced")

# Scenario:
# Peyman wants to compute an "effort score" for his life:
# age * favorite_number / number_of_countries_lived
# He has lived in 2 countries: Iran and Mexico.

def effort_score(age: int, favorite_number: int, countries_lived: int) -> float | None:
    try:
        score = age * favorite_number / countries_lived
    except ZeroDivisionError:
        print("You must have lived in at least 1 country!")
        return None
    else:
        # This block runs only if NO exception happened
        print("Effort score calculated successfully.")
        return score
    finally:
        # This block always runs, no matter what
        print("Finished effort_score calculation (success or failure).")

countries_lived = 2  # Iran and Mexico

score_ok = effort_score(peyman_age, favorite_number, countries_lived)
print("Effort score (valid):", score_ok)

score_bad = effort_score(peyman_age, favorite_number, 0)
print("Effort score (invalid):", score_bad)

print("-" * 50)


# ===========================================================
# Rank 5 — Professional
# Reusable validation + exception handling pattern
# ===========================================================

print("Rank 5 — Professional")

class ValidationError(Exception):
    """Custom exception for validation errors."""
    pass


def validate_age(age: int) -> None:
    """Validate a human age for Peyman-style data."""
    if age <= 0:
        raise ValidationError("Age must be positive.")
    if age > 120:
        raise ValidationError("Age is unrealistically high.")


def validate_year(year: int) -> None:
    """Validate a car year or general year."""
    if year < 1900:
        raise ValidationError("Year is too old for this context.")
    if year > 2100:
        raise ValidationError("Year is too far in the future.")


def build_life_summary(
    name: str,
    age: int,
    country: str,
    city: str,
    car_year: int
) -> str | None:
    """
    Build a summary string about Peyman, with strong validation.

    If validation fails, it returns None and prints a clear error.
    """

    try:
        validate_age(age)
        validate_year(car_year)
    except ValidationError as e:
        print("Validation error while building life summary:", e)
        return None
    except Exception as e:
        # Generic safety net for any unexpected errors
        print("Unexpected error:", e)
        return None
    else:
        # If there were no exceptions, build the summary
        summary = (
            f"Life Summary for {name}\n"
            f"------------------------\n"
            f"Age: {age}\n"
            f"Location: {city}, {country}\n"
            f"Car year: {car_year}\n"
        )
        return summary


# Using real Peyman data
life_summary_ok = build_life_summary(
    name="Peyman Miyandashti",
    age=peyman_age,
    country="Mexico",
    city="Mexicali",
    car_year=2024,  # Kia Sportage 2024
)

print("Valid life summary:")
print(life_summary_ok)

# Example with invalid data: negative age
life_summary_bad = build_life_summary(
    name="Peyman Miyandashti",
    age=-5,
    country="Mexico",
    city="Mexicali",
    car_year=2024,
)

print("Invalid life summary (should be None):", life_summary_bad)

print("-" * 50)
