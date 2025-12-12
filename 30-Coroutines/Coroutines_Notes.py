"""
Coroutines_Notes.py
Module 30 — Coroutines
Author: Peyman Miyandashti
Year: 2025

This module explains coroutines in Python.
Coroutines are functions that can pause execution,
receive values, and resume where they left off.
"""

# ---------------------------------------------------------------------------
# 1. What Is a Coroutine?
# ---------------------------------------------------------------------------
# A coroutine is a special kind of generator.
# It uses 'yield' to RECEIVE values, not just produce them.
#
# Coroutines are consumers of data.


# ---------------------------------------------------------------------------
# 2. Generators vs Coroutines
# ---------------------------------------------------------------------------
# Generators:
# - produce values outward
# - use 'yield value'
#
# Coroutines:
# - receive values inward
# - use 'value = yield'


# ---------------------------------------------------------------------------
# 3. Basic Coroutine Structure
# ---------------------------------------------------------------------------

def simple_coroutine():
    print("Coroutine started")
    value = yield
    print("Received:", value)


# ---------------------------------------------------------------------------
# 4. Priming a Coroutine
# ---------------------------------------------------------------------------
# A coroutine must be started before sending values.
# This is called priming.

coro = simple_coroutine()
next(coro)          # starts the coroutine
coro.send(10)       # sends a value


# ---------------------------------------------------------------------------
# 5. Receiving Multiple Values
# ---------------------------------------------------------------------------

def accumulator():
    total = 0
    while True:
        value = yield total
        total += value


coro = accumulator()
next(coro)
print(coro.send(5))   # 5
print(coro.send(10))  # 15


# ---------------------------------------------------------------------------
# 6. Infinite Coroutines
# ---------------------------------------------------------------------------
# Coroutines often run forever until explicitly closed.

def printer():
    while True:
        message = yield
        print("Message:", message)


coro = printer()
next(coro)
coro.send("Hello")
coro.send("World")


# ---------------------------------------------------------------------------
# 7. Closing a Coroutine
# ---------------------------------------------------------------------------
# Coroutines should be closed when no longer needed.

coro.close()


# ---------------------------------------------------------------------------
# 8. Handling Coroutine Exit
# ---------------------------------------------------------------------------

def safe_coroutine():
    try:
        while True:
            value = yield
            print("Processing:", value)
    except GeneratorExit:
        print("Coroutine closed safely")


coro = safe_coroutine()
next(coro)
coro.send(1)
coro.close()


# ---------------------------------------------------------------------------
# 9. When to Use Coroutines
# ---------------------------------------------------------------------------
# Use coroutines when:
# - values arrive over time
# - state must be preserved
# - pull-based iteration is not ideal
#
# Examples:
# - data pipelines
# - event handling
# - streaming input


# ---------------------------------------------------------------------------
# 10. Best Practices
# ---------------------------------------------------------------------------
# - Always prime coroutines before sending data
# - Close coroutines when finished
# - Keep coroutine logic focused
# - Use generators when you only need output
# - Use coroutines when you need input


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# Coroutines introduce controlled execution flow.
# They are a foundation for advanced asynchronous programming.
#
# Next Step:
# Continue with Coroutines_Examples.py
