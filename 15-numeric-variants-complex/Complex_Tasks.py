"""
Module 15 — Numeric Variants: Complex Numbers
Practice Tasks

This file contains a progressive set of exercises designed to help you
practice creating, manipulating, and applying complex numbers in Python.

Work through the tasks from Rank 1 to Rank 5.
Only open the solutions file after attempting the tasks honestly.
"""

# ============================================================
# Rank 1 — Beginner
# Basic creation and reading of components.
# ============================================================

# Task 1.1
# Create a complex number 4 + 5j and print it.
#
# Write your code below:


# Task 1.2
# Create a complex number using complex(real, imag):
#     complex(7, -3)
# Print the result.
#
# Write your code below:


# Task 1.3
# Given z = 9 - 2j
# Print:
#   - the real part
#   - the imaginary part
#
# Write your code below:


# ============================================================
# Rank 2 — Easy
# Simple arithmetic with complex numbers.
# ============================================================

# Task 2.1
# Compute the sum of:
#   a = 3 + 4j
#   b = 1 - 2j
# Print the result.
#
# Write your code below:


# Task 2.2
# Compute the magnitude (abs) of:
#   z = 5 + 12j
# Print the result.
#
# Write your code below:


# Task 2.3
# Compute the result of:
#   (2 + 3j) - (7 - j)
# Print the result.
#
# Write your code below:


# ============================================================
# Rank 3 — Intermediate
# Conjugates, division, conversions.
# ============================================================

# Task 3.1
# Compute the conjugate of z = 6 - 8j and print it.
#
# Write your code below:


# Task 3.2
# Compute:
#   (4 + 2j) * (1 - 3j)
# Print the result.
#
# Write your code below:


# Task 3.3
# Compute the division:
#   (10 + 5j) / (3 - j)
# Print the result.
#
# Write your code below:


# ============================================================
# Rank 4 — Advanced
# Using cmath for angles, polar coordinates, and transformations.
# ============================================================

import cmath
import math

# Task 4.1
# Compute the phase (angle) of z = 1 + j using cmath.phase().
# Print the angle in radians.
#
# Write your code below:


# Task 4.2
# Convert z = 2 + 2j to polar coordinates using cmath.polar().
# Print the magnitude and angle.
#
# Write your code below:


# Task 4.3
# Convert magnitude = 3 and angle = π/6 (30°) back into a complex number
# using cmath.rect().
#
# Write your code below:


# ============================================================
# Rank 5 — Professional
# Real-world modeling with complex numbers.
# ============================================================

# Task 5.1
# Rotate the point 5 + 0j by 90 degrees (π/2 radians)
# using complex multiplication:
#     rotated = point * complex(cosθ, sinθ)
# Print the rotated point.
#
# Write your code below:


# Task 5.2
# Perform ONE iteration of the Mandelbrot formula:
#     z = z*z + c
# starting with:
#     z = 0 + 0j
#     c = -0.1 + 0.75j
# Print the new value of z.
#
# Write your code below:


# Task 5.3
# Complex resistor calculation (engineering example):
# Total impedance of series components is:
#     Z_total = Z1 + Z2 + Z3
#
# Given:
#     Z1 = 4 + 3j
#     Z2 = 2 - j
#     Z3 = -1 + 5j
#
# Compute Z_total and print it.
#
# Write your code below:


# End of Tasks
