"""
Module 1 — Variables and Data Types
File: Explain_Variables.py

Purpose
--------------------------------------------------------------------------
This script belongs to the Learning_Python_2025 project (Module 1).
It is a *reference file* that Explains different kinds of
Python values can be stored in variables:

- Basic data types (int, float, str, bool, NoneType)
- Collections (list, tuple, dict, set, frozenset)
- Numeric variants (complex)
- Byte types (bytes, bytearray, memoryview)
- Ranges, functions, modules, custom classes/objects
- Files, generators, iterators, coroutines, context managers
- Enumerations, named tuples, data classes, frozen data classes
- Regular expressions, lambda functions, partial functions
- Decorators, class/staticmethods, properties, exceptions
- Slice objects, ellipsis, type objects, and id() values

Ranking System for the Examples and Explainings 
----------------------------------------------------------------------------
Rank 1 — Beginner      : Very basic, first contact with the concept.
Rank 2 — Easy          : Still simple, but introduces a bit more thinking.
Rank 3 — Intermediate  : Realistic, slightly more complex patterns.
Rank 4 — Advanced      : Closer to production-style or more abstract ideas.
Rank 5 — Professional  : Power-user features and deeper Python internals.
----------------------------------------------------------------------------
Author: Peyman Miyandashti
ID Number: 250161
Date of Birth: 11/11/1983
Year: 2025
----------------------------------------------------------------------------
"""
# If you are beginner  you should just pay attention to  Rank 1 and 
#untill you are not comfortable with them do not go to the next ranks.
#Let me start with explain  about Variables ! 

# 1. What Is a Variable? and Types of Variables:
#Variables in Python are used to store data values.
#Variables can hold different types of data, such as:

#1. Integer (int): Whole numbers, e.g., 10, -5  (Rank 1 - Beginner)
#Example of int:
age = 43

#2. Float: Decimal numbers, e.g., 3.14, -0.5  (Rank 1 - Beginner)
#Example of float:
height = 1.75

#3. String (str): Text enclosed in quotes, e.g., "Hello", 'Python'  (Rank 1 - Beginner)
#Example of str:
greeting = "Hello, World!"

#4. Boolean (bool): True or False values  (Rank 1 - Beginner)
#Example of bool:
is_student = False

#5. List: Ordered collection of items, e.g., [1, 2, 3], ["apple", "banana"]  (Rank 1 - Beginner)
#Example of list:
fruits = ["apple", "banana", "cherry"]

#6. Tuple: Ordered, immutable collection of items, e.g., (1, 2), ("a", "b")  (Rank 1 - Beginner)
#Example of tuple:
coordinates = (10.0, 20.0)

#7. Dictionary (dict): Key-value pairs, e.g., {"name": "Alice", "age": 25}  (Rank 1 - Beginner)
#Example of dict:
person = {"name": "Alice", "age": 25}

#8. Set: Unordered collection of unique items, e.g., {1, 2, 3}  (Rank 2 - Easy)
#Example of set:
unique_numbers = {1, 2, 3}

#9. NoneType: Represents the absence of a value, e.g., None  (Rank 2 - Easy)
#Example of NoneType:
nothing = None

#10. Complex: Complex numbers, e.g., 2 + 3j  (Rank 2 - Easy)
#Example of complex:
complex_number = 2 + 3j

#11. Bytes: Immutable sequence of bytes, e.g., b'hello'  (Rank 2 - Easy)
#Example of bytes:
byte_data = b'hello'  

# 12. Range: Represents a sequence of numbers, e.g., range(0, 10)  (Rank 2 - Easy)
#Example of range:
number_sequence = range(0, 10)


#13. Frozenset: Immutable version of a set, e.g., frozenset({1, 2, 3})  (Rank 3 - Intermediate)
#Example of frozenset:
immutable_numbers = frozenset({1, 2, 3})

#14.Bytearray: Mutable sequence of bytes, e.g., bytearray(b'hello')  (Rank 3 - Intermediate)
#Example of bytearray:
mutable_byte_data = bytearray(b'hello') 

#15. Memoryview: Allows access to the memory of other binary objects without copying  (Rank 3 - Intermediate)
#Example of memoryview:
memory_view = memoryview(byte_data)

#16. Custom Classes/Objects: User-defined types created using classes  (Rank 3 - Intermediate)
#Example of custom class:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
person1 = Person("Bob", 30)

#17. Functions: Functions are also objects in Python and can be assigned to variables  (Rank 3 - Intermediate)
#Example of function:
def greet():
    return "Hello!"

greeting_function = greet

#18. Modules: Modules are files containing Python code that can be imported and used in other Python programs  (Rank 3 - Intermediate)
#Example of module: 
import math 
math_module = math

