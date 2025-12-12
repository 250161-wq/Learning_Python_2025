"""
Partial_Functions_Notes.py
Module 38 — Partial Functions
Author: Peyman Miyandashti
Year: 2025

This module explains partial functions in Python.
Partial functions allow pre-filling arguments of a function.
"""

from functools import partial

# ---------------------------------------------------------------------------
# 1. What Is a Partial Function?
# ---------------------------------------------------------------------------
# A partial function is a new function created by fixing
# some arguments of an existing function.


# ---------------------------------------------------------------------------
# 2. Basic Example
# ---------------------------------------------------------------------------

def multiply(a, b):
    return a * b

double = partial(multiply, 2)
print(double(5))


# ---------------------------------------------------------------------------
# 3. Partial vs Lambda
# ---------------------------------------------------------------------------

double_lambda = lambda x: multiply(2, x)
print(double_lambda(5))


# ---------------------------------------------------------------------------
# 4. Fixing Multiple Arguments
# ---------------------------------------------------------------------------

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(square(4))
print(cube(3))


# ---------------------------------------------------------------------------
# 5. Using Partial with Default Arguments
# ---------------------------------------------------------------------------

def greet(greeting, name):
    return f"{greeting}, {name}"

say_hello = partial(greet, "Hello")
print(say_hello("Peyman"))


# ---------------------------------------------------------------------------
# 6. Partial with Keyword Arguments
# ---------------------------------------------------------------------------

def connect(host, port, secure):
    return f"Connecting to {host}:{port}, secure={secure}"

secure_connect = partial(connect, port=443, secure=True)
print(secure_connect("example.com"))


# ---------------------------------------------------------------------------
# 7. When to Use Partial
# ---------------------------------------------------------------------------
# Use partial when:
# - arguments are reused often
# - clarity is improved
# - a lambda would be repetitive


# ---------------------------------------------------------------------------
# 8. Best Practices
# ---------------------------------------------------------------------------
# - Use partial for configuration-like functions
# - Keep partials simple and readable
# - Avoid overusing partials for complex logic


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# Partial functions create specialized functions cleanly.
# They improve readability and reduce duplication.
#
# Next Step:
# Continue with Partial_Functions_Examples.py
