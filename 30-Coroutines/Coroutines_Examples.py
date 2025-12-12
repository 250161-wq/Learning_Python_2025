"""
Coroutines_Examples.py
Module 30 — Coroutines
Author: Peyman Miyandashti
Year: 2025

This file contains clear and practical examples
showing how coroutines work in Python.
"""

# ---------------------------------------------------------------------------
# Example 1: Minimal Coroutine
# ---------------------------------------------------------------------------

def simple_coroutine():
    print("Coroutine started")
    value = yield
    print("Received:", value)

coro = simple_coroutine()
next(coro)
coro.send(100)


# ---------------------------------------------------------------------------
# Example 2: Coroutine Receiving Multiple Values
# ---------------------------------------------------------------------------

def receiver():
    while True:
        value = yield
        print("Got:", value)

coro = receiver()
next(coro)

coro.send("Hello")
coro.send("World")
coro.send(42)


# ---------------------------------------------------------------------------
# Example 3: Coroutine with State (Accumulator)
# ---------------------------------------------------------------------------

def accumulator():
    total = 0
    while True:
        value = yield total
        total += value

coro = accumulator()
next(coro)

print(coro.send(5))
print(coro.send(10))
print(coro.send(3))


# ---------------------------------------------------------------------------
# Example 4: Closing a Coroutine
# ---------------------------------------------------------------------------

def logger():
    try:
        while True:
            message = yield
            print("Log:", message)
    except GeneratorExit:
        print("Logger closed")

coro = logger()
next(coro)

coro.send("Start")
coro.send("Processing")
coro.close()


# ---------------------------------------------------------------------------
# Example 5: Coroutine Pipeline (Sender → Processor)
# ---------------------------------------------------------------------------

def processor():
    try:
        while True:
            value = yield
            print("Processed:", value * 2)
    except GeneratorExit:
        print("Processor closed")

def sender(target):
    for number in range(1, 4):
        target.send(number)
    target.close()

proc = processor()
next(proc)
sender(proc)


# ---------------------------------------------------------------------------
# Example 6: Using send(None)
# ---------------------------------------------------------------------------
# send(None) is equivalent to next()

def echo():
    value = yield
    print("Echo:", value)

coro = echo()
coro.send(None)
coro.send("Test")


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# These examples show how coroutines:
# - receive values dynamically
# - preserve internal state
# - are closed safely
# - can form simple pipelines
#
# Next Step:
# Continue with Coroutines_Tasks.py