#19. Files: File objects represent files opened in Python and can be assigned to variables  (Rank 3 - Intermediate)
#Example of file:
file = open("example.txt", "r")

#20. Generators: Generators are iterators that yield values one at a time and can be assigned to variables  (Rank 3 - Intermediate)
#Example of generator:
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1
counter = count_up_to(5)

#21. Iterators: Iterators are objects that implement the iterator protocol and can be assigned to variables  (Rank 4 - Advanced)
#Example of iterator:
iterator = iter([1, 2, 3, 4, 5])

#22. Coroutines: Coroutines are special functions that can pause and resume their execution and can be assigned to variables  (Rank 4 - Advanced)
#Example of coroutine:
async def async_function():
    await some_async_operation()
coroutine = async_function()

#23. Context Managers: Context managers are objects that define the runtime context for a block of code and can be assigned to variables  (Rank 4 - Advanced)
#Example of context manager:
with open("example.txt", "r") as file:
    file_content = file.read()

#24. Enumerations: Enumerations are a set of symbolic names bound to unique, constant values and can be assigned to variables  (Rank 4 - Advanced)
#Example of enumeration:
from enum import Enum
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
favorite_color = Color.RED

#25. Named Tuples: Named tuples are an extension of regular tuples that allow for named fields and can be assigned to variables   (Rank 5 - Professional)
#Example of named tuple:
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
point1 = Point(10, 20)

#26. Data Classes: Data classes are a way to define classes that primarily store data and can be assigned to variables  (Rank 5 - Professional)
#Example of data class:
from dataclasses import dataclass
@dataclass
class Person:
    name: str
    age: int
person1 = Person("Bob", 30)

#27. Frozen Data Classes: Frozen data classes are immutable versions of data classes and can be assigned to variables  (Rank 5 - Professional)
#Example of frozen data class:
from dataclasses import dataclass
@dataclass(frozen=True)
class Person:
    name: str
    age: int
person1 = Person("Bob", 30)

#28. Type Hints: Type hints are a way to indicate the expected data type of a variable and can be assigned to variables  (Rank 5 - Professional)
#Example of type hint:
from typing import List
def greet_all(names: List[str]) -> None:
    for name in names:
        print("Hello, " + name)

#Variables are fundamental in programming as they allow you to store, manipulate, and retrieve data efficiently.

#29. Dynamic Typing:  (Rank 1-5 / beginner to  Professional)
#Python is a dynamically typed language, which means you don't need to declare the type of a variable explicitly.
#The type is inferred based on the value assigned to the variable.
#Example:
x = 10        # x is an integer (Rank 1 - Beginner)
x = "Hello"   # Now x is a string (Rank 1 - Beginner)
x = 3.14     # Now x is a float (Rank 1 - Beginner)
x = [1, 2, 3]  # Now x is a list (Rank 1 - Beginner)
x = {"name": "Alice"}  # Now x is a dictionary (Rank 1 - Beginner)
x = True     # Now x is a boolean (Rank 1 - Beginner)
x = (1, 2)  # Now x is a tuple (Rank 1 - Beginner)
x = {1, 2, 3}  # Now x is a set (Rank 2 - Easy)
x = None    # Now x is NoneType (Rank 2 - Easy)
x = 2 + 3j  # Now x is a complex number (Rank 2 - Easy)
x = b'hello'  # Now x is bytes (Rank 2 - Easy)
x = range(0, 10)  # Now x is range (Rank 2 - Easy)
x = bytearray(b'hello')  # Now x is bytearray   (Rank 3 - Intermediate)
x = frozenset({1, 2, 3})  # Now x is  (Rank 3 - Intermediate)
x is frozenset (Rank 2 - Easy)
x = memoryview(b'hello')  # Now x is memoryview  (Rank 3 - Intermediate)
x = Person("Bob", 30)  # Now x is an instance of the Person class  (Rank 3 - Intermediate)
x = greet  # Now x is a function  (Rank 3 - Intermediate)
x = math  # Now x is the math module  (Rank 3 - Intermediate)
x = open("example.txt", "r")  # Now x is a file object   (Rank 3 - Intermediate)
x = count_up_to(5)  # Now x is a generator (Rank 4 - Advanced)
x = iter([1, 2, 3, 4, 5])  # Now x is an iterator (Rank 4 - Advanced)
x = async_function()  # Now x is a coroutine (Rank 4 - Advanced)
x = Color.RED  # Now x is an enumeration member (Rank 4 - Advanced)
x = Point(10, 20)  # Now x is a named tuple  (Rank 5 - Professional)
x = person1  # Now x is a data class instance  (Rank 5 - Professional)
x = person1  # Now x is a frozen data class instance  (Rank 5 - Professional)
x = greet_all  # Now x is a function with type hints  (Rank 5 - Professional)

