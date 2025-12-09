"""
Module 9 — OOP: Practical Examples
----------------------------------

This file contains runnable examples demonstrating Python's
Object-Oriented Programming concepts.

Examples progress from Rank 1 → Rank 5:
- Rank 1: Basic classes, attributes, methods
- Rank 2: Constructors, instance vs class attributes
- Rank 3: Inheritance, overriding, encapsulation
- Rank 4: super(), magic methods, abstract classes
- Rank 5: Professional OOP design with composition & factories
"""


# ============================================================================
# Rank 1 — Beginner Examples
# ============================================================================

def example_1_basic_class():
    """Simple class with one method."""

    class Greeter:
        def say_hello(self):
            return "Hello!"

    g = Greeter()
    print(g.say_hello())


def example_2_attributes():
    """Class with attributes defined in __init__."""

    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def info(self):
            return f"{self.name}, {self.age} years old"

    p = Person("Peyman", 43)
    print(p.info())


# ============================================================================
# Rank 2 — Easy Examples
# ============================================================================

def example_3_instance_vs_class_attributes():
    """Illustrate the difference between class and instance attributes."""

    class Student:
        school = "UPBC"  # class attribute

        def __init__(self, name):
            self.name = name  # instance attribute

    s1 = Student("Alice")
    s2 = Student("Bob")

    print(s1.name, "-", s1.school)
    print(s2.name, "-", s2.school)


def example_4_updating_attributes():
    """Modify attributes after creation."""

    class Car:
        def __init__(self, brand, year):
            self.brand = brand
            self.year = year

    c = Car("Kia Sportage", 2024)
    print("Before:", c.brand, c.year)

    c.year = 2025
    print("After:", c.brand, c.year)


# ============================================================================
# Rank 3 — Intermediate Examples
# ============================================================================

def example_5_inheritance():
    """Basic inheritance example."""

    class Animal:
        def speak(self):
            return "Some sound"

    class Dog(Animal):
        def speak(self):
            return "Woof!"

    a = Animal()
    d = Dog()

    print(a.speak())
    print(d.speak())


def example_6_encapsulation():
    """Use private attributes with getters/setters."""

    class BankAccount:
        def __init__(self, owner, balance):
            self.owner = owner
            self.__balance = balance

        def deposit(self, amount):
            self.__balance += amount

        def get_balance(self):
            return self.__balance

    acc = BankAccount("Peyman", 1000)
    acc.deposit(500)
    print("Balance:", acc.get_balance())


def example_7_polymorphism():
    """Polymorphism using method overriding."""

    class Animal:
        def speak(self):
            return "..."

    class Cat(Animal):
        def speak(self):
            return "Meow"

    class Dog(Animal):
        def speak(self):
            return "Woof"

    animals = [Cat(), Dog(), Animal()]
    for a in animals:
        print(a.speak())


# ============================================================================
# Rank 4 — Advanced Examples
# ============================================================================

def example_8_super_constructor():
    """Using super() to call parent class constructor."""

    class Vehicle:
        def __init__(self, brand):
            self.brand = brand

    class Car(Vehicle):
        def __init__(self, brand, year):
            super().__init__(brand)
            self.year = year

    c = Car("Toyota", 2023)
    print(c.brand, c.year)


def example_9_magic_methods():
    """Magic methods: __str__, __len__, operator overloading."""

    class Book:
        def __init__(self, title, pages):
            self.title = title
            self.pages = pages

        def __str__(self):
            return f"{self.title} ({self.pages} pages)"

        def __len__(self):
            return self.pages

        def __add__(self, other):
            return self.pages + other.pages

    b1 = Book("Python 101", 300)
    b2 = Book("Advanced Python", 200)

    print(str(b1))
    print("Total pages:", b1 + b2)


def example_10_abstract_classes():
    """Using an abstract base class."""

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

    r = Rectangle(5, 4)
    print("Area:", r.area())


# ============================================================================
# Rank 5 — Professional Examples
# ============================================================================

def example_11_composition():
    """Composition: A class containing another class."""

    class Engine:
        def start(self):
            return "Engine started"

    class Car:
        def __init__(self, engine):
            self.engine = engine

        def start(self):
            return self.engine.start()

    e = Engine()
    c = Car(e)
    print(c.start())


def example_12_factory_pattern():
    """Factory method returning different subclasses based on input."""

    class Animal:
        def speak(self):
            return "..."

    class Dog(Animal):
        def speak(self):
            return "Woof"

    class Cat(Animal):
        def speak(self):
            return "Meow"

    def animal_factory(kind):
        if kind == "dog":
            return Dog()
        elif kind == "cat":
            return Cat()
        else:
            return Animal()

    a1 = animal_factory("dog")
    a2 = animal_factory("cat")
    a3 = animal_factory("unknown")

    print(a1.speak(), a2.speak(), a3.speak())


def example_13_real_world_model():
    """Professional OOP example modeling a user + address."""

    class Address:
        def __init__(self, city, country):
            self.city = city
            self.country = country

    class User:
        def __init__(self, name, age, address):
            self.name = name
            self.age = age
            self.address = address  # composition

        def profile(self):
            return f"{self.name}, {self.age}, lives in {self.address.city}"

    addr = Address("Mexicali", "Mexico")
    user = User("Peyman", 43, addr)
    print(user.profile())


# ---------------------------------------------------------------------------
# Run all examples
# ---------------------------------------------------------------------------

def main():
    print("\n--- Rank 1 ---")
    example_1_basic_class()
    example_2_attributes()

    print("\n--- Rank 2 ---")
    example_3_instance_vs_class_attributes()
    example_4_updating_attributes()

    print("\n--- Rank 3 ---")
    example_5_inheritance()
    example_6_encapsulation()
    example_7_polymorphism()

    print("\n--- Rank 4 ---")
    example_8_super_constructor()
    example_9_magic_methods()
    example_10_abstract_classes()

    print("\n--- Rank 5 ---")
    example_11_composition()
    example_12_factory_pattern()
    example_13_real_world_model()


if __name__ == "__main__":
    main()
