"""
Module 6 — Dictionaries: Practical Examples
-------------------------------------------

This file contains runnable examples that demonstrate how to use
Python dictionaries in real-world scenarios.

Examples progress by difficulty:
- Rank 1: Basic creation & lookup
- Rank 2: Updating & deleting keys
- Rank 3: Looping & transformations
- Rank 4: Nested dictionaries, merging
- Rank 5: Professional utility patterns
"""


# ---------------------------------------------------------------------------
# Rank 1 — Beginner Examples
# ---------------------------------------------------------------------------

def example_1_create_dict():
    """Create a simple dictionary."""
    user = {"name": "Peyman", "age": 43, "country": "Mexico"}
    print("User dictionary:", user)


def example_2_access_values():
    """Access dictionary values using keys."""
    user = {"name": "Peyman", "age": 43}
    print("Name:", user["name"])
    print("Age:", user["age"])


def example_3_safe_access():
    """Use .get() for safe access with default values."""
    user = {"name": "Peyman"}
    print("Nickname:", user.get("nickname", "No nickname provided"))


# ---------------------------------------------------------------------------
# Rank 2 — Easy Examples
# ---------------------------------------------------------------------------

def example_4_add_update():
    """Add and update dictionary keys."""
    book = {"title": "Python Basics"}
    book["author"] = "Nova"
    book["title"] = "Advanced Python"
    print("Updated book:", book)


def example_5_remove_keys():
    """Delete keys using del and pop()."""
    data = {"a": 1, "b": 2, "c": 3}
    del data["b"]
    removed_value = data.pop("c")
    print("After deletions:", data)
    print("Removed value:", removed_value)


def example_6_check_membership():
    """Check if a key exists in the dictionary."""
    settings = {"theme": "dark", "volume": 80}
    print("Has 'theme'? ->", "theme" in settings)
    print("Has 'brightness'? ->", "brightness" in settings)


# ---------------------------------------------------------------------------
# Rank 3 — Intermediate Examples
# ---------------------------------------------------------------------------

def example_7_looping():
    """Loop through keys, values, and items."""
    scores = {"Alice": 90, "Bob": 75, "Peyman": 88}

    print("--- Keys ---")
    for k in scores.keys():
        print(k)

    print("--- Values ---")
    for v in scores.values():
        print(v)

    print("--- Items ---")
    for name, score in scores.items():
        print(name, "=>", score)


def example_8_count_frequencies():
    """Use a dictionary to count item frequencies."""
    items = ["apple", "banana", "apple", "orange", "banana", "apple"]
    freq = {}

    for item in items:
        freq[item] = freq.get(item, 0) + 1

    print("Frequencies:", freq)


def example_9_transform_values():
    """Transform values using dictionary comprehension."""
    prices = {"apple": 10, "banana": 8, "orange": 12}
    discounted = {k: v * 0.9 for k, v in prices.items()}  # 10% off
    print("Discounted prices:", discounted)


# ---------------------------------------------------------------------------
# Rank 4 — Advanced Examples
# ---------------------------------------------------------------------------

def example_10_nested_dict():
    """Create and access nested dictionaries."""
    student = {
        "name": "Alice",
        "scores": {"math": 90, "science": 85, "english": 92},
        "address": {"city": "Mexicali", "zip": 21000},
    }

    print("Math score:", student["scores"]["math"])
    print("City:", student["address"]["city"])


def example_11_merge_dicts():
    """Merge dictionaries using update() and | operator."""
    a = {"x": 1, "y": 2}
    b = {"y": 20, "z": 3}

    merged_update = a.copy()
    merged_update.update(b)

    merged_pipe = a | b  # Python 3.9+

    print("Merged with update():", merged_update)
    print("Merged with | operator:", merged_pipe)


def example_12_reverse_lookup():
    """Find key by value (reverse mapping)."""
    colors = {"red": "#FF0000", "blue": "#0000FF", "green": "#00FF00"}

    # Find the key for a given value
    value = "#0000FF"
    key = None
    for k, v in colors.items():
        if v == value:
            key = k
            break

    print("Color for value #0000FF:", key)


# ---------------------------------------------------------------------------
# Rank 5 — Professional Examples
# ---------------------------------------------------------------------------

def example_13_group_by_first_letter(names):
    """
    Group names by their first letter using a dictionary.
    Useful for indexing and categorizing.
    """
    groups = {}

    for name in names:
        first = name[0].upper()
        groups.setdefault(first, []).append(name)

    print("Grouped names:", groups)


def example_14_invert_dictionary(mapping):
    """
    Create a reversed dictionary: value -> key.
    Assumes values are unique.
    """
    inverted = {v: k for k, v in mapping.items()}
    print("Inverted dictionary:", inverted)


def example_15_safe_update_record(record, updates):
    """
    Professionally update a record using safe patterns.
    Keys not present in 'updates' remain unchanged.
    """
    new_record = record.copy()
    new_record.update(updates)
    print("Updated record:", new_record)


# ---------------------------------------------------------------------------
# Demonstration Section
# ---------------------------------------------------------------------------

def main():
    print("--- Rank 1 ---")
    example_1_create_dict()
    example_2_access_values()
    example_3_safe_access()

    print("\n--- Rank 2 ---")
    example_4_add_update()
    example_5_remove_keys()
    example_6_check_membership()

    print("\n--- Rank 3 ---")
    example_7_looping()
    example_8_count_frequencies()
    example_9_transform_values()

    print("\n--- Rank 4 ---")
    example_10_nested_dict()
    example_11_merge_dicts()
    example_12_reverse_lookup()

    print("\n--- Rank 5 ---")
    example_13_group_by_first_letter(["Alice", "Arlette", "Peyman", "Bob"])
    example_14_invert_dictionary({"red": "#FF0000", "blue": "#0000FF"})
    example_15_safe_update_record(
        {"name": "Peyman", "age": 43},
        {"age": 44, "country": "Mexico"}
    )


if __name__ == "__main__":
    main()
