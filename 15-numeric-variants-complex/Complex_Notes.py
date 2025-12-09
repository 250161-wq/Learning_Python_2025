"""
Module 15 — Numeric Variants: Complex Numbers
Professional Notes

Python has built-in support for complex numbers, expressed in the form:
        a + bj
where:
    a → real part
    b → imaginary part
    j → the imaginary unit (√−1)

Complex numbers are used widely in mathematics, physics, engineering,
signal processing, fractals, and simulations.
"""


# ---------------------------------------------------------------------------
# 1. Creating Complex Numbers
# ---------------------------------------------------------------------------
# There are two main ways to create complex numbers:

# Method 1: Literal syntax
c1 = 3 + 4j

# Method 2: Using the complex() constructor
c2 = complex(5, -2)  # 5 − 2j

print("c1 =", c1)
print("c2 =", c2)


# ---------------------------------------------------------------------------
# 2. Accessing Real and Imaginary Parts
# ---------------------------------------------------------------------------
# Complex numbers have read-only attributes:
#   number.real
#   number.imag

z = 7 - 3j
print("Real part:", z.real)
print("Imag part:", z.imag)


# ---------------------------------------------------------------------------
# 3. Basic Arithmetic with Complex Numbers
# ---------------------------------------------------------------------------
# Python supports full arithmetic between complex numbers:

a = 2 + 3j
b = 1 - 4j

print("Addition:      ", a + b)
print("Subtraction:   ", a - b)
print("Multiplication:", a * b)
print("Division:      ", a / b)


# ---------------------------------------------------------------------------
# 4. Complex Conjugates
# ---------------------------------------------------------------------------
# A conjugate flips the sign of the imaginary part:
#   (x + yj) → (x − yj)

z = 6 + 8j
print("Conjugate:", z.conjugate())


# ---------------------------------------------------------------------------
# 5. Magnitude (Absolute Value)
# ---------------------------------------------------------------------------
# abs(z) returns the magnitude, or distance from the origin:
# 
#           |a + bj| = sqrt(a² + b²)

z = 3 + 4j
print("Magnitude (abs):", abs(z))  # -> 5


# ---------------------------------------------------------------------------
# 6. Using the cmath Module
# ---------------------------------------------------------------------------
# cmath is the complex-number version of the math module.
# It includes:
#   - phase()
#   - polar()
#   - rect()
#   - sqrt() for negative values
#   - exp(), sin(), cos() for complex domains

import cmath

z = 1 + 1j

print("Phase (radians):", cmath.phase(z))
print("Polar coords:   ", cmath.polar(z))  # (magnitude, angle)
print("Rect from polar:", cmath.rect(1.414, cmath.pi/4))


# ---------------------------------------------------------------------------
# 7. Complex Numbers in Real Scenarios
# ---------------------------------------------------------------------------
# ✔ Electrical engineering (AC signals)
# ✔ Rotations in 2D using multiplication by e^(iθ)
# ✔ Fourier transforms
# ✔ Fractals (Mandelbrot, Julia sets)
# ✔ Physics wave equations
# ✔ Vector transformations

# Example: rotate a point 45° counterclockwise using complex multiplication
import math

point = 3 + 0j
rotation = complex(math.cos(math.pi/4), math.sin(math.pi/4))
rotated_point = point * rotation

print("Rotated point:", rotated_point)


# ---------------------------------------------------------------------------
# 8. Common Mistakes
# ---------------------------------------------------------------------------
# ❌ Using "i" instead of "j"
#     Python only supports "j" for imaginary numbers.
#
# ❌ Treating complex numbers like tuples
#     They are not sequences — only .real and .imag attributes exist.
#
# ❌ Forgetting that dividing by a purely imaginary number is valid:
#     (5 / (2j)) works fine.
#
# ✔ Correct mindset:
#     “Complex numbers behave like real numbers, but with a second dimension.”


# ---------------------------------------------------------------------------
# 9. Summary
# ---------------------------------------------------------------------------
# In this module, I learned:
# - How to create complex numbers using literals and constructor syntax
# - How to access real and imaginary components
# - How to perform arithmetic (add, subtract, multiply, divide)
# - How to use conjugates and magnitude
# - How to use cmath for advanced operations
# - Real-world examples where complex numbers are useful
#
# End of Notes
