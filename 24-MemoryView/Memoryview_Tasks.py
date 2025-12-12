"""
Memoryview_Tasks.py
Module 24 — memoryview
Author: Peyman Miyandashti
Year: 2025

Practice exercises for mastering Python's memoryview.
Tasks progress from simple creation (Rank 1) to professional zero-copy
buffer manipulation (Rank 5).

Instructions:
- Complete every task BEFORE checking the solutions file.
- Write your answers beneath each task.
- Focus on how memoryview interacts with bytes, bytearray, and slicing.
"""


# ---------------------------------------------------------------------------
# ⭐ RANK 1 — BEGINNER
# Basic creation and simple slicing.
# ---------------------------------------------------------------------------

# 1. Create a bytearray b"Hello World" and a memoryview pointing to it.

# 2. Print the value of the first byte through the memoryview.

# 3. Slice the memoryview so it represents only b"Hello".

# 4. Convert the slice to bytes using .tobytes().

# 5. Create a memoryview of b"Python" and print its length.


# ---------------------------------------------------------------------------
# ⭐ RANK 2 — EASY
# Slicing, viewing segments, converting, reading values.
# ---------------------------------------------------------------------------

# 6. Given data = bytearray(b"ABCDEFG"):
#       Create a memoryview and slice out b"BCD".

# 7. Convert a memoryview to a list of integers using .tolist().

# 8. Convert a memoryview of bytearray(b"Data") back to bytes.

# 9. Create a memoryview from b"Immutable" and print the third byte.

# 10. Create a memoryview from bytearray(b"123456") and slice out even-index bytes.


# ---------------------------------------------------------------------------
# ⭐ RANK 3 — INTERMEDIATE
# Modifying data through memoryviews.
# ---------------------------------------------------------------------------

# 11. Modify bytearray(b"HELLO") through a memoryview:
#       Change 'H' to 'Y' using the memoryview.

# 12. Replace slice [2:5] in bytearray(b"AAAAAA") with b"XYZ" using memoryview.

# 13. Create a function mv_slice(data, start, end) that returns a memoryview slice.

# 14. Create bytearray(b"ABCDEFGH"):
#       Use a memoryview to replace b"DEF" with b"123".

# 15. Create a function mv_edit(barr, index, newvalue) that:
#       - Edits the bytearray through memoryview
#       - Ensures 0 <= newvalue <= 255


# ---------------------------------------------------------------------------
# ⭐ RANK 4 — ADVANCED
# Packet parsing, multi-slices, buffer editing.
# ---------------------------------------------------------------------------

# 16. A packet is bytearray(b"\x10\x20\x30\x40\x50"):
#       - Create a memoryview
#       - Slice header = first two bytes
#       - Slice payload = remaining bytes
#       - Print both as bytes

# 17. Create a function update_payload(pkt, start, new_bytes):
#       - pkt is a bytearray
#       - Use memoryview to replace pkt[start : start + len(new_bytes)]
#       - Return modified pkt

# 18. Using bytearray(b"ABCDEFGHIJK"):
#       - Create a memoryview
#       - Slice out "DEFG"
#       - Then slice the inner slice to get "EF"

# 19. Write a function join_views(v1, v2):
#       - v1 and v2 are memoryviews
#       - Return bytes(v1) + bytes(v2)

# 20. Modify the last 3 bytes of bytearray(b"AAAAAAA") to b"XYZ" using memoryview.


# ---------------------------------------------------------------------------
# ⭐ RANK 5 — PROFESSIONAL
# Zero-copy binary workflows and realistic processing tasks.
# ---------------------------------------------------------------------------

# 21. Write a function parse_header(data):
#       - data is bytearray
#       - Return:
#           version  = first byte
#           flags    = second byte
#       - Use memoryview (zero-copy)

# 22. Write a function checksum_view(barr):
#       - Using memoryview:
#           Sum all bytes in barr
#           Return sum % 256

# 23. Write a function mv_window(barr, start, size):
#       - Returns a memoryview window barr[start : start + size]
#       - No copying allowed.

# 24. Write a function edit_inplace(barr, start, new_bytes):
#       - Edit barr directly through memoryview
#       - Return the modified bytearray

# 25. Write a function mv_decode_safe(view):
#       - Attempts to decode the underlying memoryview slice using UTF-8
#       - Returns decoded text
#       - Returns None if decoding fails (use try/except)
