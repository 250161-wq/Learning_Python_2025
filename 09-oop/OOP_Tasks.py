"""
Module 9 — Object-Oriented Programming (OOP): Practice Exercises
----------------------------------------------------------------

This file contains structured OOP exercises, progressing from simple
class definitions to professional-level OOP design patterns.

I should:
- Implement each class and method myself
- NOT look at solutions until I finish
- Follow clean, readable OOP principles
- Move from Rank 1 → Rank 5 at my own pace
"""


# =============================================================================
# Rank 1 — Beginner
# =============================================================================

class BasicGreeter:
    """
    Task:
        Create a class with:
            - a method greet() that returns: "Hello!"
    """
    # TODO: Implement greet()
    pass


class Person:
    """
    Task:
        Create a class Person with:
            - attributes: name, age
            - a method info() → "<name> is <age> years old"
    """
    # TODO: Define __init__ and info()
    pass


class Rectangle:
    """
    Task:
        Create a Rectangle class with:
            - width
            - height
        Add a method area() returning width * height.
    """
    # TODO: Implement class
    pass


# =============================================================================
# Rank 2 — Easy
# =============================================================================

class Student:
    """
    Task:
        Add:
            - class attribute school = "UPBC"
            - instance attribute name
        Add method describe():
            "<name> studies at <school>"
    """
    # TODO: Implement __init__, describe()
    pass


class Car:
    """
    Task:
        Class with:
            - brand
            - year
        Add method age(current_year) that returns how old the car is.
    """
    # TODO: Implement class
    pass


class Counter:
    """
    Task:
        Create a Counter class that starts at 0.
        Methods:
            increment() → increases count by 1
            reset() → back to 0
            value() → returns current count
    """
    # TODO: Implement class
    pass


# =============================================================================
# Rank 3 — Intermediate
# =============================================================================

class Animal:
    """
    Task:
        Base class with method speak() returning "Some sound"
    """
    # TODO: Implement speak()
    pass


class Dog(Animal):
    """
    Task:
        Override speak() → "Woof!"
    """
    # TODO: Override speak()
    pass


class Cat(Animal):
    """
    Task:
        Override speak() → "Meow"
    """
    # TODO: Override speak()
    pass


class BankAccount:
    """
    Task:
        Use encapsulation:
            - owner (public)
            - __balance (private)

        Methods:
            deposit(amount)
            withdraw(amount)
            get_balance()
    """
    # TODO: Implement private & public methods
    pass


# =============================================================================
# Rank 4 — Advanced
# =============================================================================

class Vehicle:
    """
    Task:
        Class with attribute brand.
    """
    # TODO: Implement __init__()
    pass


class ElectricCar(Vehicle):
    """
    Task:
        Subclass of Vehicle using super()
        Attributes:
            brand
            battery_kwh
    """
    # TODO: Implement subclass with super()
    pass


class Book:
    """
    Task:
        Add magic methods:
            __str__ → "<title> (<pages> pages)"
            __len__ → return pages
    Attributes:
        title
        pages
    """
    # TODO: Implement magic methods
    pass


from abc import ABC, abstractmethod

class Shape(ABC):
    """
    Task:
        Abstract class with abstract method area()
    """
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    """
    Task:
        Implement area():
            π * r^2
    """
    # TODO: Implement class
    pass


# =============================================================================
# Rank 5 — Professional
# =============================================================================

class Engine:
    """
    Task:
        Method start() → "Engine started"
    """
    # TODO: Implement method
    pass


class CarWithEngine:
    """
    Task:
        Demonstrate COMPOSITION:
            - CarWithEngine has-an Engine
        Methods:
            start() → calls engine.start()
    """
    # TODO: Implement class with composition
    pass


class User:
    """
    Task:
        Model a user with:
            name
            email

        Add validate():
            - name must be at least 2 chars
            - email must contain '@'
        Return "OK" or "Invalid: <reason>"
    """
    # TODO: Implement class with validation
    pass


class AnimalFactory:
    """
    Task:
        Factory pattern:
            create("dog") → Dog()
            create("cat") → Cat()
            create(anything else) → Animal()
    """
    # TODO: Implement factory method
    pass


class Address:
    """
    Task:
        Attributes: city, country
    """
    # TODO: Implement simple class
    pass


class Customer:
    """
    Task:
        Use COMPOSITION:
            Customer has-an Address
        Method full_info() → "<name> from <city>, <country>"
    """
    # TODO: Implement class
    pass


# =============================================================================
# Optional Testing Area
# =============================================================================

if __name__ == "__main__":
    pass
