"""
Module 4 — Boolean Variables: Practice Exercises
Comprehensive practice with Python boolean variables, from beginner to
professional, production-style usage.

In this module I:
- Practice how to create and use boolean variables.
- Understand comparison operators and logical operations.
- Move from basic True/False to real-world decision making.
- Start at Rank 1 (Beginner) and progress to Rank 5 (Professional).

Ranking system:
- Rank 1  -> Beginner: simple booleans and prints.
- Rank 2  -> Easy: comparisons and expressions.
- Rank 3  -> Intermediate: logical operators and conditions.
- Rank 4  -> Advanced: boolean lists and filtering.
- Rank 5  -> Professional: reusable boolean-based functions.

Author: Peyman Miyandashti
Date of Birth: 11/11/1983
ID Number: 250161
Year: 2025
"""

# ===========================================================
# Rank 1 — Beginner
# Creating boolean variables
# ===========================================================

is_student = True
is_married = True
likes_red_color = True

print("Rank 1 — Beginner")
print("Is Peyman a student?", is_student)
print("Is he married?", is_married)
print("Does he like red color?", likes_red_color)
print("-" * 50)


# ===========================================================
# Rank 2 — Easy
# Comparisons that produce boolean results
# ===========================================================

age = 43
wife_age = 47
favorite_number = 11

is_older_than_wife = age > wife_age
is_favorite_even = (favorite_number % 2 == 0)
is_age_over_40 = age >= 40

print("Rank 2 — Easy")
print("Is Peyman older than Arlette?", is_older_than_wife)
print("Is Peyman's favorite number even?", is_favorite_even)
print("Is Peyman 40 or older?", is_age_over_40)
print("-" * 50)


# ===========================================================
# Rank 3 — Intermediate
# Using boolean logic (and, or, not)
# ===========================================================

lives_in_mexico = True
born_in_iran = True
height_cm = 187.3
weight_kg = 72.5

healthy_bmi = (18.5 <= (weight_kg / (height_cm/100)**2) <= 24.9)
tall_person = height_cm > 180

# complex decision
is_healthy_and_tall = healthy_bmi and tall_person
is_iranian_or_mexican = born_in_iran or lives_in_mexico

print("Rank 3 — Intermediate")
print("Healthy BMI?", healthy_bmi)
print("Tall person?", tall_person)
print("Healthy AND tall?", is_healthy_and_tall)
print("Iranian OR living in Mexico?", is_iranian_or_mexican)
print("NOT healthy?", not healthy_bmi)
print("-" * 50)


# ===========================================================
# Rank 4 — Advanced
# Boolean filtering & validating a dataset
# ===========================================================

gpa_scores = [9.7, 8.5, 9.1, 7.9, 10.0]

# Create a boolean list marking scores above 9.0
high_scores_flags = [score > 9.0 for score in gpa_scores]

# Count how many True values exist
high_score_count = sum(high_scores_flags)

print("Rank 4 — Advanced")
print("GPA Scores:", gpa_scores)
print("Scores > 9.0 (booleans):", high_scores_flags)
print("Number of very high scores:", high_score_count)

# Example: verify if all scores are passing
passing_flags = [score >= 6.0 for score in gpa_scores]
all_passing = all(passing_flags)

print("All scores passing?", all_passing)
print("-" * 50)


# ===========================================================
# Rank 5 — Professional
# Real-world boolean decision function
# ===========================================================

def build_upbc_eligibility_report(
    age: int,
    is_student: bool,
    gpa: float,
    attendance_rate: float
) -> str:
    """
    Determine if a student meets UPBC academic and attendance requirements.

    Demonstrates:
    - chained booleans
    - readable decision logic
    - clean multi-line formatted output
    """

    meets_age_requirement = age >= 18
    meets_gpa_requirement = gpa >= 8.0
    meets_attendance = attendance_rate >= 0.85

    fully_eligible = (
        meets_age_requirement
        and meets_gpa_requirement
        and meets_attendance
        and is_student
    )

    report = (
        "UPBC Eligibility Report\n"
        "=======================\n"
        f"{'Age OK:':20} {meets_age_requirement}\n"
        f"{'GPA OK:':20} {meets_gpa_requirement}\n"
        f"{'Attendance OK:':20} {meets_attendance}\n"
        f"{'Is Student:':20} {is_student}\n"
        f"{'FULLY ELIGIBLE:':20} {fully_eligible}\n"
    )
    return report


print("Rank 5 — Professional")
eligibility_report = build_upbc_eligibility_report(
    age=43,
    is_student=True,
    gpa=9.4,
    attendance_rate=0.92
)

print(eligibility_report)
print("-" * 50)
