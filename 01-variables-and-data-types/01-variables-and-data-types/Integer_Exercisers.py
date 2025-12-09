"""
Module 2 — Integer Variables: Practice Exercises
Comprehensive practice with Python integer variables, from beginner to
more professional, production-style usage.

In this module I will:
- Practice how to create, modify, and use integer variables.
- Start from very simple examples (Rank 1) and move toward
  more realistic, professional patterns (Rank 5).
- Focus only on the integer type here. Other variable types will get
  their own practice files later.

Ranking system:
- Rank 1  -> Beginner: basic integer declarations and operations.
- Rank 2  -> Easy: simple math and combining integer concepts.
- Rank 3  -> Intermediate: real calculations + transformations.
- Rank 4  -> Advanced: integer lists, loops, and formatted output.
- Rank 5  -> Professional: reusable integer-processing functions.

Author: Peyman Miyandashti
Date of Birth: 11/11/1983
ID Number: 250161
Year: 2025
"""

# ===========================================================
# Rank 1 — Beginner
# Simple integer creation and printing
# ===========================================================

age = 43
wife_age = 47
favorite_number = 11

print("Rank 1 — Beginner")
print("Your age:", age)
print("Wife age:", wife_age)
print("Favorite number:", favorite_number)
print("Sum of ages:", age + wife_age)
print("-" * 50)


# ===========================================================
# Rank 2 — Easy
# Basic integer math and comparisons
# ===========================================================

birth_year = 1983
current_year = 2025

calculated_age = current_year - birth_year
difference_ages = wife_age - age
car_year = 2024
wife_car_year = 2018

print("Rank 2 — Easy")
print("Calculated age from year:", calculated_age)
print("Age difference:", difference_ages)
print("Your car age:", current_year - car_year)
print("Wife's car age:", current_year - wife_car_year)
print("Is Peyman older than Arlette?", age > wife_age)
print("-" * 50)


# ===========================================================
# Rank 3 — Intermediate
# More operations in a single example
# ===========================================================

# Update integers, floor division, modulus, and derived values
games_played = 120        # example integer
wins = 75
losses = games_played - wins

win_percentage = (wins * 100) // games_played   # integer percentage

years_in_mexico = current_year - 2017  # example relocation year

print("Rank 3 — Intermediate")
print("Games played:", games_played)
print("Wins:", wins)
print("Losses:", losses)
print("Win percentage (integer):", win_percentage, "%")
print("Years living in Mexico:", years_in_mexico)
print("Favorite number * age =", favorite_number * age)
print("-" * 50)


# ===========================================================
# Rank 4 — Advanced
# Working with lists of integers + loops + formatted output
# ===========================================================

# Example: tracking integer values about Peyman's life
important_years = [
    birth_year,
    2017,            # moved to Mexico
    car_year,
    wife_car_year,
    current_year
]

differences = [
    current_year - y for y in important_years
]

print("Rank 4 — Advanced")
print("Important Years:")
for y in important_years:
    print(f"- {y}")

print("\nYears passed since each event:")
for d in differences:
    print(f"- {d} years")

# Building a formatted block with integers
integer_profile = (
    f"Integer Profile\n"
    f"-----------------\n"
    f"Age: {age}\n"
    f"Wife Age: {wife_age}\n"
    f"Favorite Number: {favorite_number}\n"
    f"Car Years: {car_year}, {wife_car_year}\n"
)

print("\n", integer_profile)
print("-" * 50)


# ===========================================================
# Rank 5 — Professional
# Function that processes and returns integer-based analytics
# ===========================================================

def analyze_person(
    age: int,
    favorite_number: int,
    birth_year: int,
    current_year: int
) -> str:
    """
    Return a formatted integer analytics report.
    This simulates real-world data-processing style code.
    """

    years_lived = current_year - birth_year
    decade = (age // 10) * 10  # find decade (40s, 50s, etc.)
    number_squared = favorite_number * favorite_number

    report = (
        "Integer Analysis Report\n"
        "=======================\n"
        f"{'Age:':20} {age}\n"
        f"{'Years lived:':20} {years_lived}\n"
        f"{'Age decade:':20} {decade}s\n"
        f"{'Fav number²:':20} {number_squared}\n"
    )
    return report


print("Rank 5 — Professional")
result = analyze_person(
    age=age,
    favorite_number=favorite_number,
    birth_year=birth_year,
    current_year=current_year,
)
print(result)
print("-" * 50)
