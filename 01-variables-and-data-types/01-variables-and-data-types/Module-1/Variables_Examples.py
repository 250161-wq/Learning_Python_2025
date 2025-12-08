"""
Module 1 — Variables and Data Types
Comprehensive examples of Python variable types used for learning and practice.
Author: Peyman (2025)
"""

import math
import asyncio
import re
from functools import partial
from contextlib import contextmanager
from enum import Enum
from collections import namedtuple
from dataclasses import dataclass

# -----------------------------------------------------------
# 1. Basic Data Types
# -----------------------------------------------------------

# Integer
age = 43
print("Integer:", age, type(age))

# Float
height = 1.75
print("Float:", height, type(height))

# String
name = "Peyman"
print("String:", name, type(name))

# Boolean
is_student = False
print("Boolean:", is_student, type(is_student))

# NoneType
nothing = None
print("NoneType:", nothing, type(nothing))


# -----------------------------------------------------------
# 2. Collections (Lists, Tuples, Dicts, Sets)
# -----------------------------------------------------------

# List
fruits = ["apple", "banana", "cherry"]
print("List:", fruits, type(fruits))

# Tuple
coordinates = (10, 20)
print("Tuple:", coordinates, type(coordinates))

# Dictionary
person = {"name": "Alice", "age": 25}
print("Dictionary:", person, type(person))

# Set (duplicates are removed)
unique_numbers = {1, 2, 3, 3}
print("Set:", unique_numbers, type(unique_numbers))

# FrozenSet (immutable set)
immutable_numbers = frozenset({1, 2, 3})
print("FrozenSet:", immutable_numbers, type(immutable_numbers))


# -----------------------------------------------------------
# 3. Numeric Variant
# -----------------------------------------------------------

# Complex number
complex_number = 2 + 3j
print("Complex:", complex_number, type(complex_number))


# -----------------------------------------------------------
# 4. Byte-related Types
# -----------------------------------------------------------

# Bytes (immutable)
byte_data = b"hello"
print("Bytes:", byte_data, type(byte_data))

# Bytearray (mutable)
mutable_byte_data = bytearray(b"hello")
print("Bytearray:", mutable_byte_data, type(mutable_byte_data))

# MemoryView (view over bytes without copying)
memory_view_var = memoryview(byte_data)
print("Memoryview:", memory_view_var, type(memory_view_var))


# -----------------------------------------------------------
# 5. Range Type
# -----------------------------------------------------------

number_range = range(0, 10)
print("Range:", number_range, type(number_range))


# -----------------------------------------------------------
# 6. Functions as Variables
# -----------------------------------------------------------

def greet():
    return "Hello, World!"


greeting_function = greet
print("Function as variable:", greeting_function(), type(greeting_function))


# -----------------------------------------------------------
# 7. Modules as Variables
# -----------------------------------------------------------

math_module = math
print("Module:", math_module, type(math_module))


# -----------------------------------------------------------
# 8. Custom Classes and Objects
# -----------------------------------------------------------

class Car:
    def __init__(self, brand: str, year: int) -> None:
        self.brand = brand
        self.year = year

    def __repr__(self) -> str:
        return f"Car(brand={self.brand!r}, year={self.year})"


my_car = Car("Toyota", 2020)
print("Custom Object:", my_car, type(my_car))


# -----------------------------------------------------------
# 9. Files as Variables
# -----------------------------------------------------------

# Note: Using a context manager to open/close the file safely.
try:
    with open("example.txt", "w", encoding="utf-8") as f:
        f.write("Hello file!")

    f = open("example.txt", "r", encoding="utf-8")
    print("File object:", f, type(f))
    print("File content:", f.read())
    f.close()
except Exception as e:
    print("File demonstration skipped:", e)


# -----------------------------------------------------------
# 10. Generators
# -----------------------------------------------------------

def count_up_to(n: int):
    count = 1
    while count <= n:
        yield count
        count += 1


counter = count_up_to(5)
print("Generator:", counter, type(counter))
print("Generator values:", list(counter))


# -----------------------------------------------------------
# 11. Iterators
# -----------------------------------------------------------

iterator = iter([1, 2, 3])
print("Iterator:", iterator, type(iterator))
print("Iterator values:", list(iterator))


# -----------------------------------------------------------
# 12. Coroutines (Async)
# -----------------------------------------------------------

async def async_example():
    return "Async Result"


coroutine = async_example()
print("Coroutine object:", coroutine, type(coroutine))

# Run the coroutine to get a result (works when run as a script)
try:
    result = asyncio.run(async_example())
    print("Coroutine result:", result)
except RuntimeError:
    # This can happen inside some environments (like notebooks with an active loop)
    print("Coroutine result: (cannot run asyncio.run() in this environment)")


# -----------------------------------------------------------
# 13. Context Managers
# -----------------------------------------------------------

@contextmanager
def simple_context():
    print("Entering context...")
    yield "Context value"
    print("Exiting context...")


with simple_context() as ctx:
    print("Context manager value:", ctx)


# -----------------------------------------------------------
# 14. Enumerations
# -----------------------------------------------------------

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


