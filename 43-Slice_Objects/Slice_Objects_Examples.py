"""
Slice_Objects_Examples.py
Module 43 — Slice Objects
Author: Peyman Miyandashti
Year: 2025

This file contains clear and practical examples
showing how slice objects are used in Python.
"""

# ---------------------------------------------------------------------------
# Example 1: Basic Slice Object
# ---------------------------------------------------------------------------

numbers = [10, 20, 30, 40, 50, 60]

middle = slice(1, 5)
print(numbers[middle])


# ---------------------------------------------------------------------------
# Example 2: Slice with Step
# ---------------------------------------------------------------------------

every_second = slice(None, None, 2)
print(numbers[every_second])


# ---------------------------------------------------------------------------
# Example 3: Comparing Slice Syntax and Slice Object
# ---------------------------------------------------------------------------

print(numbers[2:5])
same_slice = slice(2, 5)
print(numbers[same_slice])


# ---------------------------------------------------------------------------
# Example 4: Reusable Slice Logic
# ---------------------------------------------------------------------------

first_part = slice(0, 3)
last_part = slice(3, None)

print(numbers[first_part])
print(numbers[last_part])


# ---------------------------------------------------------------------------
# Example 5: Slicing Strings with Slice Objects
# ---------------------------------------------------------------------------

text = "LearningPython"
first_word = slice(0, 8)
second_word = slice(8, None)

print(text[first_word])
print(text[second_word])


# ---------------------------------------------------------------------------
# Example 6: Slice Attributes
# ---------------------------------------------------------------------------

s = slice(1, 10, 3)
print(s.start)
print(s.stop)
print(s.step)


# ---------------------------------------------------------------------------
# Example 7: Slice Objects Passed as Arguments
# ---------------------------------------------------------------------------

def apply_slice(data, slicer):
    return data[slicer]

print(apply_slice(numbers, slice(1, 4)))


# ---------------------------------------------------------------------------
# Example 8: Slice Objects in Custom Classes
# ---------------------------------------------------------------------------

class DataContainer:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, item):
        if isinstance(item, slice):
            return self.data[item]
        return self.data[item]


container = DataContainer(numbers)
print(container[1:5])
print(container[slice(0, None, 2)])


# ---------------------------------------------------------------------------
# Example 9: Negative Indices with Slice Objects
# ---------------------------------------------------------------------------

last_three = slice(-3, None)
print(numbers[last_three])


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# These examples show how slice objects:
# - make slicing reusable
# - improve readability
# - work with lists, strings, and custom classes
#
# Next Step:
# Continue with Slice_Objects_Tasks.py
