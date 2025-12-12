"""
Array_Examples.py
Module 25 — array.array
Author: Peyman Miyandashti
Year: 2025

This file contains practical examples demonstrating how array.array works:
creation, modification, slicing, conversions, and realistic binary usage.
"""

from array import array


# ---------------------------------------------------------------------------
# Example 1: Creating arrays with type codes
# ---------------------------------------------------------------------------

ints = array('i', [10, 20, 30])
print(ints)   # array('i', [10, 20, 30])

floats = array('f', [1.5, 2.5, 3.5])
print(floats) # array('f', [1.5, 2.5, 3.5])


# ---------------------------------------------------------------------------
# Example 2: Array from bytes (unsigned byte type 'B')
# ---------------------------------------------------------------------------

byte_values = array('B', b"ABC")
print(byte_values)  # array('B', [65, 66, 67])


# ---------------------------------------------------------------------------
# Example 3: Accessing and modifying elements
# ---------------------------------------------------------------------------

nums = array('i', [1, 2, 3, 4])
nums[0] = 99
print(nums)  # array('i', [99, 2, 3, 4])


# ---------------------------------------------------------------------------
# Example 4: Slicing arrays
# ---------------------------------------------------------------------------

sub = nums[1:3]
print(sub)  # array('i', [2, 3])


# ---------------------------------------------------------------------------
# Example 5: Appending and extending
# ---------------------------------------------------------------------------

arr = array('i', [10, 20])
arr.append(30)
arr.extend([40, 50])
print(arr)  # array('i', [10, 20, 30, 40, 50])


# ---------------------------------------------------------------------------
# Example 6: Inserting and deleting
# ---------------------------------------------------------------------------

arr2 = array('i', [1, 2, 3])
arr2.insert(1, 100)  # Insert at index 1
print(arr2)

del arr2[2]  # Remove element at index 2
print(arr2)


# ---------------------------------------------------------------------------
# Example 7: Converting array → bytes
# ---------------------------------------------------------------------------

arr3 = array('i', [5, 6, 7])
bytes_data = arr3.tobytes()
print(bytes_data)


# ---------------------------------------------------------------------------
# Example 8: Converting bytes → array
# ---------------------------------------------------------------------------

arr4 = array('i')
arr4.frombytes(bytes_data)
print(arr4)  # array('i', [5, 6, 7])


# ---------------------------------------------------------------------------
# Example 9: Arrays store numeric types efficiently
# ---------------------------------------------------------------------------

large = array('f', [1.0] * 5)
print(large)


# ---------------------------------------------------------------------------
# Example 10: Example of a binary-like buffer using array('B')
# ---------------------------------------------------------------------------

packet = array('B', [0x10, 0x20, 0x30])
packet.append(0xFF)
print(packet)  # array('B', [16, 32, 48, 255])


# ---------------------------------------------------------------------------
# Example 11: Performing fast numeric operations
# ---------------------------------------------------------------------------

values = array('i', [1, 2, 3, 4])
for i in range(len(values)):
    values[i] *= 3
print(values)  # array('i', [3, 6, 9, 12])


# ---------------------------------------------------------------------------
# Example 12: Using array for structured binary data
# ---------------------------------------------------------------------------

header = array('B', [1, 0, 255, 128])
print(header.tobytes())  # b'\x01\x00\xff\x80'
