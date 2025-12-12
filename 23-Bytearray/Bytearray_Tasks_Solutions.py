"""
Bytearray_Tasks_Solutions.py
Module 23 — bytearray
Author: Peyman Miyandashti
Year: 2025

Solutions for all bytearray practice tasks.
Use this file only AFTER completing all tasks honestly.
"""


# ---------------------------------------------------------------------------
# ⭐ RANK 1 — BEGINNER
# ---------------------------------------------------------------------------

# 1.
b1 = bytearray(b"Hello")

# 2.
b2 = bytearray("Python".encode("utf-8"))

# 3.
b3 = bytearray(b"Jello")
b3[0] = 72   # 'H'

# 4.
b4 = bytearray([65, 66, 67])  # b'ABC'

# 5.
length_hola = len(bytearray(b"Hola"))


# ---------------------------------------------------------------------------
# ⭐ RANK 2 — EASY
# ---------------------------------------------------------------------------

# 6.
b6 = bytearray(b"Python")
b6[0:2] = b"My"     # bytearray(b"Mython")

# 7.
b7 = bytearray(b"Hi")
b7.append(33)       # '!'

# 8.
b8 = bytearray(b"Data")
b8.extend(b" Science")

# 9.
b9 = bytearray(b"ello")
b9.insert(0, 72)     # Insert 'H'

# 10.
b10 = bytearray(b"ABCDE")
del b10[2]           # Remove 'C'


# ---------------------------------------------------------------------------
# ⭐ RANK 3 — INTERMEDIATE
# ---------------------------------------------------------------------------

# 11.
def make_bytearray(text):
    return bytearray(text.encode("utf-8"))

# 12.
b12 = bytearray(b"Computer")
slice_put = b12[3:6]  # b'put'

# 13.
b13 = bytearray(b"World")
b13[-1] = 33  # '!' → bytearray(b'World!')

# 14.
combined = bytearray(b"Hello") + bytearray(b"World")

# 15.
def shift_bytes(barr):
    for i in range(len(barr)):
        barr[i] = (barr[i] + 1) % 256
    return barr


# ---------------------------------------------------------------------------
# ⭐ RANK 4 — ADVANCED
# ---------------------------------------------------------------------------

# 16.
packet = bytearray(b"\x10\x20\x30\x40")
packet[1] = 255
packet.append(0xAA)

# 17.
def overwrite_range(barr, start, end, new_bytes):
    barr[start:end] = new_bytes
    return barr

# 18.
b18 = bytearray(b"AAAAAAA")
b18[2:5] = b"XYZ"

# 19.
def merge_packets(p1, p2):
    return bytearray(p1 + p2)

# 20.
b20 = bytearray(b"\x01\x02\x03\x04")
del b20[-1]
del b20[-1]


# ---------------------------------------------------------------------------
# ⭐ RANK 5 — PROFESSIONAL
# ---------------------------------------------------------------------------

# 21.
def build_message(cmd, payload):
    return bytearray([cmd]) + payload

# 22.
def add_checksum(barr):
    total = sum(barr) % 256
    new_packet = bytearray(barr)
    new_packet.append(total)
    return new_packet

# 23.
def safe_mutate(barr, index, value):
    if not (0 <= value <= 255):
        return None
    if not (0 <= index < len(barr)):
        return None
    barr[index] = value
    return barr

# 24.
def packet_header(version, flags):
    return bytearray([version, flags])

# 25.
def decode_safe(barr):
    try:
        return barr.decode("utf-8")
    except Exception:
        return None
