"""
Bytearray_Notes.py
Module 23 — bytearray
Author: Peyman Miyandashti
Year: 2025

Comprehensive notes about Python's bytearray type — a mutable sequence of 
byte values (0–255). Unlike `bytes`, which is immutable, `bytearray` allows 
modifying binary data directly. This makes it extremely useful for:

- Editing binary files
- Building or modifying network packets
- Protocol parsing and construction
- Efficient memory manipulation
- Encrypting/decrypting buffers
- Any scenario where raw data must be changed in-place

This file introduces creation, modification, slicing, appending, extending,
and converting between `bytes` and `bytearray`.
"""


# ---------------------------------------------------------------------------
# 1. What Is bytearray?
# ---------------------------------------------------------------------------
# bytearray is similar to bytes, but it is mutable — meaning its contents
# can be changed after creation.
#
# Internally, it stores integers from 0 to 255.
#
# Key idea:
#   bytes      → immutable
#   bytearray  → mutable (editable)

barr = bytearray(b"Hello")
print(barr)  # bytearray(b'Hello')


# ---------------------------------------------------------------------------
# 2. Creating bytearray Objects
# ---------------------------------------------------------------------------

# Method 1: From a bytes literal
b1 = bytearray(b"Python")
print(b1)

# Method 2: From a string (must encode first)
text = "Hola"
b2 = bytearray(text.encode("utf-8"))
print(b2)

# Method 3: From a list of integers (0–255)
b3 = bytearray([65, 66, 67])  # "ABC"
print(b3)


# ---------------------------------------------------------------------------
# 3. Modifying bytearray Values
# ---------------------------------------------------------------------------
# Since bytearray is mutable, individual bytes can be changed directly.

b4 = bytearray(b"Jello")
b4[0] = 72  # Change 'J' (74) → 'H' (72)
print(b4)   # bytearray(b'Hello')

# Modifying a slice
b4[1:3] = b"AI"   # Replace positions 1 and 2
print(b4)         # bytearray(b'HAIo')


# ---------------------------------------------------------------------------
# 4. Appending and Extending
# ---------------------------------------------------------------------------

# Append a single byte (as integer)
b5 = bytearray(b"Hi")
b5.append(33)     # ASCII for '!'
print(b5)         # bytearray(b'Hi!')

# Extend with another bytes/bytearray object
b5.extend(b" Peyman")
print(b5)


# ---------------------------------------------------------------------------
# 5. Inserting and Deleting Bytes
# ---------------------------------------------------------------------------

b6 = bytearray(b"World")
b6.insert(0, 72)   # Insert 'H' (72) at the beginning
print(b6)          # bytearray(b'HWorld')

del b6[1]          # Remove 'W'
print(b6)          # bytearray(b'Horld')


# ---------------------------------------------------------------------------
# 6. Converting Between bytes and bytearray
# ---------------------------------------------------------------------------

# bytearray → bytes
immutable_version = bytes(b4)
print(immutable_version)

# bytes → bytearray
mutable_version = bytearray(b"Data")
print(mutable_version)


# ---------------------------------------------------------------------------
# 7. Slicing Behaves Like bytes
# ---------------------------------------------------------------------------

s = b4[0:2]
print(s)      # bytearray(b'HA')


# ---------------------------------------------------------------------------
# 8. Practical Scenarios Where bytearray Shines
# ---------------------------------------------------------------------------

# Scenario 1: Building a network packet
packet = bytearray(b"\x01\x00\xFF")
packet.append(120)      # Add new byte
print(packet)

# Scenario 2: Editing binary data
buffer = bytearray(b"AAAAAAA")
buffer[2:5] = b"XYZ"
print(buffer)           # bytearray(b"AAXYZA")

# Scenario 3: Performance-sensitive loops
data = bytearray(b"Hello World")
for i in range(len(data)):
    data[i] = (data[i] + 1) % 256
print(data)


# ---------------------------------------------------------------------------
# 9. Best Practices
# ---------------------------------------------------------------------------
# ✔ Use bytes for read-only binary data
# ✔ Use bytearray when modification is required
# ✔ Always ensure values are in 0–255 range
# ✔ Encode/decode strings explicitly (UTF-8 recommended)
# ✔ Convert back to bytes when immutability or hashing is needed
# ✔ Use slicing and extend for efficient buffer editing


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# bytearray is a powerful tool for binary data manipulation in modern Python.
# It enables editing binary files, constructing packets, and performing efficient
# memory operations without creating new objects each time (unlike bytes).

# Next Step:
# Continue with Bytearray_Examples.py to see practical, runnable examples.
