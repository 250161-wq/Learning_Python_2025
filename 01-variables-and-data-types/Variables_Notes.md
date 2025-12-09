# Learning_Python_2025  📖
A modern, structured, and hands-on repository designed to document my journey learning Python throughout 2025.  
This project includes progressive exercises, mini-projects, and real-world applications to build strong foundations in programming and data analysis.

---

# Topics Covered:
# This repository will explore Python step by step, including:

# ✔️ Variables  
# Understanding how to store, modify, and work with data.
((
# Python Variables — Complete Professional Guide

This document provides a comprehensive, production-quality explanation of **Python variables**, including data types, naming rules, assignments, best practices, scopes, annotations, and advanced examples.  
Perfect for learning, teaching, or using in professional GitHub repositories.

---

1. What Is a Variable?

A **variable** in Python is a name that stores a value in memory.

Example:
```python
name = "Peyman"
```

Here:
- `name` → variable  
- `"Peyman"` → value stored in memory  

Variables allow you to store, reuse, and manipulate data efficiently.

---

2. Python Variable Types (With Examples)

Python supports many types of variables. Here is a complete list with examples:

Integer (int)

```python
age = 43
```

Float (float)

```python
height = 1.75
```

String (str)

```python
greeting = "Hello, World!"
```

Boolean (bool)

```python
is_student = False
```

List

```python
fruits = ["apple", "banana", "cherry"]
```

Tuple

```python
coordinates = (10.0, 20.0)
```

Dictionary (dict)

```python
person = {"name": "Alice", "age": 25}
```

Set

```python
unique_numbers = {1, 2, 3}
```

NoneType

```python
nothing = None
```

Complex numbers

```python
complex_number = 2 + 3j
```

Bytes

```python
byte_data = b'hello'
```

Bytearray

```python
mutable_byte_data = bytearray(b'hello')
```

Frozenset

```python
immutable_numbers = frozenset({1, 2, 3})
```

Range

```python
number_sequence = range(0, 10)
```

Memoryview

```python
memory_view = memoryview(byte_data)
```

Custom Classes

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Bob", 30)
```

Functions as variables

```python
def greet():
    return "Hello!"

greeting_function = greet
```

Modules

```python
import math
math_module = math
```

File objects

```python
file = open("example.txt", "r")
```

Generators

```python
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

counter = count_up_to(5)
```

Iterators

```python
iterator = iter([1, 2, 3, 4, 5])
```

Coroutines

```python
async def async_function():
    await some_async_operation()

coroutine = async_function()
```

Enumerations

```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

favorite_color = Color.RED
```

Named Tuples

```python
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
point1 = Point(10, 20)
```

Data Classes

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

person1 = Person("Bob", 30)
```

Frozen Data Classes

```python
@dataclass(frozen=True)
class Person:
    name: str
    age: int
```

Type Hints

```python
from typing import List

def greet_all(names: List[str]) -> None:
    for name in names:
        print("Hello, " + name)
```

---

3. Dynamic Typing in Python

Python allows variables to change type:

```python
x = 10            # int
x = "Hello"       # str
x = 3.14          # float
x = [1, 2, 3]     # list
x = {"name": "Alice"}   # dict
x = True          # bool
x = None          # NoneType
x = 2 + 3j        # complex
x = memoryview(b'hello')  
```

---

4. Naming Rules for Variables

Valid rules:
- Must start with a letter or underscore  
- Can contain letters, numbers, underscores  
- Case-sensitive (`age` ≠ `Age`)  
- No spaces or hyphens  
- Cannot use Python keywords  

✔ Valid:
```python
name = "Peyman"
user_name = "PM"
_age = 43
country1 = "Iran"
```

❌ Invalid:
```python
2name = "x"
user-name = "x"
is Student = True
for = 10
```

---

5. Assigning Values

```python
age = 43
country = "Iran"
is_student = False
height_m = 1.75
```

Multiple assignment:
```python
x, y, z = 10, 20, 30
```

### Same value:
```python
a = b = c = 100
```

---

6. Using Variables

```python
print("Name:", name)
print("Age:", age)
print("Country:", country)
```

Mathematical operations:
```python
total = x + y + z
```

---

7. Updating Variables

```python
age = age + 1
country = "Canada"
```

---

8. Deleting Variables

```python
del is_student
```

---

9. Constants (by convention)

```python
PI = 3.14159
GRAVITY = 9.81
MAX_USERS = 100
API_URL = "https://api.example.com"
```

---
10. Variable Scope

### Local Scope
```python
def my_function():
    local_var = "I am local"
```

### Global Scope
```python
global_var = "I am global"
```

### Modifying global variable:
```python
counter = 0

def increment_counter():
    global counter
    counter += 1
```

---
 11. Variable Annotations (Type Hints)

```python
name: str = "Peyman"
age: int = 43
height_m: float = 1.86
is_student: bool = True
```

---

12. Updating Variables with Operators

```python
counter = 10
counter += 5
counter *= 2
counter -= 4
counter /= 3
```

---

 13. Swapping Variables

```python
a = 5
b = 10
a, b = b, a
```

---

14. Testing Variables

```python
def test_variable_assignment():
    test_var = 10
    assert test_var == 10

test_variable_assignment()
print("All tests passed!")
```

---
 ✅ Conclusion

Python variables are fundamental structures that let you store, manipulate, and retrieve data.  
This guide covered **basic to advanced concepts**, ensuring you understand how variables work in real-world professional code.

---

## ⭐⭐ Author⭐⭐
**Peyman** — Python learner and future software engineer 😄🚀
))
# ✔️ Data Types  
# Numbers, strings, booleans, lists, tuples, dictionaries, and more.

# ✔️ Loops  
# Mastering `for` and `while` loops with practical exercises.

# ✔️ Functions  
# Writing clean, reusable, modular code.

# ✔️ Working With Files  
# Reading and writing text, CSV, and more.

# ✔️ Working With APIs  
# Making requests, parsing data, building small API-based applications.

# ✔️ JSON  
# Handling structured data like a professional.

# ✔️ Pandas + Data Analysis  
# Loading data, cleaning it, exploring patterns, and analyzing datasets.

# ✔️ Plotting Graphs  
# Creating visualizations using Matplotlib or Seaborn.

# ✔️ Building Simple Apps  
# Small projects to apply everything learned.

---

# 📁 Repository Structure (planned)

