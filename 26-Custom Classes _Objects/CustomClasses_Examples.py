"""
CustomClasses_Examples.py
Module 26 — Custom Classes & Objects
Author: Peyman Miyandashti
Year: 2025

This file contains clear, practical examples demonstrating how to:
- create classes
- define attributes
- write methods
- use the __init__ constructor
- represent objects with __str__ and __repr__
- interact with custom objects
"""


# ---------------------------------------------------------------------------
# Example 1: The simplest possible class
# ---------------------------------------------------------------------------

class EmptyClass:
    pass

obj = EmptyClass()
print(type(obj))


# ---------------------------------------------------------------------------
# Example 2: Class with constructor (__init__)
# ---------------------------------------------------------------------------

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Peyman", 43)
print(p.name, p.age)


# ---------------------------------------------------------------------------
# Example 3: Instance methods
# ---------------------------------------------------------------------------

class Dog:
    def __init__(self, name):
        self.name = name
        self.energy = 50

    def bark(self):
        return f"{self.name} says: Woof!"

    def run(self):
        self.energy -= 10
        return f"{self.name} is running. Energy left: {self.energy}"

d = Dog("Rex")
print(d.bark())
print(d.run())


# ---------------------------------------------------------------------------
# Example 4: Adding methods that change internal state
# ---------------------------------------------------------------------------

class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def reset(self):
        self.value = 0

c = Counter()
c.increment()
c.increment()
print(c.value)  # 2
c.reset()
print(c.value)  # 0


# ---------------------------------------------------------------------------
# Example 5: Custom __str__ and __repr__
# ---------------------------------------------------------------------------

class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def __str__(self):
        return f"{self.brand} ({self.year})"

    def __repr__(self):
        return f"Car(brand={self.brand!r}, year={self.year})"

car = Car("Kia Sportage", 2024)
print(car)
print(repr(car))


# ---------------------------------------------------------------------------
# Example 6: Class with default values
# ---------------------------------------------------------------------------

class Student:
    def __init__(self, name, grade=1):
        self.name = name
        self.grade = grade

    def promote(self):
        self.grade += 1

s = Student("Luis")
print(s.grade)
s.promote()
print(s.grade)


# ---------------------------------------------------------------------------
# Example 7: Methods that take arguments
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
acct.deposit(250)
print(acct.withdraw(100))


# ---------------------------------------------------------------------------
# Example 8: Simple object-to-object interaction
# ---------------------------------------------------------------------------

class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def attack(self, target, damage):
        target.hp -= damage
        return f"{self.name} hit {target.name} for {damage} damage!"

p1 = Player("Hero", 100)
p2 = Player("Monster", 80)

print(p1.attack(p2, 15))
print(f"{p2.name} HP:", p2.hp)


# ---------------------------------------------------------------------------
# Example 9: Updating attributes after creation
# ---------------------------------------------------------------------------

class Profile:
    def __init__(self, username):
        self.username = username
        self.online = False

profile = Profile("Peyman")
profile.online = True
print(profile.username, profile.online)


# ---------------------------------------------------------------------------
# Example 10: A realistic class example
# ---------------------------------------------------------------------------

class Product:
    def __init__(self, name, price, stock=0):
        self.name = name
        self.price = price
        self.stock = stock

    def restock(self, amount):
        self.stock += amount
        return self.stock

    def sell(self, amount):
        if amount > self.stock:
            return "Not enough stock"
        self.stock -= amount
        return f"Sold {amount} units. Remaining: {self.stock}"

item = Product("Keyboard", 750, 10)
print(item.sell(3))
print(item.restock(5))
