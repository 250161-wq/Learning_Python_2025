"""
Module 2 — Loops: Practice Tasks
--------------------------------

This file contains guided practice tasks for Python loops.

In this module I will:
- Use `for` loops to iterate over ranges, strings, lists, and dictionaries.
- Use `while` loops to repeat actions until a condition is met.
- Practice `break`, `continue`, and `else` with loops.
- Combine loops with basic logic to solve small, realistic problems.

How to use this file:
- Work through the tasks from Rank 1 to Rank 5.
- Write your solutions directly under each task description.
- Do NOT look at the solutions file until you have tried the task honestly.

There is a separate file:
- Loops_Tasks_Solutions.py  → contains one possible solution for each task.
"""

# ============================================================
# Rank 1 → Beginner
# Very simple loop patterns to get comfortable with syntax.
# ============================================================

# Task 1.1
# Print the numbers from 1 to 5 (inclusive) using a for loop.
# Each number should appear on its own line.
#
# Write your code below:


# Task 1.2
# Given this list of names:
#   names = ["Peyman", "Arlette", "Alex"]
# Use a for loop to print: "Hello, <name>!" for each element.
#
# Example output:
#   Hello, Peyman!
#   Hello, Arlette!
#   Hello, Alex!
#
# Write your code below:


# Task 1.3
# Use a for loop and the range() function to print all even numbers
# from 0 to 10 (inclusive).
#
# Write your code below:


# Task 1.4
# Use a while loop to count down from 5 to 1 and then print "Lift off!".
#
# Expected output:
#   5
#   4
#   3
#   2
#   1
#   Lift off!
#
# Write your code below:


# ============================================================
# Rank 2 → Easy
# Still simple, but combining 2 or more ideas in each task.
# ============================================================

# Task 2.1
# Ask the user for a number N (using input()) and then:
# - Use a for loop to print all numbers from 1 to N (inclusive).
#
# Example:
#   Input: 4
#   Output:
#     1
#     2
#     3
#     4
#
# Write your code below:


# Task 2.2
# Given this list:
#   numbers = [3, 7, 10, 15, 21]
# Use a for loop to calculate the sum of all numbers
# and then print: "Total:", followed by the result.
#
# Write your code below:


# Task 2.3
# Given a string:
#   text = "Python"
# Use a for loop to print each character on a separate line.
#
# Example:
#   P
#   y
#   t
#   h
#   o
#   n
#
# Write your code below:


# Task 2.4
# Use a while loop to repeatedly ask the user to type a word.
# Stop when the user types the word "exit".
#
# Hints:
# - Use an infinite loop (while True) and break when the user types "exit".
#
# Write your code below:


# ============================================================
# Rank 3 → Intermediate
# Longer tasks with more steps and simple logic.
# ============================================================

# Task 3.1
# Multiplication table:
# Ask the user for a number N and then print the multiplication
# table for that number from 1 to 10.
#
# Example for N = 3:
#   3 x 1 = 3
#   3 x 2 = 6
#   ...
#   3 x 10 = 30
#
# Write your code below:


# Task 3.2
# Count vowels:
# Ask the user for a text and use a for loop to count
# how many vowels (a, e, i, o, u) appear in the text.
# Ignore case (treat 'A' and 'a' the same).
#
# Finally print: "Vowel count:", <number_of_vowels>
#
# Write your code below:


# Task 3.3
# Filter positive numbers:
# Given the list:
#   numbers = [10, -3, 0, 7, -1, 5]
# Use a for loop to create a new list called "positives"
# that contains only the numbers greater than 0.
# Then print the new list.
#
# Write your code below:


# Task 3.4
# Password attempts:
# You have a secret password stored in a variable:
#   secret = "python123"
# Use a while loop to give the user up to 3 attempts to guess the password.
# - If the user guesses correctly, print "Access granted" and stop the loop.
# - If, after 3 attempts, the user still fails, print "Access denied".
#
# Write your code below:


# ============================================================
# Rank 4 → Advanced
# More realistic tasks using break, continue, and nested loops.
# ============================================================

# Task 4.1
# Skip negative numbers:
# Given the list:
#   numbers = [4, -1, 7, 0, -5, 10]
# Use a for loop to:
# - Skip all negative numbers using "continue".
# - Stop the loop completely if you find a zero using "break".
# - Print every number that you actually process (not skipped and before zero).
#
# Write your code below:


# Task 4.2
# Grades summary:
# Given a list of student grades:
#   grades = [9.5, 7.0, 8.3, 6.0, 10.0, 5.5]
# Use a for loop to:
# - Calculate the average grade.
# - Count how many grades are passing (>= 6.0).
# At the end, print:
#   "Average:", <average_value>
#   "Passing:", <count_of_passing>
#
# Write your code below:


# Task 4.3
# Nested loops — simple grid:
# Use nested for loops to print a 3x3 grid of stars like this:
#   * * *
#   * * *
#   * * *
#
# Hint: You can either:
# - build a string for each row and print it, OR
# - print() inside an inner loop with end=" ".
#
# Write your code below:


# Task 4.4
# Dictionary iteration:
# Given a dictionary of products and prices:
#   prices = {
#       "apple": 1.2,
#       "banana": 0.8,
#       "orange": 1.5,
#   }
# Use a for loop to print lines like:
#   "apple → 1.2"
#   "banana → 0.8"
#   "orange → 1.5"
#
# Write your code below:


# ============================================================
# Rank 5 → Professional
# More "production-style" tasks that look like real code.
# ============================================================

# Task 5.1
# Reusable function: range summary
# Write a function called "range_summary(start, end)" that:
# - Uses a for loop to iterate from start to end (inclusive).
# - Calculates:
#     * the total sum of the numbers,
#     * how many numbers are even,
#     * how many numbers are odd.
# - Returns a dictionary with this structure:
#     {
#         "sum": <total_sum>,
#         "even_count": <how_many_even>,
#         "odd_count": <how_many_odd>,
#     }
#
# Example:
#   result = range_summary(1, 5)
#   # result -> {"sum": 15, "even_count": 2, "odd_count": 3}
#
# Write your code below:


# Task 5.2
# Clean user input with a loop:
# Write a function called "ask_for_positive_integer()" that:
# - Uses a while loop to repeatedly ask the user:
#       "Enter a positive integer: "
# - If the user types something that cannot be converted to an integer,
#   print an error message and ask again.
# - If the user types an integer <= 0, print an error and ask again.
# - Only when the user enters a valid positive integer, return that value.
#
# Note: This is a common real-world pattern for validating input.
#
# Write your code below:


# Task 5.3
# Search in a list (manual implementation):
# Given a list of usernames:
#   users = ["peyman", "alex", "arlette", "admin"]
# Write a function "user_exists(username)" that:
# - Uses a for loop (do NOT use `in` or `.index()` directly).
# - Returns True if the username is in the list, otherwise False.
#
# Example:
#   user_exists("alex")   -> True
#   user_exists("nova")   -> False
#
# Write your code below:


# Task 5.4
# Simple report with enumerate():
# Given a list of tasks:
#   tasks = ["Install Python", "Create virtual environment", "Run first script"]
# Use a for loop with enumerate() to print a numbered report like:
#   1. Install Python
#   2. Create virtual environment
#   3. Run first script
#
# This is a very common pattern in professional code for displaying lists.
#
# Write your code below:
