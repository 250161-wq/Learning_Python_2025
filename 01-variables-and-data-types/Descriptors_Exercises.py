"""
Module 43 — Descriptors: Practice Exercises
Comprehensive practice with Python descriptors, from beginner
to more professional, production-style usage.

In this module I:
- Understand the descriptor protocol (__get__, __set__, __delete__).
- Create simple read/write descriptors.
- Build validation descriptors for strong attribute control.
- Use descriptors to create computed fields and cached values.
- Build a professional-grade "field" system similar to ORM models.

Ranking system:
- Rank 1  -> Beginner: understanding what a descriptor is.
- Rank 2  -> Easy: simple read/write descriptor.
- Rank 3  -> Intermediate: validation descriptors.
- Rank 4  -> Advanced: computed & cached descriptors.
- Rank 5  -> Professional: mini ORM-like field model using descriptors.

Author: Peyman Miyandashti
Date of Birth: 11/11/1983
ID Number: 250161
Year: 2025
"""

from __future__ import annotations
from typing import Any, Dict
import math


# ===========================================================
# Rank 1 — Beginner
# What is a descriptor?
# ===========================================================

print("Rank 1 — Beginner")

class SimpleDescriptor:
    """
    Minimal descriptor demonstrating __get__ and __set__.
    """

    def __init__(self):
        self.value = None

    def __get__(self, instance, owner):
        print(f"__get__ called on {self} for instance={instance}")
        return self.value

    def __set__(self, instance, value):
        print(f"__set__ called on {self} for instance={instance} value={value}")
        self.value = value


class Demo:
    field = SimpleDescriptor()


d = Demo()
d.field = 10     # triggers __set__
x = d.field      # triggers __get__

print("d.field:", x)
print("-" * 50)


# ===========================================================
# Rank 2 — Easy
# Descriptor storing values per-instance
# ===========================================================

print("Rank 2 — Easy")

class InstanceStorage:
    """
    Descriptor that stores values *on each instance*,
    not on the descriptor itself.
    """

    def __init__(self, name: str):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Person:
    age = InstanceStorage("age")
    name = InstanceStorage("name")


p1 = Person()
p2 = Person()

p1.name = "Peyman"
p2.name = "Ana"

p1.age = 41
p2.age = 20

print("p1:", p1.name, p1.age)
print("p2:", p2.name, p2.age)
print("-" * 50)


# ===========================================================
# Rank 3 — Intermediate
# Validation descriptors
# ===========================================================

print("Rank 3 — Intermediate")

class PositiveNumber:
    """
    Ensures attribute value must be a positive number.
    """

    def __set_name__(self, owner, name):
        self.private_name = f"_{name}"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.private_name, None)

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be numeric")
        if value <= 0:
            raise ValueError("Value must be positive")
        setattr(instance, self.private_name, value)


class Student:
    score = PositiveNumber()
    height = PositiveNumber()


s = Student()
s.score = 95
s.height = 1.75

print("Student:", s.score, s.height)

try:
    s.score = -10
except Exception as e:
    print("Error:", e)

print("-" * 50)


# ===========================================================
# Rank 4 — Advanced
# Computed & cached descriptors
# ===========================================================

print("Rank 4 — Advanced")

class CachedProperty:
    """
    Descriptor that computes a value once and caches it.
    Similar to functools.cached_property.
    """

    def __init__(self, func):
        self.func = func
        self.private_name = f"_{func.__name__}"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.private_name not in instance.__dict__:
            instance.__dict__[self.private_name] = self.func(instance)
        return instance.__dict__[self.private_name]


class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    @CachedProperty
    def area(self):
        print("Computing area...")
        return math.pi * (self.radius ** 2)

    @CachedProperty
    def circumference(self):
        print("Computing circumference...")
        return 2 * math.pi * self.radius


c = Circle(10)
print("Area first:", c.area)
print("Area second (cached):", c.area)

print("Circ first:", c.circumference)
print("Circ second (cached):", c.circumference)

print("-" * 50)


# ===========================================================
# Rank 5 — Professional
# Mini ORM-like field model with descriptors
# ===========================================================

print("Rank 5 — Professional")

class Field:
    """
    Base descriptor for ORM fields.
    """

    def __init__(self):
        self.private_name = None

    def __set_name__(self, owner, name):
        self.private_name = f"_{name}"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.private_name)

    def __set__(self, instance, value):
        instance.__dict__[self.private_name] = self.validate(value)

    def validate(self, value):
        return value


class IntegerField(Field):
    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError("Expected int")
        return value


class StringField(Field):
    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected string")
        return value


class PositiveIntegerField(Field):
    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError("Expected int")
        if value <= 0:
            raise ValueError("Expected a positive integer")
        return value


class Model:
    """
    Base ORM model that uses descriptors as field definitions.
    """

    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)


class User(Model):
    id = PositiveIntegerField()
    name = StringField()
    age = IntegerField()


u = User(id=1, name="Peyman", age=41)
print("User:", u.id, u.name, u.age)

try:
    u.age = "not a number"
except Exception as e:
    print("Error:", e)

try:
    u.id = -5
except Exception as e:
    print("Error:", e)

print("-" * 50)
