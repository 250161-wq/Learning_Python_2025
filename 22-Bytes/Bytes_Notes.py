"""
Bytes_Notes.py
Module 22 — Bytes
Author: Peyman Miyandashti
Year: 2025

Comprehensive notes about Python’s bytes type — a sequence of raw, immutable 
byte values used for binary data processing. Bytes are essential when working 
with files, images, networking, cryptography, and low-level protocols.

In this module, I explore:
- What bytes are and why they matter
- How to create bytes objects
- Encoding and decoding between strings and bytes
- Slicing bytes and checking values
- The difference between bytes and bytearray
- Realistic examples where bytes are used in modern software

This file prepares me for the examples and tasks that follow.
"""


# ---------------------------------------------------------------------------
# 1. What Are Bytes?
# ---------------------------------------------------------------------------
# A bytes object is an immutable sequence of integers between 0 and 255.
# It is commonly used for handling binary data.
#
# Examples:
# - Images (JPEG, PNG)
# - Audio files (MP3, WAV)
# - Network communication packets
# - Encryption and hashing
# - Reading binary files

raw_bytes = b"Hello"
print(raw_bytes)  # b'Hello'


# ---------------------------------------------------------------------------
# 2. Creating Bytes
# ---------------------------------------------------------------------------

# Method 1: Using a bytes literal with b"..."
b1 = b"Python"
print(b1)

# Method 2: Converting a string to bytes using .encode()
text = "Hola Peyman"
b2 = text.encode("utf-8")
print(b2)

# Method 3: Creating bytes from a list of integers (0–255)
b3 = bytes([80, 121, 116, 104, 111, 110])  # ASCII for "Python"
print(b3)


# ---------------------------------------------------------------------------
# 3. Encoding and Decoding (VERY IMPORTANT)
# ---------------------------------------------------------------------------
# Encoding: string → bytes
# Decoding: bytes → string
#
# Common encodings:
# - UTF-8  (most used)
# - ASCII  (only simple characters)
#
# Encoding converts human text to binary representation.
# Decoding converts binary data back to readable text.

s = "México"
encoded = s.encode("utf-8")
decoded = encoded.decode("utf-8")

print("Encoded:", encoded)
print("Decoded:", decoded)


# ---------------------------------------------------------------------------
# 4. Accessing Bytes
# ---------------------------------------------------------------------------
# Each element in a bytes object is an integer (0–255), not a character.

sample = b"ABC"
print(sample[0])  # 65 (ASCII for 'A')

# Bytes can be sliced like strings:
print(sample[1:])  # b'BC'


# ---------------------------------------------------------------------------
# 5. Bytes Are Immutable
# ---------------------------------------------------------------------------
# You cannot modify a byte directly.
# This will produce an error:
#
# sample[0] = 90   ❌ Not allowed (bytes are immutable)
#
# To modify, you must create a new bytes object or use bytearray.

# Creating new bytes:
modified = b"A" + b"BC"
print(modified)


# ---------------------------------------------------------------------------
# 6. bytearray — Mutable Version of Bytes
# ---------------------------------------------------------------------------
# bytearray works like bytes but allows modification.

ba = bytearray(b"Hello")
ba[0] = 74   # Change 'H' (72) to 'J' (74)
print(ba)    # bytearray(b'Jello')


# ---------------------------------------------------------------------------
# 7. Checking Type and Length
# ---------------------------------------------------------------------------

print(type(b1))       # <class 'bytes'>
print(len(b1))        # Number of bytes
print(len(b"á"))      # 2 bytes in UTF-8 encoding!


# ---------------------------------------------------------------------------
# 8. Realistic Scenarios Using Bytes
# ---------------------------------------------------------------------------

# Example 1: Reading a binary file (image, audio, etc.)
# with open("photo.jpg", "rb") as f:
#     data = f.read()

# Example 2: Sending bytes over a network (simplified)
packet = b"\x10\x20\x30\x40"
print("Packet:", packet)

# Example 3: Hashing (cryptography)
import hashlib
h = hashlib.sha256(b"password").hexdigest()
print("SHA256:", h)


# ---------------------------------------------------------------------------
# 9. Best Practices with Bytes
# ---------------------------------------------------------------------------
# ✔ Always specify encoding when converting strings → bytes
# ✔ Use UTF-8 encoding unless there is a specific reason not to
# ✔ Remember that bytes are NOT text — they are raw data
# ✔ Use bytearray when you need to modify binary data
# ✔ Be careful with slicing because it still returns bytes, not strings
# ✔ Use .decode() when converting bytes back to text


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# Bytes are essential in modern Python applications:
# - Web development
# - Networking and APIs
# - File storage systems
# - Cryptography and cybersecurity
# - Data serialization
#
# Mastering bytes prepares me for advanced modules involving files, streams,
# protocols, and low-level processing.

# Next Step:
# Continue with Bytes_Examples.py to practice small, focused demonstrations.
