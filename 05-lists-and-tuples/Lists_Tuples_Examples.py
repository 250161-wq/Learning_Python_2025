"""
Module 5 — Lists & Tuples: Practical Examples
---------------------------------------------

This file contains runnable examples that demonstrate how to use lists
and tuples in real Python code.

Examples are organized by difficulty (Rank 1–5) and show:
- Indexing and slicing
- List modification
- Common list/tuple methods
- Loops and comprehensions
- Tuple packing/unpacking
- Nested structures
- Professional patterns
"""


# ---------------------------------------------------------------------------
# Rank 1 — Beginner Examples
# ---------------------------------------------------------------------------

def example_1_basic_list():
    """Create and print a basic list."""
    fruits = ["apple", "banana", "cherry"]
    print("Fruits:", fruits)


def example_2_accessing_items():
    """Show accessing list items via indexes."""
    colors = ["red", "green", "blue"]
    print(colors[0])
    print(colors[1])
    print(colors[-1])


def example_3_modify_list():
    """Modify list elements."""
    nums = [1, 2, 3]
    nums[1] = 99
    print("Modified:", nums)


# ---------------------------------------------------------------------------
# Rank 2 — Easy Examples
# ---------------------------------------------------------------------------

def example_4_list_methods():
    """Demonstrate common list methods."""
    items = [10, 20, 30]
    items.append(40)
    items.insert(1, 15)
    items.remove(20)
    print("List methods result:", items)


def example_5_slicing_examples():
    """Examples of list slicing."""
    letters = ["a", "b", "c", "d", "e"]
    print(letters[:3])     # first 3
    print(letters[2:])     # from index 2 onward
    print(letters[1:4])    # slice 1–3
    print(letters[::-1])   # reversed


def example_6_list_comprehensions():
    """Demonstrate list comprehension patterns."""
    squares = [x * x for x in range(5)]
    evens = [x for x in range(10) if x % 2 == 0]
    print("Squares:", squares)
    print("Even numbers:", evens)


# ---------------------------------------------------------------------------
# Rank 3 — Intermediate Examples
# ---------------------------------------------------------------------------

def example_7_filter_positive(nums: list[int]) -> list[int]:
    """Return only positive numbers from a list."""
    return [n for n in nums if n > 0]


def example_8_unpack_tuple():
    """Show tuple unpacking."""
    point = (5, 10)
    x, y = point
    print("X:", x, "Y:", y)


def example_9_nested_structures():
    """Print values from a nested list."""
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    for row in matrix:
        for value in row:
            print(value, end=" ")
    print()


# ---------------------------------------------------------------------------
# Rank 4 — Advanced Examples
# ---------------------------------------------------------------------------

def example_10_sorting_examples():
    """Show sorting lists and using sorted()."""
    nums = [5, 1, 8, 3, 2]
    nums.sort()
    print("Sorted (in place):", nums)

    nums_desc = sorted(nums, reverse=True)
    print("Sorted (new list):", nums_desc)


def example_11_tuple_as_dictionary_key():
    """Use tuples as keys because they are immutable."""
    locations = {
        (32.5, -115.3): "Mexicali",
        (19.4, -99.1): "CDMX",
    }
    print("Location lookup:", locations[(32.5, -115.3)])


def example_12_unpack_rest():
    """Unpack a tuple using *rest syntax."""
    values = (1, 2, 3, 4, 5)
    a, b, *rest = values
    print("a:", a, "b:", b, "rest:", rest)


# ---------------------------------------------------------------------------
# Rank 5 — Professional Examples
# ---------------------------------------------------------------------------

def example_13_clean_list_of_strings(names: list[str]) -> list[str]:
    """
    Clean a list of strings by stripping whitespace and filtering empty values.
    Professional data-cleaning pattern.
    """
    return [name.strip() for name in names if name.strip()]


def example_14_pairwise_sum(nums: list[int]) -> list[int]:
    """
    Create a list where each element is the sum of two consecutive nums.

    nums = [1,2,3,4]
    result = [3,5,7]
    """
    return [nums[i] + nums[i + 1] for i in range(len(nums) - 1)]


def example_15_find_duplicates(values: list[int]) -> tuple[list[int], list[int]]:
    """
    Find duplicates in a list.

    Returns:
        (unique_items, duplicates)
    """
    seen = set()
    duplicates = set()

    for v in values:
        if v in seen:
            duplicates.add(v)
        else:
            seen.add(v)

    return list(seen), list(duplicates)


# ---------------------------------------------------------------------------
# Demonstration section
# ---------------------------------------------------------------------------

def main():
    print("--- Rank 1 ---")
    example_1_basic_list()
    example_2_accessing_items()
    example_3_modify_list()

    print("\n--- Rank 2 ---")
    example_4_list_methods()
    example_5_slicing_examples()
    example_6_list_comprehensions()

    print("\n--- Rank 3 ---")
    print(example_7_filter_positive([-2, 0, 5, 9, -1]))
    example_8_unpack_tuple()
    example_9_nested_structures()

    print("\n--- Rank 4 ---")
    example_10_sorting_examples()
    example_11_tuple_as_dictionary_key()
    example_12_unpack_rest()

    print("\n--- Rank 5 ---")
    print(example_13_clean_list_of_strings(["  Alice ", " ", "Bob"]))
    print(example_14_pairwise_sum([1, 2, 3, 4, 5]))
    print(example_15_find_duplicates([1, 2, 3, 2, 1, 4, 5, 3]))


if __name__ == "__main__":
    main()
