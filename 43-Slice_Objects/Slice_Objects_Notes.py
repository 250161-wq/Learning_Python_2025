"""
Slice_Objects_Notes.py
Module 43 — Slice Objects
Author: Peyman Miyandashti
Year: 2025

This module explains slice objects in Python.
Slice objects represent slicing instructions
that can be reused and passed around.
"""

# ---------------------------------------------------------------------------
# 1. What Is a Slice?
# ---------------------------------------------------------------------------
# A slice defines a portion of a sequence.
# Syntax form:
#   sequence[start:stop:step]


# ---------------------------------------------------------------------------
# 2. Creating a Slice Object
# ---------------------------------------------------------------------------

s = slice(1, 5)
data = [10, 20, 30, 40, 50, 60]
print(data[s])


# ---------------------------------------------------------------------------
# 3. Slice with Step
# ---------------------------------------------------------------------------

every_second = slice(None, None, 2)
print(data[every_second])


# ---------------------------------------------------------------------------
# 4. Slice Object vs Slice Syntax
# ---------------------------------------------------------------------------

print(data[1:5])
print(data[s])


# ---------------------------------------------------------------------------
# 5. Why Use Slice Objects?
# ---------------------------------------------------------------------------
# - reuse slicing logic
# - improve readability
# - avoid magic numbers
# - pass slices as arguments


# ---------------------------------------------------------------------------
# 6. Named Slices (Readable Code)
# ---------------------------------------------------------------------------

first_half = slice(0, 3)
second_half = slice(3, None)

print(data[first_half])
print(data[second_half])


# ---------------------------------------------------------------------------
# 7. Slice Attributes
# ---------------------------------------------------------------------------
# slice objects have:
# - start
# - stop
# - step

print(s.start, s.stop, s.step)


# ---------------------------------------------------------------------------
# 8. Slice Objects in Custom Classes
# ---------------------------------------------------------------------------
# When __getitem__ receives a slice,
# it allows custom slicing behavior.

class Sample:
    def __getitem__(self, item):
        if isinstance(item, slice):
            return f"Slice received: {item.start}:{item.stop}:{item.step}"
        return item

obj = Sample()
print(obj[1:10:2])


# ---------------------------------------------------------------------------
# 9. Common Mistakes
# ---------------------------------------------------------------------------
# - forgetting that stop is exclusive
# - confusing None with 0
# - overusing slice objects when simple syntax is clearer


# ---------------------------------------------------------------------------
# 10. Best Practices
# ---------------------------------------------------------------------------
# - use slice objects when slicing logic is reused
# - name slices meaningfully
# - keep slicing readable


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# Slice objects expose Python’s slicing model explicitly.
# They improve clarity and reusability in sequence processing.
#
# Next Step:
# Continue with Slice_Objects_Examples.py
