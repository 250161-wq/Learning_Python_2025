"""
Iterators_Notes.py
Module 29 — Iterators
Author: Peyman Miyandashti
Year: 2025

This module explains iterators in Python.
Iterators define how objects are traversed one value at a time.
"""

# ---------------------------------------------------------------------------
# 1. What Is an Iterable?
# ---------------------------------------------------------------------------
# An iterable is any object that can return an iterator.
# Examples include:
# - lists
# - tuples
# - strings
# - sets
# - dictionaries

numbers = [1, 2, 3]
text = "Python"


# ---------------------------------------------------------------------------
# 2. What Is an Iterator?
# ---------------------------------------------------------------------------
# An iterator is an object that:
# - remembers its current position
# - returns values one at a time
# - raises StopIteration when finished


# ---------------------------------------------------------------------------
# 3. Using iter()
# ---------------------------------------------------------------------------
# iter() converts an iterable into an iterator.

numbers_iterator = iter(numbers)


# ---------------------------------------------------------------------------
# 4. Using next()
# ---------------------------------------------------------------------------
# next() retrieves the next value from an iterator.

print(next(numbers_iterator))  # 1
print(next(numbers_iterator))  # 2
print(next(numbers_iterator))  # 3
# next(numbers_iterator) would raise StopIteration


# ---------------------------------------------------------------------------
# 5. StopIteration
# ---------------------------------------------------------------------------
# When an iterator is exhausted, Python raises StopIteration.
# for-loops handle this automatically.


# ---------------------------------------------------------------------------
# 6. Iterators and for-loops
# ---------------------------------------------------------------------------
# A for-loop does the following internally:
# 1. calls iter()
# 2. repeatedly calls next()
# 3. stops when StopIteration occurs

for char in text:
    print(char)


# ---------------------------------------------------------------------------
# 7. Iterators Are Single-Use
# ---------------------------------------------------------------------------
# Once an iterator is exhausted, it cannot be reused.

iterator = iter([10, 20, 30])

for value in iterator:
    print(value)

# This will not print anything
for value in iterator:
    print(value)


# ---------------------------------------------------------------------------
# 8. Creating a Custom Iterator
# ---------------------------------------------------------------------------
# Custom iterators are usually classes that define:
# - __iter__()
# - __next__()

class CountUp:
    def __init__(self, limit):
        self.current = 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.limit:
            raise StopIteration
        value = self.current
        self.current += 1
        return value


for number in CountUp(5):
    print(number)


# ---------------------------------------------------------------------------
# 9. Iterators vs Generators
# ---------------------------------------------------------------------------
# Generators automatically implement the iterator protocol.
# Iterators require explicit class definitions.


# ---------------------------------------------------------------------------
# 10. Best Practices
# ---------------------------------------------------------------------------
# - Use for-loops instead of next() when possible
# - Use generators for simpler iteration logic
# - Use iterator classes when state control is required
# - Always handle StopIteration properly


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# Iterators explain how Python moves through data.
# Understanding them makes loops, generators, and pipelines clearer.
#
# Next Step:
# Continue with Iterators_Examples.py
