"""
Decorators_Examples.py
Module 39 — Decorators
Author: Peyman Miyandashti
Year: 2025

This file contains clear and practical examples
showing how decorators are used in Python.
"""

import time
from functools import wraps

# ---------------------------------------------------------------------------
# Example 1: Simple Decorator
# ---------------------------------------------------------------------------

def simple_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper


@simple_decorator
def say_hello():
    print("Hello")

say_hello()


# ---------------------------------------------------------------------------
# Example 2: Decorator with Return Value
# ---------------------------------------------------------------------------

def return_decorator(func):
    def wrapper():
        print("Calling function")
        return func()
    return wrapper


@return_decorator
def get_message():
    return "Message received"

print(get_message())


# ---------------------------------------------------------------------------
# Example 3: Decorator with Arguments
# ---------------------------------------------------------------------------

def args_decorator(func):
    def wrapper(*args, **kwargs):
        print("Arguments:", args, kwargs)
        return func(*args, **kwargs)
    return wrapper


@args_decorator
def add(a, b):
    return a + b

print(add(5, 7))


# ---------------------------------------------------------------------------
# Example 4: Using functools.wraps
# ---------------------------------------------------------------------------

def logging_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Running {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


@logging_decorator
def multiply(a, b):
    return a * b

print(multiply.__name__)
print(multiply(3, 4))


# ---------------------------------------------------------------------------
# Example 5: Timing Decorator
# ---------------------------------------------------------------------------

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Elapsed time:", end - start)
        return result
    return wrapper


@timer
def slow_function():
    time.sleep(1)

slow_function()


# ---------------------------------------------------------------------------
# Example 6: Decorator with Parameters
# ---------------------------------------------------------------------------

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
# Example 7: Decorator for Validation
# ---------------------------------------------------------------------------

def validate_positive(func):
    @wraps(func)
    def wrapper(x):
        if x < 0:
            raise ValueError("Value must be positive")
        return func(x)
    return wrapper


@validate_positive
def square(x):
    return x * x

print(square(5))
# square(-3)  # would raise ValueError


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# These examples show how decorators:
# - wrap function behavior
# - handle arguments and return values
# - apply reusable logic cleanly
#
# Next Step:
# Continue with Decorators_Tasks.py