#Checking the type of variable x
print(type(x))
#checking the type of variable name
print(type(name))
#checking the type of variable age
print(type(age))
#checking the type of variable height
print(type(height_m))
#checking the type of variable is_student
print(type(is_student))
#checking the type of variable fruits
print(type(fruits))
#checking the type of variable person
print(type(person))
#checking the type of variable complex_number
print(type(complex_number))
#checking the type of variable byte_data
print(type(byte_data))
#checking the type of variable mutable_byte_data
print(type(mutable_byte_data))
#checking the type of variable immutable_numbers
print(type(immutable_numbers))
#checking the type of variable number_sequence
print(type(number_sequence))
#checking the type of variable memory_view
print(type(memory_view))
#checking the type of variable person1
print(type(person1))
#checking the type of variable greeting_function
print(type(greeting_function))
#checking the type of variable math_module
print(type(math_module))
#checking the type of variable file
print(type(file))
#checking the type of variable counter
print(type(counter))
#checking the type of variable iterator
print(type(iterator))
#checking the type of variable coroutine
print(type(coroutine))
#checking the type of variable favorite_color
print(type(favorite_color))
#checking the type of variable point1
print(type(point1))
#checking the type of variable person1 (data class)
print(type(person1))
#checking the type of variable person1 (frozen data class)
print(type(person1))
#checking the type of variable greet_all
print(type(greet_all))



#In Python, a variable is a name that stores a value in memory.  (Rank 1 - Beginner)
#It allows you to reuse data without repeating it. 
#Think of a variable as a label attached to a value.  

#Example:
name = "Peyman"

#Here, 'name' is a variable that holds the string value "Peyman".  (Rank 1 - Beginner)

#"Peyman" is stored in memory, and we can refer to it using the variable 'name'. so peyman is valued in memory  

# 2. Rules for naming variables:  (Rank 1 - Beginner)

#Python variable names must follow these rules:

#1. Must start with a letter (a-z, A-Z) or an underscore (_).

#2. Can contain letters, digits (0-9), and underscores.

#3. Case-sensitive (name , Name, and NAME are different variables that means name ≠ Name or Name ≠ NAME).

#4. Cannot contain spaces or special characters (like !, @, #, $, %, etc.).

#5. Cannot be a reserved keyword in Python (like if, else, while, for, etc.).


# Example of valid variable names:

name = "Peyman"
_age = 43
country1 = "Iran"
user_name = "peymaN43"
is_Student = True
weight_kg = 75.5

#example of invalid variable names:

# 2name = "Peyman"  # Starts with a digit
# user-name = "peymaN43"  # Contains a hyphen
# is Student = True  # Contains a space
# for = 10  # 'for' is a reserved keyword
# class = "Math"  # 'class' is a reserved keyword
# why? = "Invalid"  # Contains a special character '?'

# 3. Assigning Values to Variables:  (Rank 1 - Beginner)

#You can assign values to variables using the assignment operator (=).

age = 43
country = "Iran"
is_student = False
height_m = 1.75

#You can also assign multiple variables in one line:

x, y, z = 10, 20, 30

#Or assign the same value to multiple variables:

a = b = c = 100

# 4. Using Variables: (Rank 1 - Beginner)

#Once a variable is assigned a value, you can use it in expressions, functions, and print statements.

print("Name:", name)
print("Age:", age)
print("Country:", country)
print("Is Student:", is_student)
print("Height (m):", height_m)

#You can also perform operations using variables:

total = x + y + z
print("Total:", total)

# 5. Updating Variables:  (Rank 1 - Beginner)

#You can update the value of a variable by reassigning it.
age = age + 1  # Increment age by 1
print("Updated Age:", age)
country = "Canada"  # Change country
print("Updated Country:", country)

# 6. Deleting Variables: (Rank 1 - Beginner)

#You can delete a variable using the del keyword.

del is_student

#print(is_student)  # This will raise an error since is_student is deleted

# 7. Best Practices for Naming Variables:  (Rank 1 - Beginner)
#Use descriptive names that convey the purpose of the variable.
#Use lowercase letters and separate words with underscores (snake_case).
#Avoid using single-letter names except for counters or iterators.
#you can reassign variables anytime in your code.

student_name = "Alice"
student_name = "Bob"  # Reassigned to a new value
print("Student Name:", student_name)

# 8. Variable Reassignment and type flexibility:  (Rank 1 - Beginner)

