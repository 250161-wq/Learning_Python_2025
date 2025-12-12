"""
Named_Tuples_Examples.py
Module 33 — Named Tuples
Author: Peyman Miyandashti
Year: 2025

This file contains clear and practical examples
showing how named tuples are used in Python.
"""

from collections import namedtuple

# ---------------------------------------------------------------------------
# Example 1: Basic Named Tuple Creation
# ---------------------------------------------------------------------------

Point = namedtuple("Point", ["x", "y"])

p = Point(10, 20)
print(p)
print(p.x)
print(p.y)


# ---------------------------------------------------------------------------
# Example 2: Access by Index and Name
# ---------------------------------------------------------------------------

print(p[0])
print(p[1])
print(p.x)
print(p.y)


# ---------------------------------------------------------------------------
# Example 3: Named Tuple in a Function
# ---------------------------------------------------------------------------

def distance_from_origin(point):
    return (point.x ** 2 + point.y ** 2) ** 0.5

print(distance_from_origin(p))


# ---------------------------------------------------------------------------
# Example 4: Replacing Values with _replace()
# ---------------------------------------------------------------------------

p2 = p._replace(x=15)
print(p2)


# ---------------------------------------------------------------------------
# Example 5: Converting to Dictionary
# ---------------------------------------------------------------------------

point_dict = p._asdict()
print(point_dict)


# ---------------------------------------------------------------------------
# Example 6: Iterating Over Fields
# ---------------------------------------------------------------------------

for value in p:
    print(value)


# ---------------------------------------------------------------------------
# Example 7: Named Tuple as Return Value
# ---------------------------------------------------------------------------

Student = namedtuple("Student", ["name", "grade"])

def get_student():
    return Student("Arlette", 95)

student = get_student()
print(student.name, student.grade)


# ---------------------------------------------------------------------------
# Example 8: Comparing Named Tuples
# ---------------------------------------------------------------------------

p3 = Point(10, 20)
print(p == p3)


# ---------------------------------------------------------------------------
# Example 9: Default Values
# ---------------------------------------------------------------------------

Person = namedtuple("Person", ["name", "age", "country"])
Person.__new__.__defaults__ = ("Unknown",)

person1 = Person("Peyman", 43)
person2 = Person("Someone", 30, "Mexico")

print(person1)
print(person2)


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# These examples show how named tuples:
# - improve readability
# - replace simple tuples
# - act as lightweight data containers
#
# Next Step:
# Continue with Named_Tuples_Tasks.py
