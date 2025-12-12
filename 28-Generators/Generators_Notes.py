"""
Generators_Notes.py
Module 28 — Generators
Author: Peyman Miyandashti
Year: 2025

This module explains generators in Python.
Generators allow functions to produce values one at a time,
using lazy evaluation and the 'yield' keyword.
"""

# ---------------------------------------------------------------------------
# 1. What Is a Generator?
# ---------------------------------------------------------------------------
# A generator is a special type of function that produces values one at a time.
# Instead of returning a value and stopping, it yields a value and pauses.
#
# When execution resumes, the generator continues from where it left off.


# ---------------------------------------------------------------------------
# 2. Why Generators Exist
# ---------------------------------------------------------------------------
# Generators are useful when:
# - data is large
# - data is infinite
# - memory efficiency matters
#
# They avoid storing all values in memory.


# ---------------------------------------------------------------------------
# 3. Simple Generator Function
# ---------------------------------------------------------------------------

def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()

print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3


# ---------------------------------------------------------------------------
# 4. Generator vs List
# ---------------------------------------------------------------------------
# Lists compute and store all values immediately.
numbers_list = [x for x in range(5)]

# Generators compute values only when requested.
numbers_generator = (x for x in range(5))

print(numbers_list)
print(numbers_generator)


# ---------------------------------------------------------------------------
# 5. Iterating Over a Generator
# ---------------------------------------------------------------------------
# The safest and most common way to use a generator is with a for-loop.

def count_up(limit):
    current = 1
    while current <= limit:
        yield current
        current += 1

for number in count_up(5):
    print(number)


# ---------------------------------------------------------------------------
# 6. Using next()
# ---------------------------------------------------------------------------
# next() retrieves the next available value.

gen = count_up(3)
print(next(gen))
print(next(gen))
print(next(gen))
# A further call would raise StopIteration.


# ---------------------------------------------------------------------------
# 7. StopIteration
# ---------------------------------------------------------------------------
# When a generator has no more values, Python raises StopIteration.
# for-loops handle this automatically.


# ---------------------------------------------------------------------------
# 8. Infinite Generators
# ---------------------------------------------------------------------------
# Generators can run forever if designed that way.

def infinite_counter():
    num = 0
    while True:
        yield num
        num += 1

# Example usage (commented to avoid infinite loop):
# for n in infinite_counter():
#     print(n)


# ---------------------------------------------------------------------------
# 9. Memory Efficiency
# ---------------------------------------------------------------------------
# Generators are ideal for:
# - file processing
# - streams
# - large datasets
# - pipelines


# ---------------------------------------------------------------------------
# 10. Best Practices
# ---------------------------------------------------------------------------
# - Use generators when data size is unknown or large
# - Prefer generators for sequential processing
# - Keep generator logic simple and readable
# - Avoid converting generators to lists unless necessary


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# Generators allow Python programs to work efficiently and scale well.
# Understanding generators is a key step toward professional-level Python.
#
# Next Step:
# Continue with Generators_Examples.py
