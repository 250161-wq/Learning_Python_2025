"""
Module 7 — Sets: Notes & Explanations
-------------------------------------

A set is an **unordered**, **mutable**, **unique-collection** of items.

Key characteristics:
- NO duplicates
- Very fast membership checks:  x in my_set
- Unordered (no indexing)
- Supports mathematical operations:
    - union
    - intersection
    - difference
    - symmetric difference

Sets are extremely useful for:
- Removing duplicates from lists
- Comparing groups of values
- Fast lookups
- Working with large datasets efficiently
"""


# ---------------------------------------------------------------------------
# 1. Creating Sets
# ---------------------------------------------------------------------------
"""
Sets are created using curly braces {} or the set() constructor.

Examples:
    s1 = {1, 2, 3}
    s2 = set([1, 2, 2, 3])   -> {1, 2, 3}

Important:
- Duplicate values are automatically removed.
"""

s1 = {1, 2, 3}
s2 = set([1, 2, 2, 3])     # duplicates removed → {1, 2, 3}


# ---------------------------------------------------------------------------
# 2. Adding and Removing Items
# ---------------------------------------------------------------------------
"""
Sets are mutable — I can add or remove items:

    s.add(value)
    s.remove(value)        # Raises KeyError if missing
    s.discard(value)       # Safe removal (no error)
    s.pop()                # Removes a random item
    s.clear()              # Removes all items
"""

colors = {"red", "blue"}
colors.add("green")
colors.discard("red")


# ---------------------------------------------------------------------------
# 3. Membership Testing (FAST!)
# ---------------------------------------------------------------------------
"""
Set membership checks are much faster than lists.

Example:
    "apple" in fruits_set
"""

fruits = {"apple", "banana", "cherry"}
test = "banana" in fruits      # True


# ---------------------------------------------------------------------------
# 4. Set Operations (VERY IMPORTANT)
# ---------------------------------------------------------------------------
"""
Sets support mathematical operations that return NEW sets.

Union (all unique items):
    a | b
    a.union(b)

Intersection (items present in both):
    a & b
    a.intersection(b)

Difference (items in a but NOT in b):
    a - b
    a.difference(b)

Symmetric difference (items NOT shared):
    a ^ b
    a.symmetric_difference(b)
"""

a = {1, 2, 3}
b = {3, 4, 5}

union_result = a | b          # {1, 2, 3, 4, 5}
intersection_result = a & b   # {3}
difference_result = a - b     # {1, 2}
sym_diff_result = a ^ b       # {1, 2, 4, 5}


# ---------------------------------------------------------------------------
# 5. Removing Duplicates Using Sets
# ---------------------------------------------------------------------------
"""
Using a set is one of the fastest ways to remove duplicates from a list:

    unique = list(set([1, 2, 2, 3]))
"""

unique_numbers = list(set([1, 2, 2, 3, 3, 4]))   # → [1, 2, 3, 4]


# ---------------------------------------------------------------------------
# 6. Converting Between Lists and Sets
# ---------------------------------------------------------------------------
"""
Convert list → set:
    set([1, 2, 3])

Convert set → list:
    list(my_set)

Useful when:
- I want to remove duplicates
- I need fast membership checking
"""

numbers = [1, 2, 2, 3]
numbers_set = set(numbers)
back_to_list = list(numbers_set)


# ---------------------------------------------------------------------------
# 7. Comparing Sets
# ---------------------------------------------------------------------------
"""
Set comparisons:

Subset:
    a <= b   (a is subset of b)
Superset:
    a >= b   (a is superset of b)
Disjoint:
    a.isdisjoint(b)

Examples:
"""

x = {1, 2}
y = {1, 2, 3}

is_subset = x <= y          # True
is_superset = y >= x        # True
are_disjoint = x.isdisjoint({4, 5})   # True


# ---------------------------------------------------------------------------
# 8. Typical Use Cases in Real Projects
# ---------------------------------------------------------------------------
"""
✔ Removing duplicates from user data  
✔ Finding common elements between lists  
✔ Fast permission checks (e.g., allowed_roles)  
✔ Comparing datasets  
✔ Ensuring unique items (e.g., unique tags, IDs)  
✔ Detecting differences between two datasets  
"""


# ---------------------------------------------------------------------------
# 9. Best Practices
# ---------------------------------------------------------------------------
"""
✔ Use sets when you require uniqueness  
✔ Use sets when you need fast membership checking  
✔ Use set operations for clear, readable logic  
✔ Convert to list if you need ordering  
✔ Avoid indexing (sets do not maintain order)  
✔ Prefer .discard() over .remove() to avoid KeyError  
"""


# ---------------------------------------------------------------------------
# 10. Summary
# ---------------------------------------------------------------------------
"""
In this module I learned:

- What sets are and how they work
- How to add, remove, and check items
- How to use union, intersection, difference, and symmetric difference
- How to remove duplicates easily
- How to compare sets (subset, superset, disjoint)
- When to choose sets over lists

Next:
    Run Sets_Examples.py for practical demonstrations.
    Solve Sets_Tasks.py to build real skill.
"""
