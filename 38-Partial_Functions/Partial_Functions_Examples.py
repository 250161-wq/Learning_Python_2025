"""
Partial_Functions_Examples.py
Module 38 — Partial Functions
Author: Peyman Miyandashti
Year: 2025

This file contains clear and practical examples
showing how partial functions are used in Python.
"""

from functools import partial

# ---------------------------------------------------------------------------
# Example 1: Basic Partial Function
# ---------------------------------------------------------------------------

def add(a, b):
    return a + b

add_five = partial(add, 5)
print(add_five(10))


# ---------------------------------------------------------------------------
# Example 2: Partial vs Lambda
# ---------------------------------------------------------------------------

add_five_lambda = lambda x: add(5, x)
print(add_five_lambda(10))


# ---------------------------------------------------------------------------
# Example 3: Fixing Keyword Arguments
# ---------------------------------------------------------------------------

def greet(greeting, name):
    return f"{greeting}, {name}"

say_hi = partial(greet, "Hi")
print(say_hi("Peyman"))


# ---------------------------------------------------------------------------
# Example 4: Multiple Fixed Arguments
# ---------------------------------------------------------------------------

def calculate(price, tax, discount):
    return price + tax - discount

calculate_with_tax = partial(calculate, tax=5, discount=2)
print(calculate_with_tax(100))


# ---------------------------------------------------------------------------
# Example 5: Partial with map()
# ---------------------------------------------------------------------------

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
numbers = [1, 2, 3, 4]
squares = list(map(square, numbers))
print(squares)


# ---------------------------------------------------------------------------
# Example 6: Partial for Configuration
# ---------------------------------------------------------------------------

def connect(host, port, secure):
    return f"Connecting to {host}:{port}, secure={secure}"

secure_connect = partial(connect, port=443, secure=True)
print(secure_connect("example.com"))


# ---------------------------------------------------------------------------
# Example 7: Chaining Partials
# ---------------------------------------------------------------------------
# Chaining partials is possible but should be used carefully.

double = partial(add, 2)
quadruple = partial(double, 2)
print(quadruple(10))


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# These examples show how partial functions:
# - reduce repeated arguments
# - improve readability
# - create specialized functions
#
# Next Step:
# Continue with Partial_Functions_Tasks.py
