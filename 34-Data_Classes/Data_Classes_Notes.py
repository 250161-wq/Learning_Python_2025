"""
Data_Classes_Notes.py
Module 34 — Data Classes
Author: Peyman Miyandashti
Year: 2025

This module explains data classes in Python.
Data classes simplify the creation of classes
that are primarily used to store data.
"""

from dataclasses import dataclass, field

# ---------------------------------------------------------------------------
# 1. What Is a Data Class?
# ---------------------------------------------------------------------------
# A data class is a class that automatically generates:
# - __init__
# - __repr__
# - __eq__
# and other methods based on class attributes.


# ---------------------------------------------------------------------------
# 2. Creating a Basic Data Class
# ---------------------------------------------------------------------------

@dataclass
class Person:
    name: str
    age: int
    city: str


p1 = Person("Peyman", 43, "Mexicali")
print(p1)


# ---------------------------------------------------------------------------
# 3. Automatic Equality Comparison
# ---------------------------------------------------------------------------

p2 = Person("Peyman", 43, "Mexicali")
print(p1 == p2)


# ---------------------------------------------------------------------------
# 4. Default Values
# ---------------------------------------------------------------------------

@dataclass
class Product:
    name: str
    price: float
    in_stock: bool = True


item = Product("Laptop", 1200.0)
print(item)


# ---------------------------------------------------------------------------
# 5. Using field()
# ---------------------------------------------------------------------------
# field() allows more control over attributes.

@dataclass
class Order:
    id: int
    items: list = field(default_factory=list)


order = Order(1)
order.items.append("Book")
print(order)


# ---------------------------------------------------------------------------
# 6. Updating Values
# ---------------------------------------------------------------------------
# Data class attributes are mutable by default.

p1.age = 44
print(p1)


# ---------------------------------------------------------------------------
# 7. Frozen Data Classes
# ---------------------------------------------------------------------------
# Frozen data classes are immutable.

@dataclass(frozen=True)
class Point:
    x: int
    y: int


pt = Point(10, 20)
print(pt)
# pt.x = 15  # This would raise FrozenInstanceError


# ---------------------------------------------------------------------------
# 8. Data Classes vs Named Tuples
# ---------------------------------------------------------------------------
# Data classes:
# - mutable by default
# - support methods
# - more flexible
#
# Named tuples:
# - immutable
# - lightweight
# - simpler


# ---------------------------------------------------------------------------
# 9. Adding Methods
# ---------------------------------------------------------------------------

@dataclass
class Rectangle:
    width: float
    height: float

    def area(self):
        return self.width * self.height


rect = Rectangle(5, 4)
print(rect.area())


# ---------------------------------------------------------------------------
# 10. Best Practices
# ---------------------------------------------------------------------------
# - Use data classes for structured data
# - Use frozen=True when immutability is needed
# - Use default_factory for mutable defaults
# - Keep data classes focused on data


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# Data classes reduce boilerplate and improve readability.
# They are ideal for clean and modern Python code.
#
# Next Step:
# Continue with Data_Classes_Examples.py
