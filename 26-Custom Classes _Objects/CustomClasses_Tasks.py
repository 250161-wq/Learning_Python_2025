"""
CustomClasses_Tasks.py
Module 26 — Custom Classes & Objects
Author: Peyman Miyandashti
Year: 2025

Practice exercises for mastering custom Python classes.
Tasks progress from defining simple classes (Rank 1) to building realistic,
professional-level object models (Rank 5).

Instructions:
- Complete all tasks BEFORE checking the solutions file.
- Write your answers under each task.
- Focus on using __init__, instance methods, and clean class design.
"""


# ---------------------------------------------------------------------------
# ⭐ RANK 1 — BEGINNER
# Basic class creation, attributes, and printing.
# ---------------------------------------------------------------------------

# 1. Create a class Person with attributes name and age.

# 2. Create an object p1 = Person("Peyman", 43).

# 3. Print p1.name and p1.age.

# 4. Create a class Dog with an attribute breed.

# 5. Create a Dog object and print its breed.


# ---------------------------------------------------------------------------
# ⭐ RANK 2 — EASY
# Writing methods, modifying attributes, using constructors.
# ---------------------------------------------------------------------------

# 6. Create a class Counter with:
#       - attribute value (start at 0)
#       - method increment() that adds 1
#       - method reset()

# 7. Create a class Student with attributes name and grade.
#       Add a method promote() that increases grade by 1.

# 8. Create a class Rectangle with attributes width and height.
#       Add a method area() that returns width * height.

# 9. Create a class Product with attributes name and price.
#       Add a method apply_discount(percent) that updates the price.

# 10. Create a class LightBulb with:
#       - attribute is_on (start at False)
#       - method turn_on()
#       - method turn_off()


# ---------------------------------------------------------------------------
# ⭐ RANK 3 — INTERMEDIATE
# Special methods, object behavior, multiple attributes.
# ---------------------------------------------------------------------------

# 11. Create a class Book with attributes title, author, pages.
#       Add __str__ to return: "Title by Author (X pages)"

# 12. Create a class BankAccount with:
#       - owner, balance
#       - deposit(amount)
#       - withdraw(amount) with insufficient-funds check

# 13. Create a class Player with:
#       - name, hp
#       - method attack(target, damage)

# 14. Create a class Temperature with Celsius.
#       Add a method to_fahrenheit() that converts correctly.

# 15. Create a class Laptop with attributes brand, ram, storage.
#       Add __repr__ that returns clean debugging information.


# ---------------------------------------------------------------------------
# ⭐ RANK 4 — ADVANCED
# State changes, object interactions, validation, computed values.
# ---------------------------------------------------------------------------

# 16. Create a class Inventory to store products:
#       - internal list items = []
#       - method add(item)
#       - method total_items() returns number of items

# 17. Create a class User with:
#       - username, password
#       - method check_password(pwd)
#       - method change_password(new_pwd)

# 18. Create a class Car with:
#       - brand, fuel
#       - method drive(distance) that reduces fuel
#       - method refuel(amount)

# 19. Create a class GradeBook that:
#       - stores student names and grades in a list of tuples
#       - method add_grade(name, grade)
#       - method average_grade()

# 20. Create a class ShoppingCart that:
#       - holds items as (name, price)
#       - method add_item(name, price)
#       - method total_cost()


# ---------------------------------------------------------------------------
# ⭐ RANK 5 — PROFESSIONAL
# Realistic modeling, multi-class interaction, clean architecture.
# ---------------------------------------------------------------------------

# 21. Create a class Movie with:
#       - title, year, rating
#       - __str__ showing "Title (Year) — Rating/10"

# 22. Create a class Library that:
#       - stores Book objects
#       - method add_book(book)
#       - method list_books()

# 23. Create a class BankSystem:
#       - contains multiple BankAccount objects
#       - method add_account(account)
#       - method total_money()

# 24. Create a class Teacher and class Classroom:
#       - Teacher has name and subject
#       - Classroom has teacher and list of students
#       - method add_student(name)
#       - method info() describing class teacher + students

# 25. Create a class RPGCharacter with:
#       - name, hp, attack_power
#       - method attack(other)
#       - method is_alive()
#       - clean __str__ showing status
