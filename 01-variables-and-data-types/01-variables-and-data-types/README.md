# Module 1 — Variables and Data Types
Welcome to **Module 1** of the *Learning_Python_2025* project.  
This module introduces the foundation of all Python programming: **variables** and **data types**.

Author: **Peyman**  
Year: **2025**

---
#Overview

In Python, a **variable** is a name that stores a value.  
This value can be a number, text, a list of items, or even more complex structures.

Understanding variables and data types is essential because they form the basis of everything you will build in Python — from simple scripts to full applications.

---
Core Data Types in Python
Type              	  Description	                           Example
int	                  Whole numbers	                         age = 43
float               	Decimal numbers	                       height = 1.75
str	                  Text (strings)	                       greeting = "Hello"
bool	                True / False                           values	is_student = False
list	                Ordered collection of items          	 nums = [1, 2, 3]
---
Included File
variables_examples.py

This file demonstrates:

Creating variables

Printing values

Updating values

Working with lists
---

## 🔹 Topics Covered

Python Variables — Complete Professional Guide
This document provides a comprehensive, production-quality explanation of Python variables, including data types, naming rules, assignments, best practices, scopes, annotations, and advanced examples.
Perfect for learning, teaching, or using in professional GitHub repositories.

What Is a Variable?
A variable in Python is a name that stores a value in memory.

Example:

name = "Peyman"
Here:

name → variable
"Peyman" → value stored in memory
Variables allow you to store, reuse, and manipulate data efficiently.

Python Variable Types (With Examples)
Python supports many types of variables. Here is a complete list with examples:

Integer (int)

age = 43
Float (float)

height = 1.75
String (str)

greeting = "Hello, World!"
Boolean (bool)

is_student = False
List

fruits = ["apple", "banana", "cherry"]
Tuple

coordinates = (10.0, 20.0)
Dictionary (dict)

person = {"name": "Alice", "age": 25}
Set

unique_numbers = {1, 2, 3}
NoneType

nothing = None
Complex numbers

complex_number = 2 + 3j
Bytes

byte_data = b'hello'
Bytearray

mutable_byte_data = bytearray(b'hello')
Frozenset

immutable_numbers = frozenset({1, 2, 3})
Range

number_sequence = range(0, 10)
Memoryview

memory_view = memoryview(byte_data)
Custom Classes

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Bob", 30)
Functions as variables

def greet():
    return "Hello!"

greeting_function = greet
Modules

import math
math_module = math
File objects

file = open("example.txt", "r")
Generators

def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

counter = count_up_to(5)
Iterators

iterator = iter([1, 2, 3, 4, 5])
Coroutines

async def async_function():
    await some_async_operation()

coroutine = async_function()
Enumerations

from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

favorite_color = Color.RED
Named Tuples

from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
point1 = Point(10, 20)
Data Classes

from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

person1 = Person("Bob", 30)
Frozen Data Classes

@dataclass(frozen=True)
class Person:
    name: str
    age: int
Type Hints

from typing import List

def greet_all(names: List[str]) -> None:
    for name in names:
        print("Hello, " + name)
Dynamic Typing in Python
Python allows variables to change type:

x = 10            # int
x = "Hello"       # str
x = 3.14          # float
x = [1, 2, 3]     # list
x = {"name": "Alice"}   # dict
x = True          # bool
x = None          # NoneType
x = 2 + 3j        # complex
x = memoryview(b'hello')  
Naming Rules for Variables
Valid rules:

Must start with a letter or underscore
Can contain letters, numbers, underscores
Case-sensitive (age ≠ Age)
No spaces or hyphens
Cannot use Python keywords
✔ Valid:

name = "Peyman"
user_name = "PM"
_age = 43
country1 = "Iran"
❌ Invalid:

2name = "x"
user-name = "x"
is Student = True
for = 10
Assigning Values
age = 43
country = "Iran"
is_student = False
height_m = 1.75
Multiple assignment:

x, y, z = 10, 20, 30
Same value:
a = b = c = 100
Using Variables
print("Name:", name)
print("Age:", age)
print("Country:", country)
Mathematical operations:

total = x + y + z
Updating Variables
age = age + 1
country = "Canada"
Deleting Variables
del is_student
Constants (by convention)
PI = 3.14159
GRAVITY = 9.81
MAX_USERS = 100
API_URL = "https://api.example.com"
Variable Scope
Local Scope
def my_function():
    local_var = "I am local"
Global Scope
global_var = "I am global"
Modifying global variable:
counter = 0

def increment_counter():
    global counter
    counter += 1
Variable Annotations (Type Hints)
name: str = "Peyman"
age: int = 43
height_m: float = 1.86
is_student: bool = True
Updating Variables with Operators
counter = 10
counter += 5
counter *= 2
counter -= 4
counter /= 3
Swapping Variables
a = 5
b = 10
a, b = b, a
Testing Variables
def test_variable_assignment():
    test_var = 10
    assert test_var == 10

test_variable_assignment()
print("All tests passed!")
✅ Conclusion

Python variables are fundamental structures that let you store, manipulate, and retrieve data.
This guide covered basic to advanced concepts, ensuring you understand how variables work in real-world professional code.

