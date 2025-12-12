"""
Properties_Examples.py
Module 41 — Properties
Author: Peyman Miyandashti
Year: 2025

This file contains clear and practical examples
showing how properties are used in Python.
"""

# ---------------------------------------------------------------------------
# Example 1: Read-Only Property
# ---------------------------------------------------------------------------

class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self._birth_year = birth_year

    @property
    def age(self):
        return 2025 - self._birth_year


p = Person("Peyman", 1982)
print(p.name)
print(p.age)


# ---------------------------------------------------------------------------
# Example 2: Property with Setter (Validation)
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
item.price = 150
print(item.price)
# item.price = -10  # would raise ValueError


# ---------------------------------------------------------------------------
# Example 3: Computed Property
# ---------------------------------------------------------------------------

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height


rect = Rectangle(4, 5)
print(rect.area)


# ---------------------------------------------------------------------------
# Example 4: Refactoring with Properties
# ---------------------------------------------------------------------------
# External code still uses obj.value,
# internal implementation can change safely.

class Data:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value * 2


d = Data(10)
print(d.value)


# ---------------------------------------------------------------------------
# Example 5: Read-Only Property Without Setter
# ---------------------------------------------------------------------------

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2


c = Circle(7)
print(c.diameter)
# c.diameter = 20  # AttributeError


# ---------------------------------------------------------------------------
# Example 6: Property with Deleter
# ---------------------------------------------------------------------------

class Account:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.deleter
    def balance(self):
        print("Balance deleted")
        del self._balance


acc = Account(500)
print(acc.balance)
del acc.balance


# ---------------------------------------------------------------------------
# Example 7: Property vs Public Attribute
# ---------------------------------------------------------------------------
# Properties allow validation and control
# without changing how attributes are accessed.

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero")
        self._celsius = value


temp = Temperature(25)
temp.celsius = 30
print(temp.celsius)


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# These examples show how properties:
# - protect internal state
# - validate data
# - compute values dynamically
#
# Next Step:
# Continue with Properties_Tasks.py
