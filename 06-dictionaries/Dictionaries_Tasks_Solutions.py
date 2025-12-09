"""
Module 6 — Dictionaries: Task Solutions
---------------------------------------

Clean, professional, production-style solutions for all tasks in
Dictionaries_Tasks.py.

These examples demonstrate safe access, merging, comprehensions,
nested lookups, grouping logic, frequency counting, and more.
"""


# =============================================================================
# Rank 1 — Beginner
# =============================================================================

def create_user_profile():
    """Return a simple user dictionary."""
    return {"name": "Peyman", "age": 43, "country": "Mexico"}


def get_country(user):
    """Return the country stored in the user dictionary."""
    return user.get("country")


def add_email(user, email):
    """Add a new 'email' key to the dictionary and return it."""
    user["email"] = email
    return user


# =============================================================================
# Rank 2 — Easy
# =============================================================================

def remove_key(data, key):
    """Remove the given key safely using pop()."""
    data.pop(key, None)
    return data


def safe_get_value(data, key, default=None):
    """Return data.get(key, default)."""
    return data.get(key, default)


def key_exists(data, key):
    """Return True if a key exists in the dictionary."""
    return key in data


# =============================================================================
# Rank 3 — Intermediate
# =============================================================================

def count_words(words):
    """Return a dictionary counting occurrences of each word."""
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq


def invert_dictionary(d):
    """Return a new dictionary with reversed key/value pairs."""
    return {v: k for k, v in d.items()}


def double_values(data):
    """Return a new dictionary with numeric values doubled."""
    return {k: v * 2 for k, v in data.items()}


# =============================================================================
# Rank 4 — Advanced
# =============================================================================

def get_nested_value(data, key1, key2):
    """Safely return data[key1][key2], or None if missing."""
    inner = data.get(key1)
    if isinstance(inner, dict):
        return inner.get(key2)
    return None


def merge_dicts(a, b):
    """Merge dictionaries without modifying originals."""
    return {**a, **b}


def reverse_lookup(d, value):
    """Return the first key whose value matches the given value."""
    for k, v in d.items():
        if v == value:
            return k
    return None


# =============================================================================
# Rank 5 — Professional
# =============================================================================

def group_by_first_letter(names):
    """Group names by first letter, case-insensitive."""
    groups = {}
    for name in names:
        first = name[0].upper()
        groups.setdefault(first, []).append(name)
    return groups


def merge_user_settings(defaults, overrides):
    """
    Return a NEW dictionary where overrides update defaults.
    """
    merged = defaults.copy()
    merged.update(overrides)
    return merged


def summarize_inventory(inventory):
    """
    Summarize inventory structure and compute totals.
    """
    total_items = 0
    total_value = 0.0
    item_types = len(inventory)

    for item, info in inventory.items():
        stock = info.get("stock", 0)
        price = info.get("price", 0)
        total_items += stock
        total_value += stock * price

    return {
        "total_items": total_items,
        "total_value": total_value,
        "items": item_types,
    }


# =============================================================================
# Optional Test Run
# =============================================================================

if __name__ == "__main__":
    print(create_user_profile())
    print(get_country({"country": "Canada"}))
    print(add_email({"name": "Bob"}, "bob@mail.com"))

    print(remove_key({"a": 1, "b": 2}, "a"))
    print(safe_get_value({"x": 10}, "y", 0))
    print(key_exists({"x": 1}, "x"))

    print(count_words(["apple", "banana", "apple"]))
    print(invert_dictionary({"a": 1, "b": 2}))
    print(double_values({"a": 2, "b": 5}))

    nested = {"user": {"age": 30, "city": "Mexicali"}}
    print(get_nested_value(nested, "user", "age"))

    print(merge_dicts({"x": 1}, {"x": 2, "y": 3}))
    print(reverse_lookup({"a": 1, "b": 2}, 2))

    print(group_by_first_letter(["Alice", "Arlette", "Bob"]))
    print(merge_user_settings({"theme": "light"}, {"theme": "dark"}))

    inventory = {
        "apples": {"price": 2, "stock": 50},
        "oranges": {"price": 3, "stock": 20},
    }
    print(summarize_inventory(inventory))
