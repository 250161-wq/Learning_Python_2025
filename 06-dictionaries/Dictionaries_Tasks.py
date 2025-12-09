"""
Module 6 — Dictionaries: Practice Exercises
-------------------------------------------

This file contains structured dictionary exercises, ranked from
beginner to professional-level difficulty.

I should:
- Try each task on my own.
- NOT look at the solutions until I finish.
- Write clean, readable code inside each function.
- Move rank by rank: 1 → 5.

When finished, compare answers with Dictionaries_Tasks_Solutions.py.
"""


# =============================================================================
# Rank 1 — Beginner
# =============================================================================

def create_user_profile():
    """
    Task:
        Return a dictionary representing a user profile with these keys:
        - "name"
        - "age"
        - "country"

    Choose any values you want.

    Example return:
        {"name": "Alice", "age": 30, "country": "USA"}

    Return:
        dict
    """
    # TODO: Replace {} with a dictionary containing your own values.
    return {}


def get_country(user):
    """
    Task:
        Given a dictionary `user`, return the value stored under "country".

    Example:
        get_country({"country": "Mexico"}) -> "Mexico"

    Args:
        user (dict)

    Return:
        str
    """
    # TODO: Return user["country"] or user.get("country").
    return None


def add_email(user, email):
    """
    Task:
        Add a new key-value pair ("email": email) to the dictionary.

    Example:
        add_email({"name": "Bob"}, "bob@mail.com")
            -> {"name": "Bob", "email": "bob@mail.com"}

    Args:
        user (dict)
        email (str)

    Return:
        dict: Updated dictionary.
    """
    # TODO: Add the key and return the updated dict.
    return user


# =============================================================================
# Rank 2 — Easy
# =============================================================================

def remove_key(data, key):
    """
    Task:
        Remove the given key from the dictionary if it exists.
        Use pop(key, default) to avoid KeyError.

    Example:
        remove_key({"a": 1, "b": 2}, "a") -> {"b": 2}

    Args:
        data (dict)
        key: Key to remove.

    Return:
        dict
    """
    # TODO: Use pop() safely.
    return data


def safe_get_value(data, key, default=None):
    """
    Task:
        Return the value for `key` using data.get(key, default).

    Example:
        safe_get_value({"x": 10}, "x") -> 10
        safe_get_value({"x": 10}, "y", 0) -> 0

    Args:
        data (dict)
        key
        default

    Return:
        Any
    """
    # TODO: Use data.get(key, default)
    return None


def key_exists(data, key):
    """
    Task:
        Return True if `key` exists in the dictionary, otherwise False.

    Args:
        data (dict)
        key

    Return:
        bool
    """
    # TODO: Use the `in` operator.
    return False


# =============================================================================
# Rank 3 — Intermediate
# =============================================================================

def count_words(words):
    """
    Task:
        Given a list of words, return a dictionary mapping each word
        to the number of times it appears.

    Example:
        count_words(["apple", "banana", "apple"])
            -> {"apple": 2, "banana": 1}

    Args:
        words (list[str])

    Return:
        dict[str, int]
    """
    # TODO: Build frequency dictionary.
    return {}


def invert_dictionary(d):
    """
    Task:
        Return a NEW dictionary where keys become values and
        values become keys.

    NOTE:
        Assume all values are unique and hashable.

    Example:
        invert_dictionary({"a": 1, "b": 2})
            -> {1: "a", 2: "b"}

    Args:
        d (dict)

    Return:
        dict
    """
    # TODO: Build a reversed dictionary.
    return {}


def double_values(data):
    """
    Task:
        Return a NEW dictionary where all numeric values
        are doubled.

    Example:
        double_values({"a": 2, "b": 5})
            -> {"a": 4, "b": 10}

    Args:
        data (dict[str, int|float])

    Return:
        dict
    """
    # TODO: Use dictionary comprehension.
    return {}


# =============================================================================
# Rank 4 — Advanced
# =============================================================================

def get_nested_value(data, key1, key2):
    """
    Task:
        Given a nested dictionary, return data[key1][key2]
        safely using .get()

    Example:
        d = {"user": {"age": 20}}
        get_nested_value(d, "user", "age") -> 20

    If any key is missing, return None.

    Args:
        data (dict)
        key1: Outer key
        key2: Inner key

    Return:
        Any
    """
    # TODO: Implement nested safe lookup.
    return None


def merge_dicts(a, b):
    """
    Task:
        Merge dictionaries `a` and `b` into a NEW dictionary.

    Requirements:
        - Do NOT modify originals.
        - b should overwrite a on duplicate keys.
        - Use either update() or | operator.

    Example:
        merge_dicts({"x": 1}, {"x": 2, "y": 3})
            -> {"x": 2, "y": 3}

    Args:
        a (dict)
        b (dict)

    Return:
        dict
    """
    # TODO: Return merged dictionary.
    return {}


def reverse_lookup(d, value):
    """
    Task:
        Given a dictionary, return the FIRST key whose value equals `value`.

    Example:
        reverse_lookup({"a": 1, "b": 2}, 2) -> "b"

    If no match, return None.

    Args:
        d (dict)
        value

    Return:
        key | None
    """
    # TODO: Loop through d.items() to find matching value.
    return None


# =============================================================================
# Rank 5 — Professional
# =============================================================================

def group_by_first_letter(names):
    """
    Task:
        Group names by their first letter, case-insensitive.

    Example:
        group_by_first_letter(["Alice", "Bob", "Arlette"])
            -> {"A": ["Alice", "Arlette"], "B": ["Bob"]}

    Args:
        names (list[str])

    Return:
        dict[str, list[str]]
    """
    # TODO: Build grouped dictionary.
    return {}


def merge_user_settings(defaults, overrides):
    """
    Task:
        Return a NEW dictionary where:
        - defaults provides base values
        - overrides replaces only keys that exist in it

    Example:
        defaults = {"theme": "light", "volume": 50}
        overrides = {"volume": 80}
        -> {"theme": "light", "volume": 80}

    Args:
        defaults (dict)
        overrides (dict)

    Return:
        dict
    """
    # TODO: Copy defaults, apply overrides.
    return {}


def summarize_inventory(inventory):
    """
    Task:
        Given an inventory dictionary structured like:

            {
                "apples": {"price": 2, "stock": 50},
                "oranges": {"price": 3, "stock": 20},
            }

        Return a NEW dictionary summarizing:

            {
                "total_items": (sum of all stock),
                "total_value": (sum of price * stock),
                "items": number of different product types
            }

    Args:
        inventory (dict[str, dict[str, int|float]])

    Return:
        dict[str, int|float]
    """
    # TODO: Calculate total stock, total value, item count.
    return {}


# =============================================================================
# Optional Testing Area
# =============================================================================

if __name__ == "__main__":
    pass
