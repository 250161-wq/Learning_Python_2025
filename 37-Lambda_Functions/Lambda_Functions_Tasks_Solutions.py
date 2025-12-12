"""
Lambda_Functions_Tasks_Solutions.py
Module 37 — Lambda Functions
Author: Peyman Miyandashti
Year: 2025

This file contains clean and professional solutions
for the lambda function exercises in this module.
"""

# ---------------------------------------------------------------------------
# Rank 1 — Beginner
# ---------------------------------------------------------------------------

# Task 1 Solution
add = lambda a, b: a + b
print(add(3, 7))


# Task 2 Solution
is_even = lambda x: x % 2 == 0
print(is_even(4))
print(is_even(5))


# ---------------------------------------------------------------------------
# Rank 2 — Easy
# ---------------------------------------------------------------------------

# Task 3 Solution
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)


# Task 4 Solution
values = [-5, 3, -1, 10]
positive = list(filter(lambda x: x > 0, values))
print(positive)


# ---------------------------------------------------------------------------
# Rank 3 — Intermediate
# ---------------------------------------------------------------------------

# Task 5 Solution
pairs = [("a", 3), ("b", 1), ("c", 2)]
sorted_pairs = sorted(pairs, key=lambda item: item[1])
print(sorted_pairs)


# Task 6 Solution
highest = max(pairs, key=lambda item: item[1])
print(highest)


# ---------------------------------------------------------------------------
# Rank 4 — Advanced
# ---------------------------------------------------------------------------

# Task 7 Solution
is_long = lambda s: len(s) > 5
print(is_long("Python"))
print(is_long("Code"))


# Task 8 Solution
operations = {
    "add": lambda a, b: a + b,
    "subtract": lambda a, b: a - b
}

print(operations["add"](5, 3))
print(operations["subtract"](5, 3))


# ---------------------------------------------------------------------------
# Rank 5 — Professional
# ---------------------------------------------------------------------------

# Task 9 Solution
users = [
    {"name": "Peyman", "age": 43},
    {"name": "Arlette", "age": 47},
    {"name": "John", "age": 30}
]

names = list(map(lambda u: u["name"], users))
print(names)


# Task 10 Solution
# Lambda is NOT suitable here due to complexity.
def process_numbers(numbers):
    total = 0
    for n in numbers:
        if n > 0:
            total += n
    return total

print(process_numbers([1, -2, 3, 4]))


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# These solutions show how lambdas:
# - simplify small operations
# - integrate with built-in functions
# - should be avoided for complex logic
#
# Next Step:
# Move on to the next module when ready.
