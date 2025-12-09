"""
Module 17 — Integers: Practice Tasks
------------------------------------

This file contains guided practice tasks focused on Python's integer type.

In this module I will:
- Create and update integer variables.
- Use integer arithmetic operators (+, -, *, //, %, **).
- Convert between strings and integers with int().
- Combine integers with input() and simple validation.
- Apply integers in small, realistic problems (counters, scores, prices).

How to use this file:
- Work through the tasks from Rank 1 to Rank 5.
- Write your solutions directly under each task description.
- Do NOT look at the solutions file until you have tried the task honestly.

There is a separate file:
- Integer_Tasks_Solutions.py  → contains one possible solution for each task.
"""

# ============================================================
# Rank 1 → Beginner
# Very simple integer tasks to warm up.
# ============================================================

# Task 1.1
# Create two integer variables:
#   - birth_year → your year of birth
#   - current_year → this year
# Then calculate your age and print it as:
#   "I am <age> years old."
#
# Write your code below:


# Task 1.2
# Simple arithmetic:
# Create three integer variables:
#   a = 8
#   b = 3
#   c = 2
# Calculate and print:
#   - a + b
#   - a - b
#   - a * c
# Each result should be printed on its own line with a label, for example:
#   "a + b =", <result>
#
# Write your code below:


# Task 1.3
# String to integer conversion:
# You are given a string:
#   number_text = "42"
# Convert it to an integer and then print:
#   "The number is", <value>, "and its double is", <double_value>
#
# Write your code below:


# Task 1.4
# Read a number from the user using input() and convert it to int.
# Then print:
#   "You typed:", <number>
#
# Hint:
#   value = int(input("Type a number: "))
#
# Write your code below:


# ============================================================
# Rank 2 → Easy
# Combine integers with input, conversion, and simple formulas.
# ============================================================

# Task 2.1
# Temperature difference:
# Create two integer variables:
#   morning_temp = 18
#   afternoon_temp = 27
# Calculate the difference and print:
#   "The temperature changed by <difference> degrees."
#
# Write your code below:


# Task 2.2
# Minutes to seconds:
# Ask the user for a number of minutes (integer) and convert it to seconds.
# Then print:
#   "<minutes> minutes = <seconds> seconds"
#
# Example:
#   Input: 5
#   Output: "5 minutes = 300 seconds"
#
# Write your code below:


# Task 2.3
# Floor division and modulo:
# You have 23 candies and want to distribute them equally among 4 children.
# Use integer division (//) and modulo (%) to calculate:
#   - how many candies each child gets
#   - how many candies remain
# Print:
#   "Each child gets <per_child> candies."
#   "Candies left over: <remainder>"
#
# Write your code below:


# Task 2.4
# Simple counter:
# Create an integer variable:
#   counter = 0
# Increase it step by step:
#   - add 1
#   - add 5
#   - subtract 2
# After the updates, print:
#   "Final counter value:", <counter>
#
# Write your code below:


# ============================================================
# Rank 3 → Intermediate
# Multi-step problems using integer logic.
# ============================================================

# Task 3.1
# Basic calculator:
# Ask the user for two integers: a and b.
# Then calculate and print:
#   - sum (a + b)
#   - difference (a - b)
#   - product (a * b)
#   - integer division result (a // b)  → only if b is not zero
# Use clear labels in your output.
#
# Hint:
#   You should check if b is zero BEFORE dividing.
#
# Write your code below:


# Task 3.2
# Even or odd:
# Ask the user for an integer.
# If the number is even, print:
#   "<number> is even."
# If the number is odd, print:
#   "<number> is odd."
#
# Hint:
#   Use the modulo operator % 2.
#
# Write your code below:


# Task 3.3
# Score total:
# Imagine a small game with 3 levels.
# Ask the user to type an integer score for each level:
#   level_1, level_2, level_3
# Then calculate the total score and print:
#   "Total score:", <total>
#
# Write your code below:


# Task 3.4
# Clamp a value into a range:
# Ask the user for an integer between 0 and 100.
# If the user types a number less than 0, treat it as 0.
# If the user types a number greater than 100, treat it as 100.
# Then print:
#   "Clamped value:", <final_value>
#
# (You will do this using if/else in the solutions,
#  but here just think about the integer logic.)
#
# Write your code below:


# ============================================================
# Rank 4 → Advanced
# Work with lists of integers and simple statistics.
# ============================================================

# Task 4.1
# List statistics:
# Given the list:
#   numbers = [10, 4, 7, 0, -3, 15]
# Use integers and a for-loop to calculate:
#   - the smallest number
#   - the largest number
#   - the sum of all numbers
# Then print them with clear labels.
#
# Write your code below:


# Task 4.2
# Count positives, negatives, and zeros:
# Using the same list:
#   numbers = [10, 4, 7, 0, -3, 15]
# Count how many values are:
#   - positive (> 0)
#   - negative (< 0)
#   - zero (== 0)
# Print:
#   "Positives:", <count_pos>
#   "Negatives:", <count_neg>
#   "Zeros:", <count_zero>
#
# Write your code below:


# Task 4.3
# Average of exam scores:
# Ask the user how many exam scores they want to enter.
# Then use a loop to read that many integer scores (0–100).
# Calculate the average score as an integer (use // for integer division).
# Print:
#   "Average score:", <average>
#
# Write your code below:


# Task 4.4
# Simple step counter:
# Imagine a fitness app that tracks steps taken each day for a week.
# You are given:
#   steps = [3500, 5000, 4200, 6000, 7100, 3000, 8000]
# Use integer arithmetic to calculate:
#   - total steps for the week
#   - average steps per day (integer average)
# Print both values with clear labels.
#
# Write your code below:


# ============================================================
# Rank 5 → Professional
# Small, realistic utilities using integers and functions.
# ============================================================

# Task 5.1
# Function: percentage_of(part, whole)
# Write a function that:
#   - Takes two integers: part and whole.
#   - Returns the percentage (0–100) as an integer, rounded down.
#     (Use integer arithmetic: result = part * 100 // whole)
#   - If whole is 0, decide how you want to handle it (e.g., return 0).
#
# Example:
#   percentage_of(25, 100) -> 25
#   percentage_of(1, 3)    -> 33
#
# Write your code below:


# Task 5.2
# Function: days_to_weeks_days(total_days)
# Write a function that:
#   - Receives an integer total_days.
#   - Returns a tuple (weeks, days) where:
#       weeks  → how many full weeks fit in total_days
#       days   → how many days remain
#
# Example:
#   days_to_weeks_days(10) -> (1, 3)
#   days_to_weeks_days(21) -> (3, 0)
#
# Use integer division and modulo.
#
# Write your code below:


# Task 5.3
# Function: clamp(value, minimum, maximum)
# Write a function that:
#   - Takes three integers: value, minimum, maximum.
#   - Returns:
#       minimum if value is less than minimum,
#       maximum if value is greater than maximum,
#       otherwise returns value.
#
# This is a very common utility in real projects.
#
# Example:
#   clamp(150, 0, 100)  -> 100
#   clamp(-5, 0, 100)   -> 0
#   clamp(50, 0, 100)   -> 50
#
# Write your code below:


# Task 5.4
# Function: next_even(n)
# Write a function that:
#   - Takes an integer n.
#   - Returns the smallest even integer that is >= n.
#
# Examples:
#   next_even(4)  -> 4
#   next_even(5)  -> 6
#   next_even(10) -> 10
#
# Hint:
#   Use % 2 to check if n is even.
#
# Write your code below:
