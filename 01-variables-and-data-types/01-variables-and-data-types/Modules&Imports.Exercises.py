"""
Module 14 — Modules & Imports
Professional practice with:
- import statements
- importing functions from other modules
- using standard library modules
- alias imports
- custom module creation
- best practices for reusable Python code

Ranking:
- Rank 1 -> Beginner: basic imports and using built-in modules.
- Rank 2 -> Easy: alias imports, selective imports.
- Rank 3 -> Intermediate: importing your OWN modules.
- Rank 4 -> Advanced: package folders + __init__.py structure.
- Rank 5 -> Professional: real project architecture + modular design.

Author: Peyman Miyandashti
Student at UPBC — IT Engineering & Digital Innovation
Year: 2025
"""

# ===========================================================
# Rank 1 — Beginner
# Basic imports from the Python Standard Library
# ===========================================================

print("Rank 1 — Beginner")

import math
import random

number = 11

print("Square root of 11:", math.sqrt(number))
print("Random number (0–1):", random.random())

print("-" * 50)


# ===========================================================
# Rank 2 — Easy
# Alias imports + FROM imports
# ===========================================================

print("Rank 2 — Easy")

import math as m
from random import randint

print("Cosine of 43 degrees:", m.cos(43))
print("Random int between 1–100:", randint(1, 100))

print("-" * 50)


# ===========================================================
# Rank 3 — Intermediate
# Importing **your own modules**
# ===========================================================

print("Rank 3 — Intermediate")

# Example: Suppose you have a file in the same folder:
#   utils.py
# Containing:
#   def greet(name):
#       return f"Hello {name}, welcome back!"

# We simulate it here using inline definition:
def greet(name):
    return f"Hello {name}, welcome back!"

# Now “use it as imported”
print(greet("Peyman"))

# Typical project layout example:
# from utils import greet
# from helpers.calculations import add_numbers

print("-" * 50)


# ===========================================================
# Rank 4 — Advanced
# Creating a PACKAGE with __init__.py and submodules
# ===========================================================

print("Rank 4 — Advanced")

# A real package structure looks like this:
#
# my_project/
# ├── data/
# │   ├── __init__.py
# │   ├── loader.py
# │   └── parser.py
# ├── core/
# │   ├── __init__.py
# │   ├── user.py
# │   └── engine.py
# ├── utils/
# │   ├── __init__.py
# │   └── math_tools.py
# └── app.py
#
# In app.py you might write:
#
# from utils.math_tools import average
# from core.user import User
#
# This allows PRO-level modularity.

print("Example package architecture printed above.")
print("-" * 50)


# ===========================================================
# Rank 5 — Professional
# Real-world modular code: reusable modules with imports
# ===========================================================

print("Rank 5 — Professional")

# Example of a modular architecture:

# Imagine this file structure:
#
# ── project/
#    ├── math_ops.py
#    ├── student_tools.py
#    └── main.py
#
# math_ops.py:
#     def compute_bmi(weight, height_cm):
#         return weight / (height_cm/100)**2
#
# student_tools.py:
#     from math_ops import compute_bmi
#
#     def build_student_record(name, scores):
#         avg = sum(scores) / len(scores)
#         return {
#             "name": name,
#             "average": avg
#         }
#
# main.py:
#     from student_tools import build_student_record
#     from math_ops import compute_bmi
#
#     bmi = compute_bmi(72.5, 187.3)
#     record = build_student_record("Peyman", [9.7, 9.4, 9.2])
#
#     print(bmi, record)

# Simulated example below:

def compute_bmi(weight, height_cm):
    return weight / (height_cm/100)**2

def build_student_record(name, scores):
    avg = sum(scores) / len(scores)
    return {
        "name": name,
        "average": round(avg, 2)
    }

# “Main program” section (as if importing these)
pey_bmi = compute_bmi(72.5, 187.3)
pey_record = build_student_record("Peyman Miyandashti", [9.7, 9.4, 9.2, 9.8])

print("BMI:", round(pey_bmi, 2))
print("Student Record:", pey_record)

print("-" * 50)
