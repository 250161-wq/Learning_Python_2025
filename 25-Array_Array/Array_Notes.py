"""
Array_Notes.py
Module 25 — array.array
Author: Peyman Miyandashti
Year: 2025

Comprehensive notes about Python's array.array type — a typed, memory-efficient
numeric sequence. Unlike Python lists, array.array stores elements in a compact
C-style format, making it ideal for performance-sensitive and low-level tasks.

This module covers:
- What arrays are and why they are useful
- Type codes for storing different numeric data
- Creating and modifying arrays
- Slicing, inserting, appending, deleting
- Converting arrays to bytes and from bytes
- Practical usage in binary processing and numeric pipelines
"""


# ---------------------------------------------------------------------------
# 1. What Is array.array?
# ---------------------------------------------------------------------------
# An array is a sequence of numbers stored efficiently in memory.
# All elements must be the SAME type, determined by a "type code".
#
# Examples of type codes:
#   'b' → signed byte      (-128 to 127)
#   'B' → unsigned byte    (0 to 255)
#   'h' → short
#   'H' → unsigned short
#   'i' → integer
#   'I' → unsigned integer
#   'f' → float
#   'd' → double float
#
# Arrays are useful when:
#   ✔ You need numeric homogeneity
#   ✔ You want compact storage (less RAM)
#   ✔ You work with binary data formats
#   ✔ You need faster numeric operations than lists can provide

from array import array

arr1 = array('i', [10, 20, 30])
print(arr1)  # array('i', [10, 20, 30])


# ---------------------------------------------------------------------------
# 2. Creating Arrays
# ---------------------------------------------------------------------------

# Create from Python list
ints = array('i', [1, 2, 3, 4])
print(ints)

# Create empty array
floats = array('f')
floats.append(3.14)
print(floats)

# Using bytes-like data (for unsigned bytes)
ubytes = array('B', b"Hello")
print(ubytes)  # array('B', [72, 101, 108, 108, 111])


# ---------------------------------------------------------------------------
# 3. Accessing and Modifying Elements
# ---------------------------------------------------------------------------

nums = array('i', [10, 20, 30, 40])
nums[0] = 99
print(nums)

# Slicing
slice_part = nums[1:3]
print(slice_part)  # array('i', [20, 30])


# ---------------------------------------------------------------------------
# 4. Appending, Extending, Inserting, and Removing
# ---------------------------------------------------------------------------

arr = array('i', [1, 2, 3])

arr.append(4)
print(arr)

arr.extend([5, 6])
print(arr)

arr.insert(1, 100)
print(arr)

arr.remove(3)
print(arr)

del arr[2]  # Delete by index
print(arr)


# ---------------------------------------------------------------------------
# 5. Array and Bytes Conversion
# ---------------------------------------------------------------------------
# Arrays can convert to and from raw bytes — great for binary file formats.

# Convert array → bytes
arr_bytes = arr.tobytes()
print(arr_bytes)

# Convert bytes → array
new_arr = array('i')
new_arr.frombytes(arr_bytes)
print(new_arr)


# ---------------------------------------------------------------------------
# 6. Arrays Are Efficient for Large Numeric Data
# ---------------------------------------------------------------------------

large = array('f', [1.0] * 10_000)
print(len(large))  # 10,000 floats stored efficiently


# ---------------------------------------------------------------------------
# 7. Practical Scenarios for array.array
# ---------------------------------------------------------------------------

# Scenario 1: Low-level binary file interaction
# with open("numbers.bin", "wb") as f:
#     f.write(arr.tobytes())

# Scenario 2: Interfacing with systems expecting C numeric buffers
buf = array('B', b"\x10\x20\x30")
print(buf)

# Scenario 3: Fast numeric loops
data = array('i', [1, 2, 3, 4, 5])
for i in range(len(data)):
    data[i] *= 2
print(data)


# ---------------------------------------------------------------------------
# 8. Best Practices
# ---------------------------------------------------------------------------
# ✔ Choose the correct type code for your numeric needs
# ✔ Use arrays when all elements are numeric and uniform
# ✔ Convert to bytes when interacting with binary files
# ✔ Convert from bytes safely using frombytes()
# ✔ Avoid mixing incompatible numeric types
# ✔ Use array for performance-critical workflows
# ✔ Use lists when flexibility matters more than speed or memory


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# array.array is a powerful built-in module for efficient numeric storage and
# manipulation. It acts as a bridge between high-level Python and low-level
# binary systems, making it perfect for performance and memory-sensitive tasks.

# Next Step:
# Continue with Array_Examples.py to practice core behavior.
