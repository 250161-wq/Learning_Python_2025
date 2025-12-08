#  What Is a Variable? and Types of Variables:

#Variables in Python are used to store data values.
#Variables can hold different types of data, such as:

#1. Integer (int): Whole numbers, e.g., 10, -5,
#Example of int:
age = 43

#2. Float: Decimal numbers, e.g., 3.14, -0.5
#Example of float:
height = 1.75

#3. String (str): Text enclosed in quotes, e.g., "Hello", 'Python'
#Example of str:
greeting = "Hello, World!"

#4. Boolean (bool): True or False values
#Example of bool:
is_student = False

#5. List: Ordered collection of items, e.g., [1, 2, 3], ["apple", "banana"]
#Example of list:
fruits = ["apple", "banana", "cherry"]

#6. Tuple: Ordered, immutable collection of items, e.g., (1, 2), ("a", "b")
#Example of tuple:
coordinates = (10.0, 20.0)

#7. Dictionary (dict): Key-value pairs, e.g., {"name": "Alice", "age": 25}
#Example of dict:
person = {"name": "Alice", "age": 25}

#8. Set: Unordered collection of unique items, e.g., {1, 2, 3}
#Example of set:
unique_numbers = {1, 2, 3}

#9. NoneType: Represents the absence of a value, e.g., None
#Example of NoneType:
nothing = None

#10. Complex: Complex numbers, e.g., 2 + 3j
#Example of complex:
complex_number = 2 + 3j

#11. Bytes: Immutable sequence of bytes, e.g., b'hello'
#Example of bytes:
byte_data = b'hello' 

#12. Bytearray: Mutable sequence of bytes, e.g., bytearray(b'hello')
#Example of bytearray:
mutable_byte_data = bytearray(b'hello')

#13. Frozenset: Immutable version of a set, e.g., frozenset({1, 2, 3})
#Example of frozenset:
immutable_numbers = frozenset({1, 2, 3})

#14. Range: Represents a sequence of numbers, e.g., range(0, 10)
#Example of range:
number_sequence = range(0, 10)

#15. Memoryview: Allows access to the memory of other binary objects without copying
#Example of memoryview:
memory_view = memoryview(byte_data)

#16. Custom Classes/Objects: User-defined types created using classes
#Example of custom class:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
person1 = Person("Bob", 30)

#17. Functions: Functions are also objects in Python and can be assigned to variables
#Example of function:
def greet():
    return "Hello!"
greeting_function = greet

#18. Modules: Modules are files containing Python code that can be imported and used in other Python programs
#Example of module: 
import math 
math_module = math

#19. Files: File objects represent files opened in Python and can be assigned to variables
#Example of file:
file = open("example.txt", "r")

#20. Generators: Generators are iterators that yield values one at a time and can be assigned to variables
#Example of generator:
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1
counter = count_up_to(5)

#21. Iterators: Iterators are objects that implement the iterator protocol and can be assigned to variables
#Example of iterator:
iterator = iter([1, 2, 3, 4, 5])

#22. Coroutines: Coroutines are special functions that can pause and resume their execution and can be assigned to variables
#Example of coroutine:
async def async_function():
    await some_async_operation()
coroutine = async_function()

#23. Context Managers: Context managers are objects that define the runtime context for a block of code and can be assigned to variables
#Example of context manager:
with open("example.txt", "r") as file:
    file_content = file.read()

#24. Enumerations: Enumerations are a set of symbolic names bound to unique, constant values and can be assigned to variables
#Example of enumeration:
from enum import Enum
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
favorite_color = Color.RED

#25. Named Tuples: Named tuples are an extension of regular tuples that allow for named fields and can be assigned to variables
#Example of named tuple:
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
point1 = Point(10, 20)

#26. Data Classes: Data classes are a way to define classes that primarily store data and can be assigned to variables
#Example of data class:
from dataclasses import dataclass
@dataclass
class Person:
    name: str
    age: int
person1 = Person("Bob", 30)

#27. Frozen Data Classes: Frozen data classes are immutable versions of data classes and can be assigned to variables
#Example of frozen data class:
from dataclasses import dataclass
@dataclass(frozen=True)
class Person:
    name: str
    age: int
person1 = Person("Bob", 30)

#28. Type Hints: Type hints are a way to indicate the expected data type of a variable and can be assigned to variables
#Example of type hint:
from typing import List
def greet_all(names: List[str]) -> None:
    for name in names:
        print("Hello, " + name)

#Variables are fundamental in programming as they allow you to store, manipulate, and retrieve data efficiently.

#29. Dynamic Typing:
#Python is a dynamically typed language, which means you don't need to declare the type of a variable explicitly.
#The type is inferred based on the value assigned to the variable.
#Example:
x = 10        # x is an integer
x = "Hello"   # Now x is a string
x = 3.14     # Now x is a float
x = [1, 2, 3]  # Now x is a list
x = {"name": "Alice"}  # Now x is a dictionary
x = True     # Now x is a boolean
x = (1, 2)  # Now x is a tuple
x = {1, 2, 3}  # Now x is a set
x = None    # Now x is NoneType
x = 2 + 3j  # Now x is a complex number
x = b'hello'  # Now x is bytes
x = bytearray(b'hello')  # Now x is bytearray
x = frozenset({1, 2, 3})  # Now x is
x is frozenset
x = range(0, 10)  # Now x is range
x = memoryview(b'hello')  # Now x is memoryview
x = Person("Bob", 30)  # Now x is an instance of the Person class
x = greet  # Now x is a function
x = math  # Now x is the math module
x = open("example.txt", "r")  # Now x is a file object
x = count_up_to(5)  # Now x is a generator
x = iter([1, 2, 3, 4, 5])  # Now x is an iterator
x = async_function()  # Now x is a coroutine
x = Color.RED  # Now x is an enumeration member
x = Point(10, 20)  # Now x is a named tuple
x = person1  # Now x is a data class instance
x = person1  # Now x is a frozen data class instance
x = greet_all  # Now x is a function with type hints

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

