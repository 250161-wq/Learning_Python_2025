"""
ID_Values_Notes.py
Module 46 — id() Values
Author: Peyman Miyandashti
Year: 2025

This module explains object identity in Python
using the id() function.
"""

# ---------------------------------------------------------------------------
# 1. What Is id()?
# ---------------------------------------------------------------------------
# id(obj) returns a unique integer identifying the object.
# This value is constant for the object during its lifetime.

x = 10
print(id(x))


# ---------------------------------------------------------------------------
# 2. Identity vs Equality
# ---------------------------------------------------------------------------
# Identity  -> is
# Equality  -> ==

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)   # same values
print(a is b)   # different objects
print(id(a), id(b))


# ---------------------------------------------------------------------------
# 3. Same Object, Same id
# ---------------------------------------------------------------------------

c = a
print(c is a)
print(id(c) == id(a))


# ---------------------------------------------------------------------------
# 4. Immutable Objects
# ---------------------------------------------------------------------------
# Immutable objects may be reused by Python.

x = 100
y = 100

print(x == y)
print(x is y)
print(id(x), id(y))


# ---------------------------------------------------------------------------
# 5. Mutable Objects
# ---------------------------------------------------------------------------
# Mutable objects usually have distinct identities.

list1 = []
list2 = []

print(list1 == list2)
print(list1 is list2)
print(id(list1), id(list2))


# ---------------------------------------------------------------------------
# 6. id() and is
# ---------------------------------------------------------------------------
# is compares identity, not value.

name1 = "Python"
name2 = "Python"

print(name1 is name2)
print(id(name1), id(name2))


# ---------------------------------------------------------------------------
# 7. Object Lifetime
# ---------------------------------------------------------------------------
# Once an object is destroyed, its id may be reused.
# Never rely on id() values for program logic.


# ---------------------------------------------------------------------------
# 8. Common Mistakes
# ---------------------------------------------------------------------------
# - using is instead of ==
# - assuming same value means same object
# - using id() for comparisons in business logic


# ---------------------------------------------------------------------------
# 9. Best Practices
# ---------------------------------------------------------------------------
# - use == for value comparison
# - use is for identity (None, True, False)
# - use id() for learning and debugging only


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# id() reveals how Python manages object identity.
# It is a learning and debugging tool, not application logic.
#
# Next Step:
# Continue with ID_Values_Examples.py
