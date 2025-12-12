"""
Memoryview_Tasks_Solutions.py
Module 24 — memoryview
Author: Peyman Miyandashti
Year: 2025

Solutions to all memoryview tasks.
Use this only AFTER you have tried the tasks yourself.
"""


# ---------------------------------------------------------------------------
# ⭐ RANK 1 — BEGINNER
# ---------------------------------------------------------------------------

# 1.
data = bytearray(b"Hello World")
mv1 = memoryview(data)

# 2.
first_byte = mv1[0]   # 72

# 3.
slice_hello = mv1[:5]

# 4.
hello_bytes = slice_hello.tobytes()  # b'Hello'

# 5.
mv_python = memoryview(b"Python")
len_mv_python = len(mv_python)


# ---------------------------------------------------------------------------
# ⭐ RANK 2 — EASY
# ---------------------------------------------------------------------------

# 6.
data2 = bytearray(b"ABCDEFG")
mv2 = memoryview(data2)
slice_bcd = mv2[1:4]   # b'BCD'

# 7.
mv_list = mv2.tolist()

# 8.
mv_data = memoryview(bytearray(b"Data"))
back_to_bytes = mv_data.tobytes()

# 9.
mv_immutable = memoryview(b"Immutable")
third_byte = mv_immutable[2]

# 10.
mv_even = memoryview(bytearray(b"123456"))
even_bytes = mv_even[0::2]  # indexes 0,2,4


# ---------------------------------------------------------------------------
# ⭐ RANK 3 — INTERMEDIATE
# ---------------------------------------------------------------------------

# 11.
buf11 = bytearray(b"HELLO")
mv11 = memoryview(buf11)
mv11[0] = ord("Y")     # H → Y

# 12.
buf12 = bytearray(b"AAAAAA")
mv12 = memoryview(buf12)
mv12[2:5] = b"XYZ"

# 13.
def mv_slice(data, start, end):
    return memoryview(data)[start:end]

# 14.
buf14 = bytearray(b"ABCDEFGH")
mv14 = memoryview(buf14)
mv14[3:6] = b"123"   # Replace DEF

# 15.
def mv_edit(barr, index, newvalue):
    if not (0 <= newvalue <= 255):
        return None
    if not (0 <= index < len(barr)):
        return None
    mv = memoryview(barr)
    mv[index] = newvalue
    return barr


# ---------------------------------------------------------------------------
# ⭐ RANK 4 — ADVANCED
# ---------------------------------------------------------------------------

# 16.
pkt = bytearray(b"\x10\x20\x30\x40\x50")
mv_pkt = memoryview(pkt)
header = mv_pkt[:2]
payload = mv_pkt[2:]
header_bytes = header.tobytes()
payload_bytes = payload.tobytes()

# 17.
def update_payload(pkt, start, new_bytes):
    mv = memoryview(pkt)
    mv[start : start + len(new_bytes)] = new_bytes
    return pkt

# 18.
buf18 = bytearray(b"ABCDEFGHIJK")
mv18 = memoryview(buf18)
slice_defg = mv18[3:7]        # "DEFG"
slice_ef = slice_defg[1:3]     # "EF"

# 19.
def join_views(v1, v2):
    return bytes(v1) + bytes(v2)

# 20.
buf20 = bytearray(b"AAAAAAA")
mv20 = memoryview(buf20)
mv20[-3:] = b"XYZ"  # last 3 bytes


# ---------------------------------------------------------------------------
# ⭐ RANK 5 — PROFESSIONAL
# ---------------------------------------------------------------------------

# 21.
def parse_header(data):
    mv = memoryview(data)
    version = mv[0]
    flags = mv[1]
    return version, flags

# 22.
def checksum_view(barr):
    mv = memoryview(barr)
    return sum(mv) % 256

# 23.
def mv_window(barr, start, size):
    return memoryview(barr)[start : start + size]

# 24.
def edit_inplace(barr, start, new_bytes):
    mv = memoryview(barr)
    mv[start : start + len(new_bytes)] = new_bytes
    return barr

# 25.
def mv_decode_safe(view):
    try:
        return view.tobytes().decode("utf-8")
    except:
        return None
