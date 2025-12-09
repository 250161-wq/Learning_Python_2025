"""
Module 27 — Named Tuples: Solutions
"""

from collections import namedtuple

# Task 1
Car = namedtuple("Car", ["brand", "model", "year"])
my_car = Car("Kia", "Sportage", 2024)

# Task 2
print(my_car.brand, my_car.year)

# Task 3
updated_car = my_car._replace(model="Sportage Turbo")
print(updated_car)

# Task 4
print(my_car._asdict())

# Task 5
Point = namedtuple("Point", ["x", "y"])
p1 = Point(3, 7)
p2 = Point(-2, 10)
print(p1.x, p1.y)
print(p2.x, p2.y)

# Task 6
Student = namedtuple("Student", ["name", "grade", "passed"])
s1 = Student("Ana", 95, True)
s2 = Student("Luis", 70, True)
s3 = Student("Mia", 55, False)
print(s1)
print(s2)
print(s3)

# Task 7
print(s1 == s2)

# Task 8
cars = [
    Car("Kia", "Sportage", 2024),
    Car("Hyundai", "Creta", 2018),
    Car("Toyota", "Corolla", 2020)
]

for car in cars:
    print(car.brand, car.model)

# Task 9
Book = namedtuple("Book", ["title", "author", "year"])
Book.__new__.__defaults__ = (2025,)
my_book = Book("Python Mastery", "Peyman")
print(my_book)

# Task 10
Engine = namedtuple("Engine", ["hp", "type"])
FullCar = namedtuple("FullCar", ["brand", "model", "engine"])

engine_data = Engine(240, "Hybrid")
my_full_car = FullCar("Kia", "Sportage", engine_data)

print(my_full_car.engine.hp)
