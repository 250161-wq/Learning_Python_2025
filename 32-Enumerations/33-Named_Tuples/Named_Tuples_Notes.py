"""
Named_Tuples_Notes.py
Module 33 — Named Tuples
Author: Peyman Miyandashti
Year: 2025

This module explains named tuples in Python.
Named tuples provide tuple-like objects with named fields.
"""

# ---------------------------------------------------------------------------
# 1. What Is a Named Tuple?
# ---------------------------------------------------------------------------
# A named tuple is a subclass of tuple.
# It allows accessing elements using names instead of indexes.
#
# Named tuples are immutable, just like normal tuples.


# ---------------------------------------------------------------------------
# 2. Importing namedtuple
# ---------------------------------------------------------------------------

from collections import namedtuple


# ---------------------------------------------------------------------------
# 3. Creating a Named Tuple
# ---------------------------------------------------------------------------

Person = namedtuple("Person", ["name", "age", "city"])

p1 = Person("Peyman", 43, "Mexicali")

print(p1)
print(p1.name)
print(p1.age)
print(p1.city)


# ---------------------------------------------------------------------------
# 4. Accessing by Index vs Name
# ---------------------------------------------------------------------------

print(p1[0])     # name
print(p1[1])     # age
print(p1.name)   # clearer and safer


# ---------------------------------------------------------------------------
# 5. Immutability
# ---------------------------------------------------------------------------
# Named tuples cannot be modified after creation.

# p1.age = 44  # This would raise AttributeError


# ---------------------------------------------------------------------------
# 6. Using _replace()
# ---------------------------------------------------------------------------
# _replace() creates a new instance with updated values.

p2 = p1._replace(age=44)
print(p2)


# ---------------------------------------------------------------------------
# 7. Converting to Dictionary
# ---------------------------------------------------------------------------

person_dict = p1._asdict()
print(person_dict)


# ---------------------------------------------------------------------------
# 8. Using Named Tuples in Functions
# ---------------------------------------------------------------------------

def describe_person(person):
    return f"{person.name} is {person.age} years old"

print(describe_person(p1))


# ---------------------------------------------------------------------------
# 9. When to Use Named Tuples
# ---------------------------------------------------------------------------
# Use named tuples when:
# - data is simple and fixed
# - immutability is desired
# - readability matters
# - a full class would be overkill


# ---------------------------------------------------------------------------
# 10. Named Tuples vs Classes
# ---------------------------------------------------------------------------
# Named tuples:
# - lightweight
# - immutable
# - no custom methods by default
#
# Classes:
# - mutable by default
# - support behavior and logic
# - more flexible


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# Named tuples provide a clean way to structure data
# without the overhead of full classes.
#
# Next Step:
# Continue with Named_Tuples_Examples.py
