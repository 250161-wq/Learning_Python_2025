"""
Module 14 — Frozenset
Examples File

This file contains practical examples that demonstrate how Python's frozenset
works in real scenarios. Each example is small, focused, and easy to run.

Run this file directly to see all examples:
    python Frozenset_Examples.py
"""


# ---------------------------------------------------------------------------
# Rank 1 — Basic frozenset creation
# ---------------------------------------------------------------------------

def example_1_basic_creation() -> None:
    """Create basic frozensets from different types."""
    print("Example 1 — Basic frozenset creation")

    fs1 = frozenset([1, 2, 3])
    fs2 = frozenset({3, 4, 5})
    fs3 = frozenset("hello")  # characters become elements

    print("fs1:", fs1)
    print("fs2:", fs2)
    print("fs3:", fs3)
    print()


def example_2_uniqueness() -> None:
    """Demonstrate automatic removal of duplicates."""
    print("Example 2 — Uniqueness rule")

    fs = frozenset([1, 2, 2, 3, 3, 3])
    print("frozenset([1, 2, 2, 3, 3, 3]) ->", fs)
    print()


# ---------------------------------------------------------------------------
# Rank 2 — Allowed operations
# ---------------------------------------------------------------------------

def example_3_union_intersection() -> None:
    """Demonstrate union and intersection."""
    print("Example 3 — Union & intersection")

    a = frozenset([1, 2, 3])
    b = frozenset([3, 4])

    print("Union:", a.union(b))
    print("Intersection:", a.intersection(b))
    print()


def example_4_difference() -> None:
    """Difference between frozensets."""
    print("Example 4 — Difference")

    a = frozenset([1, 2, 3])
    b = frozenset([2, 3])

    print("a - b:", a.difference(b))
    print()


# ---------------------------------------------------------------------------
# Rank 3 — Hashability & dictionary keys
# ---------------------------------------------------------------------------

def example_5_as_dict_keys() -> None:
    """Use frozensets as dictionary keys."""
    print("Example 5 — Frozensets as dictionary keys")

    tracks = {
        frozenset(["math", "physics"]): "Science Track",
        frozenset(["art", "design"]): "Arts Track",
    }

    key = frozenset(["math", "physics"])
    print("Lookup:", tracks[key])
    print()


def example_6_inside_sets() -> None:
    """Show that frozensets can be elements of a set."""
    print("Example 6 — Frozensets inside a set")

    combos = {frozenset([1, 2]), frozenset([3, 4])}
    print("Set of frozensets:", combos)
    print()


# ---------------------------------------------------------------------------
# Rank 4 — Immutability demonstration
# ---------------------------------------------------------------------------

def example_7_mutation_error() -> None:
    """Show that frozensets cannot be modified (demonstration only)."""
    print("Example 7 — Attempting to mutate frozenset")

    fs = frozenset([1, 2, 3])
    print("Frozenset:", fs)

    print("Trying fs.add(4)... (this would cause an error)")
    print("frozensets are immutable, so methods like add(), remove(), pop() do not exist.")
    print()


# ---------------------------------------------------------------------------
# Rank 5 — Realistic usage patterns
# ---------------------------------------------------------------------------

def example_8_configuration_lock() -> None:
    """Use frozenset to protect configuration options."""
    print("Example 8 — Configuration lock pattern")

    allowed_settings = frozenset(["dark_mode", "notifications", "auto_save"])

    print("Allowed settings:", allowed_settings)

    # Pretend we are checking a user input:
    user_choice = "dark_mode"

    if user_choice in allowed_settings:
        print("Setting is allowed.")
    else:
        print("Invalid setting!")

    print()


def example_9_unique_combinations() -> None:
    """Group unique combinations using frozensets."""
    print("Example 9 — Unique combination grouping")

    combos = [
        ["apple", "banana"],
        ["banana", "apple"],  # same combination
        ["orange", "kiwi"],
    ]

    unique_groups = {frozenset(combo) for combo in combos}
    print("Unique combinations:", unique_groups)
    print()


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def main() -> None:
    """Run all examples in sequence."""

    # Rank 1
    example_1_basic_creation()
    example_2_uniqueness()

    # Rank 2
    example_3_union_intersection()
    example_4_difference()

    # Rank 3
    example_5_as_dict_keys()
    example_6_inside_sets()

    # Rank 4
    example_7_mutation_error()

    # Rank 5
    example_8_configuration_lock()
    example_9_unique_combinations()


if __name__ == "__main__":
    main()
