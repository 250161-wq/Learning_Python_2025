"""
Ellipsis_Notes.py
Module 44 — Ellipsis
Author: Peyman Miyandashti
Year: 2025

This module explains the ellipsis object (...) in Python.
Ellipsis is a built-in singleton used as a placeholder
and in advanced slicing contexts.
"""

# ---------------------------------------------------------------------------
# 1. What Is Ellipsis?
# ---------------------------------------------------------------------------
# Ellipsis is a built-in object.
# It can be written as:
#   ...
# or
#   Ellipsis

print(...)
print(Ellipsis)
print(... is Ellipsis)


# ---------------------------------------------------------------------------
# 2. Ellipsis as a Placeholder
# ---------------------------------------------------------------------------
# Ellipsis is often used where code is intentionally incomplete.

def future_function():
    ...


class FutureClass:
    def method(self):
        ...


# ---------------------------------------------------------------------------
# 3. Ellipsis vs pass
# ---------------------------------------------------------------------------
# pass does nothing.
# ... expresses intentional omission or future implementation.


# ---------------------------------------------------------------------------
# 4. Ellipsis in Data Structures
# ---------------------------------------------------------------------------

data = [1, 2, 3, ...]
print(data)


# ---------------------------------------------------------------------------
# 5. Ellipsis in Slicing (Conceptual)
# ---------------------------------------------------------------------------
# Ellipsis is used in multi-dimensional slicing
# to mean "fill in the rest of the dimensions".

# Example concept:
# array[..., 0]


# ---------------------------------------------------------------------------
# 6. Ellipsis as an Argument
# ---------------------------------------------------------------------------
# Ellipsis can be passed and checked like any object.

def process(value):
    if value is ...:
        print("Ellipsis received")

process(...)


# ---------------------------------------------------------------------------
# 7. Ellipsis in APIs and Stubs
# ---------------------------------------------------------------------------
# Often used in library stubs to indicate missing implementation.


# ---------------------------------------------------------------------------
# 8. Common Mistakes
# ---------------------------------------------------------------------------
# - Using ellipsis accidentally instead of pass
# - Assuming ellipsis executes logic (it does not)
# - Overusing ellipsis where real code is required


# ---------------------------------------------------------------------------
# 9. Best Practices
# ---------------------------------------------------------------------------
# - Use ellipsis to signal intentional incompleteness
# - Prefer ellipsis over pass in stubs
# - Keep usage explicit and readable


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# Ellipsis is a real object, not just three dots.
# It improves readability when used intentionally.
#
# Next Step:
# Continue with Ellipsis_Examples.py
