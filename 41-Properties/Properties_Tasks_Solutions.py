"""
Properties_Tasks_Solutions.py
Module 41 — Properties
Author: Peyman Miyandashti
Year: 2025

This file contains clean and professional solutions
for the properties exercises in this module.
"""

# ---------------------------------------------------------------------------
# Rank 1 — Beginner
# ---------------------------------------------------------------------------

# Task 1 Solution
class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name_length(self):
        return len(self.name)


# Task 2 Solution
p = Person("Peyman")
print(p.name_length)


# ---------------------------------------------------------------------------
# Rank 2 — Easy
# ---------------------------------------------------------------------------

# Task 3 Solution
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


# Task 4 Solution
item = Product(100)
item.price = 150
print(item.price)


# ---------------------------------------------------------------------------
# Rank 3 — Intermediate
# ---------------------------------------------------------------------------

# Task 5 Solution
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height


# Task 6 Solution
rect = Rectangle(4, 5)
print(rect.area)

rect.width = 10
print(rect.area)


# ---------------------------------------------------------------------------
# Rank 4 — Advanced
# ---------------------------------------------------------------------------

# Task 7 Solution
# Refactoring a public attribute into a property
# without changing external access.

class Data:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value


# Task 8 Solution
class SafeData:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if new_value < 0:
            raise ValueError("Value must be non-negative")
        self._value = new_value


data = SafeData(10)
data.value = 20
print(data.value)


# ---------------------------------------------------------------------------
# Rank 5 — Professional
# ---------------------------------------------------------------------------

# Task 9 Solution
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = amount

    @property
    def is_overdrawn(self):
        return self._balance == 0


account = BankAccount("Peyman", 500)
print(account.balance)
account.balance = 300
print(account.is_overdrawn)


# Task 10 Solution
# Properties are preferred over public attributes because:
# - they allow validation when values change
# - internal representation can change without breaking code
# - they protect object invariants
# - they provide a clean and stable public interface


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# These solutions demonstrate:
# - read-only properties
# - properties with setters and validation
# - computed properties
# - safe encapsulation and refactoring
#
# Next Step:
# Move on to the next module when ready.
