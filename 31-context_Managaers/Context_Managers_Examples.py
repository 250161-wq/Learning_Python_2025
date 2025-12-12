"""
Context_Managers_Examples.py
Module 31 — Context Managers
Author: Peyman Miyandashti
Year: 2025

This file contains clear and practical examples
showing how context managers work in Python.
"""

# ---------------------------------------------------------------------------
# Example 1: Built-in Context Manager (Files)
# ---------------------------------------------------------------------------

with open("example.txt", "w") as file:
    file.write("Hello from a context manager\n")

with open("example.txt", "r") as file:
    print(file.read())


# ---------------------------------------------------------------------------
# Example 2: Manual Resource Handling (What with Replaces)
# ---------------------------------------------------------------------------

file = open("manual.txt", "w")
try:
    file.write("Manual handling\n")
finally:
    file.close()


# ---------------------------------------------------------------------------
# Example 3: Simple Custom Context Manager (Class-Based)
# ---------------------------------------------------------------------------

class SimpleContext:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")


with SimpleContext():
    print("Inside the context")


# ---------------------------------------------------------------------------
# Example 4: Context Manager Handling Exceptions
# ---------------------------------------------------------------------------

class ErrorHandlingContext:
    def __enter__(self):
        print("Context started")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print("Exception caught:", exc_type.__name__)
        print("Context ended")
        return True


with ErrorHandlingContext():
    raise RuntimeError("Example error")


# ---------------------------------------------------------------------------
# Example 5: Using contextlib.contextmanager
# ---------------------------------------------------------------------------

from contextlib import contextmanager

@contextmanager
def simple_manager():
    print("Enter")
    yield
    print("Exit")


with simple_manager():
    print("Doing work")


# ---------------------------------------------------------------------------
# Example 6: Measuring Execution Time
# ---------------------------------------------------------------------------

import time
from contextlib import contextmanager

@contextmanager
def timer():
    start = time.time()
    yield
    end = time.time()
    print("Elapsed time:", end - start)


with timer():
    total = 0
    for i in range(1_000_000):
        total += i


# ---------------------------------------------------------------------------
# Example 7: Nested Context Managers
# ---------------------------------------------------------------------------

with open("file1.txt", "w") as f1, open("file2.txt", "w") as f2:
    f1.write("File one\n")
    f2.write("File two\n")


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# These examples show:
# - why context managers exist
# - how they replace try/finally
# - how to build custom managers
#
# Next Step:
# Continue with Context_Managers_Tasks.py
