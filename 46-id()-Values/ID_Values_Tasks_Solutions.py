"""
ID_Values_Tasks_Solutions.py
Module 46 — id() Values
Author: Peyman Miyandashti
Year: 2025

This file contains clean and professional solutions
for the id() and object identity exercises in this module.
"""

# ---------------------------------------------------------------------------
# Rank 1 — Beginner
# ---------------------------------------------------------------------------

# Task 1 Solution
x = 42
print("Value:", x, "ID:", id(x))


# Task 2 Solution
text = "Hello"
print("Value:", text, "ID:", id(text))


# ---------------------------------------------------------------------------
# Rank 2 — Easy
# ---------------------------------------------------------------------------

# Task 3 Solution
list_a = [1, 2, 3]
list_b = [1, 2, 3]

print("list_a == list_b:", list_a == list_b)
print("list_a is list_b:", list_a is list_b)
print("ID list_a:", id(list_a))
print("ID list_b:", id(list_b))


# Task 4 Solution
list_c = list_a
print("list_c is list_a:", list_c is list_a)
print("ID list_c:", id(list_c))


# ---------------------------------------------------------------------------
# Rank 3 — Intermediate
# ---------------------------------------------------------------------------

# Task 5 Solution
a = 10
b = 10

print("a == b:", a == b)
print("a is b:", a is b)
print("ID a:", id(a))
print("ID b:", id(b))

# Small integers are cached by Python,
# so they may share the same identity.


# Task 6 Solution
a = 11
print("New a:", a, "ID:", id(a))

# Reassignment creates a new object.


# ---------------------------------------------------------------------------
# Rank 4 — Advanced
# ---------------------------------------------------------------------------

# Task 7 Solution
def modify_list(lst):
    print("Before:", id(lst))
    lst.append(99)
    print("After:", id(lst))

numbers = [1, 2, 3]
modify_list(numbers)

# Mutable objects keep the same identity
# when modified.


# Task 8 Solution
def modify_number(n):
    print("Before:", id(n))
    n += 1
    print("After:", id(n))

num = 5
modify_number(num)

# Immutable objects create new objects
# when modified.


# ---------------------------------------------------------------------------
# Rank 5 — Professional
# ---------------------------------------------------------------------------

# Task 9 Solution
# id() should not be used for application logic because:
# - ids are implementation details
# - ids may be reused after object destruction
# - code becomes non-portable and fragile


# Task 10 Solution
# Use `is`:
# - to compare with None
# - to compare True / False
# - to check object identity
#
# Use `==`:
# - to compare values
# - for business logic comparisons


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# These solutions demonstrate:
# - correct use of id()
# - identity vs equality
# - mutability effects on identity
#
# Next Step:
# Move on to the next module when ready.
