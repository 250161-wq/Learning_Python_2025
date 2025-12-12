"""
Bytes_Examples.py
Module 22 — Bytes
Author: Peyman Miyandashti
Year: 2025

This file contains small, practical examples showing how Python bytes work.
Each example is short, focused, and designed to build intuition about how
binary data behaves in Python.
"""


# ---------------------------------------------------------------------------
# Example 1: Basic Bytes Literal
# ---------------------------------------------------------------------------

b1 = b"Hello"
print(b1)  # b'Hello'


# ---------------------------------------------------------------------------
# Example 2: Converting a String to Bytes (Encoding)
# ---------------------------------------------------------------------------

text = "Hola Peyman"
encoded = text.encode("utf-8")
print(encoded)  # b'Hola Peyman'


# ---------------------------------------------------------------------------
# Example 3: Converting Bytes Back to String (Decoding)
# ---------------------------------------------------------------------------

decoded = encoded.decode("utf-8")
print(decoded)  # "Hola Peyman"


# ---------------------------------------------------------------------------
# Example 4: Creating Bytes from a List of Values (0–255)
# ---------------------------------------------------------------------------

byte_values = bytes([80, 121, 116, 104, 111, 110])  # "Python"
print(byte_values)


# ---------------------------------------------------------------------------
# Example 5: Accessing Individual Bytes
# ---------------------------------------------------------------------------

b2 = b"ABC"
print(b2[0])     # 65
print(b2[1])     # 66
print(b2[2])     # 67


# ---------------------------------------------------------------------------
# Example 6: Slicing Bytes
# ---------------------------------------------------------------------------

print(b2[:2])    # b'AB'
print(b2[1:])    # b'BC'


# ---------------------------------------------------------------------------
# Example 7: Bytes Are Immutable
# ---------------------------------------------------------------------------

b3 = b"Data"
# b3[0] = 90      # ❌ Not allowed, bytes are immutable

# Create a new bytes object instead:
b3_new = b"Z" + b3[1:]
print(b3_new)    # b'Zata'


# ---------------------------------------------------------------------------
# Example 8: Using bytearray for Mutable Binary Data
# ---------------------------------------------------------------------------

ba = bytearray(b"Hello")
ba[0] = 74  # 74 = ASCII 'J'
print(ba)   # bytearray(b'Jello')


# ---------------------------------------------------------------------------
# Example 9: Hashing Data (Cryptography)
# ---------------------------------------------------------------------------

import hashlib
result = hashlib.md5(b"password").hexdigest()
print("MD5:", result)


# ---------------------------------------------------------------------------
# Example 10: Fake Binary Packet Example (Network Simulation)
# ---------------------------------------------------------------------------

packet = b"\x01\x10\xFF\x7A"
print("Packet:", packet)
print("First byte:", packet[0])
print("Fourth byte:", packet[3])
