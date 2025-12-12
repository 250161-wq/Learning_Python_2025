"""
Array_Tasks_Solutions.py
Module 25 — array.array
Author: Peyman Miyandashti
Year: 2025

Solutions to all array.array practice tasks.
Use this file only AFTER attempting the tasks yourself.
"""

from array import array


# ---------------------------------------------------------------------------
# ⭐ RANK 1 — BEGINNER
# ---------------------------------------------------------------------------

# 1.
arr1 = array('i', [10, 20, 30])

# 2.
arr2 = array('f', [1.5, 2.5, 3.5])

# 3.
arr3 = array('B', b"ABC")

# 4.
first_value = array('i', [100, 200, 300])[0]

# 5.
length_arr = len(array('B', [1, 2, 3, 4]))


# ---------------------------------------------------------------------------
# ⭐ RANK 2 — EASY
# ---------------------------------------------------------------------------

# 6.
task6 = array('i', [1, 2, 3])
task6.append(4)

# 7.
task7 = array('i', [10, 20])
task7.extend([30, 40])

# 8.
task8 = array('i', [5, 6, 7, 8])[1:3]  # [6, 7]

# 9.
task9 = array('i', [1, 2, 3])
task9.insert(1, 100)

# 10.
task10 = array('i', [10, 20, 30, 40])
del task10[2]


# ---------------------------------------------------------------------------
# ⭐ RANK 3 — INTERMEDIATE
# ---------------------------------------------------------------------------

# 11.
arr11 = array('i', [5, 6, 7])
bytes11 = arr11.tobytes()

# 12.
arr12 = array('i')
arr12.frombytes(bytes11)   # loads [5, 6, 7]

# 13.
arr13 = array('i', [10, 11, 12, 13])
arr13[1:3] = array('i', [99, 88])

# 14.
def scale_array(arr, factor):
    for i in range(len(arr)):
        arr[i] *= factor
    return arr

# 15.
def copy_array(arr):
    return array(arr.typecode, arr)


# ---------------------------------------------------------------------------
# ⭐ RANK 4 — ADVANCED
# ---------------------------------------------------------------------------

# 16.
pkt = array('B', [0x10, 0x20, 0x30])
pkt.append(0xFF)
pkt[1] = 0x99  # Replace second byte

# 17.
def replace_range(arr, start, new_values):
    arr[start:start+len(new_values)] = array(arr.typecode, new_values)
    return arr

# 18.
arr18_original = array('i', [1, 2, 3])
arr18_bytes = arr18_original.tobytes()
arr18_new = array('i')
arr18_new.frombytes(arr18_bytes)

# 19.
def sum_bytes(arr):
    return sum(arr) % 256

# 20.
task20 = array('B', [1, 2, 3, 4, 5])[0::2]  # indexes 0,2,4


# ---------------------------------------------------------------------------
# ⭐ RANK 5 — PROFESSIONAL
# ---------------------------------------------------------------------------

# 21.
def build_packet(version, flag, payload):
    return array('B', [version, flag] + list(payload))

# 22.
def serialize_floats(arr):
    return arr.tobytes()

# 23.
def deserialize_floats(bdata):
    out = array('f')
    out.frombytes(bdata)
    return out

# 24.
def normalize(arr):
    for i in range(len(arr)):
        arr[i] = arr[i] % 101
    return arr

# 25.
def binary_header(version, size):
    header = array('I', [version, size])
    return header, header.tobytes()
