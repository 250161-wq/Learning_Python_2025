"""
Bytes_Tasks.py
Module 22 — Bytes
Author: Peyman Miyandashti
Year: 2025

Practice exercises for mastering Python's bytes type.
Tasks move from basic creation and encoding (Rank 1) to realistic binary
processing (Rank 5).

Instructions:
- Try every task BEFORE checking the solutions file.
- Write your answers below each task.
- Focus on correct encoding/decoding, immutability, and byte construction.
"""


# ---------------------------------------------------------------------------
# ⭐ RANK 1 — BEGINNER
# Basic creation of bytes and type checking.
# ---------------------------------------------------------------------------

# 1. Create a bytes object b"Hello".

# 2. Convert the string "Python" into bytes using UTF-8 encoding.

# 3. Create a bytes object from this list: [65, 66, 67] (ASCII A, B, C).

# 4. Access the first byte of b"Data" and print it.

# 5. Check the length of b"Hola".


# ---------------------------------------------------------------------------
# ⭐ RANK 2 — EASY
# Encoding, decoding, slicing, and simple manipulation.
# ---------------------------------------------------------------------------

# 6. Encode the word "México" into bytes using UTF-8.

# 7. Decode the previous bytes back into a string.

# 8. Slice b"Python" so that only b"hon" remains.

# 9. Create a new bytes object that changes the first byte in b"Code"
#    to 'M' (ASCII 77) by creating a NEW object (since bytes are immutable).

# 10. Create a function to_bytes(text) that returns text encoded in UTF-8.


# ---------------------------------------------------------------------------
# ⭐ RANK 3 — INTERMEDIATE
# More complex conversions and byte construction.
# ---------------------------------------------------------------------------

# 11. Create bytes from this list: [10, 20, 30, 40, 50].

# 12. Write a function safe_encode(value) that:
#       - Returns None if value is None
#       - Otherwise returns value encoded in UTF-8.

# 13. Combine two bytes objects: b"Hello" + b"World".
#     Save the result.

# 14. Given b"\x10\x20\x30", access the last byte.

# 15. Write a function ascii_values(text) that:
#       Returns a list of ASCII integer values for every character in text.


# ---------------------------------------------------------------------------
# ⭐ RANK 4 — ADVANCED
# Realistic binary processing.
# ---------------------------------------------------------------------------

# 16. Simulate a binary packet:
#       packet = b"\x01\xFF\x34\x7A"
#     Write code to:
#       - Print the first byte
#       - Print the last byte
#       - Print the length

# 17. Create a bytearray from b"Hello" and modify the last letter to '!' (ASCII 33).

# 18. Write a function prefix_bytes(prefix, data) that:
#       - Takes a prefix (bytes) and data (bytes)
#       - Returns prefix + data

# 19. Convert the string "Peyman" into bytes, then slice out b"man".

# 20. Write a function count_zero_bytes(b) that:
#       - Returns how many zero bytes (\x00) appear in a bytes object.


# ---------------------------------------------------------------------------
# ⭐ RANK 5 — PROFESSIONAL
# Production-style binary logic and safe data handling.
# ---------------------------------------------------------------------------

# 21. Write a function load_binary(text) that:
#       - Returns text encoded in UTF-8
#       - Returns None if text is empty or None

# 22. A networking protocol requires all messages to begin with byte 0xAA.
#     Write a function validate_packet(packet) that:
#       - Returns True if packet starts with 0xAA
#       - Returns False otherwise

# 23. Write a function build_message(command, payload) that:
#       - Takes command (int) and payload (bytes)
#       - Returns a packet: bytes([command]) + payload

# 24. A file header contains:
#       version = 1
#       flags = 0
#     Create bytes representing this: b"\x01\x00"

# 25. Write a function extract_text(b) that:
#       - Attempts to decode bytes using UTF-8
#       - Returns None if decoding fails (use try/except)
