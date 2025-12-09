"""
Module 6 — Dictionaries: Notes & Explanations
---------------------------------------------

A dictionary is a collection of **key-value pairs**.  
It is one of Python’s most powerful and flexible data structures.

Dictionaries allow:
- Fast lookups
- Structuring data like JSON
- Counting items
- Grouping information
- Modeling complex real-world objects

Syntax:
    my_dict = {"key": "value"}

Keys MUST be immutable types (e.g., strings, ints, tuples).
Values can be ANY type.
"""


# ---------------------------------------------------------------------------
# 1. What is a Dictionary?
# ---------------------------------------------------------------------------
"""
A dictionary stores data in KEY → VALUE form.

Example:
    user = {
        "name": "Peyman",
        "age": 43,
        "country": "Mexico"
    }

Access values using keys:
    user["name"]  -> "Peyman"
"""

user = {"name": "Peyman", "age": 43, "country": "Mexico"}


# ---------------------------------------------------------------------------
# 2. Accessing Dictionary Values
# ---------------------------------------------------------------------------
"""
Two main methods:

1. Direct key access:
        user["name"]
    - Raises KeyError if key does not exist.

2. Safe access:
        user.get("name")
        user.get("nickname", "Not provided")
    - Does NOT raise KeyError.
    - Allows default values.
"""

name = user.get("name")
nickname = user.get("nickname", "Unknown")


# ---------------------------------------------------------------------------
# 3. Adding & Updating Dictionary Keys
# ---------------------------------------------------------------------------
"""
Dictionaries are MUTABLE.

Example:
    user["email"] = "peyman@example.com"   # Add new key
    user["age"] = 44                       # Update existing key
"""

user["email"] = "peyman@example.com"
user["age"] = 44


# ---------------------------------------------------------------------------
# 4. Removing Items from a Dictionary
# ---------------------------------------------------------------------------
"""
Common removal operations:

del dictionary[key]        -> Remove the key completely
dictionary.pop(key)        -> Remove key & return its value
dictionary.pop(key, None)  -> Safe version (prevents KeyError)
dictionary.clear()         -> Remove ALL items
"""

# Example:
# del user["email"]
# removed_age = user.pop("age", None)


# ---------------------------------------------------------------------------
# 5. Dictionary Methods (Must-Know for Professionals)
# ---------------------------------------------------------------------------
"""
keys()       -> returns all keys
values()     -> returns all values
items()      -> returns (key, value) pairs
update(dict) -> merge another dictionary into this one

Example:
    for key in user.keys():
        print(key)

    for value in user.values():
        print(value)

    for k, v in user.items():
        print(k, v)
"""


# ---------------------------------------------------------------------------
# 6. Checking if a Key Exists
# ---------------------------------------------------------------------------
"""
Use the `in` keyword:

    if "age" in user:
        print("Age exists")

    if "email" not in user:
        print("Missing email")
"""

key_exists = "name" in user


# ---------------------------------------------------------------------------
# 7. Looping Through Dictionaries
# ---------------------------------------------------------------------------
"""
Loop through:
- Keys
- Values
- Key-value pairs

Examples:
    for key in user:
        print(key)

    for key, value in user.items():
        print(key, value)
"""


# ---------------------------------------------------------------------------
# 8. Dictionary Comprehensions (Professional Technique)
# ---------------------------------------------------------------------------
"""
Useful for building dictionaries from loops.

Example:
    squares = {x: x*x for x in range(5)}
    -> {0:0, 1:1, 2:4, 3:9, 4:16}

Filtering example:
    evens = {k: v for k, v in data.items() if v % 2 == 0}
"""

squares = {x: x * x for x in range(5)}


# ---------------------------------------------------------------------------
# 9. Nested Dictionaries
# ---------------------------------------------------------------------------
"""
Dictionaries can contain dictionaries:

    student = {
        "name": "Alice",
        "scores": {
            "math": 90,
            "science": 85
        }
    }

Access:
    student["scores"]["math"] -> 90
"""

student = {
    "name": "Alice",
    "scores": {"math": 90, "science": 85}
}


# ---------------------------------------------------------------------------
# 10. Merging Dictionaries
# ---------------------------------------------------------------------------
"""
Python offers multiple ways to merge:

1. update():
        d1.update(d2)

2. Dictionary unpacking (Python 3.9+):
        merged = d1 | d2

3. Unpacking older syntax:
        merged = {**d1, **d2}
"""

d1 = {"a": 1, "b": 2}
d2 = {"b": 200, "c": 3}
merged = d1 | d2  # New value for "b" overrides old one


# ---------------------------------------------------------------------------
# 11. Practical Use Cases of Dictionaries
# ---------------------------------------------------------------------------
"""
✔ Storing user profiles
✔ Grouping related information
✔ Counting items (frequency maps)
✔ Fast lookups by unique keys
✔ Mimicking JSON structures
✔ Mapping IDs to objects
✔ Building indexes in applications
"""


# ---------------------------------------------------------------------------
# 12. Best Practices for Professional Python
# ---------------------------------------------------------------------------
"""
✔ Use .get() when a key may not exist
✔ Use descriptive key names
✔ Use dictionary comprehensions when building dicts from loops
✔ Prefer nested dictionaries for structured data
✔ Use .items() when looping over key-value pairs
✔ Remember dictionaries are unordered before Python 3.7 (now ordered)
"""


# ---------------------------------------------------------------------------
# 13. Summary
# ---------------------------------------------------------------------------
"""
In this module I learned:

- What dictionaries are and why they are powerful
- How to access, add, update, and delete keys
- How to loop through dictionaries
- How to use .get() safely
- How to use dictionary comprehensions
- How to work with nested dictionaries
- How to merge dictionaries

Next:
    Run Dictionaries_Examples.py for practical demonstrations.
    Complete tasks in Dictionaries_Tasks.py.
"""
