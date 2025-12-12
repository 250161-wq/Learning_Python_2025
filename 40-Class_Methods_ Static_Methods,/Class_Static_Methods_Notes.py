"""
Class_Static_Methods_Notes.py
Module 40 — Class Methods & Static Methods
Author: Peyman Miyandashti
Year: 2025

This module explains instance methods, class methods,
and static methods in Python.
"""

# ---------------------------------------------------------------------------
# 1. Instance Methods
# ---------------------------------------------------------------------------
# Instance methods receive 'self'
# and operate on a specific object.

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, I am {self.name}"


# ---------------------------------------------------------------------------
# 2. Class Methods
# ---------------------------------------------------------------------------
# Class methods receive 'cls'
# and operate on the class itself.

class User:
    count = 0

    def __init__(self, username):
        self.username = username
        User.count += 1

    @classmethod
    def total_users(cls):
        return cls.count


# ---------------------------------------------------------------------------
# 3. Static Methods
# ---------------------------------------------------------------------------
# Static methods do not receive self or cls.
# They behave like regular functions but belong to the class.

class MathUtils:
    @staticmethod
    def is_even(number):
        return number % 2 == 0


# ---------------------------------------------------------------------------
# 4. When to Use Each Method
# ---------------------------------------------------------------------------
# Instance method → needs object data
# Class method     → needs class data
# Static method    → related logic, no class or instance data


# ---------------------------------------------------------------------------
# 5. Alternative Constructors (Class Methods)
# ---------------------------------------------------------------------------

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    @classmethod
    def from_string(cls, data):
        name, grade = data.split(",")
        return cls(name.strip(), int(grade))


student = Student.from_string("Peyman, 95")
print(student.name, student.grade)


# ---------------------------------------------------------------------------
# 6. Static Methods for Validation
# ---------------------------------------------------------------------------

class Validator:
    @staticmethod
    def is_valid_age(age):
        return age >= 0


# ---------------------------------------------------------------------------
# 7. Common Mistakes
# ---------------------------------------------------------------------------
# - Using staticmethod when classmethod is needed
# - Using classmethod when instance data is required
# - Putting unrelated functions inside classes


# ---------------------------------------------------------------------------
# 8. Best Practices
# ---------------------------------------------------------------------------
# - Use instance methods by default
# - Use classmethods for alternative constructors
# - Use staticmethods for utility logic
# - Keep responsibilities clear


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# Class and static methods improve class design
# when used intentionally and correctly.
#
# Next Step:
# Continue with Class_Static_Methods_Examples.py
