"""
Class_Static_Methods_Tasks_Solutions.py
Module 40 — Class Methods & Static Methods
Author: Peyman Miyandashti
Year: 2025

This file contains clean and professional solutions
for the class method and static method exercises.
"""

# ---------------------------------------------------------------------------
# Rank 1 — Beginner
# ---------------------------------------------------------------------------

# Task 1 Solution
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, my name is {self.name}"


# Task 2 Solution
p = Person("Peyman")
print(p.greet())


# ---------------------------------------------------------------------------
# Rank 2 — Easy
# ---------------------------------------------------------------------------

# Task 3 Solution
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def total(cls):
        return cls.count


# Task 4 Solution
c1 = Counter()
c2 = Counter()
c3 = Counter()

print(Counter.total())


# ---------------------------------------------------------------------------
# Rank 3 — Intermediate
# ---------------------------------------------------------------------------

# Task 5 Solution
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    @classmethod
    def from_string(cls, data):
        name, grade = data.split(",")
        return cls(name.strip(), int(grade))


# Task 6 Solution
student = Student.from_string("Arlette, 95")
print(student.name, student.grade)


# ---------------------------------------------------------------------------
# Rank 4 — Advanced
# ---------------------------------------------------------------------------

# Task 7 Solution
class MathTools:
    @staticmethod
    def is_positive(number):
        return number > 0

    @staticmethod
    def is_even(number):
        return number % 2 == 0


# Task 8 Solution
print(MathTools.is_positive(10))
print(MathTools.is_positive(-5))
print(MathTools.is_even(8))
print(MathTools.is_even(7))


# ---------------------------------------------------------------------------
# Rank 5 — Professional
# ---------------------------------------------------------------------------

# Task 9 Solution
class Product:
    tax_rate = 0.16

    def __init__(self, name, price):
        self.name = name
        self.price = price

    # Instance method: uses object data
    def price_with_tax(self):
        return self.price * (1 + Product.tax_rate)

    # Class method: configures class-level data
    @classmethod
    def set_tax_rate(cls, new_rate):
        cls.tax_rate = new_rate

    # Static method: validation logic
    @staticmethod
    def is_valid_price(price):
        return price >= 0


item = Product("Laptop", 1000)
print(item.price_with_tax())

Product.set_tax_rate(0.20)
print(item.price_with_tax())

print(Product.is_valid_price(500))
print(Product.is_valid_price(-10))


# Task 10 Solution
# Instance methods:
# - operate on a specific object
# - use self
#
# Class methods:
# - operate on the class itself
# - use cls
# - often used for alternative constructors or configuration
#
# Static methods:
# - do not depend on instance or class data
# - group related utility logic inside a class


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# These solutions demonstrate correct and intentional use of:
# - instance methods
# - class methods
# - static methods
#
# Next Step:
# Move on to the next module when ready.
