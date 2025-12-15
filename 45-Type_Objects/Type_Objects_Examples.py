"""
Type_Objects_Examples.py
Module 45 — Type Objects
Author: Peyman Miyandashti
Year: 2025

This file contains clear and practical examples
showing how type objects work in Python.
"""

# ---------------------------------------------------------------------------
# Example 1: Using type() to Inspect Objects
# ---------------------------------------------------------------------------

print(type(10))
print(type("Python"))
print(type([1, 2, 3]))
print(type(len))


# ---------------------------------------------------------------------------
# Example 2: Classes Are Objects
# ---------------------------------------------------------------------------

class Person:
    pass

p = Person()

print(type(Person))   # class of the class
print(type(p))        # class of the instance


# ---------------------------------------------------------------------------
# Example 3: type Is the Class of Built-in Classes
# ---------------------------------------------------------------------------

print(type(int))
print(type(str))
print(type(dict))


# ---------------------------------------------------------------------------
# Example 4: type Has Two Meanings
# ---------------------------------------------------------------------------
# 1) Inspecting
x = 42
print(type(x))

# 2) Creating a class dynamically
DynamicClass = type("DynamicClass", (), {"value": 100})


# ---------------------------------------------------------------------------
# Example 5: Using a Dynamically Created Class
# ---------------------------------------------------------------------------

obj = DynamicClass()
print(obj.value)


# ---------------------------------------------------------------------------
# Example 6: Adding Methods with type()
# ---------------------------------------------------------------------------

def greet(self):
    return "Hello from dynamic class"

DynamicWithMethod = type(
    "DynamicWithMethod",
    (),
    {"greet": greet}
)

d = DynamicWithMethod()
print(d.greet())


# ---------------------------------------------------------------------------
# Example 7: Inheritance with type()
# ---------------------------------------------------------------------------

class Base:
    base_value = 10

Child = type("Child", (Base,), {"child_value": 20})

c = Child()
print(c.base_value)
print(c.child_value)


# ---------------------------------------------------------------------------
# Example 8: Comparing Normal vs Dynamic Class
# ---------------------------------------------------------------------------

class Normal:
    x = 1

Dynamic = type("Dynamic", (), {"x": 1})

print(Normal.x)
print(Dynamic.x)


# ---------------------------------------------------------------------------
# Example 9: type and isinstance
# ---------------------------------------------------------------------------

print(isinstance(p, Person))
print(isinstance(p, object))


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# These examples show that:
# - classes are objects
# - type creates classes
# - Python’s object model is fully dynamic
#
# Next Step:
# Continue with Type_Objects_Tasks.py
