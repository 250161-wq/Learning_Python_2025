"""
Module 7 — Sets: Practical Examples
------------------------------------

This file contains runnable examples demonstrating how sets work
in real Python programs.

Examples are grouped by difficulty level:

- Rank 1: Basics — creating sets, adding elements, membership checks
- Rank 2: Removing items, list ↔ set conversions, duplicates
- Rank 3: Set operations (union, intersection, difference)
- Rank 4: Advanced use cases — filtering, comparisons
- Rank 5: Professional patterns using sets for real-world tasks
"""


# ---------------------------------------------------------------------------
# Rank 1 — Beginner Examples
# ---------------------------------------------------------------------------

def example_1_create_set():
    """Create a simple set and print it."""
    numbers = {1, 2, 3}
    print("Set:", numbers)


def example_2_add_items():
    """Add items to a set using add()."""
    fruits = {"apple", "banana"}
    fruits.add("cherry")
    fruits.add("banana")  # duplicate ignored
    print("Fruits:", fruits)


def example_3_membership():
    """Demonstrate membership testing."""
    colors = {"red", "blue", "green"}
    print("Is 'blue' in set?", "blue" in colors)
    print("Is 'yellow' in set?", "yellow" in colors)


# ---------------------------------------------------------------------------
# Rank 2 — Easy Examples
# ---------------------------------------------------------------------------

def example_4_remove_items():
    """Remove items using remove() and discard()."""
    items = {"pen", "pencil", "eraser"}
    items.remove("pen")       # will raise error if missing
    items.discard("marker")   # safe removal (does nothing)
    print("Items after removal:", items)


def example_5_list_to_set():
    """Convert a list to a set to remove duplicates."""
    nums = [1, 2, 2, 3, 3, 3, 4]
    unique = set(nums)
    print("Unique numbers:", unique)


def example_6_set_to_list():
    """Convert set back to list."""
    s = {"a", "b", "c"}
    lst = list(s)
    print("Converted list:", lst)


# ---------------------------------------------------------------------------
# Rank 3 — Intermediate Examples
# ---------------------------------------------------------------------------

def example_7_union():
    """Show union operations."""
    a = {1, 2, 3}
    b = {3, 4, 5}
    print("Union:", a | b)


def example_8_intersection():
    """Show intersection operations."""
    a = {"apple", "banana", "cherry"}
    b = {"banana", "orange"}
    print("Intersection:", a & b)


def example_9_difference():
    """Show difference operations."""
    a = {1, 2, 3, 4}
    b = {3, 4, 5}
    print("Difference (a - b):", a - b)


def example_10_symmetric_difference():
    """Show symmetric difference operations."""
    a = {1, 2, 3}
    b = {3, 4, 5}
    print("Symmetric difference:", a ^ b)


# ---------------------------------------------------------------------------
# Rank 4 — Advanced Examples
# ---------------------------------------------------------------------------

def example_11_filter_unique():
    """Filter names to only those that appear exactly once."""
    names = ["Alice", "Bob", "Peyman", "Alice", "Bob", "Arlette"]
    unique_names = {name for name in names if names.count(name) == 1}
    print("Names appearing once:", unique_names)


def example_12_set_comparisons():
    """Demonstrate subset, superset, and disjoint checks."""
    a = {1, 2}
    b = {1, 2, 3}
    c = {4, 5}

    print("a ⊆ b ?", a <= b)
    print("b ⊇ a ?", b >= a)
    print("a disjoint c ?", a.isdisjoint(c))


def example_13_remove_duplicates_preserve_order():
    """
    Remove duplicates while keeping order — using a set for fast checks.
    """
    seen = set()
    result = []
    items = [1, 2, 1, 3, 2, 4, 5]

    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)

    print("Clean list:", result)


# ---------------------------------------------------------------------------
# Rank 5 — Professional Examples
# ---------------------------------------------------------------------------

def example_14_detect_missing_values():
    """
    Detect which expected values are missing from a dataset.
    """
    expected = {"id", "name", "email", "age"}
    received = {"id", "name"}

    missing = expected - received
    print("Missing fields:", missing)


def example_15_detect_common_tags():
    """
    Find tags shared between two users.
    """
    user1_tags = {"python", "gaming", "mexicali"}
    user2_tags = {"gaming", "travel", "mexicali"}

    common = user1_tags & user2_tags
    print("Common tags:", common)


def example_16_compare_datasets():
    """
    Determine:
    - Added items
    - Removed items
    - Shared items
    """
    old = {"apple", "banana", "cherry"}
    new = {"banana", "dragonfruit", "cherry", "elderberry"}

    added = new - old
    removed = old - new
    unchanged = new & old

    print("Added:", added)
    print("Removed:", removed)
    print("Unchanged:", unchanged)


# ---------------------------------------------------------------------------
# Demonstration Section
# ---------------------------------------------------------------------------

def main():
    print("--- Rank 1 ---")
    example_1_create_set()
    example_2_add_items()
    example_3_membership()

    print("\n--- Rank 2 ---")
    example_4_remove_items()
    example_5_list_to_set()
    example_6_set_to_list()

    print("\n--- Rank 3 ---")
    example_7_union()
    example_8_intersection()
    example_9_difference()
    example_10_symmetric_difference()

    print("\n--- Rank 4 ---")
    example_11_filter_unique()
    example_12_set_comparisons()
    example_13_remove_duplicates_preserve_order()

    print("\n--- Rank 5 ---")
    example_14_detect_missing_values()
    example_15_detect_common_tags()
    example_16_compare_datasets()


if __name__ == "__main__":
    main()
