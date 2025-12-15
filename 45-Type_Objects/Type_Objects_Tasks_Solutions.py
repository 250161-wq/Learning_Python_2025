"""
Type_Objects_Tasks_Solutions.py
Module 45 — Type Objects
Author: Peyman Miyandashti
Year: 2025

This file contains clean and professional solutions
for the type object exercises in this module.
"""

# ---------------------------------------------------------------------------
# Rank 1 — Beginner
# ---------------------------------------------------------------------------

# Task 1 Solution
print(type(10))
print(type("Python"))
print(type([1, 2, 3]))


# Task 2 Solution
class Sample:
    pass

sample_instance = Sample()

print(type(Sample))
print(type(sample_instance))


# ---------------------------------------------------------------------------
# Rank 2 — Easy
# ---------------------------------------------------------------------------

# Task 3 Solution
print(isinstance(int, type))
print(isinstance(str, type))


# Task 4 Solution
print(isinstance(sample_instance, object))


# ---------------------------------------------------------------------------
# Rank 3 — Intermediate
# ---------------------------------------------------------------------------

# Task 5 Solution
DynamicClass = type("DynamicClass", (), {"value": 42})
obj = DynamicClass()
print(obj.value)


# Task 6 Solution
def greet(self):
    return "Hello from dynamic method"

DynamicWithMethod = type(
    "DynamicWithMethod",
    (),
    {"greet": greet}
)

dynamic_obj = DynamicWithMethod()
print(dynamic_obj.greet())


# ---------------------------------------------------------------------------
# Rank 4 — Advanced
# ---------------------------------------------------------------------------

# Task 7 Solution
class Base:
    base_value = 100

Child = type("Child", (Base,), {"child_value": 200})


# Task 8 Solution
child_instance = Child()
print(child_instance.base_value)
print(child_instance.child_value)


# ---------------------------------------------------------------------------
# Rank 5 — Professional
# ---------------------------------------------------------------------------

# Task 9 Solution
# Understanding type objects is important because:
# - frameworks use metaclasses to modify class creation
# - ORMs inspect and transform classes dynamically
# - decorators and descriptors rely on type behavior
# - reading advanced Python requires this knowledge


# Task 10 Solution
# Dynamic class creation is appropriate when:
# - classes must be generated programmatically
# - behavior depends on runtime data
# - building frameworks or DSLs
#
# Normal class syntax is better when:
# - structure is static
# - readability is a priority
# - maintainability matters


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# These solutions demonstrate:
# - inspection using type()
# - dynamic class creation
# - inheritance through type
#
# Next Step:
# Move on to the next module when ready.
