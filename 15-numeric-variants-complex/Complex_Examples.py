"""
Module 15 — Numeric Variants: Complex Numbers
Examples File

This file contains practical, runnable examples showing how Python's
complex numbers work in real code. Each example demonstrates a key
concept: creation, arithmetic, magnitude, conjugates, and cmath usage.

Run this file directly to see all examples:
    python Complex_Examples.py
"""


# ---------------------------------------------------------------------------
# Rank 1 — Basic creation and components
# ---------------------------------------------------------------------------

def example_1_basic_creation() -> None:
    """Show simple ways to create complex numbers."""
    print("Example 1 — Basic complex number creation")

    a = 3 + 4j
    b = complex(5, -2)

    print("a:", a)
    print("b:", b)
    print()


def example_2_access_parts() -> None:
    """Access real and imaginary components."""
    print("Example 2 — Real and imaginary parts")

    z = 7 - 3j
    print("z:", z)
    print("Real:", z.real)
    print("Imag:", z.imag)
    print()


# ---------------------------------------------------------------------------
# Rank 2 — Arithmetic operations
# ---------------------------------------------------------------------------

def example_3_arithmetic() -> None:
    """Perform basic arithmetic with complex numbers."""
    print("Example 3 — Arithmetic")

    a = 2 + 3j
    b = 1 - 4j

    print("a + b =", a + b)
    print("a - b =", a - b)
    print("a * b =", a * b)
    print("a / b =", a / b)
    print()


def example_4_magnitude() -> None:
    """Calculate the magnitude of a complex number."""
    print("Example 4 — Magnitude (abs)")

    z = 3 + 4j
    print("z:", z)
    print("abs(z):", abs(z))
    print()


# ---------------------------------------------------------------------------
# Rank 3 — Conjugates & type conversions
# ---------------------------------------------------------------------------

def example_5_conjugate() -> None:
    """Show how to compute the complex conjugate."""
    print("Example 5 — Conjugates")

    z = 6 + 8j
    print("z:", z)
    print("Conjugate:", z.conjugate())
    print()


def example_6_convert_from_float() -> None:
    """Create complex numbers using float values."""
    print("Example 6 — Creating from floats")

    z = complex(2.5, -0.75)
    print("Complex number:", z)
    print()


# ---------------------------------------------------------------------------
# Rank 4 — cmath operations
# ---------------------------------------------------------------------------

import cmath
import math

def example_7_phase_and_polar() -> None:
    """Show phase (angle) and polar coordinate conversions."""
    print("Example 7 — Phase and polar coordinates")

    z = 1 + 1j

    print("z:", z)
    print("Phase:", cmath.phase(z))
    print("Polar:", cmath.polar(z))
    print()


def example_8_rect_from_polar() -> None:
    """Convert polar coordinates back to a complex number."""
    print("Example 8 — Rectangular from polar")

    magnitude = 2
    angle = math.pi / 3  # 60 degrees

    z = cmath.rect(magnitude, angle)
    print("Rectangular form:", z)
    print()


# ---------------------------------------------------------------------------
# Rank 5 — Real-world usage
# ---------------------------------------------------------------------------

def example_9_rotation() -> None:
    """Rotate a point in 2D using complex multiplication."""
    print("Example 9 — 2D Rotation with complex numbers")

    point = 4 + 0j
    angle = math.pi / 4  # 45 degrees

    rotation = complex(math.cos(angle), math.sin(angle))
    rotated = point * rotation

    print("Original point:", point)
    print("Rotated point:", rotated)
    print()


def example_10_fractal_step() -> None:
    """One iteration of the Mandelbrot formula."""
    print("Example 10 — Mandelbrot iteration step")

    z = 0 + 0j
    c = -0.7 + 0.27015j

    z = z * z + c  # Standard Mandelbrot iteration
    print("Next z value:", z)
    print()


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def main() -> None:
    """Run all example functions in sequence."""

    # Rank 1
    example_1_basic_creation()
    example_2_access_parts()

    # Rank 2
    example_3_arithmetic()
    example_4_magnitude()

    # Rank 3
    example_5_conjugate()
    example_6_convert_from_float()

    # Rank 4
    example_7_phase_and_polar()
    example_8_rect_from_polar()

    # Rank 5
    example_9_rotation()
    example_10_fractal_step()


if __name__ == "__main__":
    main()
