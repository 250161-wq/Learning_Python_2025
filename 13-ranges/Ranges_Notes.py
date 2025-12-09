"""
Module 13 — Ranges
Professional Notes

This file provides a clear and practical explanation of Python's range object.
Ranges are used extensively in loops, indexing, numeric sequences, and
controlled iteration. Understanding how they work is essential for writing
clean and efficient Python code.
"""

# ---------------------------------------------------------------------------
# 1. What Is a range?
# ---------------------------------------------------------------------------
# A range represents a sequence of numbers, but it does NOT store all the
# numbers in memory. Instead, it generates values on demand.
#
# Example:
r = range(5)
print(r)           # range(0, 5)
print(list(r))     # [0, 1, 2, 3, 4]
#
# Important:
# - range objects are efficient and lightweight
# - they are commonly used in for-loops and indexing logic


# ---------------------------------------------------------------------------
# 2. Basic Forms of range()
# ---------------------------------------------------------------------------
# Python supports three main forms of range:
#
#   range(stop)
#   range(start, stop)
#   range(start, stop, step)
#
# All ranges include the start value but EXCLUDE the stop value.


# Example: range(stop)
print(list(range(4)))  # [0, 1, 2, 3]


# Example: range(start, stop)
print(list(range(2, 6)))  # [2, 3, 4, 5]


# Example: range(start, stop, step)
print(list(range(1, 10, 2)))  # [1, 3, 5, 7, 9]


# ---------------------------------------------------------------------------
# 3. Negative Steps and Reverse Ranges
# ---------------------------------------------------------------------------
# A negative step allows a range to count backward.
#
# Example:
print(list(range(10, 0, -1)))  # [10, 9, 8, ..., 1]


# A common pattern to reverse a sequence:
print(list(range(5, -1, -1)))  # [5, 4, 3, 2, 1, 0]


# ---------------------------------------------------------------------------
# 4. Off-by-One Rules
# ---------------------------------------------------------------------------
# The stop value is never included.
#
# range(0, 5) gives: 0, 1, 2, 3, 4
#
# To include 5, you must use:
print(list(range(0, 6)))  # [0, 1, 2, 3, 4, 5]


# ---------------------------------------------------------------------------
# 5. Ranges in Loops
# ---------------------------------------------------------------------------
# Ranges are most commonly used in loops:
#
for i in range(3):
    print("Loop iteration:", i)
#
# Output:
# Loop iteration: 0
# Loop iteration: 1
# Loop iteration: 2


# Example with start and stop:
for i in range(5, 8):
    print("Value:", i)


# Example with step:
for i in range(0, 10, 3):
    print("Step of 3:", i)


# ---------------------------------------------------------------------------
# 6. Ranges vs Lists (Performance)
# ---------------------------------------------------------------------------
# A range does NOT store all values — it calculates them when needed.
# This makes it memory efficient.
#
large_range = range(1_000_000)
# This uses very little memory.
#
# But converting to a list uses a lot of memory:
# big_list = list(range(1_000_000))


# ---------------------------------------------------------------------------
# 7. Checking Membership
# ---------------------------------------------------------------------------
# You can check if a number is inside a range:
print(10 in range(20))      # True
print(21 in range(20))      # False


# ---------------------------------------------------------------------------
# 8. Common Mistakes
# ---------------------------------------------------------------------------
# ❌ Forgetting that stop is excluded
# range(5) → does NOT include 5
#
# ❌ Using step=0 (invalid)
# range(1, 10, 0) → ERROR
#
# ❌ Trying to index a range beyond its length
# r = range(5)
# r[5] → ERROR (valid indexes: 0–4)
#
# ❌ Confusing reversed range with wrong stop value
# range(5, 0, -1) → [5, 4, 3, 2, 1]  (0 is NOT included)


# ---------------------------------------------------------------------------
# 9. Best Practices
# ---------------------------------------------------------------------------
# ✔ Use ranges inside loops for numeric iteration
# ✔ Prefer ranges over constructing long lists manually
# ✔ Use descriptive variable names in loops
# ✔ When reversing sequences, use clear negative steps
# ✔ Never assume the stop value is included
# ✔ Use steps to simplify logic instead of nested conditions


# ---------------------------------------------------------------------------
# 10. Summary
# ---------------------------------------------------------------------------
# In this module, I learned:
# - What ranges are and how they behave
# - How to use start, stop, and step parameters
# - How to work with negative ranges and reverse sequences
# - How ranges differ from lists in memory usage
# - How to use ranges in loops and membership tests
# - Common mistakes and best practices
#
# End of Notes
