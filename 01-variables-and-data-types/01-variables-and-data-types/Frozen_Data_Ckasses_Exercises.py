"""
Module 29 — Frozen Data Classes: Practice Exercises
Comprehensive practice with Python frozen data classes, from beginner to
more professional, production-style usage.

In this module I:
- Practice how to create and use @dataclass(frozen=True).
- Learn immutability rules and how to modify using replace().
- Understand how frozen data classes behave in real applications.
- Move from very simple use cases (Rank 1) to clean,
  production-grade patterns (Rank 5).

Ranking system:
- Rank 1  -> Beginner: basic frozen class creation.
- Rank 2  -> Easy: immutability errors & replace().
- Rank 3  -> Intermediate: hashing, equality, dictionary keys.
- Rank 4  -> Advanced: nested frozen classes, safe updates.
- Rank 5  -> Professional: configuration, caching, value objects.

Author: Peyman Miyandashti
Date of Birth: 11/11/1983
ID Number: 250161
Year: 2025
"""

from dataclasses import dataclass, replace, asdict
from typing import Dict


# ===========================================================
# Rank 1 — Beginner
# Basic frozen data class and attribute access
# ===========================================================

print("Rank 1 — Beginner")


@dataclass(frozen=True)
class User:
    username: str
    age: int


user = User(username="peyman250", age=41)

print("User:", user)
print("Username:", user.username)
print("Age:", user.age)

# Attempting to modify will raise an error (demonstration)
try:
    user.age = 42  # ❌ cannot modify frozen class
except Exception as e:
    print("Error on modification (expected):", e)

print("-" * 50)


# ===========================================================
# Rank 2 — Easy
# replace() usage and default values in frozen classes
# ===========================================================

print("Rank 2 — Easy")


@dataclass(frozen=True)
class Product:
    name: str
    price: float
    in_stock: bool = True


p1 = Product("Keyboard", 599.0)
p2 = replace(p1, price=499.0)  # create a modified copy

print("Original product:", p1)
print("Updated price product:", p2)

print("-" * 50)


# ===========================================================
# Rank 3 — Intermediate
# Frozen classes as dictionary keys & hashing behavior
# ===========================================================

print("Rank 3 — Intermediate")


@dataclass(frozen=True)
class Coordinate:
    x: int
    y: int


a = Coordinate(1, 2)
b = Coordinate(1, 2)
c = Coordinate(5, 9)

coords_dict: Dict[Coordinate, str] = {
    a: "Origin-ish",
    c: "Far point",
}

print("Coordinate A equals B? ->", a == b)
print("Dict lookup using coordinate A:", coords_dict[a])
print("Dict lookup using coordinate C:", coords_dict[c])

# Confirm hashing behavior
print("Hashes:", hash(a), hash(b), hash(c))

print("-" * 50)


# ===========================================================
# Rank 4 — Advanced
# Nested frozen classes & safe update patterns
# ===========================================================

print("Rank 4 — Advanced")


@dataclass(frozen=True)
class Engine:
    hp: int
    type: str  # "Hybrid", "Gas", "Electric"


@dataclass(frozen=True)
class Car:
    brand: str
    model: str
    engine: Engine


engine_v1 = Engine(hp=240, type="Hybrid")
car_v1 = Car(brand="KIA", model="Sportage", engine=engine_v1)

# To “update” nested values, rebuild using replace()
engine_v2 = replace(engine_v1, hp=260)
car_v2 = replace(car_v1, engine=engine_v2)

print("Car (original):", car_v1)
print("Car (updated engine):", car_v2)

print("-" * 50)


# ===========================================================
# Rank 5 — Professional
# Frozen data classes as configuration objects used in apps
# ===========================================================

print("Rank 5 — Professional")


@dataclass(frozen=True)
class AppConfig:
    """
    A real-world style immutable configuration object.

    Frozen classes are ideal for:
    - Settings that should never change at runtime
    - Cache keys
    - Value objects
    - Ensuring program stability
    """
    app_name: str
    version: str
    debug: bool
    api_url: str
    retries: int = 3


default_config = AppConfig(
    app_name="SchoolManager",
    version="2.0.0",
    debug=True,
    api_url="https://api.schoolmanager.com",
)

# Convert to dict (for JSON, logging, etc.)
config_dict = asdict(default_config)

# Create a production-safe version
production_config = replace(default_config, debug=False)

print("Default config:", default_config)
print("As dict:", config_dict)
print("Production config:", production_config)

print("-" * 50)
