"""
Module 11 — Advanced Functions
High-level practice with Python functions including:
- higher-order functions
- lambda expressions
- closures
- decorators
- functional programming patterns

This module expands on Module 7 (basic functions) and teaches
professional techniques used in real software engineering.

Ranking:
- Rank 1 -> Beginner Advanced: lambda + simple higher-order use.
- Rank 2 -> Easy Advanced: callbacks + passing functions as data.
- Rank 3 -> Intermediate: closures + stateful inner functions.
- Rank 4 -> Advanced: decorators + wrapper logic.
- Rank 5 -> Professional: real-world decorators & functional pipelines.

Author: Peyman Miyandashti
Student at UPBC — IT Engineering & Digital Innovation
Year: 2025
"""

# ===========================================================
# Rank 1 — Beginner Advanced
# Lambda functions + simple higher-order function
# ===========================================================

print("Rank 1 — Beginner Advanced")

# Basic lambda (anonymous function)
square = lambda x: x * x
double = lambda x: x * 2

print("Square of 11:", square(11))
print("Double of 11:", double(11))

# Higher-order: a function that TAKES another function
def apply_operation(value, func):
    return func(value)

print("Apply square on 7:", apply_operation(7, square))
print("Apply double on 7:", apply_operation(7, double))

print("-" * 50)


# ===========================================================
# Rank 2 — Easy Advanced
# Callbacks — passing functions into other functions
# ===========================================================

print("Rank 2 — Easy Advanced")

def notify_user(callback):
    """
    Executes a callback function after performing an action.
    """
    print("Processing some task...")
    return callback()

def peyman_notification():
    return "Task Completed — Great job, Peyman!"

print(notify_user(peyman_notification))

print("-" * 50)


# ===========================================================
# Rank 3 — Intermediate
# Closures — functions that remember state
# ===========================================================

print("Rank 3 — Intermediate")

def make_multiplier(factor):
    """
    Returns a function that MULTIPLIES any number by 'factor'.
    Demonstrates closures.
    """
    def inner(number):
        return number * factor
    return inner

double_func = make_multiplier(2)
triple_func = make_multiplier(3)

print("Double 10:", double_func(10))
print("Triple 10:", triple_func(10))

# Real example: GPA scaling (fun example)
scale_gpa = make_multiplier(1.1)
print("Scaled GPA of 9.5:", scale_gpa(9.5))

print("-" * 50)


# ===========================================================
# Rank 4 — Advanced
# Decorators — modifying function behavior
# ===========================================================

print("Rank 4 — Advanced")

def log_function(func):
    """
    Decorator that logs when a function is called.
    """
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_function
def greet(name):
    return f"Hello, {name}! Welcome back."

print(greet("Peyman"))

print("-" * 50)


# ===========================================================
# Rank 5 — Professional
# Real-world decorator + functional pipeline
# ===========================================================

print("Rank 5 — Professional")

import time

def performance_timer(func):
    """
    Decorator that measures how long a function takes.
    Professional-level debugging & profiling technique.
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[PERFORMANCE] {func.__name__} took {end - start:.6f}s")
        return result
    return wrapper

@performance_timer
def heavy_computation(limit):
    total = 0
    for i in range(limit):
        total += i * i
    return total

print("Result of heavy computation:", heavy_computation(500_000))


# Functional pipeline pattern (professional)
def pipeline(data, *funcs):
    """
    Pass data through multiple functions in order.
    """
    for f in funcs:
        data = f(data)
    return data

increment = lambda x: x + 1
square = lambda x: x * x
halve = lambda x: x / 2

result = pipeline(10, increment, square, halve)

print("Pipeline result:", result)
print("-" * 50)
