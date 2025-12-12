"""
Properties_Notes.py
Module 41 — Properties
Author: Peyman Miyandashti
Year: 2025

This module explains properties in Python.
Properties control attribute access using methods
while preserving simple attribute syntax.
"""

# ---------------------------------------------------------------------------
# 1. Why Properties Exist
# ---------------------------------------------------------------------------
# Properties allow logic to run when accessing or modifying attributes.
# This helps with validation, computation, and encapsulation.


# ---------------------------------------------------------------------------
# 2. Basic Property (Read-Only)
# ---------------------------------------------------------------------------

class Person:
    def __init__(self, name, birth_year):
        self._birth_year = birth_year
        self.name = name

    @property
    def age(self):
        return 2025 - self._birth_year


p = Person("Peyman", 1982)
print(p.age)


# ---------------------------------------------------------------------------
# 3. Property with Setter
# ---------------------------------------------------------------------------

class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value


item = Product(100)
item.price = 120
print(item.price)


# ---------------------------------------------------------------------------
# 4. Property Naming Convention
# ---------------------------------------------------------------------------
# Internal attributes are usually prefixed with _
# Public access is controlled via property methods.


# ---------------------------------------------------------------------------
# 5. Read-Only Property
# ---------------------------------------------------------------------------

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14159 * self.radius ** 2


c = Circle(5)
print(c.area)


# ---------------------------------------------------------------------------
# 6. Property with Deleter
# ---------------------------------------------------------------------------

class Account:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.deleter
    def balance(self):
        print("Deleting balance")
        del self._balance


acc = Account(1000)
del acc.balance


# ---------------------------------------------------------------------------
# 7. Refactoring with Properties
# ---------------------------------------------------------------------------
# Properties allow changing internal implementation
# without changing the public API.


# ---------------------------------------------------------------------------
# 8. When to Use Properties
# ---------------------------------------------------------------------------
# Use properties when:
# - validation is required
# - values are computed
# - internal state must be protected
# - public API stability matters


# ---------------------------------------------------------------------------
# 9. Common Mistakes
# ---------------------------------------------------------------------------
# - Overusing properties for simple attributes
# - Putting heavy logic inside properties
# - Forgetting to validate in setters


# ---------------------------------------------------------------------------
# 10. Best Practices
# ---------------------------------------------------------------------------
# - Keep properties lightweight
# - Use clear naming
# - Use private attributes internally
# - Prefer read-only properties when possible


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# Properties provide controlled access without sacrificing usability.
# They are a cornerstone of clean object-oriented design.
#
# Next Step:
# Continue with Properties_Examples.py
