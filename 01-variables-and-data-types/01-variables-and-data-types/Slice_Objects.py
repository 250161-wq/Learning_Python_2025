"""
Module 37 — Slice Objects: Practice Exercises
Comprehensive practice with Python slice objects, from beginner
to more professional, production-style usage.

In this module I:
- Understand how the slice(start, stop, step) object works.
- Use slices as reusable “views” into lists and strings.
- Apply slicing for chunking, stepping, and reversing data.
- Use slices dynamically to simulate windows, pagination, and matrix extraction.
- Build a professional mini "data window manager" using slice objects.

Ranking system:
- Rank 1  -> Beginner: basic slice(start, stop, step) usage.
- Rank 2  -> Easy: reusable slice objects and applying them.
- Rank 3  -> Intermediate: dynamic slice generation and utilities.
- Rank 4  -> Advanced: slicing multidimensional structures.
- Rank 5  -> Professional: window/segment manager with slice objects.

Author: Peyman Miyandashti  
Date of Birth: 11/11/1983  
ID Number: 250161  
Year: 2025
"""

from __future__ import annotations
from typing import List, Any


# ===========================================================
# Rank 1 — Beginner
# Basic slice(start, stop, step)
# ===========================================================

print("Rank 1 — Beginner")

numbers = list(range(20))

s1 = slice(0, 5)      # first five items
s2 = slice(5, 15, 2)  # items from index 5 to 14, step 2
s3 = slice(None, None, -1)  # reverse slice

print("numbers:", numbers)
print("slice(0,5):", numbers[s1])
print("slice(5,15,2):", numbers[s2])
print("reverse:", numbers[s3])
print("-" * 50)


# ===========================================================
# Rank 2 — Easy
# Reusable slice objects
# ===========================================================

print("Rank 2 — Easy")

first_half = slice(0, len(numbers)//2)
second_half = slice(len(numbers)//2, None)

print("First half:", numbers[first_half])
print("Second half:", numbers[second_half])

# Slice applied to a string
text = "Hello Peyman!"
letters_only = slice(0, None, 2)

print("letters_only:", text[letters_only])
print("-" * 50)


# ===========================================================
# Rank 3 — Intermediate
# Dynamic slice generation utilities
# ===========================================================

print("Rank 3 — Intermediate")


def chunk_slice(start: int, size: int) -> slice:
    """
    Generates a slice for a chunk of `size` starting at `start`.
    """
    return slice(start, start + size)


def step_slice(step: int) -> slice:
    """
    Slice that selects every `step` element.
    """
    return slice(None, None, step)


nums = list(range(1, 21))

print("Chunk (start=5, size=4):", nums[chunk_slice(5, 4)])
print("Every 3rd element:", nums[step_slice(3)])
print("-" * 50)


# ===========================================================
# Rank 4 — Advanced
# Multidimensional slicing with slice objects
# ===========================================================

print("Rank 4 — Advanced")

matrix = [
    [10, 11, 12, 13],
    [20, 21, 22, 23],
    [30, 31, 32, 33],
    [40, 41, 42, 43],
]

# Extract rows 1–3 and columns 1–3
row_slice = slice(1, 3)
col_slice = slice(1, 3)

submatrix = [row[col_slice] for row in matrix[row_slice]]

print("Original matrix:")
for row in matrix:
    print(row)

print("\nSubmatrix rows 1–3, cols 1–3:")
for row in submatrix:
    print(row)

# Reverse rows and columns
print("\nFully reversed matrix:")
for row in matrix[::-1]:
    print(row[::-1])

print("-" * 50)


# ===========================================================
# Rank 5 — Professional
# Window Manager using Slice Objects
# ===========================================================

print("Rank 5 — Professional")


class WindowManager:
    """
    A class that manages sliding windows into a dataset using slice objects.

    Methods:
    - current(): return current window of data
    - next(): move window forward
    - prev(): move window backward
    - goto(index): jump to a specific starting index
    """

    def __init__(self, data: List[Any], window_size: int) -> None:
        self.data = data
        self.window_size = window_size
        self.position = 0  # starting index

    @property
    def window_slice(self) -> slice:
        """
        Computed slice describing the current window.
        """
        return slice(self.position, self.position + self.window_size)

    def current(self) -> List[Any]:
        return self.data[self.window_slice]

    def next(self) -> List[Any]:
        if self.position + self.window_size < len(self.data):
            self.position += self.window_size
        return self.current()

    def prev(self) -> List[Any]:
        if self.position - self.window_size >= 0:
            self.position -= self.window_size
        return self.current()

    def goto(self, index: int) -> List[Any]:
        index = max(0, min(index, len(self.data) - self.window_size))
        self.position = index
        return self.current()

    def __repr__(self) -> str:
        return f"WindowManager(size={self.window_size}, position={self.position})"


data_list = list(range(1, 51))
manager = WindowManager(data_list, 10)

print("Initial window:", manager.current())
print("Next window:", manager.next())
print("Next window:", manager.next())
print("Previous window:", manager.prev())
print("Jump to index 25:", manager.goto(25))

print("-" * 50)
