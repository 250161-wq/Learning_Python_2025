"""
Lambda_Functions_Notes.py
Module 37 — Lambda Functions
Author: Peyman Miyandashti
Year: 2025

This module explains lambda functions in Python.
Lambda functions are small, anonymous functions
written in a single expression.
"""

# ---------------------------------------------------------------------------
# 1. What Is a Lambda Function?
# ---------------------------------------------------------------------------
# A lambda function is a short function defined without a name.
# Syntax:
#   lambda arguments: expression


# ---------------------------------------------------------------------------
# 2. Basic Lambda Example
# ---------------------------------------------------------------------------

add = lambda a, b: a + b
print(add(3, 5))


# ---------------------------------------------------------------------------
# 3. Lambda vs Regular Function
# ---------------------------------------------------------------------------

def add_def(a, b):
    return a + b

print(add_def(3, 5))


# ---------------------------------------------------------------------------
# 4. Single-Argument Lambda
# ---------------------------------------------------------------------------

square = lambda x: x ** 2
print(square(4))


# ---------------------------------------------------------------------------
# 5. Lambdas Are Expressions
# ---------------------------------------------------------------------------
# Lambda functions can only contain expressions,
# not statements like loops or assignments.


# ---------------------------------------------------------------------------
# 6. Using Lambdas with map()
# ---------------------------------------------------------------------------

numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)


# ---------------------------------------------------------------------------
# 7. Using Lambdas with filter()
# ---------------------------------------------------------------------------

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)


# ---------------------------------------------------------------------------
# 8. Using Lambdas with sorted()
# ---------------------------------------------------------------------------

pairs = [(1, 3), (4, 1), (2, 2)]
sorted_pairs = sorted(pairs, key=lambda item: item[1])
print(sorted_pairs)


# ---------------------------------------------------------------------------
# 9. When Not to Use Lambda
# ---------------------------------------------------------------------------
# Do NOT use lambda when:
# - logic is complex
# - readability suffers
# - multiple steps are required
#
# Use def instead.


# ---------------------------------------------------------------------------
# 10. Best Practices
# ---------------------------------------------------------------------------
# - Keep lambdas short and readable
# - Use lambdas for simple transformations
# - Prefer def for complex logic
# - Avoid nesting lambdas


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# Lambda functions are a useful tool for concise code.
# Used correctly, they improve clarity instead of reducing it.
#
# Next Step:
# Continue with Lambda_Functions_Examples.py
