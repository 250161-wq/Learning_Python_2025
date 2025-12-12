"""
Bytearray_Examples.py
Module 23 — bytearray
Author: Peyman Miyandashti
Year: 2025

This file contains practical examples demonstrating how Python's bytearray 
works. Each example is short and focused on a specific behavior:
modification, slicing, appending, inserting, deleting, and building binary data.
"""


# ---------------------------------------------------------------------------
# Example 1: Creating a bytearray
# ---------------------------------------------------------------------------

b1 = bytearray(b"Hello")
print(b1)   # bytearray(b'Hello')


# ---------------------------------------------------------------------------
# Example 2: Creating bytearray from string (encoding first)
# ---------------------------------------------------------------------------

text = "Peyman"
b2 = bytearray(text.encode("utf-8"))
print(b2)


# ---------------------------------------------------------------------------
# Example 3: Modifying a single byte
# ---------------------------------------------------------------------------

b3 = bytearray(b"Jello")
b3[0] = 72  # Change 'J' (74) to 'H' (72)
print(b3)   # bytearray(b'Hello')


# ---------------------------------------------------------------------------
# Example 4: Modifying a slice
# ---------------------------------------------------------------------------

b4 = bytearray(b"Python")
b4[0:2] = b"CY"   # Replace "Py" → "CY"
print(b4)         # bytearray(b'CYthon')


# ---------------------------------------------------------------------------
# Example 5: Appending bytes
# ---------------------------------------------------------------------------

b5 = bytearray(b"Hi")
b5.append(33)     # ASCII '!'
print(b5)         # bytearray(b'Hi!')


# ---------------------------------------------------------------------------
# Example 6: Extending bytearray with bytes
# ---------------------------------------------------------------------------

b6 = bytearray(b"Data")
b6.extend(b" Science")
print(b6)


# ---------------------------------------------------------------------------
# Example 7: Inserting and deleting bytes
# ---------------------------------------------------------------------------

b7 = bytearray(b"World")
b7.insert(0, 72)  # Insert 'H' at the beginning
print(b7)         # bytearray(b'HWorld')

del b7[1]         # Remove 'W'
print(b7)         # bytearray(b'Horld')


# ---------------------------------------------------------------------------
# Example 8: Converting bytearray ↔ bytes
# ---------------------------------------------------------------------------

ba = bytearray(b"Hello")
immutable_bytes = bytes(ba)
print(immutable_bytes)   # b'Hello'

new_ba = bytearray(b"Example")
print(new_ba)


# ---------------------------------------------------------------------------
# Example 9: Slicing a bytearray
# ---------------------------------------------------------------------------

b8 = bytearray(b"Computer")
slice_part = b8[3:7]
print(slice_part)   # bytearray(b'pute')


# ---------------------------------------------------------------------------
# Example 10: Building a fake binary packet
# ---------------------------------------------------------------------------

packet = bytearray(b"\x01\x00\xFF")
packet.append(120)  # Add new byte
packet.extend(b"\xAA\xBB")
print(packet)


# ---------------------------------------------------------------------------
# Example 11: Efficient mutation in a loop
# ---------------------------------------------------------------------------

buffer = bytearray(b"ABCXYZ")
for i in range(len(buffer)):
    buffer[i] = (buffer[i] + 1) % 256  # Shift each byte
print(buffer)


# ---------------------------------------------------------------------------
# Example 12: Replacing part of a binary buffer
# ---------------------------------------------------------------------------

data = bytearray(b"AAAAAAA")
data[2:5] = b"XYZ"
print(data)  # bytearray(b'AAXYZA')
