"""
Module 7 — Sets: Task Solutions
-------------------------------

This file contains clean, professional solutions for all exercises
from Sets_Tasks.py.

These examples demonstrate:
- Membership tests
- Removing duplicates
- Set operations (union, intersection, difference, symmetric difference)
- Real-world patterns using sets efficiently
"""


# =============================================================================
# Rank 1 — Beginner
# =============================================================================

def create_basic_set():
    """Return a set of three fruits."""
    return {"apple", "banana", "cherry"}


def check_membership(s, item):
    """Return True if `item` is in the set `s`."""
    return item in s


def add_item(s, item):
    """Add an item to the set and return it."""
    s.add(item)
    return s


# =============================================================================
# Rank 2 — Easy
# =============================================================================

def remove_item(s, item):
    """Safely remove an item using discard()."""
    s.discard(item)
    return s


def convert_list_to_set(values):
    """Convert list to set to remove duplicates."""
    return set(values)


def convert_set_to_list(values):
    """Convert set to list."""
    return list(values)


# =============================================================================
# Rank 3 — Intermediate
# =============================================================================

def union_sets(a, b):
    """Return union of sets a and b."""
    return a | b


def intersection_sets(a, b):
    """Return intersection of sets a and b."""
    return a & b


def difference_sets(a, b):
    """Return items in a but not in b."""
    return a - b


# =============================================================================
# Rank 4 — Advanced
# =============================================================================

def symmetric_difference_sets(a, b):
    """Return symmetric difference of sets a and b."""
    return a ^ b


def remove_duplicates_preserve_order(values):
    """Return list with duplicates removed while preserving original order."""
    seen = set()
    result = []

    for item in values:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result


def find_unique_items(a, b):
    """Return items that appear in exactly ONE of the sets."""
    return a ^ b


# =============================================================================
# Rank 5 — Professional
# =============================================================================

def missing_expected_fields(expected, received):
    """Return a set of missing fields: expected - received."""
    return expected - received


def shared_tags(user1_tags, user2_tags):
    """Return tags both users share."""
    return user1_tags & user2_tags


def dataset_changes(old_set, new_set):
    """
    Compare old_set vs new_set and return a dictionary describing:
    - items added
    - items removed
    - items unchanged
    """
    added = new_set - old_set
    removed = old_set - new_set
    unchanged = new_set & old_set

    return {
        "added": added,
        "removed": removed,
        "unchanged": unchanged,
    }


# =============================================================================
# Optional Self-Test
# =============================================================================

if __name__ == "__main__":
    print(create_basic_set())
    print(check_membership({"a", "b"}, "a"))
    print(add_item({"x"}, "y"))

    print(remove_item({1, 2, 3}, 2))
    print(convert_list_to_set([1, 1, 2, 3, 3]))
    print(convert_set_to_list({"a", "b"}))

    print(union_sets({1, 2}, {2, 3}))
    print(intersection_sets({1, 2, 3}, {3, 4}))
    print(difference_sets({1, 2, 3}, {2, 3}))

    print(symmetric_difference_sets({1, 2}, {2, 3}))
    print(remove_duplicates_preserve_order([1, 2, 1, 3, 2]))
    print(find_unique_items({1, 2}, {2, 3}))

    print(missing_expected_fields({"id", "name", "email"}, {"id"}))
    print(shared_tags({"python", "gaming"}, {"gaming", "lol"}))

    print(dataset_changes({"a", "b"}, {"b", "c"}))
