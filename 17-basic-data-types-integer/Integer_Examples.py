"""
Module 17 — Basic Data Types: Integer (int)
Examples File

This file contains small, focused demonstrations of Python integers.
Run this file to see the output of each example:

    python Integer_Examples.py
"""


# ---------------------------------------------------------------------------
# Rank 1 — Basic integer creation and arithmetic
# ---------------------------------------------------------------------------

def example_1_simple_integers():
    """Create basic integers and print them."""
    print("Example 1 — Simple integers")
    a = 10
    b = -3
    c = 0
    print(a, b, c)
    print()


def example_2_basic_arithmetic():
    """Show basic arithmetic operations."""
    print("Example 2 — Basic arithmetic")
    x = 12
    y = 5
    print("x + y =", x + y)
    print("x - y =", x - y)
    print("x * y =", x * y)
    print()


# ---------------------------------------------------------------------------
# Rank 2 — Division, modulus, exponentiation, conversion
# ---------------------------------------------------------------------------

def example_3_division_operations():
    """Demonstrate / and // differences."""
    print("Example 3 — Division operations")
    print("7 / 2  =", 7 / 2)
    print("7 // 2 =", 7 // 2)
    print("7 % 2  =", 7 % 2)
    print()


def example_4_exponentiation_and_int_conversion():
    """Power operator and type conversion."""
    print("Example 4 — Exponentiation & int() conversion")
    print("2 ** 5 =", 2 ** 5)
    print("int('123') =", int("123"))
    print("int(9.8)   =", int(9.8))  # truncates
    print()


# ---------------------------------------------------------------------------
# Rank 3 — Binary, hex, octal, and bitwise operations
# ---------------------------------------------------------------------------

def example_5_integer_literal_forms():
    """Show binary, octal, and hex literal forms."""
    print("Example 5 — Literal integer forms")
    print("Binary 0b1010 ->", 0b1010)
    print("Octal  0o12   ->", 0o12)
    print("Hex    0xA    ->", 0xA)
    print()


def example_6_bitwise_operations():
    """Demonstrate bitwise AND, OR, XOR, shifts."""
    print("Example 6 — Bitwise operations")
    x = 0b1010  # 10
    y = 0b1100  # 12
    print("x & y  ->", bin(x & y))
    print("x | y  ->", bin(x | y))
    print("x ^ y  ->", bin(x ^ y))
    print("x << 1 ->", bin(x << 1))
    print("x >> 1 ->", bin(x >> 1))
    print()


# ---------------------------------------------------------------------------
# Rank 4 — Large integers and performance considerations
# ---------------------------------------------------------------------------

def example_7_unlimited_precision():
    """Demonstrate Python's huge integer support."""
    print("Example 7 — Unlimited precision integers")
    big = 10**50
    print("Big integer:", big)
    print("Digits:", len(str(big)))
    print()


def example_8_large_integer_arithmetic():
    """Show arithmetic with very large integers."""
    print("Example 8 — Arithmetic with large integers")
    a = 10**30
    b = 10**25
    print("a + b =", a + b)
    print("a - b =", a - b)
    print("a * b =", a * b)
    print()


# ---------------------------------------------------------------------------
# Rank 5 — Real-world integer usage patterns
# ---------------------------------------------------------------------------

def example_9_loop_counter_pattern():
    """Use integers as counters inside a loop."""
    print("Example 9 — Loop counter pattern")
    for i in range(1, 6):
        print("Step:", i)
    print()


def example_10_id_generation_pattern():
    """Simulate auto-incrementing ID generation."""
    print("Example 10 — Auto ID generation")
    next_id = 1000
    for _ in range(3):
        print("Generated ID:", next_id)
        next_id += 1
    print()


def example_11_mask_flag_pattern():
    """Using bit masks to represent permissions/flags."""
    print("Example 11 — Bit mask pattern")

    READ  = 0b001
    WRITE = 0b010
    EXEC  = 0b100

    user_permissions = READ | WRITE  # enable two permissions

    print("Has READ? ", bool(user_permissions & READ))
    print("Has EXEC? ", bool(user_permissions & EXEC))
    print()


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def main():
    """Run all examples in order."""
    # Rank 1
    example_1_simple_integers()
    example_2_basic_arithmetic()

    # Rank 2
    example_3_division_operations()
    example_4_exponentiation_and_int_conversion()

    # Rank 3
    example_5_integer_literal_forms()
    example_6_bitwise_operations()

    # Rank 4
    example_7_unlimited_precision()
    example_8_large_integer_arithmetic()

    # Rank 5
    example_9_loop_counter_pattern()
    example_10_id_generation_pattern()
    example_11_mask_flag_pattern()


if __name__ == "__main__":
    main()
