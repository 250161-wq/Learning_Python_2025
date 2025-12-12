"""
Memoryview_Notes.py
Module 24 — memoryview
Author: Peyman Miyandashti
Year: 2025

Comprehensive notes about Python’s memoryview object — a powerful tool that
allows zero-copy access to binary data. With memoryview, I can read or modify
parts of a bytes-like object (such as bytearray) *without creating new copies*.

This makes memoryview extremely useful for:
- High-performance binary processing
- Editing large buffers efficiently
- Streaming data
- Network packet manipulation
- Working with slices of binary data
- Interfacing with libraries that operate on raw memory

This file introduces creation, slicing, editing, conversions, and best practices.
"""


# ---------------------------------------------------------------------------
# 1. What Is memoryview?
# ---------------------------------------------------------------------------
# memoryview is a built-in object that provides a "view" of binary data
# without copying it. It works with:
#   - bytes
#   - bytearray
#   - array.array
#   - many buffer-compatible objects
#
# Key idea:
#   memoryview does NOT store data.
#   It only references existing data.
#
# This gives:
#   ✔ Zero-copy slicing
#   ✔ Faster performance
#   ✔ Lower memory usage

data = bytearray(b"Hello World")
view = memoryview(data)
print(view)            # <memory at ...>
print(view[0])         # 72 ('H')


# ---------------------------------------------------------------------------
# 2. Creating memoryview Objects
# ---------------------------------------------------------------------------

# From bytearray (mutable)
b1 = bytearray(b"Python")
v1 = memoryview(b1)

# From bytes (immutable)
b2 = b"Immutable"
v2 = memoryview(b2)

print(v1, v2)


# ---------------------------------------------------------------------------
# 3. Slicing memoryview (ZERO-COPY)
# ---------------------------------------------------------------------------
# Slicing a memoryview creates another memoryview — NOT a new bytes object.

mv = memoryview(bytearray(b"ABCDEFGHIJ"))
slice_mv = mv[2:7]   # View of "CDEFG"
print(slice_mv.tobytes())  # b'CDEFG'


# ---------------------------------------------------------------------------
# 4. Modifying Data Through a memoryview
# ---------------------------------------------------------------------------
# This only works if the underlying object is mutable (bytearray, array.array).
# Any change affects the original buffer immediately.

buf = bytearray(b"HELLO")
mv2 = memoryview(buf)

mv2[0] = ord("Y")   # Replace 'H' with 'Y'
print(buf)          # bytearray(b'YELLO')


# ---------------------------------------------------------------------------
# 5. memoryview and Formats
# ---------------------------------------------------------------------------
# memoryview supports different data formats:
#   'B' = unsigned bytes (0–255)
#   'h' = short integers
#   'i' = integers
#   'f' = floats
#
# For this module, we focus on the standard 'B' byte format.

mv_numbers = memoryview(bytearray(b"\x01\x02\x03\x04"))
print(mv_numbers.tolist())   # [1, 2, 3, 4]


# ---------------------------------------------------------------------------
# 6. Converting memoryview to Bytes or Bytearray
# ---------------------------------------------------------------------------

# Convert to bytes (makes a copy)
bytes_copy = mv_numbers.tobytes()
print(bytes_copy)

# Convert to bytearray (also a copy)
bytearray_copy = mv_numbers.tolist()
print(bytearray_copy)


# ---------------------------------------------------------------------------
# 7. Realistic Examples Using memoryview
# ---------------------------------------------------------------------------

# Example 1: Parsing packet header
packet = bytearray(b"\x10\x20\x30\x40\x50")
header = memoryview(packet)[:2]  # First two bytes
print(header.tobytes())          # b'\x10\x20'


# Example 2: Editing packet payload
payload = memoryview(packet)[2:]
payload[0] = 99     # Change byte at index 2
print(packet)       # bytearray with modified byte


# Example 3: Large buffer operations (simulated)
buffer = bytearray(b"A" * 20)
mv_buffer = memoryview(buffer)
mv_buffer[5:10] = b"HELLO"
print(buffer)


# ---------------------------------------------------------------------------
# 8. When Should I Use memoryview?
# ---------------------------------------------------------------------------
# ✔ When working with large binary data (files, streams)
# ✔ When slicing binary structures without copying
# ✔ When modifying only a small segment of a buffer
# ✔ When building or parsing network packets
# ✔ When performance and memory efficiency matter
#
# Avoid memoryview when:
# ✘ You don’t understand the underlying buffer structure
# ✘ You need a fresh copy (use bytes() or .tobytes())


# ---------------------------------------------------------------------------
# 9. Best Practices
# ---------------------------------------------------------------------------
# ✔ Use memoryview to avoid unnecessary copying
# ✔ Use slices carefully — they reference the same memory
# ✔ Convert back to bytes only when needed
# ✔ Work with bytearray for mutable operations
# ✔ Always keep track of the original buffer (memoryview does not own data)
# ✔ Use .tobytes() for read-only copies
# ✔ Use .cast() only if you understand buffer formats (advanced)


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# memoryview is a powerful Python feature for advanced binary processing.
# It enables zero-copy slicing, fast editing, efficient parsing, and clean
# workflows for large data systems.

# Next Step:
# Continue with Memoryview_Examples.py to practice small, practical examples.
