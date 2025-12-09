"""
Module 8 — Tuples: Practice Exercises
Comprehensive practice with Python tuples, from beginner to
professional, production-style usage.

In this module I:
- Learn how tuples work and how they differ from lists.
- Use indexing, unpacking, nested tuples, and real-world patterns.
- Progress from Rank 1 (Beginner) to Rank 5 (Professional).

Ranking system:
- Rank 1  -> Beginner: basic tuple creation and indexing.
- Rank 2  -> Easy: unpacking and tuple operations.
- Rank 3  -> Intermediate: nested tuples + loops.
- Rank 4  -> Advanced: tuples mixed with data structures.
- Rank 5  -> Professional: returning structured tuple data.

Author: Peyman Miyandashti
Date of Birth: 11/11/1983
ID Number: 250161
Year: 2025
"""

# ===========================================================
# Rank 1 — Beginner
# Creating and accessing basic tuples
# ===========================================================

print("Rank 1 — Beginner")

basic_info = ("Peyman", 43, "Mexicali")

print("Tuple:", basic_info)
print("Name:", basic_info[0])
print("Age:", basic_info[1])
print("City:", basic_info[2])
print("-" * 50)


# ===========================================================
# Rank 2 — Easy
# Tuple unpacking, length, and simple operations
# ===========================================================

print("Rank 2 — Easy")

favorite_numbers = (11, 7, 25, 99)

# Tuple unpacking
n1, n2, n3, n4 = favorite_numbers

print("Favorite numbers tuple:", favorite_numbers)
print("Unpacked n1:", n1)
print("Unpacked n2:", n2)

# Length of tuple
print("Length of tuple:", len(favorite_numbers))

# Tuple slicing (still allowed even though immutable)
print("First two numbers:", favorite_numbers[:2])
print("-" * 50)


# ===========================================================
# Rank 3 — Intermediate
# Nested tuples and loops
# ===========================================================

print("Rank 3 — Intermediate")

family_tuple = (
    ("Peyman", 43, "Kia Sportage 2024"),
    ("Arlette", 47, "Hyundai Creta 2018")
)

for name, age, car in family_tuple:
    print(f"Name: {name}, Age: {age}, Car: {car}")

print("-" * 50)


# ===========================================================
# Rank 4 — Advanced
# Tuples inside dictionaries and dictionaries inside tuples
# ===========================================================

print("Rank 4 — Advanced")

# Tuple of GPA scores
gpa_scores = (9.7, 9.4, 9.2, 9.8)

# Dictionary that uses tuple
academic_profile = {
    "name": "Peyman Miyandashti",
    "scores": gpa_scores,
    "average": sum(gpa_scores) / len(gpa_scores)
}

print("Academic Profile:")
for key, value in academic_profile.items():
    print(f"{key:10}: {value}")

# Tuple of dictionaries
locations = (
    {"city": "Mexicali", "country": "Mexico"},
    {"city": "Tabriz", "country": "Iran"},
)

print("\nLocations Tuple:")
for loc in locations:
    print(f"{loc['city']} - {loc['country']}")

print("-" * 50)


# ===========================================================
# Rank 5 — Professional
# Real project use-case: a function that returns tuple data
# ===========================================================

def analyze_physical_stats(height_cm: float, weight_kg: float):
    """
    Returns a tuple:
    (BMI, BMI Category, Healthy Range Boolean)

    Demonstrates:
    - returning multiple values cleanly
    - immutable structured data
    - perfect for APIs and production work
    """

    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    healthy = (category == "Normal")

    return (round(bmi, 2), category, healthy)


print("Rank 5 — Professional")

result = analyze_physical_stats(187.3, 72.5)
bmi_value, category, healthy_flag = result

print("BMI:", bmi_value)
print("Category:", category)
print("Healthy Range:", healthy_flag)

print("-" * 50)
