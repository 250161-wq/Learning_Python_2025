"""
Iterators_Tasks_Solutions.py
Module 29 — Iterators
Author: Peyman Miyandashti
Year: 2025

This file contains clean and professional solutions
for the iterator exercises in this module.
"""

# ---------------------------------------------------------------------------
# Rank 1 — Beginner
# ---------------------------------------------------------------------------

# Task 1 Solution
numbers = [1, 2, 3]

for number in numbers:
    print(number)


# Task 2 Solution
values = [10, 20, 30]
iterator = iter(values)

try:
    while True:
        print(next(iterator))
except StopIteration:
    pass


# ---------------------------------------------------------------------------
# Rank 2 — Easy
# ---------------------------------------------------------------------------

# Task 3 Solution
text = "Python"
text_iterator = iter(text)

try:
    while True:
        print(next(text_iterator))
except StopIteration:
    pass


# Task 4 Solution
data = [4, 5, 6]
data_iterator = iter(data)

while True:
    try:
        value = next(data_iterator)
        print(value)
    except StopIteration:
        break


# ---------------------------------------------------------------------------
# Rank 3 — Intermediate
# ---------------------------------------------------------------------------

# Task 5 Solution
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


# Task 6 Solution
class ReverseListIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        value = self.data[self.index]
        self.index -= 1
        return value


for value in ReverseListIterator([1, 2, 3]):
    print(value)


# ---------------------------------------------------------------------------
# Rank 4 — Advanced
# ---------------------------------------------------------------------------

# Task 7 Solution
class EvenNumbers:
    def __init__(self, limit):
        self.current = 0
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.limit:
            raise StopIteration
        value = self.current
        self.current += 2
        return value


for even in EvenNumbers(10):
    print(even)


# Task 8 Solution
class FibonacciIterator:
    def __init__(self, max_value):
        self.a = 0
        self.b = 1
        self.max_value = max_value

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > self.max_value:
            raise StopIteration
        value = self.a
        self.a, self.b = self.b, self.a + self.b
        return value


for fib in FibonacciIterator(20):
    print(fib)


# ---------------------------------------------------------------------------
# Rank 5 — Professional
# ---------------------------------------------------------------------------

# Task 9 Solution
class RestartableRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        current = self.start
        end = self.end

        class _Iterator:
            def __iter__(self):
                return self

            def __next__(self):
                nonlocal current
                if current > end:
                    raise StopIteration
                value = current
                current += 1
                return value

        return _Iterator()


for num in RestartableRange(1, 3):
    print(num)


# Task 10 Solution
class SafeListIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value


for item in SafeListIterator(["a", "b", "c"]):
    print(item)


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# These solutions demonstrate proper use of the iterator protocol,
# safe handling of StopIteration, and professional iterator design.
#
# Next Step:
# Continue to the next module when ready.
