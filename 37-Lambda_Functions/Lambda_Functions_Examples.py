"""
Lambda_Functions_Examples.py
Module 37 — Lambda Functions
Author: Peyman Miyandashti
Year: 2025

This file contains clear and practical examples
showing how lambda functions are used in Python.
"""

# ---------------------------------------------------------------------------
# Example 1: Basic Lambda Function
# ---------------------------------------------------------------------------

add = lambda a, b: a + b
print(add(2, 3))


# ---------------------------------------------------------------------------
# Example 2: Lambda with One Argument
# ---------------------------------------------------------------------------

square = lambda x: x ** 2
print(square(5))


# ---------------------------------------------------------------------------
# Example 3: Lambda with map()
# ---------------------------------------------------------------------------

numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)


# ---------------------------------------------------------------------------
# Example 4: Lambda with filter()
# ---------------------------------------------------------------------------

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)


# ---------------------------------------------------------------------------
# Example 5: Lambda with sorted()
# ---------------------------------------------------------------------------

students = [
    ("Peyman", 85),
    ("Arlette", 95),
    ("John", 78)
]

sorted_students = sorted(students, key=lambda item: item[1])
print(sorted_students)


# ---------------------------------------------------------------------------
# Example 6: Lambda as Key in min() and max()
# ---------------------------------------------------------------------------

print(min(students, key=lambda item: item[1]))
print(max(students, key=lambda item: item[1]))


# ---------------------------------------------------------------------------
# Example 7: Replacing a Small Function with Lambda
# ---------------------------------------------------------------------------

def is_positive(x):
    return x > 0

is_positive_lambda = lambda x: x > 0

print(is_positive(10))
print(is_positive_lambda(10))


# ---------------------------------------------------------------------------
# Example 8: Lambdas Inside List Comprehensions
# ---------------------------------------------------------------------------
# Lambdas are often unnecessary here,
# list comprehensions are clearer.

squares = [(lambda x: x ** 2)(x) for x in range(5)]
print(squares)


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# These examples show how lambdas:
# - reduce boilerplate
# - work well with built-in functions
# - should remain simple and readable
#
# Next Step:
# Continue with Lambda_Functions_Tasks.py