#In Python, a variable is a name that stores a value in memory.
#It allows you to reuse data without repeating it.

#Think of a variable as a label attached to a value.

#Example:
name = "Peyman"

#Here, 'name' is a variable that holds the string value "Peyman".

#"Peyman" is stored in memory, and we can refer to it using the variable 'name'. so peyman is valued in memory

# Rules for naming variables:
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
user_name = "Peyman43"
is_Student = True
weight_kg = 72.5

#example of invalid variable names:

2name = "Peyman"  # Starts with a digit
user-name = "peymaN43"  # Contains a hyphen
is Student = True  # Contains a space
for = 10  # 'for' is a reserved keyword
class = "Math"  # 'class' is a reserved keyword
why? = "Invalid"  # Contains a special character '?'

# 3. Assigning Values to Variables:
#You can assign values to variables using the assignment operator (=).

age = 43
country = "Iran"
is_student = False
height_m = 1.75

#You can also assign multiple variables in one line:

x, y, z = 10, 20, 30

#Or assign the same value to multiple variables:

a = b = c = 100

# 4. Using Variables:
#Once a variable is assigned a value, you can use it in expressions, functions, and print statements.

print("Name:", name)
print("Age:", age)
print("Country:", country)
print("Is Student:", is_student)
print("Height (m):", height_m)

#You can also perform operations using variables:

total = x + y + z
print("Total:", total)

# 5. Updating Variables:
#You can update the value of a variable by reassigning it.

age = age + 1  # Increment age by 1
print("Updated Age:", age)
country = "Canada"  # Change country
print("Updated Country:", country)

# 6. Deleting Variables:
#You can delete a variable using the del keyword.

del is_student
#print(is_student)  # This will raise an error since is_student is deleted

# 7. Best Practices for Naming Variables:
#Use descriptive names that convey the purpose of the variable.
#Use lowercase letters and separate words with underscores (snake_case).
#Avoid using single-letter names except for counters or iterators.
#you can reassign variables anytime in your code.

student_name = "Alice"
student_name = "Bob"  # Reassigned to a new value
print("Student Name:", student_name)

# 8. Variable Reassignment and type flexibility:

x = 10       # x is an integer
x = "Ten"   # Now x is a string
x = 3.14     # Now x is a float
x = [1, 2, 3]  # Now x is a list
x = {"name": "Alice"}  # Now x is a dictionary
print("Current value of x:", x)
print("Type of x:", type(x))

#This flexibility allows you to use variables in different contexts without strict type declarations.

# 9. Constants:
#While Python does not have built-in constant types, you can indicate that a variable should be treated as a constant by using uppercase letters.

PI = 3.14159
GRAVITY = 9.81  # m/s^2

#By convention, constants are written in uppercase to signal that their values should not be changed.

print("Value of PI:", PI)
print("Value of GRAVITY:", GRAVITY)

#Remember, variables are fundamental in programming as they allow you to store, manipulate, and retrieve data efficiently.

#Best Practices (To write  production-quality code):
#Use meaningful and descriptive variable names.
first_name = "Peyman" # better than 'fn'

#Follow consistent naming conventions.
# Example  (e.g., snake_case for variables).

#Avoid using reserved keywords as variable names.
#example of reserved keywords that cannot be used as variable names:
# False      await      else       import     pass

#Keep variable names concise but informative.
# example user_age = 25

#Comment your code to explain the purpose of variables when necessary.
# Example of explaining  ->  #This variable stores the user's age  user_age = 25

#Avoid using global variables unless necessary.
#Example def calculate_area(radius):

#Use constants for values that should not change.
example of constant:
PI = 3.14159

#Test your code to ensure variables hold the expected values.

#By following these best practices, we can write clean, maintainable, and understandable code.

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

# 1. Variable Scope:
#Variable scope refers to the visibility and accessibility of variables in different parts of your code.
#There are two main types of variable scope in Python:
#1. Local Scope: Variables defined within a function are local to that function and cannot be
#accessed outside of it.
def my_function():
    local_var = "I am local"
    print(local_var)
my_function()
#print(local_var)  # This will raise an error since local_var is not accessible here    

#2. Global Scope: Variables defined outside of any function are global and can be accessed from anywhere in the code.
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

# 3. Variable Annotations (Type Hints):
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

# Updating variables

counter = 10
counter += 5                       # Increment counter by 5
print("Updated Counter:", counter)
counter *= 2                       # Double the counter
print("Doubled Counter:", counter)
counter -= 4                        # Decrement counter by 4
print("Decremented Counter:", counter)
counter /= 3                          # Divide counter by 3
print("Divided Counter:", counter)
# 15. Swapping Variables:
a = 5
b = 10
a, b = b, a                          # Swap values
print("a:", a)
print("b:", b)
                             #this is how we can update our variable 
