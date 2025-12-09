"""
Module 13 — Ranges
Examples File

This file contains practical examples showing how to use Python's range()
function in real code. These examples demonstrate numeric sequences,
looping patterns, reverse iteration, and performance-friendly usage.

Run this file directly to see the output:
    python Ranges_Examples.py
"""


# ---------------------------------------------------------------------------
# Rank 1 — Basic range usage
# ---------------------------------------------------------------------------

def example_1_range_stop() -> None:
    """Simple range(stop) usage."""
    print("Example 1 — range(stop)")
    r = range(5)
    print("range(5):", r)
    print("Converted to list:", list(r))
    print()


def example_2_range_start_stop() -> None:
    """Use range(start, stop)."""
    print("Example 2 — range(start, stop)")
    r = range(2, 6)
    print("range(2, 6):", list(r))
    print()


def example_3_range_step() -> None:
    """Use range(start, stop, step)."""
    print("Example 3 — range(start, stop, step)")
    r = range(1, 10, 2)
    print("range(1, 10, 2):", list(r))
    print()


# ---------------------------------------------------------------------------
# Rank 2 — Ranges in loops
# ---------------------------------------------------------------------------

def example_4_loop_basic() -> None:
    """Loop through a simple range."""
    print("Example 4 — Looping with range")
    for i in range(3):
        print("Iteration:", i)
    print()


def example_5_loop_with_start_stop() -> None:
    """Loop with custom start/stop values."""
    print("Example 5 — Loop with start and stop")
    for i in range(5, 8):
        print("Value:", i)
    print()


def example_6_loop_with_step() -> None:
    """Loop using step increments."""
    print("Example 6 — Loop with steps of 3")
    for i in range(0, 10, 3):
        print("i =", i)
    print()


# ---------------------------------------------------------------------------
# Rank 3 — Reverse ranges & negative steps
# ---------------------------------------------------------------------------

def example_7_reverse_range() -> None:
    """Count backward using range()."""
    print("Example 7 — Reverse range")
    for i in range(10, 0, -1):
        print(i, end=" ")
    print("\n")


def example_8_reverse_to_zero() -> None:
    """Reverse including zero."""
    print("Example 8 — Reverse to zero")
    print(list(range(5, -1, -1)))
    print()


# ---------------------------------------------------------------------------
# Rank 4 — Membership and performance
# ---------------------------------------------------------------------------

def example_9_membership_check() -> None:
    """Check whether a value is inside a range."""
    print("Example 9 — Membership test")
    print("10 in range(20):", 10 in range(20))
    print("21 in range(20):", 21 in range(20))
    print()


def example_10_range_vs_list_performance() -> None:
    """Demonstrate that ranges do not store all values in memory."""
    print("Example 10 — Range efficiency concept")
    big_range = range(1_000_000)
    print("Range created. It uses very little memory.")
    print("First 5 numbers:", list(big_range[:5]))
    print()


# ---------------------------------------------------------------------------
# Rank 5 — More realistic patterns
# ---------------------------------------------------------------------------

def example_11_even_numbers() -> None:
    """Use range to generate even numbers."""
    print("Example 11 — Even number sequence")
    evens = list(range(0, 21, 2))
    print("Even numbers:", evens)
    print()


def example_12_index_loop() -> None:
    """Use range(len(sequence)) to loop with indexes."""
    print("Example 12 — Loop using indexes")
    names = ["Ana", "Luis", "Pablo"]
    for i in range(len(names)):
        print(f"Index {i} → {names[i]}")
    print()


def example_13_batch_processing() -> None:
    """Use ranges to process data in chunks."""
    print("Example 13 — Batch processing example")
    data = list(range(1, 21))  # pretend this is real data
    batch_size = 5

    for start in range(0, len(data), batch_size):
        end = start + batch_size
        batch = data[start:end]
        print("Batch:", batch)

    print()


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def main() -> None:
    """Run all example functions in sequence."""

    # Rank 1
    example_1_range_stop()
    example_2_range_start_stop()
    example_3_range_step()

    # Rank 2
    example_4_loop_basic()
    example_5_loop_with_start_stop()
    example_6_loop_with_step()

    # Rank 3
    example_7_reverse_range()
    example_8_reverse_to_zero()

    # Rank 4
    example_9_membership_check()
    example_10_range_vs_list_performance()

    # Rank 5
    example_11_even_numbers()
    example_12_index_loop()
    example_13_batch_processing()


if __name__ == "__main__":
    main()
