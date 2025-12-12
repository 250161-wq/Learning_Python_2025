"""
CustomClasses_Notes.py
Module 26 — Custom Classes & Objects
Author: Peyman Miyandashti
Year: 2025

This module introduces Python classes — one of the most important foundations
of object-oriented programming (OOP). Classes allow me to create custom data
types that combine attributes (data) and methods (behavior). Objects created
from a class model real-world entities such as students, cars, products, or
game characters.

This file explains:
- What classes and objects are
- How to define a class
- How to create objects (instances)
- How the __init__ constructor works
- How instance attributes and methods work
- How to use __str__ and __repr__ for clean output
- Best practices for writing clean class-based code
"""


# ---------------------------------------------------------------------------
# 1. What Is a Class?
# ---------------------------------------------------------------------------
# A class is a blueprint for creating objects.
# It defines:
#   - attributes: variables that belong to objects
#   - methods: functions that operate on those objects
#
# Example: A class "Car" describes what data every car has and how it behaves.


# ---------------------------------------------------------------------------
# 2. What Is an Object?
# ---------------------------------------------------------------------------
# An object (instance) is a concrete example created from a class blueprint.
#
# Example:
#   car1 = Car("Toyota", 2020)
#   car2 = Car("Honda", 2023)
#
# Both are based on the Car class, but contain different data.


# ---------------------------------------------------------------------------
# 3. Defining a Basic Class
# ---------------------------------------------------------------------------

class Car:
    pass  # Empty class for demonstration


# ---------------------------------------------------------------------------
# 4. The __init__ Constructor (Object Initializer)
# ---------------------------------------------------------------------------
# __init__ runs automatically when a new object is created.
# It sets up the initial state (attributes) of the object.

class Person:
    def __init__(self, name, age):
        self.name = name      # instance attribute
        self.age = age        # instance attribute

# Creating objects
p1 = Person("Peyman", 43)
p2 = Person("Arlette", 47)

print(p1.name, p1.age)
print(p2.name, p2.age)


# ---------------------------------------------------------------------------
# 5. Instance Methods (Behavior)
# ---------------------------------------------------------------------------
# Methods are functions defined inside a class that work with `self`.
# `self` refers to the current object.

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def promote(self):
        self.grade += 1     # modify object state

    def info(self):
        return f"{self.name} is in grade {self.grade}"

s = Student("Luis", 8)
s.promote()
print(s.info())  # "Luis is in grade 9"


# ---------------------------------------------------------------------------
# 6. Adding String Representations (__str__ and __repr__)
# ---------------------------------------------------------------------------
# __str__ gives a human-readable output for print().
# __repr__ is a debugging representation for developers.

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"Book: {self.title} ({self.pages} pages)"

    def __repr__(self):
        return f"Book(title={self.title!r}, pages={self.pages})"

b = Book("Python Basics", 300)
print(b)          # calls __str__
print(repr(b))    # calls __repr__


# ---------------------------------------------------------------------------
# 7. Modifying Attributes
# ---------------------------------------------------------------------------

car = Car()
car.brand = "Kia"
car.year = 2024

print(car.brand, car.year)


# ---------------------------------------------------------------------------
# 8. Combining Data and Behavior
# ---------------------------------------------------------------------------

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return self.balance

acct = BankAccount("Peyman", 500)
acct.deposit(200)
acct.withdraw(100)
print(acct.balance)


# ---------------------------------------------------------------------------
# 9. Best Practices for Custom Classes
# ---------------------------------------------------------------------------
# ✔ Use clear, descriptive class names (Car, Student, Invoice, Account)
# ✔ Initialize attributes in __init__
# ✔ Always use self.attribute for instance data
# ✔ Write small, focused methods that do one thing
# ✔ Provide __str__ and __repr__ for clean output
# ✔ Avoid creating attributes outside __init__ unless necessary
# ✔ Keep class responsibilities simple and logical


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# Classes allow me to model real-world concepts and build structured software.
# Understanding how attributes, methods, and constructors work gives me the
# foundation for more advanced topics like inheritance, encapsulation,
# polymorphism, and more.

# Next Step:
# Continue with CustomClasses_Examples.py to see practical code demonstrations.

