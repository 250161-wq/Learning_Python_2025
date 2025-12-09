"""
Module 19 — Floats: Practice Tasks
----------------------------------

This file contains hands-on exercises for the float (floating-point)
data type. The tasks progress through five difficulty levels, from
simple decimal operations to more realistic professional calculations.

How to use this file:
- Work from Rank 1 to Rank 5.
- Write your answers directly below each task.
- Do NOT open Float_Tasks_Solutions.py until you truly try your best.
"""


# ============================================================================
# Rank 1 — Beginner
# Simple warm-ups with float values.
# ============================================================================

# Task 1.1
# Create a float variable named "temperature" with value 36.5
# and print:
#   Current temperature: 36.5°C
#
# Your code below:



# Task 1.2
# Create two floats:
#   a = 5.5
#   b = 2.0
# Print:
#   Sum:
#   Difference:
#   Product:
#   Division:
#
# Your code below:



# Task 1.3
# Convert these strings into floats:
#   "3.14", "10", "-0.5"
# Print each converted value AND its type.
#
# Your code below:




# ============================================================================
# Rank 2 — Easy
# Combine floats with simple logic and calculations.
# ============================================================================

# Task 2.1
# Given:
#   price = 12.5
#   quantity = 4
# Calculate and print:
#   Total cost: <value>
#
# Your code below:



# Task 2.2
# Ask the user to input two decimal numbers (as strings), convert them
# to floats, compute their average, and print it.
#
# Example:
#   Input:  3.0 and 5.0
#   Output: Average: 4.0
#
# Your code below:



# Task 2.3
# Given the list:
#   numbers = [1.5, 2.0, 3.25, 4.75]
# Calculate:
#   - Total sum
#   - Average
# Print both.
#
# Your code below:



# Task 2.4
# Ask the user for a float number and print it rounded to 2 decimals.
#
# Example:
#   Input: 3.14159
#   Output: 3.14
#
# Your code below:




# ============================================================================
# Rank 3 — Intermediate
# Multi-step calculations using floats.
# ============================================================================

# Task 3.1
# Percentage score calculator:
# Ask the user for:
#   total_questions (int)
#   correct_answers (int)
# Compute:
#   percentage = (correct_answers / total_questions) * 100
# Print with ONE decimal place.
#
# Your code below:



# Task 3.2
# Small invoice:
# Ask the user for:
#   price (float)
#   quantity (int)
# Tax rate = 16% (0.16)
#
# Calculate:
#   subtotal
#   tax
#   total
#
# Print all values formatted to 2 decimals.
#
# Your code below:



# Task 3.3
# Average speed:
# Given:
#   distance_km = 150.0
#   time_hours = 2.5
# Compute:
#   speed = distance_km / time_hours
#
# Print:
#   Average speed: <value> km/h
#
# Your code below:



# Task 3.4
# Celsius → Fahrenheit converter:
# Formula:
#   F = C * 9/5 + 32
#
# Ask for Celsius (float)
# Print Fahrenheit with 1 decimal place.
#
# Your code below:




# ============================================================================
# Rank 4 — Advanced
# Precision, normalization, and comparison logic.
# ============================================================================

# Task 4.1
# Precision demonstration:
# Compute:
#   a = 0.1 + 0.2
#   b = 0.3
#
# Print a, b, and (a == b)
# Then explain in a comment why they are not equal.
#
# Your code below:



# Task 4.2
# Write a function:
#   floats_are_close(a, b, tolerance=1e-9)
#
# Return True if |a - b| <= tolerance.
#
# Your code below:



# Task 4.3
# Normalize three weights:
# Given:
#   w1 = 2.0
#   w2 = 3.0
#   w3 = 5.0
# Compute normalized values:
#   wi / total
# Print all three and the sum (should be 1.0).
#
# Your code below:



# Task 4.4
# Ask the user for a float.
# Print:
#   - int(value)   → truncation
#   - round(value) → rounding
#
# Add a short comment explaining the difference.
#
# Your code below:




# ============================================================================
# Rank 5 — Professional
# Small reusable helpers and real-world float utilities.
# ============================================================================

# Task 5.1
# Function: compute_average(values)
# Requirements:
# - Accept a list of floats.
# - Return the average.
# - If the list is empty, return 0.0.
#
# Your code below:



# Task 5.2
# Function: apply_discount(price, discount_percent)
# Example:
#   apply_discount(100, 10) -> 90.0
#
# Your code below:



# Task 5.3
# Function: to_fixed(value, decimals)
# Return a STRING formatted with a fixed number of decimals.
#
# Example:
#   to_fixed(3.14159, 2) -> "3.14"
#
# Your code below:



# Task 5.4
# Function: bmi(weight_kg, height_m)
# Formula:
#   BMI = weight_kg / (height_m ** 2)
#
# Return the float BMI (no rounding inside).
#
# Your code below:


# End of Float_Tasks.py
