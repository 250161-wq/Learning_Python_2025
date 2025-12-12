"""
Decorators_Notes.py
Module 39 — Decorators
Author: Peyman Miyandashti
Year: 2025

This module explains decorators in Python.
Decorators modify function behavior without changing the function itself.
"""

# ---------------------------------------------------------------------------
# 1. Functions Are Objects
# ---------------------------------------------------------------------------
# In Python, functions can be:
# - assigned to variables
# - passed as arguments
# - returned from other functions

def greet():
    return "Hello"

say_hello = greet
print(say_hello())


# ---------------------------------------------------------------------------
# 2. Functions Inside Functions
# ---------------------------------------------------------------------------

def outer():
    def inner():
        return "Inside"
    return inner

func = outer()
print(func())


# ---------------------------------------------------------------------------
# 3. Basic Decorator Structure
# ---------------------------------------------------------------------------
# A decorator is a function that:
# - takes a function as input
# - returns a new function

def my_decorator(func):
    def wrapper():
        print("Before function call")
        result = func()
        print("After function call")
        return result
    return wrapper


# ---------------------------------------------------------------------------
# 4. Applying a Decorator Manually
# ---------------------------------------------------------------------------

def say_hi():
    print("Hi")

decorated_say_hi = my_decorator(say_hi)
decorated_say_hi()


# ---------------------------------------------------------------------------
# 5. Using @ Syntax
# ---------------------------------------------------------------------------

@my_decorator
def say_hello_again():
    print("Hello again")

say_hello_again()


# ---------------------------------------------------------------------------
# 6. Decorators with Arguments
# ---------------------------------------------------------------------------
# Use *args and **kwargs to support any function signature.

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print("Calling:", func.__name__)
        return func(*args, **kwargs)
    return wrapper


@log_decorator
def add(a, b):
    return a + b

print(add(3, 4))


# ---------------------------------------------------------------------------
# 7. Preserving Function Metadata
# ---------------------------------------------------------------------------
# Use functools.wraps to preserve name and docstring.

from functools import wraps

def safe_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


# ---------------------------------------------------------------------------
# 8. When to Use Decorators
# ---------------------------------------------------------------------------
# Use decorators when:
# - behavior is cross-cutting
# - logic is reused across functions
# - separation of concerns matters


# ---------------------------------------------------------------------------
# 9. When NOT to Use Decorators
# ---------------------------------------------------------------------------
# Avoid decorators when:
# - logic is simple and local
# - readability is reduced
# - behavior becomes hidden or confusing


# ---------------------------------------------------------------------------
# 10. Best Practices
# ---------------------------------------------------------------------------
# - Keep decorators simple
# - Always use functools.wraps
# - Avoid deep decorator stacking
# - Document decorator behavior clearly


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# Decorators are one of Python’s most powerful features.
# They enable clean, reusable, and professional design patterns.
#
# Next Step:
# Continue with Decorators_Examples.py
