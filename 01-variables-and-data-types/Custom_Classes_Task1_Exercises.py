"""
Module 20 — Custom Classes & Objects: Practice Exercises
Comprehensive practice with Python classes and objects, from beginner to
more professional, production-style usage.

In this module I:
- Practice how to define classes and create objects (instances).
- Add attributes, instance methods, class methods, and properties.
- Use objects to model real-world things from my own life (Peyman).
- Move from very simple classes (Rank 1) to clean, reusable designs (Rank 5).

Ranking system:
- Rank 1  -> Beginner: basic class definition and attributes.
- Rank 2  -> Easy: methods that use and modify object state.
- Rank 3  -> Intermediate: collections of objects and simple analysis.
- Rank 4  -> Advanced: classmethods, staticmethods, and properties.
- Rank 5  -> Professional: small, realistic object model with clean design.

Author: Peyman Miyandashti
Date of Birth: 11/11/1983
ID Number: 250161
Year: 2025
"""

# ===========================================================
# Rank 1 — Beginner
# Simple class with attributes, creating one object
# ===========================================================


class SimplePerson:
    """Very simple Person model with only attributes, no methods."""

    def __init__(self, first_name: str, last_name: str, age: int, city: str, country: str):
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
# Methods that use and modify the internal state of an object
# ===========================================================


class GameProfile:
    """
    Model a simple game profile for Peyman as a player.
    """

    def __init__(self, player_name: str, favorite_game: str, level: int = 1):
        self.player_name = player_name
        self.favorite_game = favorite_game
        self.level = level
        self.hours_played = 0

    def add_play_time(self, hours: int) -> None:
        """Add hours to the total hours played."""
        if hours > 0:
            self.hours_played += hours

    def level_up(self, levels: int = 1) -> None:
        """Increase level by a given amount."""
        if levels > 0:
            self.level += levels

    def summary(self) -> str:
        """Return a short text summary of the game profile."""
        return (
            f"Player: {self.player_name} | Game: {self.favorite_game} | "
            f"Level: {self.level} | Hours played: {self.hours_played}"
        )


print("Rank 2 — Easy")

pey_man_game = GameProfile(
    player_name="Peyman Miyandashti",
    favorite_game="World of Warcraft",
    level=25,
)

pey_man_game.add_play_time(5)
pey_man_game.add_play_time(3)
pey_man_game.level_up(2)

print(pey_man_game.summary())
print("-" * 50)


# ===========================================================
# Rank 3 — Intermediate
# Multiple objects, lists of objects, and simple analysis
# ===========================================================


class Car:
    """Simple car model using integer year, showing basic object usage."""

    def __init__(self, brand: str, model: str, color: str, year: int, owner_name: str):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year
        self.owner_name = owner_name

    def age(self, current_year: int) -> int:
        """Return how old the car is based on the current year."""
        return current_year - self.year

    def description(self, current_year: int) -> str:
        """Return text description of this car."""
        return (
            f"{self.brand} {self.model} ({self.color}, {self.year}) "
            f"owned by {self.owner_name}, age: {self.age(current_year)} years"
        )


print("Rank 3 — Intermediate")

current_year = 2025

pey_man_car = Car(
    brand="Kia",
    model="Sportage",
    color="Dark Gray",
    year=2024,
    owner_name="Peyman Miyandashti",
)

arlette_car = Car(
    brand="Hyundai",
    model="Creta",
    color="White",  # not specified, so we pick a reasonable example
    year=2018,
    owner_name="Arlette Chong",
)

cars = [pey_man_car, arlette_car]

for car in cars:
    print(car.description(current_year))

# Simple analysis with objects
oldest_car = min(cars, key=lambda c: c.year)
newest_car = max(cars, key=lambda c: c.year)

print("Oldest car owner:", oldest_car.owner_name, "-", oldest_car.brand, oldest_car.model)
print("Newest car owner:", newest_car.owner_name, "-", newest_car.brand, newest_car.model)
print("-" * 50)


# ===========================================================
# Rank 4 — Advanced
# Classmethods, staticmethods, and properties
# ===========================================================


