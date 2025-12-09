"""
Module 15 — Numeric Variants: Complex Numbers
Practice Task Solutions

This file contains clear, correct, and professional solutions to all exercises
in Complex_Tasks.py. Multiple approaches exist, but these represent clean,
readable patterns appropriate for learning.

Only read after attempting the tasks honestly.
"""

# ---------------------------------------------------------------------------
# Rank 1 — Beginner
# ---------------------------------------------------------------------------

# Task 1.1
z = 4 + 5j
print(z)

# Task 1.2
z2 = complex(7, -3)
print(z2)

# Task 1.3
z3 = 9 - 2j
print("Real:", z3.real)
print("Imag:", z3.imag)


# ---------------------------------------------------------------------------
# Rank 2 — Easy
# ---------------------------------------------------------------------------

# Task 2.1
a = 3 + 4j
b = 1 - 2j
print(a + b)

# Task 2.2
z = 5 + 12j
print(abs(z))

# Task 2.3
print((2 + 3j) - (7 - 1j))  # (7 - j) same as (7 - 1j)


# ---------------------------------------------------------------------------
# Rank 3 — Intermediate
# ---------------------------------------------------------------------------

# Task 3.1
z = 6 - 8j
print(z.conjugate())

# Task 3.2
print((4 + 2j) * (1 - 3j))

# Task 3.3
print((10 + 5j) / (3 - 1j))


# ---------------------------------------------------------------------------
# Rank 4 — Advanced
# ---------------------------------------------------------------------------

import cmath
import math

# Task 4.1
z = 1 + 1j
print(cmath.phase(z))

# Task 4.2
z = 2 + 2j
mag, angle = cmath.polar(z)
print("Magnitude:", mag)
print("Angle:", angle)

# Task 4.3
result = cmath.rect(3, math.pi / 6)
print(result)


# ---------------------------------------------------------------------------
# Rank 5 — Professional
# ---------------------------------------------------------------------------

# Task 5.1
point = 5 + 0j
theta = math.pi / 2  # 90 degrees
rotation = complex(math.cos(theta), math.sin(theta))
rotated = point * rotation
print(rotated)

# Task 5.2
z = 0 + 0j
c = -0.1 + 0.75j
z = z * z + c
print(z)

# Task 5.3
Z1 = 4 + 3j
Z2 = 2 - 1j
Z3 = -1 + 5j
Z_total = Z1 + Z2 + Z3
print(Z_total)


# End of Solutions
