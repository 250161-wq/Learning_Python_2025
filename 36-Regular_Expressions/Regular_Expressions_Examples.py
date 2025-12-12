"""
Regular_Expressions_Examples.py
Module 36 — Regular Expressions
Author: Peyman Miyandashti
Year: 2025

This file contains clear and practical examples
showing how regular expressions are used in Python.
"""

import re

# ---------------------------------------------------------------------------
# Example 1: Simple Search
# ---------------------------------------------------------------------------

text = "Learning Python is fun"
result = re.search("Python", text)
print(result.group() if result else "Not found")


# ---------------------------------------------------------------------------
# Example 2: match() vs search()
# ---------------------------------------------------------------------------

print(re.match("Python", text))      # None
print(re.search("Python", text))     # Match object


# ---------------------------------------------------------------------------
# Example 3: findall()
# ---------------------------------------------------------------------------

numbers = re.findall(r"\d+", "Order 123, item 45, code 789")
print(numbers)


# ---------------------------------------------------------------------------
# Example 4: Character Classes
# ---------------------------------------------------------------------------

letters = re.findall(r"[a-zA-Z]+", "Room42A")
print(letters)


# ---------------------------------------------------------------------------
# Example 5: Quantifiers
# ---------------------------------------------------------------------------

words = re.findall(r"\w{4}", "This line has many words")
print(words)


# ---------------------------------------------------------------------------
# Example 6: Groups and Extraction
# ---------------------------------------------------------------------------

log = "2025-12-11 ERROR Server crashed"
match = re.search(r"(\d{4}-\d{2}-\d{2})\s+(\w+)", log)

if match:
    date = match.group(1)
    level = match.group(2)
    print(date, level)


# ---------------------------------------------------------------------------
# Example 7: Named Groups
# ---------------------------------------------------------------------------

match = re.search(
    r"(?P<date>\d{4}-\d{2}-\d{2})\s+(?P<level>\w+)",
    log
)

if match:
    print(match.group("date"), match.group("level"))


# ---------------------------------------------------------------------------
# Example 8: Replacing Text
# ---------------------------------------------------------------------------

masked = re.sub(r"\d", "*", "User ID 98765")
print(masked)


# ---------------------------------------------------------------------------
# Example 9: Splitting Text
# ---------------------------------------------------------------------------

parts = re.split(r"[,\s]+", "apple, banana orange,grape")
print(parts)


# ---------------------------------------------------------------------------
# Example 10: Email Validation
# ---------------------------------------------------------------------------

def is_valid_email(email):
    pattern = r"\w+@\w+\.\w+"
    return re.fullmatch(pattern, email) is not None

print(is_valid_email("user@test.com"))
print(is_valid_email("invalid-email"))


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# These examples show how regex can:
# - find patterns
# - extract structured data
# - clean text
#
# Next Step:
# Continue with Regular_Expressions_Tasks.py
