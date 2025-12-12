"""
Iterators_Examples.py
Module 29 — Iterators
Author: Peyman Miyandashti
Year: 2025

This file contains clear and practical examples
showing how iterators work in Python.
"""

# ---------------------------------------------------------------------------
# Example 1: Iterating Over an Iterable
# ---------------------------------------------------------------------------

numbers = [1, 2, 3]

for num in numbers:
    print(num)


# ---------------------------------------------------------------------------
# Example 2: Using iter() and next()
# ---------------------------------------------------------------------------

values = [10, 20, 30]
iterator = iter(values)

print(next(iterator))
print(next(iterator))
print(next(iterator))
# next(iterator) here would raise StopIteration


# ---------------------------------------------------------------------------
# Example 3: Iterating Over a String
# ---------------------------------------------------------------------------

text = "Python"
text_iterator = iter(text)

print(next(text_iterator))
print(next(text_iterator))
print(next(text_iterator))


# ---------------------------------------------------------------------------
# Example 4: for-loop Behind the Scenes
# ---------------------------------------------------------------------------
# This shows what a for-loop does internally.

data = [4, 5, 6]
data_iterator = iter(data)

while True:
    try:
        value = next(data_iterator)
        print(value)
    except StopIteration:
        break


# ---------------------------------------------------------------------------
# Example 5: Iterator Exhaustion
# ---------------------------------------------------------------------------
# Iterators can only be used once.

iterator = iter([100, 200, 300])

for value in iterator:
    print(value)

print("Iterator exhausted")

for value in iterator:
    print(value)


# ---------------------------------------------------------------------------
# Example 6: Custom Iterator Class
# ---------------------------------------------------------------------------

class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


for number in CountDown(5):
    print(number)


# ---------------------------------------------------------------------------
# Example 7: Iterator vs Generator
# ---------------------------------------------------------------------------

def generator_example():
    for i in range(3):
        yield i

gen = generator_example()
gen_iterator = iter(gen)

print(next(gen_iterator))
print(next(gen_iterator))
print(next(gen_iterator))


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# These examples demonstrate:
# - how iteration works internally
# - how iter() and next() behave
# - how custom iterators control iteration
#
# Next Step:
# Continue with Iterators_Tasks.py
