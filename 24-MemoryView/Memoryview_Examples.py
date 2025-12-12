"""
Memoryview_Examples.py
Module 24 — memoryview
Author: Peyman Miyandashti
Year: 2025

This file contains practical examples that demonstrate how memoryview works:
zero-copy slicing, reading values, modifying data, and converting between
memoryview and other binary types.
"""


# ---------------------------------------------------------------------------
# Example 1: Creating a memoryview from a bytearray (mutable)
# ---------------------------------------------------------------------------

buf = bytearray(b"Hello")
mv = memoryview(buf)

print(mv[0])        # 72
print(mv[1])        # 101
print(mv.tobytes()) # b'Hello'


# ---------------------------------------------------------------------------
# Example 2: Creating a memoryview from bytes (immutable)
# ---------------------------------------------------------------------------

immutable = b"Python"
mv2 = memoryview(immutable)
print(mv2[0])        # 80


# ---------------------------------------------------------------------------
# Example 3: Zero-copy slicing (returns a memoryview, not bytes)
# ---------------------------------------------------------------------------

data = bytearray(b"ABCDEFGHIJ")
mv3 = memoryview(data)

slice_view = mv3[2:7]  # Points to "CDEFG"
print(slice_view.tobytes())


# ---------------------------------------------------------------------------
# Example 4: Modifying binary data through memoryview
# ---------------------------------------------------------------------------

buf2 = bytearray(b"WORLD")
mv4 = memoryview(buf2)

mv4[0] = ord("M")    # Change 'W' → 'M'
print(buf2)          # bytearray(b'MORLD')


# ---------------------------------------------------------------------------
# Example 5: Editing a slice directly
# ---------------------------------------------------------------------------

buf3 = bytearray(b"AAAAAA")
mv5 = memoryview(buf3)

mv5[2:5] = b"XYZ"
print(buf3)          # bytearray(b'AAXYZA')


# ---------------------------------------------------------------------------
# Example 6: Reading a segment without copying
# ---------------------------------------------------------------------------

packet = bytearray(b"\x10\x20\x30\x40\x50")
header = memoryview(packet)[:2]
payload = memoryview(packet)[2:]

print("Header:", header.tobytes())   # b'\x10\x20'
print("Payload:", payload.tobytes()) # b'\x30\x40\x50'


# ---------------------------------------------------------------------------
# Example 7: Converting memoryview → bytes
# ---------------------------------------------------------------------------

mv_bytes = memoryview(bytearray(b"Test"))
copy_bytes = mv_bytes.tobytes()
print(copy_bytes)    # b'Test'


# ---------------------------------------------------------------------------
# Example 8: Converting memoryview → list of integers
# ---------------------------------------------------------------------------

mvlist = memoryview(bytearray(b"\x01\x02\x03"))
print(mvlist.tolist())  # [1, 2, 3]


# ---------------------------------------------------------------------------
# Example 9: Multi-slice chain
# ---------------------------------------------------------------------------

full_buffer = bytearray(b"ABCDEFGHIJKL")
mv9 = memoryview(full_buffer)
middle_part = mv9[4:10]     # "EFGHIJ"
inner_slice = middle_part[2:5]  # "GHI"

print(middle_part.tobytes())
print(inner_slice.tobytes())


# ---------------------------------------------------------------------------
# Example 10: Using memoryview for efficient mutation in a loop
# ---------------------------------------------------------------------------

buffer = bytearray(b"0123456789")
mv10 = memoryview(buffer)

for i in range(len(mv10)):
    mv10[i] = (mv10[i] + 1) % 256

print(buffer)
