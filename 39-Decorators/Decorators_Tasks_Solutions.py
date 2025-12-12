"""
Decorators_Tasks_Solutions.py
Module 39 — Decorators
Author: Peyman Miyandashti
Year: 2025

This file contains clean and professional solutions
for the decorator exercises in this module.
"""

import time
from functools import wraps

# ---------------------------------------------------------------------------
# Rank 1 — Beginner
# ---------------------------------------------------------------------------

# Task 1 Solution
def before_message(func):
    def wrapper():
        print("About to run the function")
        func()
    return wrapper


# Task 2 Solution
@before_message
def say_hello():
    print("Hello")

say_hello()


# ---------------------------------------------------------------------------
# Rank 2 — Easy
# ---------------------------------------------------------------------------

# Task 3 Solution
def before_after(func):
    def wrapper():
        print("Before function")
        result = func()
        print("After function")
        return result
    return wrapper


# Task 4 Solution
@before_after
def get_number():
    return 42

print(get_number())


# ---------------------------------------------------------------------------
# Rank 3 — Intermediate
# ---------------------------------------------------------------------------

# Task 5 Solution
def log_arguments(func):
    def wrapper(*args, **kwargs):
        print("Function:", func.__name__)
        print("Args:", args)
        print("Kwargs:", kwargs)
        return func(*args, **kwargs)
    return wrapper


# Task 6 Solution
def log_arguments_safe(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Function:", func.__name__)
        print("Args:", args)
        print("Kwargs:", kwargs)
        return func(*args, **kwargs)
    return wrapper


@log_arguments_safe
def add(a, b):
    return a + b

print(add(3, 5))
print(add.__name__)


# ---------------------------------------------------------------------------
# Rank 4 — Advanced
# ---------------------------------------------------------------------------

# Task 7 Solution
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Execution time:", end - start)
        return result
    return wrapper


@timer
def slow_task():
    time.sleep(1)

slow_task()


# Task 8 Solution
def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat(3)
def greet():
    print("Hi")

greet()


# ---------------------------------------------------------------------------
# Rank 5 — Professional
# ---------------------------------------------------------------------------

# Task 9 Solution
def require_positive(func):
    @wraps(func)
    def wrapper(x):
        if x <= 0:
            raise ValueError("Value must be positive")
        return func(x)
    return wrapper


@require_positive
def square(x):
    return x * x

print(square(4))
# square(-2)  # would raise ValueError


# Task 10 Solution
# Decorators should NOT be used when logic is complex
# or tightly coupled to one function.
# In such cases, a normal function is clearer.

def process_numbers(numbers):
    total = 0
    for n in numbers:
        if n > 0:
            total += n
    return total

print(process_numbers([1, -2, 3, 4]))


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# These solutions demonstrate:
# - basic and advanced decorator patterns
# - correct use of functools.wraps
# - when decorators improve design
# - when plain functions are clearer
#
# Next Step:
# Move on to the next module when ready.
