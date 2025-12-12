"""
Context_Managers_Tasks_Solutions.py
Module 31 — Context Managers
Author: Peyman Miyandashti
Year: 2025

This file contains clean and professional solutions
for the context manager exercises in this module.
"""

# ---------------------------------------------------------------------------
# Rank 1 — Beginner
# ---------------------------------------------------------------------------

# Task 1 Solution
with open("task1.txt", "w") as file:
    file.write("Hello from context manager")

with open("task1.txt", "r") as file:
    print(file.read())


# Task 2 Solution
file = open("task2.txt", "w")
try:
    file.write("Using try/finally")
finally:
    file.close()

# Rewritten using with
with open("task2_with.txt", "w") as file:
    file.write("Using with statement")


# ---------------------------------------------------------------------------
# Rank 2 — Easy
# ---------------------------------------------------------------------------

# Task 3 Solution
class SimpleContext:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")


with SimpleContext():
    print("Inside block")


# Task 4 Solution
class SafeContext:
    def __enter__(self):
        print("Start")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print("Handled exception:", exc_type.__name__)
        print("End")
        return True


with SafeContext():
    raise ValueError("Example error")


# ---------------------------------------------------------------------------
# Rank 3 — Intermediate
# ---------------------------------------------------------------------------

# Task 5 Solution
from contextlib import contextmanager

@contextmanager
def simple_manager():
    print("start")
    yield
    print("end")


with simple_manager():
    print("Doing work")


# Task 6 Solution
import time
from contextlib import contextmanager

@contextmanager
def timer():
    start = time.time()
    yield
    end = time.time()
    print("Elapsed time:", end - start)


with timer():
    total = sum(range(1_000_000))


# ---------------------------------------------------------------------------
# Rank 4 — Advanced
# ---------------------------------------------------------------------------

# Task 7 Solution
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()


with FileManager("task7.txt", "w") as file:
    file.write("Safe file handling")


# Task 8 Solution
class TemporaryValue:
    def __init__(self, obj, attr, temp_value):
        self.obj = obj
        self.attr = attr
        self.temp_value = temp_value
        self.original_value = None

    def __enter__(self):
        self.original_value = getattr(self.obj, self.attr)
        setattr(self.obj, self.attr, self.temp_value)

    def __exit__(self, exc_type, exc_value, traceback):
        setattr(self.obj, self.attr, self.original_value)


class Config:
    mode = "production"


with TemporaryValue(Config, "mode", "debug"):
    print("Inside:", Config.mode)

print("Outside:", Config.mode)


# ---------------------------------------------------------------------------
# Rank 5 — Professional
# ---------------------------------------------------------------------------

# Task 9 Solution
class LoggerContext:
    def __enter__(self):
        print("Log start")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Log end")


with LoggerContext():
    print("Executing code")


# Task 10 Solution
class SuppressValueError:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        return exc_type is ValueError


with SuppressValueError():
    raise ValueError("This error is suppressed")

# Other exceptions will still propagate


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# These solutions demonstrate safe and professional use
# of context managers, including cleanup and exception control.
#
# Next Step:
# Move on to the next module when ready.
