"""
Generators_Tasks_Solutions.py
Module 28 — Generators
Author: Peyman Miyandashti
Year: 2025

This file contains clean and professional solutions
for the generator exercises in this module.
"""

# ---------------------------------------------------------------------------
# Rank 1 — Beginner
# ---------------------------------------------------------------------------

# Task 1 Solution
def simple_numbers():
    yield 1
    yield 2
    yield 3


# Task 2 Solution
def letters_generator():
    yield "a"
    yield "b"
    yield "c"


# ---------------------------------------------------------------------------
# Rank 2 — Easy
# ---------------------------------------------------------------------------

# Task 3 Solution
def count_up_to(n):
    current = 1
    while current <= n:
        yield current
        current += 1


# Task 4 Solution
def even_numbers(n):
    for number in range(n + 1):
        if number % 2 == 0:
            yield number


# ---------------------------------------------------------------------------
# Rank 3 — Intermediate
# ---------------------------------------------------------------------------

# Task 5 Solution
def squares(n):
    for number in range(1, n + 1):
        yield number ** 2


# Task 6 Solution
def positive_numbers(numbers):
    for number in numbers:
        if number > 0:
            yield number


# ---------------------------------------------------------------------------
# Rank 4 — Advanced
# ---------------------------------------------------------------------------

# Task 7 Solution
def word_lengths(words):
    for word in words:
        yield len(word)


# Task 8 Solution
def running_total(numbers):
    total = 0
    for number in numbers:
        total += number
        yield total


# ---------------------------------------------------------------------------
# Rank 5 — Professional
# ---------------------------------------------------------------------------

# Task 9 Solution
def file_line_reader(filename):
    try:
        with open(filename, "r") as file:
            for line in file:
                yield line.strip()
    except FileNotFoundError:
        return


# Task 10 Solution
def log_filter(logs, keyword):
    for log in logs:
        if keyword in log:
            yield log


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# These solutions demonstrate how generators:
# - process data lazily
# - reduce memory usage
# - scale well for real-world applications
#
# Next Step:
# Move on to the next module when ready.
