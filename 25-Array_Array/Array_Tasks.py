"""
Array_Tasks.py
Module 25 — array.array
Author: Peyman Miyandashti
Year: 2025

Practice exercises for mastering Python's array.array.
Tasks progress from simple creation (Rank 1) to professional binary workflows
using typed numeric arrays (Rank 5).

Instructions:
- Complete all tasks BEFORE checking the solutions file.
- Write your answers under each task.
- Focus on using correct type codes and modifying arrays efficiently.
"""

from array import array


# ---------------------------------------------------------------------------
# ⭐ RANK 1 — BEGINNER
# Basic creation, indexing, and printing.
# ---------------------------------------------------------------------------

# 1. Create an integer array ('i') with values [10, 20, 30].

# 2. Create a float array ('f') containing [1.5, 2.5, 3.5].

# 3. Create an unsigned byte array ('B') from b"ABC".

# 4. Access the first element of array('i', [100, 200, 300]) and print it.

# 5. Get the length of array('B', [1, 2, 3, 4]).


# ---------------------------------------------------------------------------
# ⭐ RANK 2 — EASY
# Appending, extending, slicing, inserting, deleting.
# ---------------------------------------------------------------------------

# 6. Create array('i', [1, 2, 3]) and append the number 4.

# 7. Extend array('i', [10, 20]) with [30, 40].

# 8. Slice array('i', [5, 6, 7, 8]) to obtain the middle two numbers.

# 9. Insert value 100 at position 1 in array('i', [1, 2, 3]).

# 10. Delete the third element of array('i', [10, 20, 30, 40]).


# ---------------------------------------------------------------------------
# ⭐ RANK 3 — INTERMEDIATE
# Conversions, replacing slices, numeric transformations.
# ---------------------------------------------------------------------------

# 11. Convert array('i', [5, 6, 7]) to bytes using .tobytes().

# 12. Convert bytes back into an array('i') using frombytes().

# 13. Replace slice [1:3] in array('i', [10, 11, 12, 13]) with [99, 88].

# 14. Write a function scale_array(arr, factor) that multiplies each value in arr by factor.

# 15. Write a function copy_array(arr) that returns a new array with the same type code and values.


# ---------------------------------------------------------------------------
# ⭐ RANK 4 — ADVANCED
# Binary-like manipulation using arrays.
# ---------------------------------------------------------------------------

# 16. Treat array('B', [0x10, 0x20, 0x30]) as a packet and:
#       - Append 0xFF
#       - Replace the second byte with 0x99
#       - Print the final packet

# 17. Write a function replace_range(arr, start, new_values) that:
#       - Replaces arr[start:start+len(new_values)] with new_values

# 18. Convert array('i', [1, 2, 3]) to bytes and then back to array('i').

# 19. Write a function sum_bytes(arr) using type code 'B' that returns the sum of values % 256.

# 20. Slice array('B', [1, 2, 3, 4, 5]) to extract every second byte (indexes 0, 2, 4).


# ---------------------------------------------------------------------------
# ⭐ RANK 5 — PROFESSIONAL
# High-level numeric and binary file-like workflows.
# ---------------------------------------------------------------------------

# 21. Write a function build_packet(version, flag, payload):
#       - version and flag are integers (0–255)
#       - payload is array('B')
#       - Return array('B') representing: [version, flag] + payload

# 22. Write a function serialize_floats(arr):
#       - arr is array('f')
#       - Return arr converted to bytes

# 23. Write a function deserialize_floats(bdata):
#       - bdata is bytes created from array('f')
#       - Return a new array('f') loaded from bdata

# 24. Write a function normalize(arr):
#       - arr is array('i')
#       - Modify all values to be in range 0–100 (use modulo 101)

# 25. Write a function binary_header(version, size):
#       - version and size are integers
#       - Store them in array('I') (unsigned int)
#       - Return the array and its .tobytes() representation
