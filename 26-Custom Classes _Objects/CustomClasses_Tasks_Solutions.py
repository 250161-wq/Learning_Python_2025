"""
CustomClasses_Tasks_Solutions.py
Module 26 — Custom Classes & Objects
Author: Peyman Miyandashti
Year: 2025

Solutions to all class/object exercises.
Use this file ONLY after attempting the tasks yourself.
"""


# ---------------------------------------------------------------------------
# ⭐ RANK 1 — BEGINNER
# ---------------------------------------------------------------------------

# 1–3.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Peyman", 43)

# 4–5.
class Dog:
    def __init__(self, breed):
        self.breed = breed

d1 = Dog("German Shepherd")


# ---------------------------------------------------------------------------
# ⭐ RANK 2 — EASY
# ---------------------------------------------------------------------------

# 6.
class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def reset(self):
        self.value = 0


# 7.
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def promote(self):
        self.grade += 1


# 8.
class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        return self.width * self.height


# 9.
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self, percent):
        self.price -= self.price * (percent / 100)
        return self.price


# 10.
class LightBulb:
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False


# ---------------------------------------------------------------------------
# ⭐ RANK 3 — INTERMEDIATE
# ---------------------------------------------------------------------------

# 11.
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author} ({self.pages} pages)"


# 12.
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


# 13.
class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def attack(self, target, damage):
        target.hp -= damage
        return f"{self.name} attacked {target.name} for {damage} damage!"


# 14.
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32


# 15.
class Laptop:
    def __init__(self, brand, ram, storage):
        self.brand = brand
        self.ram = ram
        self.storage = storage

    def __repr__(self):
        return f"Laptop(brand={self.brand!r}, ram={self.ram}, storage={self.storage})"


# ---------------------------------------------------------------------------
# ⭐ RANK 4 — ADVANCED
# ---------------------------------------------------------------------------

# 16.
class Inventory:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def total_items(self):
        return len(self.items)


# 17.
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_password(self, pwd):
        return pwd == self.password

    def change_password(self, new_pwd):
        self.password = new_pwd


# 18.
class Car:
    def __init__(self, brand, fuel):
        self.brand = brand
        self.fuel = fuel

    def drive(self, distance):
        self.fuel -= distance
        if self.fuel < 0:
            self.fuel = 0
        return self.fuel

    def refuel(self, amount):
        self.fuel += amount
        return self.fuel


# 19.
class GradeBook:
    def __init__(self):
        self.records = []  # list of (name, grade)

    def add_grade(self, name, grade):
        self.records.append((name, grade))

    def average_grade(self):
        if not self.records:
            return 0
        total = sum(g for _, g in self.records)
        return total / len(self.records)


# 20.
class ShoppingCart:
    def __init__(self):
        self.items = []  # (name, price)

    def add_item(self, name, price):
        self.items.append((name, price))

    def total_cost(self):
        return sum(price for _, price in self.items)


# ---------------------------------------------------------------------------
# ⭐ RANK 5 — PROFESSIONAL
# ---------------------------------------------------------------------------

# 21.
class Movie:
    def __init__(self, title, year, rating):
        self.title = title
        self.year = year
        self.rating = rating

    def __str__(self):
        return f"{self.title} ({self.year}) — {self.rating}/10"


# 22.
class Library:
    def __init__(self):
        self.books = []  # list of Book objects

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        return [str(book) for book in self.books]


# 23.
class BankSystem:
    def __init__(self):
        self.accounts = []  # list of BankAccount objects

    def add_account(self, account):
        self.accounts.append(account)

    def total_money(self):
        return sum(acc.balance for acc in self.accounts)


# 24.
class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

class Classroom:
    def __init__(self, teacher):
        self.teacher = teacher
        self.students = []

    def add_student(self, name):
        self.students.append(name)

    def info(self):
        return f"Teacher: {self.teacher.name} ({self.teacher.subject}), Students: {', '.join(self.students)}"


# 25.
class RPGCharacter:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def attack(self, other):
        other.hp -= self.attack_power
        return f"{self.name} attacked {other.name} for {self.attack_power} damage!"

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name} — HP: {self.hp}, ATK: {self.attack_power}"
