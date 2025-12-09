"""
Module 20 — Custom Classes & Objects: Practice Exercises
Comprehensive practice with Python classes and objects, from beginner to
more professional, production-style usage.

In this module I:
- Practice how to define classes and create objects (instances).
- Start from very simple examples (Rank 1) and move toward
  more realistic, professional patterns (Rank 5).
- Use my real personal data (Peyman, Arlette, cars, university, games).

Ranking system:
- Rank 1  -> Beginner: basic class with attributes.
- Rank 2  -> Easy: add simple methods (behaviors).
- Rank 3  -> Intermediate: multiple objects and interactions.
- Rank 4  -> Advanced: type hints, helper methods, and composition.
- Rank 5  -> Professional: clean, reusable, and readable OOP design.

Author: Peyman Miyandashti
Date of Birth: 11/11/1983
ID Number: 250161
Year: 2025
"""

# ===========================================================
# Rank 1 — Beginner
# Simple class with attributes only
# ===========================================================


class SimplePerson:
    """
    Very simple person model (beginner level).

    - Only stores data.
    - No real behavior yet.
    """

    def __init__(self, first_name, last_name, age, city, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.country = country


print("Rank 1 — Beginner")

pey_man_simple = SimplePerson(
    first_name="Peyman",
    last_name="Miyandashti",
    age=43,
    city="Mexicali",
    country="Mexico",
)

print("First name:", pey_man_simple.first_name)
print("Last name:", pey_man_simple.last_name)
print("Age:", pey_man_simple.age)
print("City:", pey_man_simple.city)
print("Country:", pey_man_simple.country)
print("-" * 50)


# ===========================================================
# Rank 2 — Easy
# Class with a method that returns formatted info
# ===========================================================


class PersonWithIntro:
    """
    Person with a simple introduction method.
    """

    def __init__(
        self,
        first_name: str,
        last_name: str,
        age: int,
        nationality: str,
        current_city: str,
        current_country: str,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.nationality = nationality
        self.current_city = current_city
        self.current_country = current_country

    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def introduce(self) -> str:
        return (
            f"Hi, my name is {self.full_name()}. "
            f"I am {self.age} years old, I am from {self.nationality}, "
            f"and I currently live in {self.current_city}, {self.current_country}."
        )


print("Rank 2 — Easy")

pey_man_intro = PersonWithIntro(
    first_name="Peyman",
    last_name="Miyandashti",
    age=43,
    nationality="Iran (Tabriz City)",
    current_city="Mexicali",
    current_country="Mexico",
)

print(pey_man_intro.introduce())
print("Full name:", pey_man_intro.full_name())
print("-" * 50)


# ===========================================================
# Rank 3 — Intermediate
# Multiple classes and simple relationships
# (Person + Car + Game)
# ===========================================================


class Car:
    """
    Basic car model.
    """

    def __init__(self, brand: str, model: str, year: int, color: str):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def label(self) -> str:
        return f"{self.year} {self.brand} {self.model} ({self.color})"


class FavoriteGame:
    """
    Simple model for a favorite game.
    """

    def __init__(self, title: str, genre: str, platform: str | None = None):
        self.title = title
        self.genre = genre
        self.platform = platform or "PC"

    def description(self) -> str:
        return f"{self.title} — genre: {self.genre}, platform: {self.platform}"


class GamerPerson:
    """
    Person who likes games and has a car.
    """

    def __init__(
        self,
        name: str,
        age: int,
        favorite_color: str,
        favorite_game: FavoriteGame,
        car: Car,
    ):
        self.name = name
        self.age = age
        self.favorite_color = favorite_color
        self.favorite_game = favorite_game
        self.car = car

    def short_profile(self) -> str:
        return (
            f"{self.name}, {self.age} years old, loves {self.favorite_color}, "
            f"drives a {self.car.label()}, and plays {self.favorite_game.title}."
        )


print("Rank 3 — Intermediate")

pey_man_game = FavoriteGame(
    title="World of Warcraft",
    genre="MMORPG",
    platform="PC",
)

pey_man_car = Car(
    brand="Kia",
    model="Sportage",
    year=2024,
    color="Dark Gray",
)

pey_man_gamer = GamerPerson(
    name="Peyman Miyandashti",
    age=43,
    favorite_color="Red",
    favorite_game=pey_man_game,
    car=pey_man_car,
)

print(pey_man_gamer.short_profile())
print("Game details:", pey_man_game.description())
print("Car label:", pey_man_car.label())
print("-" * 50)


# ===========================================================
# Rank 4 — Advanced
# University & Student classes (composition + helper methods)
# ===========================================================


class University:
    """
    Represents a university.
    """

    def __init__(self, name: str, city: str, country: str):
        self.name = name
        self.city = city
        self.country = country

    def full_location(self) -> str:
        return f"{self.name} — {self.city}, {self.country}"


class Student:
    """
    Represents a student in a degree program.
    """

    def __init__(
        self,
        full_name: str,
        age: int,
        program: str,
        university: University,
        total_credits: int,
        completed_credits: int,
        marital_status: str,
    ):
        self.full_name = full_name
        self.age = age
        self.program = program
        self.university = university
        self.total_credits = total_credits
        self.completed_credits = completed_credits
        self.marital_status = marital_status

    def remaining_credits(self) -> int:
        remaining = self.total_credits - self.completed_credits
        return max(remaining, 0)

    def completion_percentage(self) -> float:
        if self.total_credits == 0:
            return 0.0
        return (self.completed_credits / self.total_credits) * 100

    def basic_summary(self) -> str:
        return (
            f"Student: {self.full_name}\n"
            f"Age: {self.age}\n"
            f"Program: {self.program}\n"
            f"University: {self.university.full_location()}\n"
            f"Marital status: {self.marital_status}\n"
            f"Credits: {self.completed_credits}/{self.total_credits} "
            f"({self.completion_percentage():.1f}%)\n"
        )


print("Rank 4 — Advanced")

upbc = University(
    name="Polytechnic Baja California University (UPBC)",
    city="Mexicali",
    country="Mexico",
)

pey_man_student = Student(
    full_name="Peyman Miyandashti",
    age=43,
    program="Information Technology Engineering and Digital Innovation",
    university=upbc,
    total_credits=300,      # example
    completed_credits=72,   # example
    marital_status="Married",
)

print(pey_man_student.basic_summary())
print("Remaining credits:", pey_man_student.remaining_credits())
print("Completion percentage:", f"{pey_man_student.completion_percentage():.2f}%")
print("-" * 50)


# ===========================================================
# Rank 5 — Professional
# Clean OOP model with:
# - separate Person class
# - Teacher class extending Person
# - nice __repr__ methods
# - method that builds a mini "family profile"
# ===========================================================


class Person:
    """
    More professional Person class with __repr__.
    """

    def __init__(
        self,
        first_name: str,
        last_name: str,
        age: int,
        city: str,
        country: str,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.country = country

    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def short_location(self) -> str:
        return f"{self.city}, {self.country}"

    def __repr__(self) -> str:
        return (
            f"Person(full_name={self.full_name()!r}, "
            f"age={self.age}, location={self.short_location()!r})"
        )


class Teacher(Person):
    """
    Teacher is a specialized Person with a profession and car.
    """

    def __init__(
        self,
        first_name: str,
        last_name: str,
        age: int,
        city: str,
        country: str,
        subject: str,
        car: Car | None = None,
    ):
        super().__init__(first_name, last_name, age, city, country)
        self.subject = subject
        self.car = car

    def teacher_profile(self) -> str:
        base = (
            f"{self.full_name()} is a {self.subject} teacher "
            f"in {self.short_location()} (age: {self.age})."
        )
        if self.car is not None:
            base += f" Drives a {self.car.label()}."
        return base


class FamilyProfile:
    """
    Professional-style class that uses other objects
    to build a readable summary.
    """

    def __init__(self, husband: Person, wife: Teacher, favorite_game: FavoriteGame):
        self.husband = husband
        self.wife = wife
        self.favorite_game = favorite_game

    def build_summary(self) -> str:
        summary = (
            "Family Profile\n"
            "==============\n"
            f"Husband: {self.husband.full_name()} ({self.husband.age} years old)\n"
            f"  Location: {self.husband.short_location()}\n"
            f"  Favorite game: {self.favorite_game.title}\n"
            "\n"
            f"Wife: {self.wife.full_name()} ({self.wife.age} years old)\n"
            f"  Profession: Teacher ({self.wife.subject})\n"
            f"  Location: {self.wife.short_location()}\n"
        )
        if self.wife.car is not None:
            summary += f"  Car: {self.wife.car.label()}\n"

        return summary


print("Rank 5 — Professional")

pey_man_person = Person(
    first_name="Peyman",
    last_name="Miyandashti",
    age=43,
    city="Mexicali",
    country="Mexico",
)

arlette_car = Car(
    brand="Hyundai",
    model="Creta",
    year=2018,
    color="Unknown",
)

arlette_teacher = Teacher(
    first_name="Arlette",
    last_name="Chong",
    age=47,
    city="Mexicali",
    country="Mexico",
    subject="Secondary Education",
    car=arlette_car,
)

family = FamilyProfile(
    husband=pey_man_person,
    wife=arlette_teacher,
    favorite_game=pey_man_game,
)

print("Debug __repr__ for Peyman Person object:")
print(pey_man_person)  # uses __repr__
print()
print(family.build_summary())
print("-" * 50)
