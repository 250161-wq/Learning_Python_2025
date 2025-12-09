"""
Module 16 — Python Modules
Practice Tasks

This file contains a structured set of exercises to help you practice
importing modules, creating your own modules, understanding namespaces,
and using Python's built-in libraries.

Work through the tasks from Rank 1 to Rank 5.
Only open the solutions file after attempting the tasks honestly.
"""


# ============================================================
# Rank 1 — Beginner
# Basic imports and using built-in modules.
# ============================================================

# Task 1.1
# Import the math module and print:
#   - the square root of 49
#   - the value of pi
#
# Write your code below:


# Task 1.2
# From the math module, import only the "cos" function.
# Print cos(0).
#
# Write your code below:


# Task 1.3
# Import the random module and print a random integer from 1 to 10.
#
# Write your code below:



# ============================================================
# Rank 2 — Easy
# Aliasing, wildcard imports, and namespace behavior.
# ============================================================

# Task 2.1
# Import the math module with an alias "m".
# Print m.sqrt(16).
#
# Write your code below:


# Task 2.2
# Use "from math import *" and print sin(pi/2).
# (Note: This form is not recommended in real code.)
#
# Write your code below:


# Task 2.3
# Demonstrate that importing a module runs its top-level code.
# (Hint: Create a small module file named "demo_module.py"
#        with a print() statement inside it, then import it here.)
#
# Write your explanation as a comment and import demo_module below:


# ============================================================
# Rank 3 — Intermediate
# Creating and importing your own modules.
# ============================================================

# Task 3.1
# Create a module file called tools.py containing:
#   def add(a, b):
#       return a + b
#
# Import the module here and print tools.add(4, 6).
#
# Write your code below:


# Task 3.2
# Modify tools.py to also include:
#   def greet(name):
#       return f"Hello, {name}!"
#
# Import ONLY greet() here and print greet("Peyman").
#
# Write your code below:


# Task 3.3
# Use "import tools as t" and print t.add(10, 20).
#
# Write your code below:



# ============================================================
# Rank 4 — Advanced
# Understanding module search paths, __name__, and reload behavior.
# ============================================================

import sys
import importlib

# Task 4.1
# Print the first 5 entries of sys.path to see where Python searches for modules.
#
# Write your code below:


# Task 4.2
# Create a module named name_test.py containing:
#   print("__name__ inside module:", __name__)
#
# Import it here and observe what gets printed.
#
# Write your observation as a comment and import the module below:


# Task 4.3
# Modify your tools.py file while the program is running and then use:
#   importlib.reload(tools)
# to reload the updated version.
#
# Write your code below:



# ============================================================
# Rank 5 — Professional
# Building and using multi-file projects.
# ============================================================

# Task 5.1
# Create a small project with:
#
#   math_ops.py:
#       def square(x): return x * x
#       def cube(x): return x * x * x
#
#   text_ops.py:
#       def shout(msg): return msg.upper() + "!"
#
# Import both modules here and:
#   - Print square(5)
#   - Print cube(3)
#   - Print shout("python modules are awesome")
#
# Write your code below:


# Task 5.2
# Create a package structure:
#
#   utils/
#       __init__.py
#       numbers.py
#       strings.py
#
# numbers.py:
#     def double(x): return x * 2
#
# strings.py:
#     def emphasize(msg): return msg + "!!!"
#
# Import both modules from the package and call:
#   - double(10)
#   - emphasize("modules rock")
#
# Write your code below as comments + import statements (actual package must exist):


# Task 5.3
# Build a "calculator" module with:
#   add(), subtract(), multiply(), divide()
#
# Import it and test all four functions with at least one example each.
#
# Write your code below:


# End of Tasks