x = 10       # x is an integer
x = "Ten"   # Now x is a string
x = 3.14     # Now x is a float
x = [1, 2, 3]  # Now x is a list
x = {"name": "Alice"}  # Now x is a dictionary

print("Current value of x:", x)
print("Type of x:", type(x))

#This flexibility allows you to use variables in different contexts without strict type declarations.

# 9. Constants: (Rank 1 - Beginner)
#While Python does not have built-in constant types, you can indicate that a variable should be treated as a constant by using uppercase letters.
PI = 3.14159
GRAVITY = 9.81  # m/s^2

#By convention, constants are written in uppercase to signal that their values should not be changed.
print("Value of PI:", PI)
print("Value of GRAVITY:", GRAVITY)

#Remember, variables are fundamental in programming as they allow you to store, manipulate, and retrieve data efficiently.

#10. Dynamic Typing: (Rank 1 - Beginner)
#Python is a dynamically typed language, which means you don't need to declare the type of a variable explicitly.
#The type is inferred based on the value assigned to the variable.
#Example:
x = 10        # x is an integer
x = "Hello"   # Now x is a string
x = 3.14     # Now x is a float
x = [1, 2, 3]  # Now x is a list

# 11. Best Practices (To write  production-quality code): (Rank 1 - Beginner)
#Use meaningful and descriptive variable names.

first_name = "Peyman" # better than 'fn'

#Follow consistent naming conventions (e.g., snake_case for variables).

#Avoid using reserved keywords as variable names.

#Keep variable names concise but informative.

#Comment your code to explain the purpose of variables when necessary.

#Avoid using global variables unless necessary.

#Use constants for values that should not change.

#Test your code to ensure variables hold the expected values.

#By following these best practices, you can write clean, maintainable, and understandable code.

# Define  constants in UPERCASE

MAX_USERS = 100
API_URL = "https://api.example.com"

# Use descriptive variable names

user_age = 25
user_email = "user@example.com"

# Comment your code
# This variable stores the user's age
user_age = 25

# Avoid using global variables unless necessary

def calculate_area(radius):
    PI = 3.14159  # Constant defined within the function
    return PI * radius * radius

area = calculate_area(5)
print("Area:", area)

# Test your code
def test_variable_assignment():
    test_var = 10
    assert test_var == 10, "Variable assignment failed"

test_variable_assignment()
print("All tests passed!")

# 12. Variable Scope: (Rank 2 - Easy)
#Variable scope refers to the visibility and accessibility of variables in different parts of your code.
#There are two main types of variable scope in Python:

#1. Local Scope: Variables defined within a function are local to that function and cannot be
#accessed outside of it.

def my_function():
    local_var = "I am local"
    print(local_var)

my_function()

#print(local_var)  # This will raise an error since local_var is not accessible here    

#2. Global Scope: Variables defined outside of any function are global and can be accessed from anywhere in the code.(Rank 2 - Easy)

global_var = "I am global"
def another_function():
    print(global_var)

another_function()
print(global_var)  # Accessible here as well

#You can also use the global keyword to modify a global variable from within a function.

counter = 0
def increment_counter():
    global counter
    counter += 1

increment_counter()
print("Counter:", counter)

#Remember to manage variable scope carefully to avoid unintended side effects and maintain code clarity.

# 13. Variable Annotations (Type Hints):(Rank 2 - Easy)

#Variable annotations, also known as type hints, allow you to specify the expected data type of
#a variable. This helps improve code readability and can assist with static type checking.

#Example of variable annotations:

name: str = "Peyman"
age: int = 43
height_m: float = 1.86
is_student: bool = True
fruits: list = ["apple", "banana", "cherry"]
person: dict = {"name": "Alice", "age": 25}

#You can also use type hints in function definitions:

def greet(name: str) -> str:
    return "Hello, " + name

greeting_message: str = greet("Peyman")
print(greeting_message)

#While Python does not enforce type hints at runtime, they serve as valuable documentation and can be checked using tools like mypy.
#Using variable annotations can enhance code quality and make it easier for others (and yourself) to understand the intended use of variables.

# 14. Updating variables (Rank 2 - Easy)

counter = 10
counter += 5  # Increment counter by 5
print("Updated Counter:", counter)
counter *= 2  # Double the counter
print("Doubled Counter:", counter)
counter -= 4  # Decrement counter by 4
print("Decremented Counter:", counter)
counter /= 3  # Divide counter by 3
print("Divided Counter:", counter)

# 15. Swapping Variables:(Rank 2 - Easy)

a = 5
b = 10
a, b = b, a  # Swap values
print("a:", a)
print("b:", b)

#Use constants for values that should not change. example of constant:
PI = 3.14159
