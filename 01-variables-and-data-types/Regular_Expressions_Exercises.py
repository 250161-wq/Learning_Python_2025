"""
Module 30 — Regular Expressions: Practice Exercises
Comprehensive practice with Python's 're' module, from beginner to
more professional, production-style usage.

In this module I:
- Learn how to use re.search, re.match, re.findall, and re.sub.
- Practice basic patterns (digits, words, simple validation).
- Move toward more realistic text-processing patterns.
- Build reusable, testable helpers for pattern matching.

Ranking system:
- Rank 1  -> Beginner: very basic syntax and concepts.
- Rank 2  -> Easy: still simple, but combining two or more concepts.
- Rank 3  -> Intermediate: more operations in a single example.
- Rank 4  -> Advanced: closer to how regex is used in real projects.
- Rank 5  -> Professional: clean, reusable, and testable patterns.

Author: Peyman Miyandashti
Date of Birth: 11/11/1983
ID Number: 250161
Year: 2025
"""

import re
from typing import List


# ===========================================================
# Rank 1 — Beginner
# Simple search for a word in a string
# ===========================================================

print("Rank 1 — Beginner")

text = "Python is fun. Learning Python in 2025!"
pattern = r"Python"

match = re.search(pattern, text)
if match:
    print("Found 'Python' at position:", match.start(), "-", match.end())
else:
    print("'Python' not found")

print("-" * 50)


# ===========================================================
# Rank 2 — Easy
# Find all digits and words in a string
# ===========================================================

print("Rank 2 — Easy")

log_line = "User peyman logged in from IP 192.168.1.10 at 10:45 pm"

digits = re.findall(r"\d+", log_line)
words = re.findall(r"[A-Za-z]+", log_line)

print("Digits found:", digits)
print("Words found:", words)
print("-" * 50)


# ===========================================================
# Rank 3 — Intermediate
# Simple validation: email-like pattern and substitutions
# ===========================================================

print("Rank 3 — Intermediate")

emails = [
    "user@example.com",
    "invalid-email",
    "pey.man@upbc.edu.mx",
    "test@localhost",
]

email_pattern = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")

for email in emails:
    if email_pattern.match(email):
        print(email, "-> looks VALID")
    else:
        print(email, "-> looks INVALID")

# Replace multiple spaces with a single space
messy_text = "This   sentence   has    too   many   spaces."
clean_text = re.sub(r"\s+", " ", messy_text).strip()
print("Original:", messy_text)
print("Clean   :", clean_text)

print("-" * 50)


# ===========================================================
# Rank 4 — Advanced
# Groups, named groups, and extracting structured data
# ===========================================================

print("Rank 4 — Advanced")

log_entry = "2025-11-11 21:35:01 [ERROR] code=500 message='Internal server error'"

log_pattern = re.compile(
    r"(?P<date>\d{4}-\d{2}-\d{2})\s+"
    r"(?P<time>\d{2}:\d{2}:\d{2})\s+\["
    r"(?P<level>[A-Z]+)\]\s+code=(?P<code>\d+)\s+message='(?P<msg>.*)'"
)

log_match = log_pattern.search(log_entry)
if log_match:
    data = log_match.groupdict()
    print("Parsed log data:")
    for key, value in data.items():
        print(f"  {key}: {value}")
else:
    print("Log entry did not match expected format")

print("-" * 50)


# ===========================================================
# Rank 5 — Professional
# Reusable helpers for validation and extraction
# ===========================================================

print("Rank 5 — Professional")


USERNAME_RE = re.compile(r"^[a-zA-Z0-9_]{3,20}$")
IPV4_RE = re.compile(
    r"^("
    r"(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\."
    r"(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\."
    r"(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\."
    r"(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)"
    r")$"
)


def is_valid_username(username: str) -> bool:
    return bool(USERNAME_RE.match(username))


def is_valid_ipv4(ip: str) -> bool:
    return bool(IPV4_RE.match(ip))


def extract_hashtags(text: str) -> List[str]:
    return re.findall(r"#(\w+)", text)


test_usernames = ["pey", "peyman_250161", "x", "invalid-username!!!"]
test_ips = ["192.168.0.1", "999.999.999.999", "10.0.0.5"]
tweet = "Learning #Python in #2025 is awesome! #coding #dev"

print("Username validation:")
for u in test_usernames:
    print(f"  {u:20} -> {is_valid_username(u)}")

print("\nIPv4 validation:")
for ip in test_ips:
    print(f"  {ip:15} -> {is_valid_ipv4(ip)}")

print("\nHashtags extracted from tweet:")
print(extract_hashtags(tweet))

print("-" * 50)
