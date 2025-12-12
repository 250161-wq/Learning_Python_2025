"""
Context_Managers_Notes.py
Module 31 — Context Managers
Author: Peyman Miyandashti
Year: 2025

This module explains context managers in Python.
Context managers control setup and cleanup logic
using the 'with' statement.
"""

# ---------------------------------------------------------------------------
# 1. What Is a Context Manager?
# ---------------------------------------------------------------------------
# A context manager is an object that defines:
# - what happens when a block starts
# - what happens when a block ends
#
# This is handled using __enter__ and __exit__ methods.


# ---------------------------------------------------------------------------
# 2. Why Context Managers Exist
# ---------------------------------------------------------------------------
# Context managers ensure that resources are always released,
# even if an error occurs during execution.
#
# This prevents:
# - resource leaks
# - forgotten cleanup
# - inconsistent program state


# ---------------------------------------------------------------------------
# 3. The with Statement
# ---------------------------------------------------------------------------
# The 'with' statement is used to work with context managers.

# Example:
# with open("data.txt", "r") as file:
#     content = file.read()


# ---------------------------------------------------------------------------
# 4. What Happens Internally
# ---------------------------------------------------------------------------
# with expression as variable:
#     block
#
# Internally:
# - __enter__() is called at the start
# - __exit__() is called at the end


# ---------------------------------------------------------------------------
# 5. Basic Custom Context Manager (Class-Based)
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
# 6. Handling Exceptions
# ---------------------------------------------------------------------------
# __exit__ receives exception details if an error occurs.
# Returning True suppresses the exception.

class SafeContext:
    def __enter__(self):
        print("Start")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print("Exception handled:", exc_type)
        print("End")
        return True


with SafeContext():
    raise ValueError("Something went wrong")


# ---------------------------------------------------------------------------
# 7. Using contextlib
# ---------------------------------------------------------------------------
# contextlib allows creating context managers using generators.

from contextlib import contextmanager

@contextmanager
def simple_manager():
    print("Enter")
    yield
    print("Exit")


with simple_manager():
    print("Working inside context")


# ---------------------------------------------------------------------------
# 8. When to Use Context Managers
# ---------------------------------------------------------------------------
# Use context managers when:
# - resources must be cleaned up
# - setup and teardown logic is required
# - safety and readability matter


# ---------------------------------------------------------------------------
# 9. Best Practices
# ---------------------------------------------------------------------------
# - Always use 'with' for files and locks
# - Prefer context managers over try/finally
# - Keep __enter__ and __exit__ simple
# - Avoid complex logic inside context managers


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# Context managers enforce clean structure and safe execution.
# They are essential for professional Python code.
#
# Next Step:
# Continue with Context_Managers_Examples.py
