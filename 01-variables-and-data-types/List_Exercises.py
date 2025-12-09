"""
Module 5 — Lists: Practice Exercises
Comprehensive practice with Python lists, from beginner to
professional, production-style usage.

In this module I:
- Practice creating, modifying, and using lists.
- Learn indexing, slicing, iteration, list comprehensions, and
  real-world data processing.
- Move from very simple examples (Rank 1) to professional usage (Rank 5).

Ranking system:
- Rank 1  -> Beginner: creating lists & printing values.
- Rank 2  -> Easy: indexing, slicing, modifying lists.
- Rank 3  -> Intermediate: loops, calculations, list methods.
- Rank 4  -> Advanced: list comprehensions & structured data.
- Rank 5  -> Professional: reusable list-processing functions.

Author: Peyman Miyandashti
Date of Birth: 11/11/1983
ID Number: 250161
Year: 2025
"""

# ===========================================================
# Rank 1 — Beginner
# Creating simple lists and accessing elements
# ===========================================================

favorite_numbers = [11, 7, 25, 99]
car_years = [2024, 2018]
ages = [43, 47]  # Peyman and Arlette

print("Rank 1 — Beginner")
print("Favorite numbers:", favorite_numbers)
print("First favorite number:", favorite_numbers[0])
print("Second car year:", car_years[1])
print("Ages list:", ages)
print("-" * 50)


# ===========================================================
# Rank 2 — Easy
# Slicing, modifying lists, adding & removing elements
# ===========================================================

games = ["World of Warcraft", "Diablo IV", "Elden Ring", "Valorant"]

# Modify
games[1] = "Diablo III"

# Slice
top_2_games = games[:2]

# Add
games.append("StarCraft")

# Remove
games.remove("Valorant")

print("Rank 2 — Easy")
print("Games list:", games)
print("Top 2 games:", top_2_games)
print("Total games:", len(games))
print("-" * 50)


# ===========================================================
# Rank 3 — Intermediate
# Loops, calculations, and list methods
# ===========================================================

weekly_study_hours = [2.5, 3.75, 4.0, 5.5, 6.25, 3.0, 0.0]

total_hours = sum(weekly_study_hours)
average_hours = total_hours / len(weekly_study_hours)

max_hours = max(weekly_study_hours)
min_hours = min(weekly_study_hours)

print("Rank 3 — Intermediate")
print("Weekly study hours:", weekly_study_hours)
print("Total hours studied:", total_hours)
print("Average hours/day:", round(average_hours, 2))
print("Max study time:", max_hours)
print("Min study time:", min_hours)

print("Daily breakdown:")
for i, hours in enumerate(weekly_study_hours, start=1):
    print(f"  Day {i}: {hours} hours")

print("-" * 50)


# ===========================================================
# Rank 4 — Advanced
# List comprehensions and structured list usage
# ===========================================================

gpa_scores = [9.7, 8.5, 9.1, 10.0, 7.9]

# Filter using list comprehension
scores_over_9 = [score for score in gpa_scores if score > 9.0]

# Convert GPAs to percentages
percentages = [score * 10 for score in gpa_scores]

# Create structured 2D list (table-like)
student_profile = [
    ["Peyman", 43, 187.3, "Mexicali"],
    ["Arlette", 47, 163.0, "Mexicali"]
]

print("Rank 4 — Advanced")
print("GPA scores:", gpa_scores)
print("Scores > 9.0:", scores_over_9)
print("GPA percentages:", percentages)
print("Student table:")
for row in student_profile:
    print("  ", row)

print("-" * 50)


# ===========================================================
# Rank 5 — Professional
# Reusable list-processing function
# ===========================================================

def analyze_scores(scores: list[float]) -> dict:
    """
    Analyze a list of numeric scores and return:
    - average
    - highest
    - lowest
    - number of scores above 9
    - number of passing scores
    Demonstrates real-world list processing.
    """

    average = sum(scores) / len(scores)
    highest = max(scores)
    lowest = min(scores)

    above_9 = len([s for s in scores if s > 9.0])
    passing = len([s for s in scores if s >= 6.0])

    return {
        "average": round(average, 2),
        "highest": highest,
        "lowest": lowest,
        "above_9": above_9,
        "passing": passing
    }


print("Rank 5 — Professional")

pey_man_scores = [95.5, 88.3, 92.75, 90.0, 96.4]
score_analysis = analyze_scores(pey_man_scores)

for key, value in score_analysis.items():
    print(f"{key:15}: {value}")

print("-" * 50)
