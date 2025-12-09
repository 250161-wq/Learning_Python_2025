"""
Module 5 — Lists & Tuples: Notes & Explanations
-----------------------------------------------

Lists and tuples are two of the MOST important data structures in Python.
They allow us to store collections of items and work with sequences of data.

KEY DIFFERENCE:
- Lists  -> Mutable (you can change them)
- Tuples -> Immutable (you cannot change them)

This module explains how to use both effectively and professionally.
"""


# ---------------------------------------------------------------------------
# 1. What is a List?
# ---------------------------------------------------------------------------
"""
A list is an ordered, mutable collection of items.

Examples:
    numbers = [10, 20, 30]
    mixed   = [1, "hello", 3.14, True]

Lists allow:
- Changing values
- Adding items
- Removing items
- Sorting
- Iterating easily
"""

numbers = [10, 20, 30]
mixed = [1, "hello", 3.14, True]


# ---------------------------------------------------------------------------
# 2. Indexing and Slicing Lists
# ---------------------------------------------------------------------------
"""
INDEXING:
    list[index]

Example:
    fruits = ["apple", "banana", "cherry"]
    fruits[0] -> "apple"
    fruits[1] -> "banana"
    fruits[-1] -> "cherry"   (negative indexing)

SLICING:
    list[start:end]
    list[start:end:step]

Examples:
    fruits[0:2]  -> ["apple", "banana"]
    fruits[:2]   -> ["apple", "banana"]
    fruits[1:]   -> ["banana", "cherry"]
"""

fruits = ["apple", "banana", "cherry"]


# ---------------------------------------------------------------------------
# 3. Modifying Lists (Mutability)
# ---------------------------------------------------------------------------
"""
Lists are MUTABLE — their elements can be changed.

Examples:
    nums = [1, 2, 3]
    nums[1] = 100        -> [1, 100, 3]
    nums.append(4)       -> [1, 100, 3, 4]
    nums.insert(0, 9)    -> [9, 1, 100, 3, 4]
    nums.pop()           -> removes last element
    nums.remove(100)     -> removes first matching value
"""

nums = [1, 2, 3]
nums[1] = 100   # Modify element
nums.append(4)  # Add at end


# ---------------------------------------------------------------------------
# 4. Common List Methods (Professional Must-Know)
# ---------------------------------------------------------------------------
"""
append(x)        -> Add to the end
extend(list)     -> Add all items from another list
insert(i, x)     -> Insert at index i
pop(i)           -> Remove and return item at index i
remove(x)        -> Remove first occurrence of x
sort()           -> Sort list in place
sorted(list)     -> Return a sorted copy (does NOT modify original)
reverse()        -> Reverse list in place
count(x)         -> How many times x appears
index(x)         -> Index of first occurrence of x
"""


# ---------------------------------------------------------------------------
# 5. Loops with Lists
# ---------------------------------------------------------------------------
"""
Iterating over a list is extremely common:

Example:
    for fruit in fruits:
        print(fruit)

Using index:
    for i in range(len(fruits)):
        print(i, fruits[i])
"""


# ---------------------------------------------------------------------------
# 6. List Comprehensions (Professional Technique)
# ---------------------------------------------------------------------------
"""
A list comprehension is a compact way to build lists.

Example:
    squares = [x*x for x in range(5)]
    -> [0, 1, 4, 9, 16]

Filtering example:
    evens = [n for n in nums if n % 2 == 0]
"""

squares = [x * x for x in range(5)]
evens = [n for n in range(10) if n % 2 == 0]


# ---------------------------------------------------------------------------
# 7. What is a Tuple?
# ---------------------------------------------------------------------------
"""
A tuple is an ordered, IMMUTABLE sequence of items.

Examples:
    point = (10, 20)
    data  = (1, "hello", True)

Why tuples?
- Safer when you do not want data changed
- Faster than lists
- Used in many return values
- Used as keys in dictionaries (immutable!)
"""

point = (10, 20)
person = ("Peyman", 43, "Mexico")


# ---------------------------------------------------------------------------
# 8. Tuple Indexing and Slicing
# ---------------------------------------------------------------------------
"""
Tuples work like lists for indexing/slicing:

    t[0], t[-1], t[1:3]

BUT you cannot modify them:
    t[0] = 99  -> ERROR
"""


# ---------------------------------------------------------------------------
# 9. Tuple Packing & Unpacking
# ---------------------------------------------------------------------------
"""
Packing:
    p = 10, 20   # parentheses optional

Unpacking:
    x, y = p

Advanced unpacking:
    a, b, *rest = [1, 2, 3, 4, 5]
    -> a = 1, b = 2, rest = [3, 4, 5]
"""


# ---------------------------------------------------------------------------
# 10. Converting Between Lists and Tuples
# ---------------------------------------------------------------------------
"""
Convert list -> tuple:
    tuple(list)

Convert tuple -> list:
    list(tuple)

This is useful when you want:
- temporary mutability
- or temporary immutability
"""

tuple_from_list = tuple([1, 2, 3])
list_from_tuple = list((10, 20, 30))


# ---------------------------------------------------------------------------
# 11. Nested Lists & Tuples
# ---------------------------------------------------------------------------
"""
Python allows lists inside lists, tuples inside lists, etc.

Examples:
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    coordinates = ((10, 20), (30, 40))
"""


# ---------------------------------------------------------------------------
# 12. Professional Best Practices
# ---------------------------------------------------------------------------
"""
✔ Use lists when you expect to modify or reorder items  
✔ Use tuples for fixed collections or when you want immutability  
✔ Prefer list comprehensions over long loops when building lists  
✔ Use slicing for clarity and compactness  
✔ NEVER rely on list indexes if the list can change unexpectedly  
✔ Use unpacking to write cleaner, clearer code  
"""


# ---------------------------------------------------------------------------
# 13. Summary
# ---------------------------------------------------------------------------
"""
In this module I learned:

- Core differences between lists and tuples  
- Indexing, slicing, mutability  
- Adding, inserting, removing, sorting items  
- Iteration techniques  
- List comprehensions  
- Tuple packing/unpacking  
- Conversions between lists and tuples  
- Best practices used by real developers  

Next:
- Run Lists_Tuples_Examples.py for demonstrations  
- Complete Lists_Tuples_Tasks.py to build skill  
"""