favorite_color = Color.RED
print("Enum:", favorite_color, type(favorite_color))


# -----------------------------------------------------------
# 15. Named Tuple
# -----------------------------------------------------------

Point = namedtuple("Point", ["x", "y"])

p = Point(10, 20)
print("NamedTuple:", p, type(p))


# -----------------------------------------------------------
# 16. DataClass
# -----------------------------------------------------------

@dataclass
class PersonData:
    name: str
    age: int


pd = PersonData("Alice", 30)
print("DataClass:", pd, type(pd))


# -----------------------------------------------------------
# 17. Frozen DataClass
# -----------------------------------------------------------

@dataclass(frozen=True)
class PersonFrozen:
    name: str
    age: int


pfd = PersonFrozen("John", 40)
print("Frozen DataClass:", pfd, type(pfd))


# -----------------------------------------------------------
# 18. A Few Extra Variable Tricks
# -----------------------------------------------------------

# Multiple assignment
x, y, z = 10, 20, 30
print("Multiple assignment:", x, y, z)

# Reassignment with different types (dynamic typing)
dynamic_var = 10
print("Dynamic var (int):", dynamic_var, type(dynamic_var))
dynamic_var = "Now I am a string"
print("Dynamic var (str):", dynamic_var, type(dynamic_var))
dynamic_var = [1, 2, 3]
print("Dynamic var (list):", dynamic_var, type(dynamic_var))


# -----------------------------------------------------------
# 19. Regular Expressions
# -----------------------------------------------------------

# Compiled regex pattern as a variable
digit_pattern = re.compile(r"\d+")
sample_text = "User123 has 3 messages."
match = digit_pattern.search(sample_text)

print("Regex pattern:", digit_pattern, type(digit_pattern))
print("Regex match:", match.group() if match else None)


# -----------------------------------------------------------
# 20. Lambda Functions
# -----------------------------------------------------------

square = lambda n: n * n
add_two_numbers = lambda a, b: a + b

print("Lambda square(5):", square(5), type(square))
print("Lambda add_two_numbers(2, 3):", add_two_numbers(2, 3))


# -----------------------------------------------------------
# 21. Partial Functions
# -----------------------------------------------------------

def multiply(a, b, c):
    return a * b * c


multiply_by_10 = partial(multiply, 10)
result_partial = multiply_by_10(2, 3)

print("Partial function:", multiply_by_10, type(multiply_by_10))
print("Partial function result:", result_partial)


# -----------------------------------------------------------
# 22. Decorators as Variables
# -----------------------------------------------------------

def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper


debug_decorator = debug  # Decorator stored in a variable
print("Decorator object:", debug_decorator, type(debug_decorator))


@debug_decorator
def add_numbers(a, b):
    return a + b


print("Decorated add_numbers(2, 3):", add_numbers(2, 3))


# -----------------------------------------------------------
# 23. Class Methods and Static Methods
# -----------------------------------------------------------

class MathUtils:
    factor = 10

    @classmethod
    def describe_class(cls):
        return f"MathUtils with factor={cls.factor}"

    @staticmethod
    def add(a, b):
        return a + b


class_method_var = MathUtils.describe_class
static_method_var = MathUtils.add

print("Class method variable:", class_method_var(), type(class_method_var))
print("Static method variable:", static_method_var(5, 7), type(static_method_var))


# -----------------------------------------------------------
# 24. Property Objects
# -----------------------------------------------------------

class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self._width = width
        self._height = height

    @property
    def area(self) -> float:
        return self._width * self._height


rect = Rectangle(3, 4)
area_value = rect.area
area_property_obj = Rectangle.area  # The property object itself

print("Rectangle area value:", area_value)
print("Rectangle.area property object:", area_property_obj, type(area_property_obj))


# -----------------------------------------------------------
# 25. Exception Objects
# -----------------------------------------------------------

try:
    1 / 0
except ZeroDivisionError as exc:
    exception_obj = exc

print("Exception object:", exception_obj, type(exception_obj))


# -----------------------------------------------------------
# 26. Slice Objects
# -----------------------------------------------------------

slice_obj = slice(0, 5, 2)
numbers = [0, 1, 2, 3, 4, 5, 6]
sliced_numbers = numbers[slice_obj]

print("Slice object:", slice_obj, type(slice_obj))
print("Sliced numbers:", sliced_numbers)


# -----------------------------------------------------------
# 27. Ellipsis Object (...)
# -----------------------------------------------------------

ellipsis_obj = ...
print("Ellipsis object:", ellipsis_obj, type(ellipsis_obj))


# -----------------------------------------------------------
# 28. Type Objects (classes as values)
# -----------------------------------------------------------

int_type = int
str_type = str
list_type = list

print("Type object int_type:", int_type, type(int_type))
print("Type object str_type:", str_type, type(str_type))
print("Type object list_type:", list_type, type(list_type))


# -----------------------------------------------------------
# 29. Memory Address via id()
# (Not a type, but id() result can be stored in a variable)
# -----------------------------------------------------------

name_id = id(name)
print("Memory address (id) of variable 'name':", name_id, type(name_id))
