"""
Module 9 — OOP: Task Solutions
------------------------------

This file contains clean, professional solutions for all exercises
in OOP_Tasks.py.

Covers:
- Basic classes & methods
- Constructors
- Encapsulation
- Inheritance & polymorphism
- Magic methods
- super()
- Abstract classes
- Composition
- Factory pattern
- Real-world modeling
"""


# =============================================================================
# Rank 1 — Beginner
# =============================================================================

class BasicGreeter:
    def greet(self):
        return "Hello!"


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return f"{self.name} is {self.age} years old"


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# =============================================================================
# Rank 2 — Easy
# =============================================================================

class Student:
    school = "UPBC"

    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"{self.name} studies at {self.school}"


class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def age(self, current_year):
        return current_year - self.year


class Counter:
    def __init__(self):
        self._count = 0

    def increment(self):
        self._count += 1

    def reset(self):
        self._count = 0

    def value(self):
        return self._count


# =============================================================================
# Rank 3 — Intermediate
# =============================================================================

class Animal:
    def speak(self):
        return "Some sound"


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow"


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            return "Insufficient funds"
        self.__balance -= amount

    def get_balance(self):
        return self.__balance


# =============================================================================
# Rank 4 — Advanced
# =============================================================================

class Vehicle:
    def __init__(self, brand):
        self.brand = brand


class ElectricCar(Vehicle):
    def __init__(self, brand, battery_kwh):
        super().__init__(brand)
        self.battery_kwh = battery_kwh


class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"{self.title} ({self.pages} pages)"

    def __len__(self):
        return self.pages


from math import pi
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return pi * self.r * self.r


# =============================================================================
# Rank 5 — Professional
# =============================================================================

class Engine:
    def start(self):
        return "Engine started"


class CarWithEngine:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        return self.engine.start()


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def validate(self):
        if not isinstance(self.name, str) or len(self.name) < 2:
            return "Invalid: name"
        if not isinstance(self.email, str) or "@" not in self.email:
            return "Invalid: email"
        return "OK"


class AnimalFactory:
    @staticmethod
    def create(kind):
        if kind == "dog":
            return Dog()
        if kind == "cat":
            return Cat()
        return Animal()


class Address:
    def __init__(self, city, country):
        self.city = city
        self.country = country


class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address  # Composition

    def full_info(self):
        return f"{self.name} from {self.address.city}, {self.address.country}"


# =============================================================================
# Optional Self-Test Section
# =============================================================================

if __name__ == "__main__":
    print(BasicGreeter().greet())

    p = Person("Peyman", 43)
    print(p.info())

    r = Rectangle(4, 5)
    print("Area:", r.area())

    s = Student("Alice")
    print(s.describe())

    bc = BankAccount("Peyman", 1000)
    bc.deposit(400)
    print("Balance:", bc.get_balance())

    circle = Circle(5)
    print("Circle area:", circle.area())

    engine = Engine()
    car = CarWithEngine(engine)
    print(car.start())

    addr = Address("Mexicali", "Mexico")
    cust = Customer("Peyman", addr)
    print(cust.full_info())
