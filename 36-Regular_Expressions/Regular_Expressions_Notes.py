"""
Regular_Expressions_Notes.py
Module 36 — Regular Expressions
Author: Peyman Miyandashti
Year: 2025

This module explains regular expressions in Python.
Regular expressions are patterns used to match text.
"""

import re

# ---------------------------------------------------------------------------
# 1. What Is a Regular Expression?
# ---------------------------------------------------------------------------
# A regular expression is a pattern that describes a set of strings.
# Python uses the 're' module to work with regular expressions.


# ---------------------------------------------------------------------------
# 2. Basic Matching
# ---------------------------------------------------------------------------

text = "Python is powerful"

match = re.search("Python", text)
print(match)


# ---------------------------------------------------------------------------
# 3. Common Functions
# ---------------------------------------------------------------------------
# re.search()   → finds pattern anywhere in string
# re.match()    → matches only at the beginning
# re.findall()  → returns all matches
# re.sub()      → replaces matches


# ---------------------------------------------------------------------------
# 4. Character Classes
# ---------------------------------------------------------------------------
# [abc]     → a, b, or c
# [0-9]     → any digit
# [a-zA-Z]  → any letter

digits = re.findall("[0-9]", "Room 42")
print(digits)


# ---------------------------------------------------------------------------
# 5. Special Characters
# ---------------------------------------------------------------------------
# \d  → digit
# \w  → word character
# \s  → whitespace
# .   → any character except newline

numbers = re.findall(r"\d+", "Order 123 costs 45 dollars")
print(numbers)


# ---------------------------------------------------------------------------
# 6. Quantifiers
# ---------------------------------------------------------------------------
# +  → one or more
# *  → zero or more
# ?  → zero or one
# {n} → exactly n times

word = re.findall(r"\w{5}", "Python regex")
print(word)


# ---------------------------------------------------------------------------
# 7. Groups
# ---------------------------------------------------------------------------

date = "2025-12-11"
parts = re.search(r"(\d{4})-(\d{2})-(\d{2})", date)

print(parts.group(1))
print(parts.group(2))
print(parts.group(3))


# ---------------------------------------------------------------------------
# 8. Replacing Text
# ---------------------------------------------------------------------------

masked = re.sub(r"\d", "*", "Card 1234")
print(masked)


# ---------------------------------------------------------------------------
# 9. Validation Example
# ---------------------------------------------------------------------------

email = "user@example.com"
is_valid = re.fullmatch(r"\w+@\w+\.\w+", email)
print(is_valid is not None)


# ---------------------------------------------------------------------------
# 10. Best Practices
# ---------------------------------------------------------------------------
# - Use raw strings (r"...") for regex
# - Keep patterns readable
# - Comment complex expressions
# - Test regex step by step


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# Regular expressions are extremely powerful for text processing.
# With practice, they become a natural tool.
#
# Next Step:
# Continue with Regular_Expressions_Examples.py
