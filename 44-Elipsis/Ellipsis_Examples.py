"""
Ellipsis_Examples.py
Module 44 — Ellipsis
Author: Peyman Miyandashti
Year: 2025

This file contains clear and practical examples
showing how ellipsis (...) is used in Python.
"""

# ---------------------------------------------------------------------------
# Example 1: Ellipsis Is an Object
# ---------------------------------------------------------------------------

print(...)
print(type(...))
print(... is Ellipsis)


# ---------------------------------------------------------------------------
# Example 2: Ellipsis as a Placeholder in Functions
# ---------------------------------------------------------------------------

def not_implemented_yet():
    ...


def another_future_function():
    ...


print("Functions defined without implementation")


# ---------------------------------------------------------------------------
# Example 3: Ellipsis in Classes
# ---------------------------------------------------------------------------

class IncompleteClass:
    def method_one(self):
        ...

    def method_two(self):
        ...


print("Class with placeholder methods defined")


# ---------------------------------------------------------------------------
# Example 4: Ellipsis vs pass
# ---------------------------------------------------------------------------

def using_pass():
    pass

def using_ellipsis():
    ...


print("Both functions are valid")


# ---------------------------------------------------------------------------
# Example 5: Ellipsis in Data Structures
# ---------------------------------------------------------------------------

data = [1, 2, 3, ...]
print(data)


# ---------------------------------------------------------------------------
# Example 6: Checking for Ellipsis
# ---------------------------------------------------------------------------

def handle_value(value):
    if value is ...:
        print("Ellipsis received")
    else:
        print("Value:", value)

handle_value(...)
handle_value(10)


# ---------------------------------------------------------------------------
# Example 7: Ellipsis in Slicing (Conceptual Example)
# ---------------------------------------------------------------------------
# Used heavily in libraries like NumPy for multi-dimensional slicing.
#
# Example (conceptual):
#   array[..., 0]


# ---------------------------------------------------------------------------
# Example 8: Ellipsis in API Stubs
# ---------------------------------------------------------------------------

class APIStub:
    def connect(self):
        ...

    def disconnect(self):
        ...


print("API stub defined")


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# These examples show how ellipsis:
# - acts as a real object
# - marks intentional incompleteness
# - improves readability in stubs and APIs
#
# Next Step:
# Continue with Ellipsis_Tasks.py
