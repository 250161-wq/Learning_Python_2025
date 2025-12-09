"""
Module 19 — Float (Basic Data Types)
Professional Notes

This file explains how floating-point numbers (floats) work in Python.
Use it as a reference while you practice with the exercises.
"""

# ---------------------------------------------------------------------------
# 1. What is a float?
# ---------------------------------------------------------------------------
# A float (floating-point number) represents a real number with decimals.
# Examples:
#   3.14      -> pi approximation
#   -0.5      -> negative decimal
#   100.0     -> integer value stored as a float
#
# In Python, any number with a decimal point is a float.

price = 19.99
temperature = -3.5
pi_approx = 3.14

print("Price:", price)
print("Temperature:", temperature)
print("Pi (approx):", pi_approx)
print()


# ---------------------------------------------------------------------------
# 2. Creating float values (literals)
# ---------------------------------------------------------------------------
# You can create floats in different ways:
#
# 1) Standard decimal notation:
#    1.0, 0.25, -10.75
#
# 2) Scientific notation (very large or very small numbers):
#    1.5e3  -> 1.5 * 10^3  = 1500.0
#    2e-2   -> 2 * 10^-2   = 0.02
#
#    The letter "e" means "times ten to the power of".

standard_float = 0.25
large_float = 1.5e3       # 1500.0
small_float = 2e-2        # 0.02

print("Standard float:", standard_float)
print("Large (scientific):", large_float)
print("Small (scientific):", small_float)
print()


# ---------------------------------------------------------------------------
# 3. Basic arithmetic with floats
# ---------------------------------------------------------------------------
# Floats support the usual arithmetic operators:
#   +  addition
#   -  subtraction
#   *  multiplication
#   /  true division (always returns a float)
#   ** exponent (power)
#
# Note: The / operator returns a float even if the result is a “whole” number.

a = 10.0
b = 3.0

sum_result = a + b      # 13.0
diff_result = a - b     # 7.0
prod_result = a * b     # 30.0
div_result = a / b      # 3.333...
power_result = a ** b   # 10.0 ** 3.0 = 1000.0

print("a + b =", sum_result)
print("a - b =", diff_result)
print("a * b =", prod_result)
print("a / b =", div_result)
print("a ** b =", power_result)
print()


# ---------------------------------------------------------------------------
# 4. Division operators: / vs // and %
# ---------------------------------------------------------------------------
# /  -> true division, always returns a float
# // -> floor division, “rounds down” to the nearest integer (still can be float)
# %  -> modulo, remainder of the division

x = 7.0
y = 2.0

true_div = x / y      # 3.5
floor_div = x // y    # 3.0
remainder = x % y     # 1.0

print("True division 7.0 / 2.0 =", true_div)
print("Floor division 7.0 // 2.0 =", floor_div)
print("Remainder 7.0 % 2.0 =", remainder)
print()


# ---------------------------------------------------------------------------
# 5. Converting between int and float
# ---------------------------------------------------------------------------
# Sometimes we need to convert types explicitly:
#
#   float(x)  -> convert to float
#   int(x)    -> convert to int (truncates decimals toward zero)
#
# Example:
#   int(3.99) -> 3
#   float(5)  -> 5.0

int_value = 7
float_value = 3.99

as_float = float(int_value)   # 7.0
as_int = int(float_value)     # 3 (decimals are removed, not rounded)

print("Original int:", int_value, "-> as float:", as_float)
print("Original float:", float_value, "-> as int:", as_int)
print()


# ---------------------------------------------------------------------------
# 6. Precision and rounding issues
# ---------------------------------------------------------------------------
# Floats are stored in binary (base 2), not decimal (base 10).
# This can cause small precision errors.
#
# Example: 0.1 + 0.2 is not exactly 0.3 inside the computer.

x = 0.1 + 0.2
print("0.1 + 0.2 =", x)

# To display a "clean" result, we often round or format:
print("Rounded to 2 decimals:", round(x, 2))
print()


# ---------------------------------------------------------------------------
# 7. Rounding and formatting floats
# ---------------------------------------------------------------------------
# round(number, ndigits) -> returns a rounded value
# f-strings -> allow formatted output with specific decimal places
#
# Format examples (f-strings):
#   f"{value:.2f}"  -> 2 decimal places
#   f"{value:.1f}"  -> 1 decimal place

value = 3.1415926535

rounded_2 = round(value, 2)
rounded_4 = round(value, 4)

print("Original value:", value)
print("Rounded (2 decimals):", rounded_2)
print("Rounded (4 decimals):", rounded_4)
print("Formatted with 2 decimals:", f"{value:.2f}")
print("Formatted with 1 decimal:", f"{value:.1f}")
print()


# ---------------------------------------------------------------------------
# 8. Comparisons with floats
# ---------------------------------------------------------------------------
# Because of precision issues, direct equality == can be unreliable:
#
# 0.1 + 0.2 == 0.3   # might be False!
#
# A common pattern is to compare with a tolerance (epsilon).

a = 0.1 + 0.2
b = 0.3

print("Direct comparison (a == b):", a == b)

epsilon = 1e-9  # acceptable error tolerance
are_equal = abs(a - b) < epsilon

print("Comparison with tolerance:", are_equal)
print()


# ---------------------------------------------------------------------------
# 9. Using the math module (common float operations)
# ---------------------------------------------------------------------------
# The math module provides useful functions for working with floats:
#   math.sqrt(x)   -> square root
#   math.sin(x)    -> sine (x in radians)
#   math.cos(x)    -> cosine
#   math.floor(x)  -> round down
#   math.ceil(x)   -> round up

import math

number = 16.0

print("Square root of 16.0:", math.sqrt(number))
print("cos(0.0):", math.cos(0.0))
print("floor(3.9):", math.floor(3.9))
print("ceil(3.1):", math.ceil(3.1))
print()


# ---------------------------------------------------------------------------
# 10. Common mistakes with floats
# ---------------------------------------------------------------------------
# ❌ Expecting exact decimal results:
#    - Many decimal values cannot be represented exactly.
#
# ❌ Using == for float comparisons:
#    - Prefer a tolerance approach: abs(a - b) < small_number
#
# ❌ Forgetting that / always returns a float:
#    - Example: 5 / 2 -> 2.5 (float), not 2
#
# ✔ Good practice: use floor division // only when you really need
#   an integer-like result (e.g., counting pages, groups, etc.)


# ---------------------------------------------------------------------------
# 11. Professional best practices
# ---------------------------------------------------------------------------
# ✔ Be careful with equality checks; use tolerances when needed.
# ✔ Use round() or formatted strings to present floats to users.
# ✔ Keep numeric calculations simple and clear.
# ✔ Document units (meters, dollars, seconds, etc.) in variable names or comments.
# ✔ Prefer int for counters and indexes; use float when decimals really matter.


# ---------------------------------------------------------------------------
# 12. Summary
# ---------------------------------------------------------------------------
# In this module, I learned how to:
# - Create float values using decimal and scientific notation.
# - Use arithmetic operators with floats (/, //, %, **).
# - Convert between int and float safely.
# - Understand precision issues and why 0.1 + 0.2 is not exactly 0.3.
# - Use round() and f-strings to control decimal output.
# - Compare floats using a tolerance instead of strict equality.
# - Use common functions from the math module with float values.
#
# End of Float_Notes.py
