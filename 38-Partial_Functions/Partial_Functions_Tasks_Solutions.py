"""
Partial_Functions_Tasks_Solutions.py
Module 38 — Partial Functions
Author: Peyman Miyandashti
Year: 2025

This file contains clean and professional solutions
for the partial function exercises in this module.
"""

from functools import partial

# ---------------------------------------------------------------------------
# Rank 1 — Beginner
# ---------------------------------------------------------------------------

# Task 1 Solution
def multiply(a, b):
    return a * b

multiply_by_10 = partial(multiply, 10)


# Task 2 Solution
print(multiply_by_10(3))
print(multiply_by_10(7))
print(multiply_by_10(12))


# ---------------------------------------------------------------------------
# Rank 2 — Easy
# ---------------------------------------------------------------------------

# Task 3 Solution
def greet(greeting, name):
    return f"{greeting}, {name}"

say_hello = partial(greet, "Hello")


# Task 4 Solution
print(say_hello("Peyman"))
print(say_hello("Arlette"))
print(say_hello("Student"))


# ---------------------------------------------------------------------------
# Rank 3 — Intermediate
# ---------------------------------------------------------------------------

# Task 5 Solution
def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)


# Task 6 Solution
numbers = [1, 2, 3, 4, 5]
squares = list(map(square, numbers))
print(squares)


# ---------------------------------------------------------------------------
# Rank 4 — Advanced
# ---------------------------------------------------------------------------

# Task 7 Solution
def calculate_total(price, tax, discount):
    return price + tax - discount

calculate_configured = partial(calculate_total, tax=5, discount=2)


# Task 8 Solution
prices = [100, 200, 350]
totals = [calculate_configured(price) for price in prices]
print(totals)


# ---------------------------------------------------------------------------
# Rank 5 — Professional
# ---------------------------------------------------------------------------

# Task 9 Solution
def log(prefix, message):
    print(f"{prefix}: {message}")

info_log = partial(log, "[INFO]")
error_log = partial(log, "[ERROR]")

info_log("Application started")
error_log("Connection failed")


# Task 10 Solution
# Partial improves readability when:
# - the same arguments are reused many times
# - the intent of the function becomes clearer
#
# A normal function is clearer when:
# - logic is complex
# - many parameters change frequently
# - behavior needs branching or loops
#
# Example of clearer normal function:

def process_order(price):
    tax = 5
    discount = 2
    return calculate_total(price, tax, discount)

print(process_order(150))


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# These solutions demonstrate:
# - clean argument reuse
# - clearer intent through partials
# - correct judgment between partial and def
#
# Next Step:
# Move on to the next module when ready.
