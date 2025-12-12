"""
Data_Classes_Tasks_Solutions.py
Module 34 — Data Classes
Author: Peyman Miyandashti
Year: 2025

This file contains clean and professional solutions
for the data class exercises in this module.
"""

from dataclasses import dataclass, field, replace

# ---------------------------------------------------------------------------
# Rank 1 — Beginner
# ---------------------------------------------------------------------------

# Task 1 Solution
@dataclass
class Person:
    name: str
    age: int

person1 = Person("Peyman", 43)
print(person1)


# Task 2 Solution
person2 = Person("Peyman", 43)
print(person1 == person2)


# ---------------------------------------------------------------------------
# Rank 2 — Easy
# ---------------------------------------------------------------------------

# Task 3 Solution
@dataclass
class Product:
    name: str
    price: float
    in_stock: bool = True

product = Product("Keyboard", 50.0)
print(product)


# Task 4 Solution
product.price = 45.0
print(product)


# ---------------------------------------------------------------------------
# Rank 3 — Intermediate
# ---------------------------------------------------------------------------

# Task 5 Solution
@dataclass
class Order:
    id: int
    items: list = field(default_factory=list)

order = Order(1)
print(order)


# Task 6 Solution
order.items.append("Notebook")
order.items.append("Pen")
print(order)


# ---------------------------------------------------------------------------
# Rank 4 — Advanced
# ---------------------------------------------------------------------------

# Task 7 Solution
@dataclass(frozen=True)
class Point:
    x: int
    y: int

point = Point(10, 20)
print(point)

# point.x = 15  # This would raise FrozenInstanceError


# Task 8 Solution
new_point = replace(point, x=15)
print(new_point)


# ---------------------------------------------------------------------------
# Rank 5 — Professional
# ---------------------------------------------------------------------------

# Task 9 Solution
@dataclass
class UserProfile:
    username: str
    email: str
    active: bool = True

    def deactivate(self):
        self.active = False

user = UserProfile("peyman", "peyman@example.com")
user.deactivate()
print(user)


# Task 10 Solution
@dataclass
class Result:
    success: bool
    message: str

def perform_action(ok: bool) -> Result:
    if ok:
        return Result(True, "Action completed successfully")
    return Result(False, "Action failed")

print(perform_action(True))
print(perform_action(False))


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# These solutions demonstrate:
# - clean data modeling
# - correct use of defaults and immutability
# - professional use of data classes
#
# Next Step:
# Move on to the next module when ready.
