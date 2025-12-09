"""
Module 40 — id() Values: Practice Exercises
Comprehensive practice with Python’s id() function, from beginner
to more professional, production-style usage.

In this module I:
- Understand what id() represents in CPython (memory address surrogate).
- Compare identity vs equality.
- Track object identity during mutations.
- Observe interning behavior for small integers and short strings.
- Analyze identity behavior in lists, functions, and custom objects.
- Build a small identity-tracker utility for professional debugging.

Ranking system:
- Rank 1  -> Beginner: what id() is and simple checks.
- Rank 2  -> Easy: identity vs equality.
- Rank 3  -> Intermediate: mutability and id() before/after modification.
- Rank 4  -> Advanced: interning behavior (ints, strings, tuples).
- Rank 5  -> Professional: identity tracking system for debugging memory flow.

Author: Peyman Miyandashti
Date of Birth: 11/11/1983
ID Number: 250161
Year: 2025
"""

from __future__ import annotations
from typing import Any, Dict, List


# ===========================================================
# Rank 1 — Beginner
# What id() represents
# ===========================================================

print("Rank 1 — Beginner")

a = 10
b = 10
c = 999999

print("id(a):", id(a))
print("id(b):", id(b))  # likely same (small int interning)
print("id(c):", id(c))

text = "hello"
print("id(text):", id(text))

my_list = [1, 2, 3]
print("id(my_list):", id(my_list))

print("-" * 50)


# ===========================================================
# Rank 2 — Easy
# Identity (is) vs Equality (==)
# ===========================================================

print("Rank 2 — Easy")

x = [1, 2, 3]
y = [1, 2, 3]

print("x == y:", x == y)     # same content
print("x is y:", x is y)     # not same object
print("id(x):", id(x))
print("id(y):", id(y))

# Another example: same string literal shares memory
s1 = "Peyman"
s2 = "Peyman"
print("s1 is s2:", s1 is s2)

print("-" * 50)


# ===========================================================
# Rank 3 — Intermediate
# Mutability and id() changes (or not)
# ===========================================================

print("Rank 3 — Intermediate")

lst = [1, 2, 3]
print("Original id(lst):", id(lst))

lst.append(4)
print("After append id(lst):", id(lst))  # SAME id

lst2 = lst + [5]
print("lst2 (new list) id:", id(lst2))   # new object

# Immutable type: replacement creates new identity
name = "Pey"
print("id(name):", id(name))
name += "man"
print("id(name after +=):", id(name))  # new object

print("-" * 50)


# ===========================================================
# Rank 4 — Advanced
# Interning behavior: integers, strings, tuples
# ===========================================================

print("Rank 4 — Advanced")

# Small integers [-5..256] often share identity
i1 = 256
i2 = 256
print("i1 is i2:", i1 is i2)

i3 = 257
i4 = 257
print("i3 is i4:", i3 is i4)  # Usually False — not interned

# String interning
sA = "hello_world"
sB = "hello_world"
print("sA is sB:", sA is sB)

# Dynamic strings usually NOT interned
sC = "".join(["hello", "_world"])
print("sA is sC:", sA is sC)

# Tuples of small interned items
t1 = (1, 2, 3)
t2 = (1, 2, 3)
print("t1 is t2:", t1 is t2)

print("-" * 50)


# ===========================================================
# Rank 5 — Professional
# Identity Tracker utility for debugging
# ===========================================================

print("Rank 5 — Professional")

class IdentityTracker:
    """
    Tracks id() values for objects and shows whether
    they mutated in-place or were replaced.
    """

    def __init__(self) -> None:
        self._ids: Dict[str, int] = {}

    def watch(self, label: str, obj: Any) -> None:
        """
        Register or compare an object under a label.
        """
        new_id = id(obj)
        old_id = self._ids.get(label)

        if old_id is None:
            print(f"[TRACK] {label}: id={new_id} (initial)")
        else:
            if old_id == new_id:
                print(f"[TRACK] {label}: SAME id={new_id} (mutated in-place)")
            else:
                print(f"[TRACK] {label}: CHANGED id={old_id} -> {new_id} (new object)")

        self._ids[label] = new_id


# Example usage
tracker = IdentityTracker()

data = [10, 20, 30]
tracker.watch("data", data)

# Modify in-place → id does not change
data.append(40)
tracker.watch("data", data)

# Reassign → id changes
data = data + [50]
tracker.watch("data", data)

# Immutable example
value = "Hello"
tracker.watch("value", value)
value += " World"
tracker.watch("value", value)

print("-" * 50)
