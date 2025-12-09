"""
Module 13 — Advanced Loops
Master-level practice with Python loops, including:
- for loops
- while loops
- enumerate
- zip
- nested loops
- loop else-blocks
- iterating dicts, sets, tuples
- real-world loop logic

Ranking:
- Rank 1 -> Beginner Advanced: basic for/while patterns
- Rank 2 -> Easy Advanced: enumerate, zip, break/continue
- Rank 3 -> Intermediate: nested loops + pattern logic
- Rank 4 -> Advanced: iterating dicts, sets, tuples professionally
- Rank 5 -> Professional: real-world algorithms with loops

Author: Peyman Miyandashti
Student at UPBC — IT Engineering & Digital Innovation
Year: 2025
"""

# Personal data used for examples
pey_scores = [9.7, 9.4, 9.2, 9.8]
pey_courses = ["Python", "Networking", "Math", "Linux"]
study_hours = [2.5, 4.0, 3.5, 5.2, 6.0]
names = ["Peyman", "Arlette", "Ali", "Sara"]
ages = [43, 47, 22, 19]

# ===========================================================
# Rank 1 — Beginner Advanced
# Basic for + while loop patterns
# ===========================================================

print("Rank 1 — Beginner Advanced")

for score in pey_scores:
    print("Score:", score)

count = 0
while count < 3:
    print("Counting:", count)
    count += 1

print("-" * 50)


# ===========================================================
# Rank 2 — Easy Advanced
# enumerate(), zip(), break, continue
# ===========================================================

print("Rank 2 — Easy Advanced")

# enumerate gives index + value
for index, course in enumerate(pey_courses, start=1):
    print(f"{index}. {course}")

# zip pairs elements from two lists
print("\nNames and ages:")
for name, age in zip(names, ages):
    print(name, "-", age)

# break example (stop early)
print("\nSearching for 'Math':")
for course in pey_courses:
    if course == "Math":
        print("Found Math!")
        break

# continue example (skip)
print("\nSkip GPA < 9.5:")
for score in pey_scores:
    if score < 9.5:
        continue
    print("High score:", score)

print("-" * 50)


# ===========================================================
# Rank 3 — Intermediate
# Nested loops + pattern generation
# ===========================================================

print("Rank 3 — Intermediate")

# Simple multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
    print("---")

# Combining two lists deeply:
for name in names:
    for course in pey_courses:
        print(f"{name} is reviewing {course}")

print("-" * 50)


# ===========================================================
# Rank 4 — Advanced
# Looping through dicts, sets, tuples + loop else-blocks
# ===========================================================

print("Rank 4 — Advanced")

pey_profile = {
    "name": "Peyman",
    "age": 43,
    "city": "Mexicali",
    "favorite_color": "Red",
}

print("\nDictionary loop:")
for key, value in pey_profile.items():
    print(f"{key}: {value}")

unique_set = {"Python", "Math", "Python", "Linux"}
print("\nSet loop (unique values):")
for item in unique_set:
    print(item)

tuple_data = ("Peyman", 43, "UPBC")
print("\nTuple loop:")
for element in tuple_data:
    print(element)

# Loop else-block → runs ONLY if no break occurs
print("\nSearching with loop else:")
numbers = [10, 20, 30, 40]
for n in numbers:
    if n == 99:
        print("Found 99!")
        break
else:
    print("99 NOT found (loop completed normally)")

print("-" * 50)


# ===========================================================
# Rank 5 — Professional
# Real-world loop algorithms: filtering, aggregation, detection
# ===========================================================

print("Rank 5 — Professional")

def find_first_passing(scores, minimum=9.5):
    """
    Returns first score >= minimum using loops.
    If none found → returns None.
    """
    for score in scores:
        if score >= minimum:
            return score
    return None

def calculate_average(hours):
    """
    Loop-based average calculation (manual).
    """
    total = 0
    count = 0
    for h in hours:
        total += h
        count += 1
    return total / count

def find_duplicates(items):
    """
    Detect duplicates using a set inside a loop.
    """
    seen = set()
    duplicates = set()
    for item in items:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return duplicates

print("First passing score:", find_first_passing(pey_scores))
print("Average study hours:", calculate_average(study_hours))
print("Duplicate names:", find_duplicates(["Ali", "Sara", "Ali", "Peyman", "Sara"]))

print("-" * 50)
