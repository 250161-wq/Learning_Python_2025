"""
Module 14 — Frozenset
Practice Task Solutions

This file contains clear, professional solutions to all exercises in
Frozenset_Tasks.py. These solutions demonstrate correct frozenset usage,
immutability rules, and real-world patterns.

Only review these solutions after attempting the tasks yourself.
"""

# ---------------------------------------------------------------------------
# Rank 1 — Beginner
# ---------------------------------------------------------------------------

# Task 1.1
fs = frozenset([1, 2, 3])
print(fs)

# Task 1.2
items = ["a", "b", "a", "c"]
fs_items = frozenset(items)
print(fs_items)

# Task 1.3
fs = frozenset([10, 20, 30])
print(20 in fs)


# ---------------------------------------------------------------------------
# Rank 2 — Easy
# ---------------------------------------------------------------------------

# Task 2.1
a = frozenset([1, 2, 3])
b = frozenset([3, 4])
print(a.union(b))

# Task 2.2
fs1 = frozenset([5, 6, 7])
fs2 = frozenset([7, 8, 9])
print(fs1.intersection(fs2))

# Task 2.3
fsA = frozenset([1, 2, 3, 4])
fsB = frozenset([3, 4])
print(fsA.difference(fsB))


# ---------------------------------------------------------------------------
# Rank 3 — Intermediate
# ---------------------------------------------------------------------------

# Task 3.1
d = {
    frozenset(["red", "blue"]): "primary mix"
}
print(d[frozenset(["red", "blue"])])

# Task 3.2
set_of_sets = {frozenset([1, 2]), frozenset([3, 4])}
print(set_of_sets)

# Task 3.3
item1 = ["sugar", "flour"]
item2 = ["flour", "sugar"]
item3 = ["milk", "chocolate"]

unique = {frozenset(item1), frozenset(item2), frozenset(item3)}
print(unique)


# ---------------------------------------------------------------------------
# Rank 4 — Advanced
# ---------------------------------------------------------------------------

# Task 4.1
allowed_settings = frozenset(["dark_mode", "notifications", "auto_save"])
setting = "auto_save"

if setting in allowed_settings:
    print("Setting is allowed.")
else:
    print("Invalid setting.")

# Task 4.2
# fs = frozenset([1, 2, 3])
# fs.add(4)  # ❌ ERROR — frozensets are immutable and do not allow modification.

# Task 4.3
A = frozenset([1, 2, 3])
B = frozenset([2, 3, 4])

print("Union:", A.union(B))
print("Symmetric difference:", A.symmetric_difference(B))


# ---------------------------------------------------------------------------
# Rank 5 — Professional
# ---------------------------------------------------------------------------

# Task 5.1
cache = {
    frozenset(["page=1", "limit=20"]): "Cached result"
}
key = frozenset(["page=1", "limit=20"])
print(cache[key])

# Task 5.2
allowed_roles = frozenset(["admin", "teacher", "student"])
user_role = "teacher"

if user_role in allowed_roles:
    print("Access granted")
else:
    print("Access denied")

# Task 5.3
values = [1, 2, 3]
pairs = {
    frozenset([values[0], values[1]]),
    frozenset([values[0], values[2]]),
    frozenset([values[1], values[2]]),
}
print(pairs)


# End of Solutions
