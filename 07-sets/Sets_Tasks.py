"""
Module 7 — Sets: Practice Exercises
-----------------------------------

This file contains structured practice tasks for learning Python sets.
Tasks progress from beginner to professional difficulty.

I should:
- Implement each function myself.
- NOT look at the solutions until I finish.
- Write clean, readable code.
- Move from Rank 1 → Rank 5 at my own pace.
"""


# =============================================================================
# Rank 1 — Beginner
# =============================================================================

def create_basic_set():
    """
    Task:
        Return a set containing at least three different fruits.

    Example return:
        {"apple", "banana", "cherry"}

    Return:
        set[str]
    """
    # TODO: Replace set() with your own set of fruit names.
    return set()


def check_membership(s, item):
    """
    Task:
        Return True if `item` is in set `s`, otherwise False.

    Example:
        check_membership({"a", "b"}, "a") -> True

    Args:
        s (set)
        item (Any)

    Return:
        bool
    """
    # TODO: Use the "in" operator.
    return False


def add_item(s, item):
    """
    Task:
        Add `item` to set `s` and return the updated set.

    Args:
        s (set)
        item (Any)

    Return:
        set
    """
    # TODO: Use s.add(item)
    return s


# =============================================================================
# Rank 2 — Easy
# =============================================================================

def remove_item(s, item):
    """
    Task:
        Remove `item` from set `s` safely.
        Use discard() so it does NOT raise an error.

    Example:
        remove_item({1,2,3}, 2) -> {1,3}

    Args:
        s (set)
        item

    Return:
        set
    """
    # TODO: Use discard()
    return s


def convert_list_to_set(values):
    """
    Task:
        Convert a list to a set to remove duplicates.

    Example:
        convert_list_to_set([1,1,2,3]) -> {1,2,3}

    Args:
        values (list)

    Return:
        set
    """
    # TODO: Use set(values)
    return set()


def convert_set_to_list(values):
    """
    Task:
        Convert a set to a list.

    Args:
        values (set)

    Return:
        list
    """
    # TODO: Use list(values)
    return []


# =============================================================================
# Rank 3 — Intermediate
# =============================================================================

def union_sets(a, b):
    """
    Task:
        Return the union of sets a and b.

    Example:
        union_sets({1,2}, {2,3}) -> {1,2,3}

    Return:
        set
    """
    # TODO: Use a | b or a.union(b)
    return set()


def intersection_sets(a, b):
    """
    Task:
        Return the intersection of sets a and b.

    Example:
        intersection_sets({1,2,3}, {3,4}) -> {3}

    Return:
        set
    """
    # TODO: Use a & b
    return set()


def difference_sets(a, b):
    """
    Task:
        Return items in a that are NOT in b.

    Example:
        difference_sets({1,2,3}, {2,3}) -> {1}

    Return:
        set
    """
    # TODO: Use a - b
    return set()


# =============================================================================
# Rank 4 — Advanced
# =============================================================================

def symmetric_difference_sets(a, b):
    """
    Task:
        Return the symmetric difference of sets a and b.
        (Items that appear in ONLY one of the sets.)

    Example:
        symmetric_difference_sets({1,2,3}, {3,4}) -> {1,2,4}

    Return:
        set
    """
    # TODO: Use a ^ b
    return set()


def remove_duplicates_preserve_order(values):
    """
    Task:
        Given a list of values, return a NEW list with duplicates removed
        while preserving original order.

    Example:
        remove_duplicates_preserve_order([1,2,1,3,2])
            -> [1,2,3]

    Args:
        values (list)

    Return:
        list
    """
    # TODO: Use a set for tracking and a list for results.
    return []


def find_unique_items(a, b):
    """
    Task:
        Return items that appear in EXACTLY one of the sets a or b.

    Hint:
        Use symmetric difference.

    Args:
        a (set)
        b (set)

    Return:
        set
    """
    # TODO: Use a ^ b
    return set()


# =============================================================================
# Rank 5 — Professional
# =============================================================================

def missing_expected_fields(expected, received):
    """
    Task:
        Given two sets:
            expected = {"id", "name", "email"}
            received = {"id", "name"}

        Return a set of missing fields.

    Example:
        missing_expected_fields({"a","b","c"}, {"a"}) -> {"b","c"}

    Args:
        expected (set)
        received (set)

    Return:
        set
    """
    # TODO: Use expected - received
    return set()


def shared_tags(user1_tags, user2_tags):
    """
    Task:
        Return the tags BOTH users share.

    Example:
        shared_tags({"python","gaming"}, {"gaming","travel"})
            -> {"gaming"}

    Args:
        user1_tags (set)
        user2_tags (set)

    Return:
        set
    """
    # TODO: Use intersection
    return set()


def dataset_changes(old_set, new_set):
    """
    Task:
        Compare old_set vs new_set and return a dictionary:

            {
                "added": items in new_set but not old_set,
                "removed": items in old_set but not new_set,
                "unchanged": items in BOTH sets
            }

    Example:
        old = {"a", "b"}
        new = {"b", "c"}

        dataset_changes(old, new) ->
            {
                "added": {"c"},
                "removed": {"a"},
                "unchanged": {"b"}
            }

    Args:
        old_set (set)
        new_set (set)

    Return:
        dict[str, set]
    """
    # TODO: Use union/intersection/difference patterns.
    return {
        "added": set(),
        "removed": set(),
        "unchanged": set(),
    }


# =============================================================================
# Optional Testing Area
# =============================================================================

if __name__ == "__main__":
    pass
