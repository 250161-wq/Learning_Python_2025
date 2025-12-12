"""
Coroutines_Tasks_Solutions.py
Module 30 — Coroutines
Author: Peyman Miyandashti
Year: 2025

This file contains clean and professional solutions
for the coroutine exercises in this module.
"""

# ---------------------------------------------------------------------------
# Rank 1 — Beginner
# ---------------------------------------------------------------------------

# Task 1 Solution
def simple_receiver():
    while True:
        value = yield
        print("Received:", value)


coro = simple_receiver()
next(coro)
coro.send("Hello")


# Task 2 Solution
def greeting_receiver():
    while True:
        name = yield
        print(f"Hello, {name}!")


coro = greeting_receiver()
next(coro)
coro.send("Peyman")


# ---------------------------------------------------------------------------
# Rank 2 — Easy
# ---------------------------------------------------------------------------

# Task 3 Solution
def counter():
    count = 0
    while True:
        yield
        count += 1
        print("Count:", count)


coro = counter()
next(coro)
coro.send(1)
coro.send(1)
coro.send(1)


# Task 4 Solution
def sum_receiver():
    total = 0
    while True:
        value = yield
        total += value
        print("Total:", total)


coro = sum_receiver()
next(coro)
coro.send(5)
coro.send(10)


# ---------------------------------------------------------------------------
# Rank 3 — Intermediate
# ---------------------------------------------------------------------------

# Task 5 Solution
def average_calculator():
    total = 0
    count = 0
    while True:
        value = yield
        total += value
        count += 1
        print("Average:", total / count)


coro = average_calculator()
next(coro)
coro.send(10)
coro.send(20)
coro.send(30)


# Task 6 Solution
def filter_positive():
    while True:
        value = yield
        if value > 0:
            print("Positive:", value)


coro = filter_positive()
next(coro)
coro.send(-5)
coro.send(8)


# ---------------------------------------------------------------------------
# Rank 4 — Advanced
# ---------------------------------------------------------------------------

# Task 7 Solution
def logger():
    try:
        while True:
            message = yield
            print("Log:", message)
    except GeneratorExit:
        print("Logger closed safely")


coro = logger()
next(coro)
coro.send("Start")
coro.send("Running")
coro.close()


# Task 8 Solution
def square_processor():
    try:
        while True:
            value = yield
            print("Squared:", value ** 2)
    except GeneratorExit:
        print("Processor closed")


def sender(target):
    for n in range(1, 4):
        target.send(n)
    target.close()


proc = square_processor()
next(proc)
sender(proc)


# ---------------------------------------------------------------------------
# Rank 5 — Professional
# ---------------------------------------------------------------------------

# Task 9 Solution
def running_stats():
    total = 0
    count = 0
    while True:
        value = yield
        count += 1
        total += value
        print("Count:", count, "Total:", total, "Average:", total / count)


coro = running_stats()
next(coro)
coro.send(5)
coro.send(15)
coro.send(30)


# Task 10 Solution
def data_sink():
    try:
        while True:
            yield
    except GeneratorExit:
        print("Data sink closed safely")


coro = data_sink()
next(coro)
coro.send("any data")
coro.send(123)
coro.close()


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# These solutions demonstrate proper coroutine usage,
# safe priming, state management, and clean shutdown.
#
# Next Step:
# Move to the next module when ready.
