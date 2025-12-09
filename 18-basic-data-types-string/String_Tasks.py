"""
Module 18 — Strings: Practice Tasks
-----------------------------------

This file contains guided practice tasks for Python string variables.

In this module I will:
- Create and print basic string variables.
- Concatenate strings and format messages with f-strings.
- Use indexing and slicing to access parts of a string.
- Apply common string methods (lower, upper, strip, replace, split, join).
- Search inside strings and validate user input.
- Build small, realistic text-processing utilities.

How to use this file:
- Work through the tasks from Rank 1 to Rank 5.
- Write your solutions directly under each task description.
- Do NOT look at the solutions file until you have tried the task honestly.

There is a separate file:
- String_Tasks_Solutions.py  → contains one possible solution for each task.
"""

# ============================================================
# Rank 1 → Beginner
# Very simple tasks to get comfortable with string basics.
# ============================================================

# Task 1.1
# Create a variable called "greeting" with the value "Hello, World!"
# and print it.
#
# Expected output:
#   Hello, World!
#
# Write your code below:


# Task 1.2
# Create two variables:
#   first_name = "Peyman"
#   last_name = "Miyandashti"
# Then create a variable called "full_name" that combines them with a space
# in between, and print:
#   Full name: <full_name>
#
# Example:
#   Full name: Peyman Miyandashti
#
# Write your code below:


# Task 1.3
# Create a variable:
#   city = "Mexicali"
# Use the len() function to get the length of the string and print:
#   Length of city name: <length>
#
# Write your code below:


# Task 1.4
# Use f-strings to print a short sentence using two variables.
# Example:
#   name = "Arlette"
#   age = 47
# Output:
#   Arlette is 47 years old.
#
# Create your own variables and message using an f-string.
#
# Write your code below:


# ============================================================
# Rank 2 → Easy
# Still simple, but combining 2–3 ideas in each task.
# ============================================================

# Task 2.1
# Given this string:
#   language = "Python"
# Use indexing to:
# - Print the first character.
# - Print the last character.
#
# Example:
#   First character: P
#   Last character: n
#
# Write your code below:


# Task 2.2
# Given:
#   word = "Programming"
# Use slicing to:
# - Print the first 4 characters.
# - Print the last 3 characters.
#
# Example:
#   First 4: Prog
#   Last 3: ing
#
# Write your code below:


# Task 2.3
# Given a string with extra spaces:
#   raw_name = "   peyman   "
# Use string methods to:
# - Remove spaces at the beginning and end.
# - Capitalize the first letter.
# Then print:
#   Clean name: <result>
#
# Hint: You can chain methods, for example: raw_name.strip().capitalize()
#
# Write your code below:


# Task 2.4
# Ask the user to type a word using input():
#   "Type a word: "
# Then:
# - Print the word in all lowercase.
# - Print the word in all uppercase.
#
# Example input:  Python
# Example output:
#   Lowercase: python
#   Uppercase: PYTHON
#
# Write your code below:


# ============================================================
# Rank 3 → Intermediate
# Longer tasks with more steps and basic logic.
# ============================================================

# Task 3.1
# Count vowels in a word:
# Ask the user for a word:
#   "Enter a word: "
# Use a for-loop to count how many vowels (a, e, i, o, u)
# appear in the word. Ignore case.
#
# At the end print:
#   Vowel count: <number_of_vowels>
#
# Write your code below:


# Task 3.2
# Replace words in a sentence:
# Given:
#   sentence = "I like Java, but Java is not my favorite."
# Use the replace() method to change all occurrences of "Java" to "Python"
# and print the new sentence.
#
# Expected output:
#   I like Python, but Python is not my favorite.
#
# Write your code below:


# Task 3.3
# Split full name:
# Ask the user to type their full name:
#   "Enter your full name: "
# Then:
# - Split the string by spaces into a list.
# - Print how many parts the name has (using len()).
# - Print the list of parts.
#
# Example:
#   Input:  Ana Maria Lopez
#   Parts: 3
#   ['Ana', 'Maria', 'Lopez']
#
# Write your code below:


