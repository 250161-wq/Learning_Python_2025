"""
Module 9 — NoneType: Practice Exercises
Comprehensive practice with Python's NoneType, from beginner to
professional, production-style usage.

In this module I:
- Learn what NoneType is and when to use None.
- Understand default values, missing data, and functions that return None.
- Work with conditionals, checks, placeholders, and optional values.
- Progress from Rank 1 (Beginner) to Rank 5 (Professional).

Ranking system:
- Rank 1  -> Beginner: basic None usage and printing.
- Rank 2  -> Easy: None vs. 0 vs. False, basic comparison.
- Rank 3  -> Intermediate: using None in functions.
- Rank 4  -> Advanced: None in data structures and validation.
- Rank 5  -> Professional: optional parameters and typed functions.

Author: Peyman Miyandashti
Date of Birth: 11/11/1983
ID Number: 250161
Year: 2025
"""

# ===========================================================
# Rank 1 — Beginner
# Basic NoneType usage
# ===========================================================

print("Rank 1 — Beginner")

x = None
print("x is:", x)
print("The type of x is:", type(x))

# None means “no value yet” or “empty”
profile_picture = None
print("Profile picture status:", profile_picture)

print("-" * 50)


# ===========================================================
# Rank 2 — Easy
# None vs False vs 0 — very important differences
# ===========================================================

print("Rank 2 — Easy")

value_none = None
value_zero = 0
value_false = False

print("None == 0 ?", value_none == value_zero)
print("None == False ?", value_none == value_false)
print("None is None ?", value_none is None)

# Always use "is None" or "is not None" for best practice
print("Correct check:", value_none is None)

print("-" * 50)


# ===========================================================
# Rank 3 — Intermediate
# Functions that return None when nothing is returned
# ===========================================================

print("Rank 3 — Intermediate")

def greet(name):
    print("Hello,", name)
    # This function does not return anything → returns None automatically

result = greet("Peyman")
print("Function return value = ", result)  # Will show None

def optional_game_choice(choice=None):
    if choice is None:
        return "No game selected."
    return f"You selected: {choice}"

print(optional_game_choice())  # No selection
print(optional_game_choice("World of Warcraft"))  # Selected

print("-" * 50)


# ===========================================================
# Rank 4 — Advanced
# Using None in dictionaries, validation, missing data
# ===========================================================

print("Rank 4 — Advanced")

student_profile = {
    "name": "Peyman Miyandashti",
    "height_cm": 187.3,
    "weight_kg": 72.5,
    "gpa": None,            # GPA not updated yet
    "nickname": None,       # Not assigned
}

# Checking for missing data
for key, value in student_profile.items():
    if value is None:
        print(f"{key} → MISSING VALUE")
    else:
        print(f"{key} → {value}")

print("-" * 50)


# ===========================================================
# Rank 5 — Professional
# Optional parameters, typed functions, returning (value OR None)
# ===========================================================

def find_score(scores: list[float], minimum: float) -> float | None:
    """
    Returns the first score that is >= minimum.
    If no such score exists, return None.

    This is REAL-WORLD code technique in data filtering.
    """
    for score in scores:
        if score >= minimum:
            return score
    return None  # Nothing found

print("Rank 5 — Professional")

pey_man_scores = [9.7, 9.4, 9.2, 9.8]

result = find_score(pey_man_scores, 9.5)

if result is None:
    print("No score found above 9.5")
else:
    print("Found score:", result)

# Test missing case
result2 = find_score(pey_man_scores, 10)
print("Trying minimum = 10 →", result2)

print("-" * 50)
