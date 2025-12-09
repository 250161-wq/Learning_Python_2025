"""
Module 2 — Loops (Iteration)
Professional Notes

This file provides a structured explanation of Python’s iteration mechanisms.
It is designed as a reference document with clear examples and commentary.
"""

# ---------------------------------------------------------------------------
# 1. Introduction to Iteration
# ---------------------------------------------------------------------------
# A loop is a control structure that allows code to be repeated.
# Loops are essential for:
# - Processing sequences (lists, strings, ranges, etc.)
# - Performing repeated calculations
# - Automating tasks
# - Navigating through data structures

# Python provides two primary loop types:
#   1. for-loop   → Iteration over a sequence or iterable
#   2. while-loop → Repetition based on a condition


# ---------------------------------------------------------------------------
# 2. The for-loop
# ---------------------------------------------------------------------------
# Syntax:
#   for variable in iterable:
#       block of code
#
# The loop iterates once for each element in the iterable.

# Example 1: Iterating over a list
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print("Fruit:", fruit)

# Example 2: Iterating over a string
for letter in "Python":
    print("Letter:", letter)

# Example 3: Using range() for numeric sequences
for number in range(5):  # 0,1,2,3,4
    print("Number:", number)


# ---------------------------------------------------------------------------
# 3. The while-loop
# ---------------------------------------------------------------------------
# A while-loop repeats as long as a condition is True.
#
# Syntax:
#   while condition:
#       block of code

# Example 4: Counting with a while-loop
counter = 0

while counter < 3:
    print("Counter:", counter)
    counter += 1


# ---------------------------------------------------------------------------
# 4. Control Statements: break, continue, else
# ---------------------------------------------------------------------------

# break → Stops the loop immediately.
for num in range(10):
    if num == 5:
        break
    print("Break example:", num)

# continue → Skips the rest of the current loop iteration.
for num in range(6):
    if num % 2 == 0:
        continue
    print("Continue example:", num)

# else → Executes only if loop completes naturally (no break).
for num in range(3):
    print("Looping:", num)
else:
    print("Loop completed without break.")


# ---------------------------------------------------------------------------
# 5. Nested Loops
# ---------------------------------------------------------------------------
# Loops inside loops are useful for processing multi-dimensional data.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
]

for row in matrix:
    for value in row:
        print("Matrix value:", value)


# ---------------------------------------------------------------------------
# 6. Common Loop Mistakes
# ---------------------------------------------------------------------------

# ❌ Risk: Infinite loop (condition never becomes False)
# while True:
#     print("This never stops")  # BAD PRACTICE unless intentionally controlled

# ❌ Modifying the list while iterating can cause unexpected behavior.
# Always iterate over a copy if modification is needed:
#
# for item in my_list[:]:
#     ...

# ❌ Forgetting to update loop variables in while-loops.
# Example:
# counter = 0
# while counter < 10:
#     print(counter)
# # Missing counter += 1 → infinite loop


# ---------------------------------------------------------------------------
# 7. Professional Best Practices
# ---------------------------------------------------------------------------
# ✔ Prefer for-loops when iterating over collections or ranges.
# ✔ Use while-loops only when the repetition condition is based on state.
# ✔ Keep loop bodies short and readable.
# ✔ Avoid deep nesting where possible — extract logic into functions.
# ✔ Use descriptive loop variable names (e.g., 'user', 'item', 'index').
# ✔ Use break and continue intentionally, not excessively.

# ---------------------------------------------------------------------------
# 8. Summary
# ---------------------------------------------------------------------------
# In this module, I learned how to:
# - Use for-loops for structured iteration
# - Use while-loops for condition-based repetition
# - Apply break, continue, and else to control loop flow
# - Understand nested loops and common pitfalls
# - Write clean, professional loop logic

# End of Notes