# Task 3.4
# Simple multi-line message:
# Create a multi-line string called "message" that looks like this:
#   Hello!
#   Welcome to my Python practice.
#   Have a great day.
#
# Then print the message.
#
# Hint: You can use triple quotes (""" ... """).
#
# Write your code below:


# ============================================================
# Rank 4 → Advanced
# More realistic string-processing tasks.
# ============================================================

# Task 4.1
# Simple password check:
# Ask the user to enter a password:
#   "Create a password: "
# Then:
# - Check if the password length is at least 8 characters.
# - Check if it contains at least one digit.
# - Check if it contains at least one lowercase letter.
#
# Print a message for each rule:
#   - "OK: at least 8 characters" or "ERROR: too short"
#   - "OK: contains a digit" or "ERROR: no digit found"
#   - "OK: contains lowercase" or "ERROR: no lowercase letter"
#
# Write your code below:


# Task 4.2
# Text preview:
# Ask the user to enter a long text (for example a paragraph).
# Then:
# - If the text has more than 30 characters, create a preview string
#   that contains only the first 30 characters followed by "..."
# - Otherwise, the preview is the full text.
#
# Finally print:
#   Preview: <preview_text>
#
# Write your code below:


# Task 4.3
# Find a word in a sentence:
# Ask the user for a sentence and a word:
#   "Enter a sentence: "
#   "Enter a word to search: "
# Then:
# - Check if the word is inside the sentence (use the "in" operator).
# - If it is found, print: "Found!".
# - Otherwise, print: "Not found."
#
# Bonus: Make the check case-insensitive by converting both to lowercase.
#
# Write your code below:


# Task 4.4
# CSV-style string to list:
# Given a string:
#   data = "10,20,30,40,50"
# - Split it into a list of strings.
# - Convert each element into an integer.
# - Print the final list of integers.
#
# Expected output:
#   [10, 20, 30, 40, 50]
#
# Write your code below:


# ============================================================
# Rank 5 → Professional
# Tasks that look closer to "real code" utilities.
# ============================================================

# Task 5.1
# Format product info:
# Write a function called "format_product" that receives two arguments:
#   name (str) and price (float).
# The function should return a formatted string like:
#   "Product: <NAME> | Price: $<PRICE_WITH_2_DECIMALS>"
#
# Example:
#   format_product("Keyboard", 599.9)
#   -> "Product: Keyboard | Price: $599.90"
#
# Use an f-string with formatting for the price.
#
# Write your code below:


# Task 5.2
# Username sanitizer:
# Write a function called "sanitize_username" that:
# - Receives a string "raw_username".
# - Removes spaces at the beginning and end.
# - Converts all letters to lowercase.
# - Replaces any internal spaces with underscores.
#
# Example:
#   sanitize_username("  Peyman Nova  ")
#   -> "peyman_nova"
#
# Return the cleaned username.
#
# Write your code below:


# Task 5.3
# Normalize whitespace:
# Write a function "normalize_spaces(text: str) -> str" that:
# - Splits the text into words (using split()).
# - Joins the words back together with a single space between each.
#
# This removes extra spaces, tabs, or newlines inside the text.
#
# Example:
#   normalize_spaces("Hello   world   from   Python")
#   -> "Hello world from Python"
#
# Write your code below:


# Task 5.4
# Join list of words into a sentence:
# Write a function "to_sentence(words: list[str]) -> str" that:
# - Joins the words with spaces.
# - Capitalizes the first letter of the final string.
# - Ensures the sentence ends with a period (.).
#
# Example:
#   to_sentence(["python", "is", "fun"])
#   -> "Python is fun."
#
# Hint: You can check if the sentence already ends with '.' before adding it.
#
# Write your code below:
