"""
Module 15 — Frozenset: Practice Exercises
Professional-level practice with Python's immutable set type: frozenset.

In this module I:
- Learn the difference between set and frozenset.
- Perform math operations with frozensets.
- Use frozenset as dictionary keys (since they are hashable).
- Build real-world immutable data structures.
- Progress from Rank 1 → Rank 5.

Ranking:
- Rank 1 -> Beginner: basic frozenset creation.
- Rank 2 -> Easy: membership, length, iteration.
- Rank 3 -> Intermediate: union, intersection, difference.
- Rank 4 -> Advanced: using frozenset as dictionary keys.
- Rank 5 -> Professional: real-world immutable configuration patterns.

Author: Peyman Miyandashti
Student at UPBC — IT Engineering & Digital Innovation
Year: 2025
"""

# ===========================================================
# Rank 1 — Beginner
# Creating a frozenset & comparing with set
# ===========================================================

print("Rank 1 — Beginner")

normal_set = {11, 7, 25, 11}
immutable_set = frozenset([11, 7, 25, 11])

print("Normal set:", normal_set)
print("Frozenset:", immutable_set)

# Check types
print("Type of normal_set:", type(normal_set))
print("Type of immutable_set:", type(immutable_set))

# Trying to modify → WILL FAIL (as intended)
print("Frozensets are immutable — cannot add/remove!")

print("-" * 50)


# ===========================================================
# Rank 2 — Easy
# Membership tests + iteration + length
# ===========================================================

print("Rank 2 — Easy")

courses = frozenset(["Python", "Math", "Networking", "Linux"])

print("Courses:", courses)
print("Length:", len(courses))
print("Is 'Python' in courses?", "Python" in courses)

print("Iterating values:")
for c in courses:
    print(" -", c)

print("-" * 50)


# ===========================================================
# Rank 3 — Intermediate
# Mathematical operations with frozenset
# ===========================================================

print("Rank 3 — Intermediate")

fset_A = frozenset([1, 2, 3, 4])
fset_B = frozenset([3, 4, 5, 6])

print("A ∪ B (union):", fset_A | fset_B)
print("A ∩ B (intersection):", fset_A & fset_B)
print("A - B (difference):", fset_A - fset_B)
print("B - A:", fset_B - fset_A)

print("-" * 50)


# ===========================================================
# Rank 4 — Advanced
# Using frozenset as a DICTIONARY KEY (unique ability!)
# ===========================================================

print("Rank 4 — Advanced")

# Sets cannot be dictionary keys—but frozenset can!
student_skills = {
    frozenset(["Python", "Linux"]): "Peyman",
    frozenset(["Teaching", "English"]): "Arlette",
}

for skills, student in student_skills.items():
    print(f"{student} has skills:", list(skills))

# Real-world example: unique combinations
favorite_pairs = {
    frozenset(["Red", "Black"]): "Color Combo A",
    frozenset(["Math", "Python"]): "Study Combo B",
}

print(favorite_pairs)

print("-" * 50)


# ===========================================================
# Rank 5 — Professional
# Immutable configuration & caching pattern using frozenset
# ===========================================================

def course_recommendation(user_courses: frozenset) -> str:
    """
    Returns a recommendation based on immutable set of courses.
    Demonstrates real production-level frozenset usage for caching.
    """

    advanced_path = frozenset(["Python", "Linux", "Networking"])
    data_science_path = frozenset(["Python", "Math"])

    if user_courses >= advanced_path:
        return "Recommended Track: Advanced Systems Engineering"
    if user_courses >= data_science_path:
        return "Recommended Track: Data Science Foundations"

    return "Recommended Track: Beginner Programming"


print("Rank 5 — Professional")

pey_courses = frozenset(["Python", "Linux", "Networking"])
result = course_recommendation(pey_courses)

print("Peyman's Recommendation:", result)

# Example with fewer skills
basic_user = course_recommendation(frozenset(["Python"]))
print("Basic user Recommendation:", basic_user)

print("-" * 50)