class Student:
    """
    More advanced Student model for Peyman at UPBC.

    Demonstrates:
    - classmethod as an alternative constructor
    - staticmethod for utility
    - @property for computed attributes
    """

    university_name = "Polytechnic Baja California University (UPBC)"

    def __init__(
        self,
        first_name: str,
        last_name: str,
        program: str,
        current_year: int,
        start_year: int,
        age: int,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.program = program
        self.current_year = current_year
        self.start_year = start_year
        self.age = age

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @property
    def years_studied(self) -> int:
        return max(self.current_year - self.start_year, 0)

    @classmethod
    def from_dict(cls, data: dict) -> "Student":
        """Build a Student instance from a dictionary."""
        return cls(
            first_name=data["first_name"],
            last_name=data["last_name"],
            program=data["program"],
            current_year=data["current_year"],
            start_year=data["start_year"],
            age=data["age"],
        )

    @staticmethod
    def is_adult(age: int) -> bool:
        """Check if a given age is considered an adult (18+)."""
        return age >= 18

    def summary(self) -> str:
        """Return a formatted summary of the student."""
        return (
            f"Student: {self.full_name}\n"
            f"University: {self.university_name}\n"
            f"Program: {self.program}\n"
            f"Age: {self.age}\n"
            f"Years studied so far: {self.years_studied}\n"
            f"Adult?: {self.is_adult(self.age)}"
        )


print("Rank 4 — Advanced")

pey_man_student_data = {
    "first_name": "Peyman",
    "last_name": "Miyandashti",
    "program": "Information Technology Engineering and Digital Innovation",
    "current_year": 2025,
    "start_year": 2023,
    "age": 43,
}

pey_man_student = Student.from_dict(pey_man_student_data)

print(pey_man_student.summary())
print("-" * 50)


# ===========================================================
# Rank 5 — Professional
# Small, realistic object model with clean design
# (Person + Profile + simple “database” manager)
# ===========================================================


class Person:
    """
    Base Person class to represent Peyman, Arlette, etc.
    Used as a building block for other objects.
    """

    def __init__(
        self,
        first_name: str,
        last_name: str,
        age: int,
        city: str,
        country: str,
        is_married: bool,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.country = country
        self.is_married = is_married

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def move_to(self, new_city: str, new_country: str) -> None:
        """Update the person's location."""
        self.city = new_city
        self.country = new_country

    def __repr__(self) -> str:
        return (
            f"Person(full_name={self.full_name!r}, age={self.age}, "
            f"city={self.city!r}, country={self.country!r})"
        )


class FamilyProfile:
    """
    Represents a small family profile (Peyman + spouse, etc.).

    Shows:
    - Composition of objects (Person inside FamilyProfile)
    - Methods that calculate statistics
    """

    def __init__(self, head_of_family: Person):
        self.head_of_family = head_of_family
        self.members = [head_of_family]

    def add_member(self, person: Person) -> None:
        self.members.append(person)

    @property
    def size(self) -> int:
        return len(self.members)

    @property
    def average_age(self) -> float:
        if not self.members:
            return 0.0
        total = sum(member.age for member in self.members)
        return total / len(self.members)

    def describe_family(self) -> str:
        lines = [
            f"Head of family: {self.head_of_family.full_name}",
            f"Family size: {self.size}",
            f"Average age: {self.average_age:.1f}",
            "Members:",
        ]
        for member in self.members:
            lines.append(
                f" - {member.full_name}, {member.age} years old, "
                f"living in {member.city}, {member.country}"
            )
        return "\n".join(lines)


print("Rank 5 — Professional")

pey_man_person = Person(
    first_name="Peyman",
    last_name="Miyandashti",
    age=43,
    city="Mexicali",
    country="Mexico",
    is_married=True,
)

arlette_person = Person(
    first_name="Arlette",
    last_name="Chong",
    age=47,
    city="Mexicali",
    country="Mexico",
    is_married=True,
)

pey_man_family = FamilyProfile(head_of_family=pey_man_person)
pey_man_family.add_member(arlette_person)

print(pey_man_family.describe_family())
print("-" * 50)
