"""
Module 12 — Conditionals (If / Elif / Else)
Professional practice with conditional logic in Python,
from beginner to advanced real-world patterns.

This module covers:
- basic if statements
- elif chains
- nested conditions
- logical operators in conditions
- real-world decision-making functions

Ranking:
- Rank 1 -> Beginner: simple if/else
- Rank 2 -> Easy: elif chains + comparison logic
- Rank 3 -> Intermediate: nested conditionals + combined logic
- Rank 4 -> Advanced: complex multi-condition evaluations
- Rank 5 -> Professional: real-world conditional-driven functions

Author: Peyman Miyandashti
Student at UPBC — IT Engineering & Digital Innovation
Year: 2025
"""

# Personal data used in examples
pey_age = 43
pey_weight = 72.5
pey_height = 187.3
favorite_color = "Red"
favorite_number = 11
is_student = True
gpa = 9.6
city = "Mexicali"

# ===========================================================
# Rank 1 — Beginner
# Simple IF / ELSE decisions
# ===========================================================

print("Rank 1 — Beginner")

if pey_age >= 18:
    print("Peyman is an adult.")
else:
    print("Peyman is a minor.")

if favorite_color == "Red":
    print("Red is Peyman's favorite color!")

print("-" * 50)


# ===========================================================
# Rank 2 — Easy
# Elif chains for multiple decisions
# ===========================================================

print("Rank 2 — Easy")

if pey_age < 18:
    category = "Minor"
elif pey_age < 40:
    category = "Young Adult"
elif pey_age < 60:
    category = "Adult"
else:
    category = "Senior"

print("Age category:", category)

# GPA evaluation
if gpa >= 9.5:
    print("Excellent GPA — Great job, Peyman!")
elif gpa >= 8.0:
    print("Good GPA — Keep progressing!")
else:
    print("Needs improvement — You can do it!")

print("-" * 50)


# ===========================================================
# Rank 3 — Intermediate
# Combining conditions (AND / OR)
# ===========================================================

print("Rank 3 — Intermediate")

# Determine if Peyman has a healthy BMI
bmi = pey_weight / (pey_height/100)**2

if bmi >= 18.5 and bmi <= 24.9:
    print("Peyman has a NORMAL BMI.")
elif bmi < 18.5:
    print("BMI: Underweight")
else:
    print("BMI: Overweight")

# Check if Peyman likes red OR favorite number matches
if favorite_color == "Red" or favorite_number == 11:
    print("Peyman clearly has strong preferences!")

print("-" * 50)


# ===========================================================
# Rank 4 — Advanced
# Nested conditions + multi-rule evaluation
# ===========================================================

print("Rank 4 — Advanced")

# Rule-based evaluation
if city == "Mexicali":
    if is_student:
        print("Peyman is a student living in Mexicali.")
    else:
        print("Peyman lives in Mexicali but is not a student.")
else:
    print("Peyman lives outside Mexicali.")

# Complex multi-condition rule
if pey_age > 40 and gpa > 9.0 and is_student:
    print("High-achieving adult student!")
else:
    print("Does not meet all criteria.")

print("-" * 50)


# ===========================================================
# Rank 5 — Professional
# Real-world conditional decision functions
# ===========================================================

def evaluate_admission(gpa: float, english_score: float, experience_years: int):
    """
    Real-world admission logic:
    - GPA > 9.0 or English > 85 -> strong candidate
    - experience > 5 years -> bonus
    """
    if gpa >= 9.0 and english_score >= 85:
        return "Strong candidate — Guaranteed admission!"

    if gpa >= 8.0 or english_score >= 80:
        if experience_years >= 5:
            return "Good candidate — Admitted with experience bonus."
        return "Good candidate — Likely admission."

    return "Not eligible — Improve GPA or English score."


def classify_bmi(weight: float, height_cm: float):
    """
    Professional BMI classifier with thresholds.
    """
    bmi = weight / (height_cm/100)**2

    if bmi < 18.5:
        return "Underweight", bmi
    elif bmi < 25:
        return "Normal", bmi
    elif bmi < 30:
        return "Overweight", bmi
    else:
        return "Obese", bmi


print("Rank 5 — Professional")

admission_result = evaluate_admission(
    gpa=9.6,
    english_score=88,
    experience_years=6
)

print("Admission Evaluation:", admission_result)

bmi_status, bmi_value = classify_bmi(pey_weight, pey_height)
print(f"BMI Status: {bmi_status} ({bmi_value:.2f})")

print("-" * 50)
