"""
Module 16 — Python Modules
Professional Notes

A module in Python is simply a file containing Python code. Modules allow
us to organize code into reusable units, improve maintainability, avoid
repetition, and structure real-world software into multiple files.

This file explains how modules work, how to import them, and the best
practices for writing professional module-based programs.
"""

# ---------------------------------------------------------------------------
# 1. What Is a Module?
# ---------------------------------------------------------------------------
# Any Python file with a .py extension is a module.
#
# Examples:
#   math.py
#   utilities.py
#   myproject/helpers.py
#
# When you import a module, Python executes the code inside the file once
# and makes its functions, classes, and variables available to other files.


# ---------------------------------------------------------------------------
# 2. Importing Modules
# ---------------------------------------------------------------------------
# The simplest import:
import math

print("Square root:", math.sqrt(16))

# Importing a specific name:
from math import pi
print("PI =", pi)

# Importing multiple names:
from math import sin, cos, tan

# Importing with an alias:
import math as m
print("cos(0) =", m.cos(0))


# ---------------------------------------------------------------------------
# 3. Creating Your Own Module
# ---------------------------------------------------------------------------
# Suppose you create a file named:
#
#   calculator.py
#
# containing:
#   def add(a, b):
#       return a + b
#
# Then, in another file, you can do:
#
#   import calculator
#   print(calculator.add(3, 5))
#
# Or import the specific function:
#
#   from calculator import add
#   print(add(3, 5))


# ---------------------------------------------------------------------------
# 4. Where Python Looks for Modules (Import Search Path)
# ---------------------------------------------------------------------------
# Python searches for modules in the following order:
#
# 1. The current working directory
# 2. The directories listed in the environment variable PYTHONPATH
# 3. The system's site-packages directory (installed libraries)
#
# You can check the search path using:

import sys
print("Python module search path:", sys.path)


# ---------------------------------------------------------------------------
# 5. Reloading Modules
# ---------------------------------------------------------------------------
# A module executes only once per program execution.
# If you modify the module during runtime and want to reload it:

import importlib
import calculator_example_module as calc  # hypothetical example module

# Reload the module:
importlib.reload(calc)


# ---------------------------------------------------------------------------
# 6. The __name__ Special Variable
# ---------------------------------------------------------------------------
# Every Python module has a built-in variable called __name__.
# It indicates whether the module is being run directly or imported.
#
# If the file is executed as a script:
#       __name__ == "__main__"
#
# If imported:
#       __name__ == "module_name"
#
# Typical pattern in modules:

def demo_function():
    print("Demo function executed.")

if __name__ == "__main__":
    print("This module is being run directly.")
    demo_function()
else:
    print("This module was imported.")


# ---------------------------------------------------------------------------
# 7. Built-in Modules
# ---------------------------------------------------------------------------
# Python comes with many standard modules:
#
#   random    → random numbers
#   datetime  → date & time utilities
#   os        → interacting with the operating system
#   sys       → interpreter and environment info
#   statistics→ math statistics tools
#
# Example:

import random
print("Random number:", random.randint(1, 10))


# ---------------------------------------------------------------------------
# 8. Best Practices for Writing Modules
# ---------------------------------------------------------------------------
# ✔ Use clear and descriptive module names
# ✔ Group related functions into the same module
# ✔ Keep modules focused (single responsibility)
# ✔ Avoid circular imports (A imports B, B imports A)
# ✔ Use __all__ to define what should be exported (optional)
# ✔ Add docstrings at the top of each module
# ✔ Use __name__ == "__main__" for testing


# ---------------------------------------------------------------------------
# 9. Common Mistakes
# ---------------------------------------------------------------------------
# ❌ Naming your file the same as a built-in module (e.g., math.py)
# ❌ Forgetting that imports run the code inside the module
# ❌ Circular imports causing errors or unexpected behavior
# ❌ Using wildcard imports too often:
#       from module import *
#   (This can make code harder to read.)

# ✔ Prefer explicit imports:
#     from module import function


# ---------------------------------------------------------------------------
# 10. Summary
# ---------------------------------------------------------------------------
# In this module, I learned:
# - What modules are and how Python loads them
# - The different ways to import modules and names
# - How module search paths work
# - How to write my own reusable modules
# - How __name__ helps separate import-time behavior from script execution
# - Best practices for clean, maintainable module design
#
# End of Notes
