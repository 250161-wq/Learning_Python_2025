"""
Module 39 — Type Objects: Practice Exercises
Comprehensive practice with Python’s type objects, from beginner
to more professional, production-style usage.

In this module I:
- Understand that everything in Python is an object, including types.
- Use `type()` to inspect and dynamically create objects.
- Compare built-in types vs custom classes.
- Use `isinstance` and `issubclass` in professional validation patterns.
- Dynamically generate new classes with `type(name, bases, dict)`.
- Build a small plugin/registry system that uses type objects.

Ranking system:
- Rank 1  -> Beginner: inspect objects and their types.
- Rank 2  -> Easy: type comparisons and validation helpers.
- Rank 3  -> Intermediate: isinstance / issubclass patterns.
- Rank 4  -> Advanced: dynamic class creation with type().
- Rank 5  -> Professional: plugin/registry system powered by type objects.

Author: Peyman Miyandashti
Date of Birth: 11/11/1983
ID Number: 250161
Year: 2025
"""

from __future__ import annotations
from typing import Any, Dict, Type, List


# ===========================================================
# Rank 1 — Beginner
# Basic type inspection
# ===========================================================

print("Rank 1 — Beginner")

x = 10
y = 3.14
z = "Peyman"
lst = [1, 2, 3]

print(type(x))     # <class 'int'>
print(type(y))     # <class 'float'>
print(type(z))     # <class 'str'>
print(type(lst))   # <class 'list'>

# One fact: every type is itself an instance of `type`
print(type(int))       # <class 'type'>
print(type(str))       # <class 'type'>
print(type(list))      # <class 'type'>
print(type(type))      # <class 'type'>

print("-" * 50)


# ===========================================================
# Rank 2 — Easy
# Using types for comparisons and simple validation
# ===========================================================

print("Rank 2 — Easy")

def ensure_type(value: Any, expected_type: Type) -> None:
    if type(value) is not expected_type:
        print(f"Type mismatch! Expected {expected_type.__name__}, got {type(value).__name__}")
    else:
        print(f"Correct type: {expected_type.__name__}")

ensure_type(10, int)
ensure_type("hello", int)
ensure_type(3.14, float)

print("-" * 50)


# ===========================================================
# Rank 3 — Intermediate
# isinstance(), issubclass() usage patterns
# ===========================================================

print("Rank 3 — Intermediate")

class Animal: pass
class Cat(Animal): pass
class Dog(Animal): pass

kitty = Cat()
doggo = Dog()

print("kitty is Animal?", isinstance(kitty, Animal))
print("doggo is Dog?", isinstance(doggo, Dog))
print("Cat subclass of Animal?", issubclass(Cat, Animal))
print("Dog subclass of Cat?", issubclass(Dog, Cat))

def validate_number(x: Any) -> bool:
    return isinstance(x, (int, float))

print("validate_number(10):", validate_number(10))
print("validate_number('abc'):", validate_number("abc"))

print("-" * 50)


# ===========================================================
# Rank 4 — Advanced
# Dynamic class creation using type()
# ===========================================================

print("Rank 4 — Advanced")

# Creating a new class dynamically:
# Equivalent to:
#   class Warrior:
#       role = "fighter"
#       def say_role(self): return self.role

Warrior = type(
    "Warrior",          # class name
    (object,),          # base classes
    {
        "role": "fighter",
        "say_role": lambda self: f"My role is {self.role}"
    }
)

w = Warrior()
print("Dynamic class:", type(w))
print("w.say_role():", w.say_role())

print("-" * 50)


# ===========================================================
# Rank 5 — Professional
# Plugin / registry system powered by type objects
# ===========================================================

print("Rank 5 — Professional")

class PluginBase:
    """
    All plugins must inherit from this class.

    The registry keeps references to plugin types,
    not plugin *instances*, allowing flexible creation.
    """
    registry: Dict[str, Type["PluginBase"]] = {}

    @classmethod
    def register(cls, plugin_cls: Type["PluginBase"]) -> None:
        name = plugin_cls.__name__
        cls.registry[name] = plugin_cls
        print(f"Registered plugin: {name}")

    @classmethod
    def create(cls, name: str, **kwargs) -> "PluginBase":
        if name not in cls.registry:
            raise ValueError(f"Unknown plugin: {name}")
        return cls.registry[name](**kwargs)


# Example plugin definitions
class PDFExporter(PluginBase):
    def __init__(self, pages: int = 1) -> None:
        self.pages = pages

    def run(self) -> str:
        return f"Exporting PDF with {self.pages} pages"


class ImageExporter(PluginBase):
    def __init__(self, resolution: str = "1080p") -> None:
        self.resolution = resolution

    def run(self) -> str:
        return f"Exporting image at {self.resolution}"


# Registering types (NOT instances!)
PluginBase.register(PDFExporter)
PluginBase.register(ImageExporter)

# Creating plugins dynamically using type objects
pdf = PluginBase.create("PDFExporter", pages=5)
img = PluginBase.create("ImageExporter", resolution="4K")

print(pdf.run())
print(img.run())

print("-" * 50)
