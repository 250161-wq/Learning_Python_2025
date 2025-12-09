"""
Module 14 — Frozenset
Professional Notes

This file explains Python's frozenset type: an immutable version of the set.
A frozenset contains unique, unordered elements, but unlike a normal set,
it cannot be modified after creation.

Because frozensets are immutable, they are hashable and can be used in
contexts where sets cannot be used — such as dictionary keys or elements
of another set.
"""

# ---------------------------------------------------------------------------
# 1. What Is a Frozenset?
# ---------------------------------------------------------------------------
# A frozenset is similar to a regular set:
# - Stores unique elements
# - Is unordered (no indexes)
# - Supports set operations (union, intersection, difference, etc.)
#
# Difference:
# - A normal set is mutable (it can change)
# - A frozenset is immutable (it cannot change)
#
# Create a frozenset using:
#     frozenset(iterable)

fs = frozenset([1, 2, 3])
print("Frozenset:", fs)


# ---------------------------------------------------------------------------
# 2. Why Use a Frozenset?
# ---------------------------------------------------------------------------
# Because it is immutable, a frozenset:
# ✔ Can be used as a dictionary key
# ✔ Can be added to another set
# ✔ Provides safety when you want to protect data from modification
#
# A normal set cannot do these things since it is mutable.


# ---------------------------------------------------------------------------
# 3. Creating Frozensets
# ---------------------------------------------------------------------------
# From a list:
fs1 = frozenset([1, 2, 3])

# From a set:
fs2 = frozenset({3, 4, 5})

# From a string (characters become elements):
fs3 = frozenset("hello")

print(fs1)
print(fs2)
print(fs3)


# ---------------------------------------------------------------------------
# 4. Allowed Operations
# ---------------------------------------------------------------------------
# Frozensets support all NON-mutating set operations:
#
# - union()
# - intersection()
# - difference()
# - symmetric_difference()
# - issubset()
# - issuperset()
# - isdisjoint()
#
# Example:
a = frozenset([1, 2, 3])
b = frozenset([3, 4])

print(a.union(b))          # frozenset({1, 2, 3, 4})
print(a.intersection(b))   # frozenset({3})
print(a.difference(b))     # frozenset({1, 2})


# ---------------------------------------------------------------------------
# 5. Operations NOT Allowed
# ---------------------------------------------------------------------------
# Since frozensets cannot change, the following operations DO NOT exist:
#
# - add()
# - remove()
# - discard()
# - update()
# - pop()
#
# Example (would produce an error):
#
# fs = frozenset([1, 2, 3])
# fs.add(4)     ❌ ERROR — cannot modify


# ---------------------------------------------------------------------------
# 6. Frozenset as Dictionary Keys
# ---------------------------------------------------------------------------
# Because frozensets are hashable, they can be used as dict keys.

grades = {
    frozenset(["math", "physics"]): "science track",
    frozenset(["art", "design"]): "arts track",
}

key = frozenset(["math", "physics"])
print(grades[key])  # "science track"


# ---------------------------------------------------------------------------
# 7. Frozensets Inside Sets
# ---------------------------------------------------------------------------
# Normal sets cannot contain other sets (because they are mutable).
# But they CAN contain frozensets.

combo = {frozenset([1, 2]), frozenset([3, 4])}
print(combo)


# ---------------------------------------------------------------------------
# 8. Real Use Cases
# ---------------------------------------------------------------------------
# Frozensets are useful when:
# - You want to prevent accidental modification of a collection
# - You need to use a set as a dictionary key
# - You need a set inside another set
# - You want safe, hashable, immutable data structures
#
# Common scenarios include:
# - caching
# - graph algorithms
# - grouping unique combinations
# - storing configuration values


# ---------------------------------------------------------------------------
# 9. Common Mistakes
# ---------------------------------------------------------------------------
# ❌ Trying to modify a frozenset:
#       fs.add(5)
#
# ❌ Expecting elements to be ordered
#
# ❌ Thinking a frozenset is faster than a set
#     (It is not faster; it is only immutable)
#
# ✔ Correct mindset:
#     "Use frozenset when immutability or hashability is required."


# ---------------------------------------------------------------------------
# 10. Summary
# ---------------------------------------------------------------------------
# In this module, I learned:
# - The difference between set and frozenset
# - How to create frozensets
# - Which operations are allowed and which are not
# - How immutability enables frozensets to be used as dictionary keys
# - Practical real-world use cases
#
# End of Notes
