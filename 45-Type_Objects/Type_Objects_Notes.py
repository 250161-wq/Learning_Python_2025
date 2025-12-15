"""
Type_Objects_Notes.py
Module 45 — Type Objects
Author: Peyman Miyandashti
Year: 2025

This module explains the type object in Python.
Type is the metaclass that creates classes.
"""

# ---------------------------------------------------------------------------
# 1. Everything Is an Object
# ---------------------------------------------------------------------------
# In Python, numbers, functions, classes, and modules
# are all objects.

print(type(10))
print(type("hello"))
print(type(len))


# ---------------------------------------------------------------------------
# 2. What Does type() Do?
# ---------------------------------------------------------------------------
# type(x) returns the class of x.

x = 5
print(type(x))


# ---------------------------------------------------------------------------
# 3. Classes Are Objects Too
# ---------------------------------------------------------------------------

class Person:
    pass

print(type(Person))
print(type(Person()))


# ---------------------------------------------------------------------------
# 4. type Is the Class of Classes
# ---------------------------------------------------------------------------
# Most classes are instances of type.

print(type(int))
print(type(str))
print(type(Person))


# ---------------------------------------------------------------------------
# 5. type Has Two Roles
# ---------------------------------------------------------------------------
# 1) type(obj) -> returns the object's class
# 2) type(name, bases, dict) -> creates a class


# ---------------------------------------------------------------------------
# 6. Creating a Class Dynamically
# ---------------------------------------------------------------------------

MyClass = type(
    "MyClass",
    (),
    {"x": 10, "show": lambda self: self.x}
)

obj = MyClass()
print(obj.x)
print(obj.show())


# ---------------------------------------------------------------------------
# 7. Comparing Normal Class vs type()
# ---------------------------------------------------------------------------

class NormalClass:
    y = 20

print(NormalClass.y)

DynamicClass = type("DynamicClass", (), {"y": 20})
print(DynamicClass.y)


# ---------------------------------------------------------------------------
# 8. Inheritance with type
# ---------------------------------------------------------------------------

class Base:
    base_value = 100

Child = type("Child", (Base,), {"child_value": 200})

print(Child.base_value)
print(Child.child_value)


# ---------------------------------------------------------------------------
# 9. Why This Matters
# ---------------------------------------------------------------------------
# Frameworks like Django, SQLAlchemy, and ORMs
# rely heavily on type and metaclasses.


# ---------------------------------------------------------------------------
# 10. Best Practices
# ---------------------------------------------------------------------------
# - Use normal class syntax by default
# - Use type() for dynamic or meta-programming
# - Focus on readability first


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# type is the foundation of Python’s object system.
# Understanding it unlocks advanced Python concepts.
#
# Next Step:
# Continue with Type_Objects_Examples.py
