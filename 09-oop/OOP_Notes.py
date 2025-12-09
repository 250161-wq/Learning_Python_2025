"""
Module 9 — Object-Oriented Programming (OOP): Notes & Explanations
------------------------------------------------------------------

Object-Oriented Programming (OOP) is a way to structure programs by
bundling data (attributes) and behavior (methods) inside *objects*.

In this module, I will learn:
- Classes, objects, attributes, methods
- Constructors (__init__)
- Instance vs class attributes
- Encapsulation
- Inheritance
- Polymorphism
- Method overriding
- super()
- Magic / dunder methods
- Abstract classes
"""


# ============================================================================
# 1. What Are Classes and Objects?
# ============================================================================

"""
A class defines a *blueprint* for creating objects.

An object is an instance of a class.

Example:
    class Dog:
        pass

    d = Dog()   # object of class Dog
"""


# Simple example:

class Dog:
    pass


dog1 = Dog()
dog2 = Dog()


# ============================================================================
# 2. Attributes and Methods
# ============================================================================

"""
Attributes = variables that belong to an object.
Methods = functions that belong to an object.

All instance methods must include `self` as the first parameter.
"""


class Person:
    def __init__(self, name, age):
        self.name = name      # instance attribute
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name}."


p = Person("Peyman", 43)
p.greet()   # "Hello, my name is Peyman."


# ============================================================================
# 3. The __init__ Constructor
# ============================================================================

"""
__init__ runs automatically when an object is created.

Use it to initialize attributes.
"""


class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year


my_car = Car("Kia Sportage", 2024)


# ============================================================================
# 4. Instance vs Class Attributes
# ============================================================================

"""
Instance attributes → unique to each object.
Class attributes → shared by ALL objects of the class.
"""


class Student:
    school = "UPBC"    # class attribute, shared by all students

    def __init__(self, name):
        self.name = name    # instance attribute


s1 = Student("Alice")
s2 = Student("Bob")


# ============================================================================
# 5. Encapsulation and Access Control
# ============================================================================

"""
Python does NOT enforce strict access levels, but uses naming conventions:

- public attribute:     name
- protected attribute:  _name        (internal use)
- private attribute:    __name       (name mangling)
"""


class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance   # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


acc = Account("Peyman", 1000)


# ============================================================================
# 6. Magic / Dunder Methods
# ============================================================================

"""
Magic methods start and end with __.

Common ones:
- __str__     → string representation
- __repr__    → developer representation
- __len__     → length
- __add__     → + operator
- __eq__      → ==
"""


class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"{self.title} ({self.pages} pages)"

    def __len__(self):
        return self.pages


b = Book("Python Mastery", 350)
str(b)        # "Python Mastery (350 pages)"
len(b)        # 350


# ============================================================================
# 7. Inheritance
# ============================================================================

"""
A class can inherit from another class.

Child class → Parent class.
"""


class Animal:
    def speak(self):
        return "Some generic sound"


class Dog(Animal):
    def speak(self):
        return "Woof!"


a = Animal()
d = Dog()


# ============================================================================
# 8. super() and Method Overriding
# ============================================================================

"""
super() allows calling methods from the parent class.
"""


class Vehicle:
    def __init__(self, brand):
        self.brand = brand


class Car(Vehicle):
    def __init__(self, brand, year):
        super().__init__(brand)   # call parent constructor
        self.year = year


c = Car("Toyota", 2022)


# ============================================================================
# 9. Polymorphism
# ============================================================================

"""
Polymorphism = same method name, different behavior depending on object.
"""


class Cat(Animal):
    def speak(self):
        return "Meow"


animals = [Dog(), Cat(), Animal()]
sounds = [a.speak() for a in animals]


# ============================================================================
# 10. Abstract Base Classes (ABC)
# ============================================================================

"""
Abstract classes cannot be instantiated.

Use them to enforce method requirements.
"""


from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h


rect = Rectangle(4, 5)


# ============================================================================
# 11. Composition (HAS-A relationship)
# ============================================================================

"""
Composition means a class contains another class.

Example:
    A Car HAS-A Engine
"""


class Engine:
    def start(self):
        return "Engine started"


class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        return self.engine.start()


my_engine = Engine()
my_car = Car(my_engine)


# ============================================================================
# 12. Best Practices for OOP
# ============================================================================

"""
✔ Keep classes small and focused ("Single Responsibility Principle")
✔ Prefer composition over inheritance
✔ Do NOT overuse magic methods
✔ Use meaningful method & attribute names
✔ Encapsulate internal details using _ or __
✔ Use super() when extending parent methods
✔ Override methods only when it makes sense
✔ Use abstract classes for required method definitions
"""


# ============================================================================
# 13. Summary
# ============================================================================

"""
In this module I learned:

- What classes and objects are
- How to define attributes and methods
- The purpose of __init__
- Class vs instance attributes
- Encapsulation and name mangling
- Magic methods like __str__ and __len__
- Inheritance and polymorphism
- How super() works
- Abstract classes
- Composition vs inheritance

Next:
    Run OOP_Examples.py to explore real OOP code.
    Complete the structured tasks in OOP_Tasks.py.
"""
