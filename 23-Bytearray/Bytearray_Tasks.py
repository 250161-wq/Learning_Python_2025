"""
Bytearray_Tasks.py
Module 23 — bytearray
Author: Peyman Miyandashti
Year: 2025

Practice exercises for mastering Python's bytearray type.
Tasks progress from simple creation and modification (Rank 1)
to realistic binary manipulation (Rank 5).

Instructions:
- Complete all tasks BEFORE checking the solutions file.
- Write your answers below each task.
- Focus on mutability, slicing, and safe binary editing.
"""


# ---------------------------------------------------------------------------
# ⭐ RANK 1 — BEGINNER
# Simple bytearray creation and basic mutations.
# ---------------------------------------------------------------------------

# 1. Create a bytearray from b"Hello".

# 2. Convert the string "Python" into a bytearray using UTF-8 encoding.

# 3. Change the first letter of bytearray(b"Jello") to 'H'.

# 4. Create a bytearray from the list [65, 66, 67] (ASCII A, B, C).

# 5. Get the length of bytearray(b"Hola").


# ---------------------------------------------------------------------------
# ⭐ RANK 2 — EASY
# Slicing, appending, extending, and simple modifications.
# ---------------------------------------------------------------------------

# 6. Replace "Py" with "My" in bytearray(b"Python").

# 7. Append '!' to bytearray(b"Hi").

# 8. Extend bytearray(b"Data") with b" Science".

# 9. Insert the byte for 'H' at the beginning of bytearray(b"ello").

# 10. Delete the third byte in bytearray(b"ABCDE").


# ---------------------------------------------------------------------------
# ⭐ RANK 3 — INTERMEDIATE
# More complex manipulations and conversions.
# ---------------------------------------------------------------------------

# 11. Create a function make_bytearray(text) that returns text encoded as a bytearray.

# 12. Create a bytearray b"Computer" and slice out b"put".

# 13. Build a new bytearray by modifying only the last letter of b"World" to '!'.

# 14. Combine two bytearrays: bytearray(b"Hello") + bytearray(b"World").

# 15. Write a function shift_bytes(barr) that:
#       - Adds 1 to every byte value (mod 256)
#       - Returns the modified bytearray


# ---------------------------------------------------------------------------
# ⭐ RANK 4 — ADVANCED
# Editing simulated binary packets, building buffers, modifying segments.
# ---------------------------------------------------------------------------

# 16. A packet is b"\x10\x20\x30\x40". Convert it to bytearray and:
#       - Replace the second byte with 255
#       - Append byte 0xAA
#       - Print the final packet

# 17. Write a function overwrite_range(barr, start, end, new_bytes) that:
#       - Replaces barr[start:end] with new_bytes
#       - Returns the modified bytearray

# 18. Make a bytearray from b"AAAAAAA" and replace positions 2–5 with b"XYZ".

# 19. Write a function merge_packets(p1, p2) that:
#       - Takes two bytearrays
#       - Returns a new merged bytearray (p1 + p2)

# 20. Given bytearray(b"\x01\x02\x03\x04"), remove the last two bytes.


# ---------------------------------------------------------------------------
# ⭐ RANK 5 — PROFESSIONAL
# Production-style binary editing, message building, safe workflows.
# ---------------------------------------------------------------------------

# 21. Write a function build_message(cmd, payload):
#       - cmd is an integer (0–255)
#       - payload is a bytearray
#       - Return: bytearray([cmd]) + payload

# 22. A protocol requires:
#       - First byte = command
#       - Last byte  = checksum (sum of all previous bytes % 256)
#     Write a function add_checksum(barr) that:
#       Returns a NEW bytearray with checksum appended.

# 23. Write a function safe_mutate(barr, index, value) that:
#       - Changes barr[index] to value ONLY if:
#           0 <= value <= 255
#           index is valid
#       - Otherwise returns None

# 24. Write a function packet_header(version, flags):
#       - version and flags are integers (0–255)
#       - Return: bytearray([version, flags])

# 25. Write a function decode_safe(barr):
#       - Attempts to decode barr using UTF-8
#       - Returns the decoded string
#       - Returns None if decoding fails (use try/except)
