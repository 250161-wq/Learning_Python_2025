"""
Slice_Objects_Tasks_Solutions.py
Module 43 — Slice Objects
Author: Peyman Miyandashti
Year: 2025

This file contains clean and professional solutions
for the slice object exercises in this module.
"""

# ---------------------------------------------------------------------------
# Rank 1 — Beginner
# ---------------------------------------------------------------------------

# Task 1 Solution
numbers = [10, 20, 30, 40, 50]
first_three = slice(0, 3)
print(numbers[first_three])


# Task 2 Solution
print(numbers[0:3])
print(numbers[first_three])


# ---------------------------------------------------------------------------
# Rank 2 — Easy
# ---------------------------------------------------------------------------

# Task 3 Solution
every_second = slice(None, None, 2)
print(numbers[every_second])


# Task 4 Solution
text = "SliceObjects"
print(text[every_second])


# ---------------------------------------------------------------------------
# Rank 3 — Intermediate
# ---------------------------------------------------------------------------

# Task 5 Solution
header = slice(0, 2)
body = slice(2, 4)
footer = slice(4, None)

data = ["H1", "H2", "B1", "B2", "F1"]
print(data[header])
print(data[body])
print(data[footer])


# Task 6 Solution
def apply_slice(data, slicer):
    return data[slicer]

print(apply_slice(data, slice(1, 4)))


# ---------------------------------------------------------------------------
# Rank 4 — Advanced
# ---------------------------------------------------------------------------

# Task 7 Solution
class CustomData:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, item):
        if isinstance(item, slice):
            return self.items[item]
        return self.items[item]


custom = CustomData([1, 2, 3, 4, 5])
print(custom[1:4])


# Task 8 Solution
print(custom[2])
print(custom[slice(0, None, 2)])


# ---------------------------------------------------------------------------
# Rank 5 — Professional
# ---------------------------------------------------------------------------

# Task 9 Solution
# Reusable slice objects help document intent clearly.

first_page = slice(0, 10)
second_page = slice(10, 20)

dataset = list(range(30))
print(dataset[first_page])
print(dataset[second_page])


# Task 10 Solution
# Slice objects are preferable when:
# - slicing logic is reused
# - intent should be named
# - slicing is passed as data
# - code readability matters
#
# Direct slicing is preferable for simple, one-off cases.


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# These solutions demonstrate:
# - reusable slicing logic
# - clarity through named slices
# - correct handling of slice objects
#
# Next Step:
# Move on to the next module when ready.
