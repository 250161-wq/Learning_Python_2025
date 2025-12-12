"""
Regular_Expressions_Tasks_Solutions.py
Module 36 — Regular Expressions
Author: Peyman Miyandashti
Year: 2025

This file contains clean and professional solutions
for the regular expression exercises in this module.
"""

import re

# ---------------------------------------------------------------------------
# Rank 1 — Beginner
# ---------------------------------------------------------------------------

# Task 1 Solution
text = "I am learning Python programming"
match = re.search("Python", text)
print(match.group() if match else "Not found")


# Task 2 Solution
digits = re.findall(r"\d", "Room 42, Floor 3")
print(digits)


# ---------------------------------------------------------------------------
# Rank 2 — Easy
# ---------------------------------------------------------------------------

# Task 3 Solution
sentence = "Regular expressions are very powerful"
words = re.findall(r"[a-zA-Z]+", sentence)
print(words)


# Task 4 Solution
string = "123abc"
starts_with_number = re.match(r"\d", string) is not None
print(starts_with_number)


# ---------------------------------------------------------------------------
# Rank 3 — Intermediate
# ---------------------------------------------------------------------------

# Task 5 Solution
date = "2025-12-11"
match = re.search(r"(\d{4})-(\d{2})-(\d{2})", date)

if match:
    year, month, day = match.groups()
    print(year, month, day)


# Task 6 Solution
text = """
Contact us at support@example.com or admin@test.org.
For help, email info@company.net
"""

emails = re.findall(r"\w+@\w+\.\w+", text)
print(emails)


# ---------------------------------------------------------------------------
# Rank 4 — Advanced
# ---------------------------------------------------------------------------

# Task 7 Solution
masked = re.sub(r"\d", "#", "User ID 98765")
print(masked)


# Task 8 Solution
def is_valid_password(password):
    pattern = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"
    return re.fullmatch(pattern, password) is not None

print(is_valid_password("Pass1234"))
print(is_valid_password("password"))


# ---------------------------------------------------------------------------
# Rank 5 — Professional
# ---------------------------------------------------------------------------

# Task 9 Solution
log = "2025-12-11 ERROR Server crashed unexpectedly"

match = re.search(
    r"(?P<date>\d{4}-\d{2}-\d{2})\s+(?P<level>\w+)\s+(?P<message>.+)",
    log
)

if match:
    print(match.group("date"))
    print(match.group("level"))
    print(match.group("message"))


# Task 10 Solution
raw_text = "  This   text!!!   has   extra   spaces...  "
cleaned = re.sub(r"[^\w\s]", "", raw_text)
cleaned = re.sub(r"\s+", " ", cleaned).strip()
print(cleaned)


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# These solutions demonstrate:
# - pattern matching
# - extraction
# - validation
# - cleaning and transformation
#
# Next Step:
# Move on to the next module when ready.
