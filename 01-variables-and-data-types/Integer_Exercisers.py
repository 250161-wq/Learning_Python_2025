"""
Module 2 — Integer Variables: Practice Exercises
Comprehensive practice with Python integer variables, from beginner to
more professional, production-style usage.

In this module I:
- Practice how to create, modify, and use integer variables.
- Start from very simple examples (Rank 1) and move toward
  more realistic, professional patterns (Rank 5).
- Focus only on the integer (int) type here. Floats will get
  their own practice file in Module 3.

Ranking system:
- Rank 1  -> Beginner: very basic syntax and concepts.
- Rank 2  -> Easy: still simple, but combining two or more concepts.
- Rank 3  -> Intermediate: more operations and small calculations.
- Rank 4  -> Advanced: closer to how numeric data is used in real projects.
- Rank 5  -> Professional: clean, reusable, and readable numeric logic.

Author: Peyman Miyandashti
Date of Birth: 11/11/1983
ID Number: 250161
Year: 2025
"""

# ===========================================================
# Rank 1 — Beginner
# Simple integer creation and printing
# ===========================================================

pey_man_age = 43          # Peyman's age
wife_age = 47             # Arlette's age

print("Rank 1 — Beginner")
print("Peyman's age:", pey_man_age)
print("Wife's age:", wife_age)
print("Sum of ages:", pey_man_age + wife_age)
print("-" * 50)


# ===========================================================
# Rank 2 — Easy
# Basic calculations with your personal data
# ===========================================================

current_year = 2025
pey_man_birth_year = 1983
favorite_number = 11

# Age calculated from years
calculated_age = current_year - pey_man_birth_year
age_difference = wife_age - pey_man_age

print("Rank 2 — Easy")
print("Current year:", current_year)
print("Birth year:", pey_man_birth_year)
print("Calculated age from years:", calculated_age)
print("Favorite number:", favorite_number)
print("Age difference (wife - Peyman):", age_difference)
print("Age in 10 years:", pey_man_age + 10)
print("-" * 50)


# ===========================================================
# Rank 3 — Intermediate
# Arithmetic operations ( +, -, *, //, %, ** )
# ===========================================================

# Game-related integer practice
hours_played_per_day = 2          # example value
days_per_week_playing = 5         # example value

weekly_play_time = hours_played_per_day * days_per_week_playing
favorite_number_squared = favorite_number ** 2
age_divisible_by_favorite = pey_man_age % favorite_number == 0

print("Rank 3 — Intermediate")
print("Weekly play time (hours):", weekly_play_time)
print("Favorite number squared:", favorite_number_squared)
print("Is age divisible by favorite number?:", age_divisible_by_favorite)

# Integer division and remainder examples
total_levels = 73
levels_per_week = 4
full_weeks_needed = total_levels // levels_per_week
remaining_levels = total_levels % levels_per_week

print("Total levels to complete:", total_levels)
print("Full weeks needed:", full_weeks_needed)
print("Remaining levels after full weeks:", remaining_levels)
print("-" * 50)


# ===========================================================
# Rank 4 — Advanced
# Using lists/dicts of integers and simple analysis
# ===========================================================

# Car years and basic "age" of each car
kia_sportage_year = 2024
hyundai_creta_year = 2018

kia_age = current_year - kia_sportage_year
creta_age = current_year - hyundai_creta_year

car_years = {
    "Kia Sportage": kia_sportage_year,
    "Hyundai Creta": hyundai_creta_year,
}

print("Rank 4 — Advanced")
print("Car model years:")
for car_name, year in car_years.items():
    car_age = current_year - year
    print(f"- {car_name}: year {year}, age {car_age} years")

# Simple integer-based stats
family_ages = [pey_man_age, wife_age]
total_family_age = sum(family_ages)
average_family_age = total_family_age // len(family_ages)  # integer division

print("Total family age (Peyman + Arlette):", total_family_age)
print("Average family age (integer):", average_family_age)
print("-" * 50)


# ===========================================================
# Rank 5 — Professional
# Reusable function that works with integer data
# (age checks, remaining years, goals)
# ===========================================================

def build_integer_profile(
    current_age: int,
    target_graduation_age: int,
    current_year: int,
    start_year_degree: int,
    credits_completed: int,
    total_credits: int
) -> dict:
    """
    Create a numeric profile for a student using only integer data.

    This function is an example of how integers are used in
    real-world projects: reusable calculations and clean logic.
    """
    years_until_graduation = max(target_graduation_age - current_age, 0)
    study_years_so_far = current_year - start_year_degree
    credits_remaining = max(total_credits - credits_completed, 0)
    percent_completed = (credits_completed * 100) // total_credits

    profile = {
        "current_age": current_age,
        "target_graduation_age": target_graduation_age,
        "years_until_graduation": years_until_graduation,
        "study_years_so_far": study_years_so_far,
        "credits_completed": credits_completed,
        "credits_remaining": credits_remaining,
        "percent_completed": percent_completed,
    }
    return profile


print("Rank 5 — Professional")

# Example: Peyman as a student at UPBC
pey_man_integer_profile = build_integer_profile(
    current_age=pey_man_age,
    target_graduation_age=48,   # example target age for finishing the degree
    current_year=current_year,
    start_year_degree=2023,     # example year he started at UPBC
    credits_completed=72,       # example value
    total_credits=300           # example value
)

# Nicely print the integer profile
for key, value in pey_man_integer_profile.items():
    print(f"{key:25}: {value}")

print("-" * 50)




