"""
Module 3 — Functions: Notes & Explanations
------------------------------------------

This file provides a structured, professional overview of Python functions.
It serves as a reference for understanding definitions, parameters,
return values, scope rules, and best practices.

Functions are one of the most important concepts in Python because they let
us package logic into reusable, organized, testable units.
"""


# ---------------------------------------------------------------------------
# 1. What is a Function?
# ---------------------------------------------------------------------------
"""
A function is a reusable block of code that performs a specific action.

Instead of repeating the same logic many times, we place it inside a
function and *call* the function whenever we need it.

Basic advantages:
- Avoid repeating code (DRY principle — Don't Repeat Yourself)
- Improve organization and readability
- Make programs easier to maintain and test
- Break complex tasks into smaller, manageable pieces
"""


# ---------------------------------------------------------------------------
# 2. Defining and Calling a Function
# ---------------------------------------------------------------------------
"""
Basic function definition:

    def greet():
        print("Hello")

Function call:

    greet()

A function must be defined *before* it is called.
"""


def greet():
    print("Hello from the greet() function!")


# ---------------------------------------------------------------------------
# 3. Parameters and Arguments
# ---------------------------------------------------------------------------
"""
A function can receive inputs, called **parameters** (or arguments).

Example:

    def greet_person(name):
        print("Hello,", name)

Calling the function:

    greet_person("Peyman")

Python supports different types of parameters:
- Positional parameters
- Keyword parameters
- Default parameter values
- Arbitrary argument lists (*args)
- Arbitrary keyword arguments (**kwargs)
"""


def greet_person(name):
    print(f"Hello, {name}!")


def greet_with_age(name, age):
    print(f"{name} is {age} years old.")


# ---------------------------------------------------------------------------
# 4. Default Parameter Values
# ---------------------------------------------------------------------------
"""
A default parameter gives a value when the caller does not provide one.

Example:

    def welcome(user="Guest"):
        print("Welcome,", user)

Calling:

    welcome("Peyman")   -> Welcome, Peyman
    welcome()           -> Welcome, Guest
"""


def welcome(user="Guest"):
    print(f"Welcome, {user}")


# ---------------------------------------------------------------------------
# 5. Return Values
# ---------------------------------------------------------------------------
"""
A function can compute a result and return it using **return**.

Example:

    def add(a, b):
        return a + b

If a function does not have a return statement, Python returns None.

A function may return:
- A single value
- Multiple values (as a tuple)
- Lists, dicts, sets, or custom objects
"""


def add(a, b):
    return a + b


def divide_and_remainder(x, y):
    """Return multiple values as a tuple."""
    return x // y, x % y


# ---------------------------------------------------------------------------
# 6. Function Scope (Local vs Global Variables)
# ---------------------------------------------------------------------------
"""
Variables inside a function exist in **local scope**.

Example:

    def example():
        x = 10  # local variable

A variable defined outside any function is **global scope**.

In general:
- Prefer local variables
- Avoid modifying global variables unless absolutely necessary

Python allows access to global variables inside functions, but not
modification unless using the `global` keyword.
"""

GLOBAL_COUNTER = 0


def increment_global():
    """
    Demonstrates the global keyword.
    Normally assigning to GLOBAL_COUNTER would create a local variable,
    but using global allows modifying the global variable.
    """
    global GLOBAL_COUNTER
    GLOBAL_COUNTER += 1


# ---------------------------------------------------------------------------
# 7. *args and **kwargs
# ---------------------------------------------------------------------------
"""
Sometimes we do not know how many arguments a function will receive.

*args  -> captures extra positional arguments as a tuple  
**kwargs -> captures extra keyword arguments as a dictionary

They make a function flexible and extensible.
"""


def demo_args(*args):
    print("Arguments received:", args)


def demo_kwargs(**kwargs):
    print("Keyword arguments:", kwargs)


# ---------------------------------------------------------------------------
# 8. Documentation Strings (docstrings)
# ---------------------------------------------------------------------------
"""
A docstring is a string at the top of a function that explains what it does.

Example:

    def add(a, b):
        \"\"\"Return the sum of a and b.\"\"\"
        return a + b

Docstrings are important because:
- They appear in help(add)
- They improve code readability
- They help tools generate documentation automatically
"""


def subtract(a, b):
    """Return a - b."""
    return a - b


# ---------------------------------------------------------------------------
# 9. Best Practices for Writing Functions
# ---------------------------------------------------------------------------
"""
✔ Write short functions (single responsibility principle)  
✔ Use meaningful parameter names  
✔ Avoid using global variables  
✔ Always document your function with a docstring  
✔ Return values instead of printing (printing is for user interaction)  
✔ Keep function logic clear and focused  
✔ Prefer pure functions when possible (same input -> same output)  
"""


# ---------------------------------------------------------------------------
# 10. Summary
# ---------------------------------------------------------------------------
"""
In this module I learned:

- What functions are and why they matter
- How to define and call them correctly
- How to use parameters, default values, *args, **kwargs
- How return values work
- How variable scope affects behavior inside functions
- Professional best practices to keep function code clean and maintainable

Next steps:
- See Functions_Examples.py for small, runnable demonstrations
- Complete Functions_Tasks.py to build practical skills
"""
