"""
Module 10 — Sets: Practice Exercises
Comprehensive practice with Python sets, from beginner to
professional, production-style usage.

In this module I:
- Learn set creation, uniqueness, operations, membership,
  mathematical set logic, and real-world patterns.
- Understand differences from lists and tuples.
- Progress from Rank 1 (Beginner) to Rank 5 (Professional).

Ranking system:
- Rank 1  -> Beginner: creating sets and basic behavior.
- Rank 2  -> Easy: adding, removing, and membership tests.
- Rank 3  -> Intermediate: set operations (union, intersection, difference).
- Rank 4  -> Advanced: removing duplicates, filtering, fast lookups.
- Rank 5  -> Professional: real-world set usage in functions.

Author: Peyman Miyandashti
Date of Birth: 11/11/1983
ID Number: 250161
Year: 2025
"""

# ===========================================================
# Rank 1 — Beginner
# Creating simple sets and understanding uniqueness
# ===========================================================

print("Rank 1 — Beginner")

favorite_numbers = {11, 7, 11, 25, 7, 99}
print("Favorite numbers (set removes duplicates):", favorite_numbers)

colors = {"Red", "Blue", "Red"}
print("Colors:", colors)  # Red appears only once

print("Length of favorite_numbers:", len(favorite_numbers))
print("-" * 50)


# ===========================================================
# Rank 2 — Easy
# Adding, removing, and checking membership
# ===========================================================

print("Rank 2 — Easy")

games = {"World of Warcraft", "Diablo", "Elden Ring"}

# Add item
games.add("StarCraft")

# Remove item safely
games.discard("Diablo")  # discard doesn’t error if missing

# Membership check
print("Games set:", games)
print("Is WoW in the set?", "World of Warcraft" in games)
print("Is Fortnite in the set?", "Fortnite" in games)

print("-" * 50)


# ===========================================================
# Rank 3 — Intermediate
# Set operations: union, intersection, difference
# ===========================================================

print("Rank 3 — Intermediate")

set_a = {11, 22, 33, 44}
set_b = {33, 44, 55, 66}

print("A ∪ B (union):", set_a | set_b)
print("A ∩ B (intersection):", set_a & set_b)
print("A - B (difference):", set_a - set_b)
print("B - A:", set_b - set_a)

print("-" * 50)


# ===========================================================
# Rank 4 — Advanced
# Removing duplicates and fast membership checks
# ===========================================================

print("Rank 4 — Advanced")

students_list = [
    "Peyman", "Arlette", "Peyman",
    "Ali", "Sara", "Ali", "Maria"
]

# Convert list → set to remove duplicates
unique_students = set(students_list)

print("Original list:", students_list)
print("Unique names (set):", unique_students)

# Fast lookup example
blocked_users = {"hacker01", "bot123", "spam_acc"}
user_attempt = "bot123"

if user_attempt in blocked_users:
    print(f"ACCESS DENIED → {user_attempt} is blocked.")
else:
    print("User allowed.")

print("-" * 50)


# ===========================================================
# Rank 5 — Professional
# Real-world set-based filtering function
# ===========================================================

def find_common_courses(student1: set, student2: set) -> set:
    """
    Returns the set of courses shared between two students.
    Demonstrates efficient real-world set logic.
    """
    return student1 & student2  # intersection


def find_missing_courses(required: set, completed: set) -> set:
    """
    Returns courses the student is missing.
    Demonstrates set difference.
    """
    return required - completed


print("Rank 5 — Professional")

pey_man_courses = {"Python", "Networking", "Math", "Linux"}
upbc_required_courses = {"Python", "Math", "AI", "Databases", "Linux"}

common = find_common_courses(pey_man_courses, upbc_required_courses)
missing = find_missing_courses(upbc_required_courses, pey_man_courses)

print("Courses Peyman already has:", common)
print("Courses Peyman is missing:", missing)

print("-" * 50)
