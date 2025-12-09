"""
Module 6 — Dictionaries: Practice Exercises (Set A)
Comprehensive practice with Python dictionaries, from beginner to
professional, production-style usage.

In this module I:
- Learn to create, access, modify, and use dictionaries.
- Practice nested dictionaries, loops with dictionaries,
  and real-world structured data.
- Start from Rank 1 (Beginner) and progress to Rank 5 (Professional).

Ranking system:
- Rank 1  -> Beginner: create dictionaries & read values.
- Rank 2  -> Easy: update, add, remove keys.
- Rank 3  -> Intermediate: loops + nested dictionaries.
- Rank 4  -> Advanced: dictionaries with calculations.
- Rank 5  -> Professional: reusable dictionary-processing functions.

Author: Peyman Miyandashti
Date of Birth: 11/11/1983
ID Number: 250161
Year: 2025
"""

# ===========================================================
# Rank 1 — Beginner
# Creating simple dictionaries and accessing values
# ===========================================================

pey_man = {
    "name": "Peyman Miyandashti",
    "age": 43,
    "nationality": "Iranian",
    "city": "Mexicali",
}

print("Rank 1 — Beginner")
print("Name:", pey_man["name"])
print("Age:", pey_man["age"])
print("City:", pey_man["city"])
print("-" * 50)


# ===========================================================
# Rank 2 — Easy
# Updating values, adding new keys, removing keys
# ===========================================================

print("Rank 2 — Easy")

pey_man["favorite_color"] = "Red"     # add
pey_man["favorite_game"] = "World of Warcraft"
pey_man["age"] = 43                    # update
pey_man.pop("nationality")             # remove a key

print("Updated dictionary:", pey_man)
print("Favorite game:", pey_man["favorite_game"])
print("-" * 50)


# ===========================================================
# Rank 3 — Intermediate
# Nested dictionaries and looping through items
# ===========================================================

print("Rank 3 — Intermediate")

family = {
    "Peyman": {"age": 43, "job": "Student - IT Engineering", "car": "Kia Sportage 2024"},
    "Arlette": {"age": 47, "job": "Teacher", "car": "Hyundai Creta 2018"},
}

# Loop through nested dictionary
for person, info in family.items():
    print(f"{person}:")
    for key, value in info.items():
        print(f"  {key}: {value}")

print("-" * 50)


# ===========================================================
# Rank 4 — Advanced
# Dictionaries + calculations + list inside dictionaries
# ===========================================================

print("Rank 4 — Advanced")

student_academic = {
    "name": "Peyman Miyandashti",
    "university": "UPBC",
    "program": "Information Technology Engineering & Digital Innovation",
    "gpa_scores": [9.7, 9.4, 9.2, 9.8],
}

average_gpa = sum(student_academic["gpa_scores"]) / len(student_academic["gpa_scores"])

print("Student Academic Info:")
print(student_academic)
print("Average GPA:", round(average_gpa, 2))
print("-" * 50)


# ===========================================================
# Rank 5 — Professional
# A reusable function that analyzes a student's dictionary
# ===========================================================

def analyze_student(student: dict) -> dict:
    """
    Analyze a student's dictionary with academic and personal information.
    Returns:
    - Name
    - Age group
    - GPA average
    - Status: Excellent / Good / Needs Improvement
    """

    name = student.get("name")
    age = student.get("age")
    gpas = student.get("gpa_scores", [])

    avg_gpa = sum(gpas) / len(gpas)

    if avg_gpa >= 9.5:
        status = "Excellent"
    elif avg_gpa >= 8.0:
        status = "Good"
    else:
        status = "Needs Improvement"

    return {
        "name": name,
        "age": age,
        "average_gpa": round(avg_gpa, 2),
        "academic_status": status,
    }


print("Rank 5 — Professional")

pey_man_full_profile = {
    "name": "Peyman Miyandashti",
    "age": 43,
    "gpa_scores": [9.7, 9.4, 9.2, 9.8],
}

analysis = analyze_student(pey_man_full_profile)

for key, value in analysis.items():
    print(f"{key:20}: {value}")

print("-" * 50)
