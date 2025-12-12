"""
Bytes_Tasks_Solutions.py
Module 22 — Bytes
Author: Peyman Miyandashti
Year: 2025

Solutions for all bytes practice tasks.
Use this file only AFTER attempting all exercises honestly.
"""


# ---------------------------------------------------------------------------
# ⭐ RANK 1 — BEGINNER
# ---------------------------------------------------------------------------

# 1.
b1 = b"Hello"

# 2.
b2 = "Python".encode("utf-8")

# 3.
b3 = bytes([65, 66, 67])  # b'ABC'

# 4.
first_byte = b"Data"[0]  # 68

# 5.
length_hola = len(b"Hola")  # 4


# ---------------------------------------------------------------------------
# ⭐ RANK 2 — EASY
# ---------------------------------------------------------------------------

# 6.
mexico_bytes = "México".encode("utf-8")

# 7.
mexico_decoded = mexico_bytes.decode("utf-8")

# 8.
sliced_python = b"Python"[3:]  # b'hon'

# 9.
# Change 'C' → 'M' in b"Code"
b4_original = b"Code"
b4_modified = bytes([77]) + b4_original[1:]  # b'Mode'

# 10.
def to_bytes(text):
    return text.encode("utf-8")


# ---------------------------------------------------------------------------
# ⭐ RANK 3 — INTERMEDIATE
# ---------------------------------------------------------------------------

# 11.
b_list = bytes([10, 20, 30, 40, 50])

# 12.
def safe_encode(value):
    if value is None:
        return None
    return value.encode("utf-8")

# 13.
combined_bytes = b"Hello" + b"World"

# 14.
last_byte = b"\x10\x20\x30"[-1]  # 48

# 15.
def ascii_values(text):
    return [ord(char) for char in text]


# ---------------------------------------------------------------------------
# ⭐ RANK 4 — ADVANCED
# ---------------------------------------------------------------------------

# 16.
packet = b"\x01\xFF\x34\x7A"
packet_first = packet[0]
packet_last = packet[-1]
packet_length = len(packet)

# 17.
ba = bytearray(b"Hello")
ba[-1] = 33  # '!'

# 18.
def prefix_bytes(prefix, data):
    return prefix + data

# 19.
pey_bytes = "Peyman".encode("utf-8")
slice_man = pey_bytes[3:]  # b'man'

# 20.
def count_zero_bytes(b):
    return b.count(0)


# ---------------------------------------------------------------------------
# ⭐ RANK 5 — PROFESSIONAL
# ---------------------------------------------------------------------------

# 21.
def load_binary(text):
    if text is None or text == "":
        return None
    return text.encode("utf-8")

# 22.
def validate_packet(packet):
    if len(packet) == 0:
        return False
    return packet[0] == 0xAA

# 23.
def build_message(command, payload):
    return bytes([command]) + payload

# 24.
file_header = b"\x01\x00"

# 25.
def extract_text(b):
    try:
        return b.decode("utf-8")
    except Exception:
        return None
