"""
Module 3 — Float Variables: Practice Exercises
Comprehensive practice with Python float variables, from beginner to
professional, production-style usage.

In this module I:
- Practice how to create, modify, and use float variables.
- Start from very simple examples (Rank 1) and move toward
  realistic, professional numeric operations (Rank 5).
- Focus only on the float type here. Integers and strings have
  their own modules already.

Ranking system:
- Rank 1  -> Beginner: basic float assignments and prints.
- Rank 2  -> Easy: simple arithmetic using decimals.
- Rank 3  -> Intermediate: rounding, percentages, BMI, conversions.
- Rank 4  -> Advanced: lists, averages, data cleaning.
- Rank 5  -> Professional: reusable function with formatted float output.

Author: Peyman Miyandashti
Date of Birth: 11/11/1983
ID Number: 250161
Year: 2025
"""

# ===========================================================
# Rank 1 — Beginner
# Simple float creation and printing
# ===========================================================

height = 187.3   # Peyman's height
weight = 72.5    # Peyman's weight

print("Rank 1 — Beginner")
print("Height (cm):", height)
print("Weight (kg):", weight)
print("Sum of height + weight:", height + weight)
print("-" * 50)


# ===========================================================
# Rank 2 — Easy
# Basic decimal arithmetic
# ===========================================================

gpa_semester1 = 9.4
gpa_semester2 = 9.7
gpa_average = (gpa_semester1 + gpa_semester2) / 2

height_meters = height / 100  # convert cm to meters

print("Rank 2 — Easy")
print("GPA Semester 1:", gpa_semester1)
print("GPA Semester 2:", gpa_semester2)
print("GPA Average:", gpa_average)
print("Height in meters:", height_meters)
print("-" * 50)


# ===========================================================
# Rank 3 — Intermediate
# Rounding, percentages, BMI calculation
# ===========================================================

# BMI formula: weight / (height_meters^2)
bmi = weight / (height_meters ** 2)

rounded_bmi_1 = round(bmi, 1)
rounded_bmi_2 = round(bmi, 2)

completion_score = 87.456
rounded_score = round(completion_score, 2)
percentage = (completion_score / 100) * 100

print("Rank 3 — Intermediate")
print("BMI:", bmi)
print("BMI rounded to 1 decimal:", rounded_bmi_1)
print("BMI rounded to 2 decimals:", rounded_bmi_2)
print("Rounded score:", rounded_score)
print("Percentage:", percentage)
print("-" * 50)


# ===========================================================
# Rank 4 — Advanced
# Lists of floats, average, min/max, formatted output
# ===========================================================

weekly_study_hours = [2.5, 3.75, 4.0, 5.5, 6.25, 3.0, 0.0]

average_study = sum(weekly_study_hours) / len(weekly_study_hours)
max_hours = max(weekly_study_hours)
min_hours = min(weekly_study_hours)

print("Rank 4 — Advanced")
print("Weekly study hours:", weekly_study_hours)
print("Average study hours:", round(average_study, 2))
print("Max hours in a day:", max_hours)
print("Min hours in a day:", min_hours)

formatted_block = (
    f"\nStudy Report\n"
    f"----------------------\n"
    f"Avg hours/day:   {average_study:.2f}\n"
    f"Max hours/day:   {max_hours:.2f}\n"
    f"Min hours/day:   {min_hours:.2f}\n"
)

print(formatted_block)
print("-" * 50)


# ===========================================================
# Rank 5 — Professional
# Reusable function with real float processing
# ===========================================================

def build_health_report(
    height_cm: float,
    weight_kg: float,
    last_five_scores: list[float]
) -> str:
    """
    Build a formatted health + academic performance report.

    Demonstrates professional float usage:
    - rounding
    - averages
    - computed metrics
    - formatted multi-line output
    """

    height_m = height_cm / 100
    bmi_value = weight_kg / (height_m ** 2)
    avg_score = sum(last_five_scores) / len(last_five_scores)

    report = (
        "Float Analysis Report\n"
        "=====================\n"
        f"{'Height:':20} {height_cm:.1f} cm\n"
        f"{'Weight:':20} {weight_kg:.1f} kg\n"
        f"{'BMI:':20} {bmi_value:.2f}\n"
        f"{'Avg Score:':20} {avg_score:.2f}\n"
    )
    return report


print("Rank 5 — Professional")

pey_man_report = build_health_report(
    height_cm=height,
    weight_kg=weight,
    last_five_scores=[95.5, 88.3, 92.75, 90.0, 96.4]
)

print(pey_man_report)
print("-" * 50)
