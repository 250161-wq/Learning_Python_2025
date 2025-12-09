"""
Module 16 — Python Modules
Practice Task Solutions

This file contains the official solutions for all tasks in
Modules_Tasks.py. These examples demonstrate correct importing,
aliasing, module creation, namespace behavior, and multi-file interaction.

Only read this file after attempting the tasks on your own.
"""

# ---------------------------------------------------------------------------
# Rank 1 — Beginner
# ---------------------------------------------------------------------------

# Task 1.1
import math
print(math.sqrt(49))
print(math.pi)

# Task 1.2
from math import cos
print(cos(0))

# Task 1.3
import random
print(random.randint(1, 10))


# ---------------------------------------------------------------------------
# Rank 2 — Easy
# ---------------------------------------------------------------------------

# Task 2.1
import math as m
print(m.sqrt(16))

# Task 2.2
from math import *
print(sin(pi / 2))

# Task 2.3
# Explanation:
# Importing a module executes its top-level code immediately.
# If demo_module.py contains print("demo loaded"), it will print that
# the moment we import it.
try:
    import demo_module
except ModuleNotFoundError:
    print("demo_module.py not found — create it to test this task.")


# ---------------------------------------------------------------------------
# Rank 3 — Intermediate
# ---------------------------------------------------------------------------

# Task 3.1
# tools.py must exist in the same folder for this to work.
try:
    import tools
    print(tools.add(4, 6))
except ModuleNotFoundError:
    print("tools.py not found — create it to test Task 3.1.")

# Task 3.2
try:
    from tools import greet
    print(greet("Peyman"))
except Exception:
    print("greet() not found — ensure it is defined in tools.py.")

# Task 3.3
try:
    import tools as t
    print(t.add(10, 20))
except Exception:
    print("tools.py missing or add() not defined.")


# ---------------------------------------------------------------------------
# Rank 4 — Advanced
# ---------------------------------------------------------------------------

import sys
import importlib

# Task 4.1
print("First 5 sys.path entries:")
for p in sys.path[:5]:
    print(" ", p)

# Task 4.2
# Observation:
# If name_test.py prints:
#     print("__name__ inside module:", __name__)
#
# Then when importing:
try:
    import name_test
except ModuleNotFoundError:
    print("name_test.py not found — create it to test Task 4.2.")

# Task 4.3
# After modifying tools.py, reload it:
try:
    import tools
    importlib.reload(tools)
    print("Reloaded tools module successfully.")
except Exception:
    print("Could not reload tools.py — ensure it exists.")


# ---------------------------------------------------------------------------
# Rank 5 — Professional
# ---------------------------------------------------------------------------

# Task 5.1
try:
    import math_ops
    import text_ops

    print(math_ops.square(5))
    print(math_ops.cube(3))
    print(text_ops.shout("python modules are awesome"))
except ModuleNotFoundError:
    print("math_ops.py or text_ops.py not found — create them to test Task 5.1.")


# Task 5.2
# Example solution (package must exist physically):
#
# from utils.numbers import double
# from utils.strings import emphasize
#
# print(double(10))
# print(emphasize("modules rock"))
#
# (Cannot run here unless the package exists)


# Task 5.3
try:
    import calculator
    print(calculator.add(5, 2))
    print(calculator.subtract(10, 3))
    print(calculator.multiply(4, 6))
    print(calculator.divide(20, 4))
except ModuleNotFoundError:
    print("calculator.py not found — create it to test Task 5.3.")


# End of Solutions
