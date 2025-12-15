"""
ID_Values_Examples.py
Module 46 — id() Values
Author: Peyman Miyandashti
Year: 2025

This file contains clear and practical examples
showing how id() and object identity work in Python.
"""

# ---------------------------------------------------------------------------
# Example 1: Basic id() Usage
# ---------------------------------------------------------------------------

x = 10
print("x:", x, "id:", id(x))


# ---------------------------------------------------------------------------
# Example 2: Identity vs Equality
# ---------------------------------------------------------------------------

a = [1, 2, 3]
b = [1, 2, 3]

print("a == b:", a == b)
print("a is b:", a is b)
print("id(a):", id(a))
print("id(b):", id(b))


# ---------------------------------------------------------------------------
# Example 3: Same Object Reference
# ---------------------------------------------------------------------------

c = a
print("c is a:", c is a)
print("id(c) == id(a):", id(c) == id(a))


# ---------------------------------------------------------------------------
# Example 4: Immutable Objects
# ---------------------------------------------------------------------------

x1 = 100
x2 = 100

print("x1 == x2:", x1 == x2)
print("x1 is x2:", x1 is x2)
print("id(x1):", id(x1))
print("id(x2):", id(x2))


# ---------------------------------------------------------------------------
# Example 5: Mutable Objects
# ---------------------------------------------------------------------------

list1 = []
list2 = []

print("list1 == list2:", list1 == list2)
print("list1 is list2:", list1 is list2)
print("id(list1):", id(list1))
print("id(list2):", id(list2))


# ---------------------------------------------------------------------------
# Example 6: Strings and Interning
# ---------------------------------------------------------------------------

s1 = "Python"
s2 = "Python"

print("s1 is s2:", s1 is s2)
print("id(s1):", id(s1))
print("id(s2):", id(s2))


# ---------------------------------------------------------------------------
# Example 7: id() Changes with New Objects
# ---------------------------------------------------------------------------

num = 200
print("id(num):", id(num))

num = 201
print("id(num):", id(num))


# ---------------------------------------------------------------------------
# Example 8: is vs == with None
# ---------------------------------------------------------------------------

value = None
print(value is None)
print(value == None)


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# These examples demonstrate:
# - identity vs equality
# - behavior of mutable and immutable objects
# - correct use of is and id()
#
# Next Step:
# Continue with ID_Values_Tasks.py
