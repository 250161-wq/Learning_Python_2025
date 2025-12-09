"""
Module 16 — Complex Numbers (Numeric Variants)
Comprehensive practice with Python's complex numeric type — used in:
- engineering
- signal processing
- physics
- electrical circuits
- advanced mathematics

In this module I:
- Create complex numbers
- Extract real & imaginary parts
- Perform complex arithmetic
- Use magnitude & phase
- Apply cmath for scientific-level calculations
- Build real-world complex-number functions

Ranking:
- Rank 1 -> Beginner: creating complex numbers + basic operations
- Rank 2 -> Easy: accessing real/imag parts, converting to polar
- Rank 3 -> Intermediate: cmath functions, magnitude/phase
- Rank 4 -> Advanced: lists, loops, and transformations
- Rank 5 -> Professional: real engineering-style complex functions

Author: Peyman Miyandashti
Student at UPBC — IT Engineering & Digital Innovation
Year: 2025
"""

# ===========================================================
# Rank 1 — Beginner
# Creating complex numbers + printing
# ===========================================================

print("Rank 1 — Beginner")

z1 = complex(3, 4)      # 3 + 4j
z2 = 5 + 2j             # alternative syntax

print("z1:", z1)
print("z2:", z2)
print("Addition:", z1 + z2)
print("Multiplication:", z1 * z2)
print("Conjugate of z1:", z1.conjugate())

print("-" * 50)


# ===========================================================
# Rank 2 — Easy
# Real part, imaginary part, and polar form
# ===========================================================

print("Rank 2 — Easy")

z = 7 - 9j

print("z:", z)
print("Real part:", z.real)
print("Imag part:", z.imag)

# Convert to polar
import cmath

r, theta = cmath.polar(z)
print("Magnitude (r):", r)
print("Angle (θ):", theta)

# Convert back to rectangular
z_rect = cmath.rect(r, theta)
print("Back to rectangular:", z_rect)

print("-" * 50)


# ===========================================================
# Rank 3 — Intermediate
# Magnitude, phase, and scientific utilities from cmath
# ===========================================================

print("Rank 3 — Intermediate")

zA = 2 + 3j
zB = -4 + 1j

print("zA:", zA)
print("zB:", zB)
print("abs(zA) → magnitude:", abs(zA))
print("phase(zA):", cmath.phase(zA))

# Complex exponentials
print("e^(iπ):", cmath.exp(1j * cmath.pi))

# Complex logarithm
print("log(zA):", cmath.log(zA))

print("-" * 50)


# ===========================================================
# Rank 4 — Advanced
# Applying complex transformations to a list
# ===========================================================

print("Rank 4 — Advanced")

signals = [
    1 + 2j,
    3 - 4j,
    -2 + 1j,
    5 + 0j
]

magnitudes = [abs(s) for s in signals]
phases = [cmath.phase(s) for s in signals]
conjugates = [s.conjugate() for s in signals]

print("Signals:", signals)
print("Magnitudes:", magnitudes)
print("Phases:", phases)
print("Conjugates:", conjugates)

# Rotate each signal by 45 degrees
rotation_angle = cmath.pi / 4
rotated = [s * cmath.exp(1j * rotation_angle) for s in signals]

print("Signals rotated by 45°:", rotated)

print("-" * 50)


# ===========================================================
# Rank 5 — Professional
# Engineering-style complex number functions
# ===========================================================

def impedance_resistor(R: float) -> complex:
    """Impedance of a resistor (purely real)."""
    return complex(R, 0)

def impedance_capacitor(C: float, w: float) -> complex:
    """Impedance of capacitor: Z = -j / (wC)."""
    return complex(0, -1/(w*C))

def impedance_inductor(L: float, w: float) -> complex:
    """Impedance of inductor: Z = j w L."""
    return complex(0, w*L)

def total_impedance(series_components: list[complex]) -> complex:
    """Sum of complex impedances in a series circuit."""
    total = 0 + 0j
    for Z in series_components:
        total += Z
    return total


print("Rank 5 — Professional")

# Example: simple RLC series circuit
R = 10           # ohms
C = 0.001        # farads
L = 0.2          # henry
frequency = 60   # Hz
w = 2 * cmath.pi * frequency

Z_R = impedance_resistor(R)
Z_C = impedance_capacitor(C, w)
Z_L = impedance_inductor(L, w)

Z_total = total_impedance([Z_R, Z_C, Z_L])

print("Z_R:", Z_R)
print("Z_C:", Z_C)
print("Z_L:", Z_L)
print("Total Impedance:", Z_total)
print("Magnitude:", abs(Z_total))
print("Phase angle:", cmath.phase(Z_total))

print("-" * 50)
