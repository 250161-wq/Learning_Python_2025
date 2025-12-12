"""
Generators_Examples.py
Module 28 — Generators
Author: Peyman Miyandashti
Year: 2025

This file contains short and practical examples that demonstrate
how generators work in Python and how they differ from lists.
"""

# ---------------------------------------------------------------------------
# Example 1: Basic Generator Function
# ---------------------------------------------------------------------------

def numbers_generator():
    yield 1
    yield 2
    yield 3

for number in numbers_generator():
    print(number)


# ---------------------------------------------------------------------------
# Example 2: Generator vs List (Memory Concept)
# ---------------------------------------------------------------------------

numbers_list = [x for x in range(5)]
numbers_gen = (x for x in range(5))

print("List:", numbers_list)
print("Generator:", numbers_gen)


# ---------------------------------------------------------------------------
# Example 3: Using next() Manually
# ---------------------------------------------------------------------------

def count_to_three():
    yield 1
    yield 2
    yield 3

gen = count_to_three()

print(next(gen))
print(next(gen))
print(next(gen))
# next(gen) here would raise StopIteration


# ---------------------------------------------------------------------------
# Example 4: Generator with a Loop
# ---------------------------------------------------------------------------

def count_up(limit):
    current = 1
    while current <= limit:
        yield current
        current += 1

for value in count_up(5):
    print(value)


# ---------------------------------------------------------------------------
# Example 5: Generator with a Condition
# ---------------------------------------------------------------------------

def even_numbers(limit):
    for number in range(limit):
        if number % 2 == 0:
            yield number

for even in even_numbers(10):
    print(even)


# ---------------------------------------------------------------------------
# Example 6: Infinite Generator (Controlled Usage)
# ---------------------------------------------------------------------------

def infinite_counter():
    num = 0
    while True:
        yield num
        num += 1

counter = infinite_counter()

for _ in range(5):
    print(next(counter))


# ---------------------------------------------------------------------------
# Example 7: Generator Expression
# ---------------------------------------------------------------------------

squares = (x ** 2 for x in range(5))

for square in squares:
    print(square)


# ---------------------------------------------------------------------------
# Example 8: Generator Used Once
# ---------------------------------------------------------------------------
# Once a generator is exhausted, it cannot be reused.

gen = (x for x in range(3))

for x in gen:
    print(x)

print("Generator exhausted")

# This loop will not print anything
for x in gen:
    print(x)


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# These examples show how generators:
# - produce values lazily
# - save memory
# - are ideal for large or infinite data
#
# Next Step:
# Continue with Generators_Tasks.py
