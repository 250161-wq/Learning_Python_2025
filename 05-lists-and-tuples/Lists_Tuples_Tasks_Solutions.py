"""
Module 5 — Lists & Tuples: Task Solutions
-----------------------------------------

This file contains complete, professional solutions for all exercises
found in `Lists_Tuples_Tasks.py`. Solutions are written cleanly and
intentionally to demonstrate best practices in sequence handling,
list comprehensions, tuple operations, and general Pythonic techniques.
"""


# =============================================================================
# Rank 1 — Beginner
# =============================================================================

def create_number_list():
    """Return a simple list of five integers."""
    return [10, 20, 30, 40, 50]


def first_and_last(elements):
    """Return a tuple containing the first and last elements of a list."""
    return (elements[0], elements[-1])


def create_color_tuple():
    """Return a tuple of three colors."""
    return ("red", "green", "blue")


# =============================================================================
# Rank 2 — Easy
# =============================================================================

def append_item(shopping_list, item):
    """Append an item to a shopping list and return it."""
    shopping_list.append(item)
    return shopping_list


def list_to_tuple(values):
    """Convert a list to a tuple."""
    return tuple(values)


def tuple_to_list(values):
    """Convert a tuple to a list."""
    return list(values)


# =============================================================================
# Rank 3 — Intermediate
# =============================================================================

def get_middle_slice(numbers):
    """Return all elements except the first and last; requires >= 3 elements."""
    if len(numbers) < 3:
        return []
    return numbers[1:-1]


def remove_all_occurrences(values, target):
    """Return a new list with all occurrences of target removed."""
    return [v for v in values if v != target]


def count_unique_items(values):
    """Count distinct elements in the list."""
    return len(set(values))


# =============================================================================
# Rank 4 — Advanced
# =============================================================================

def pair_names_and_ages(names, ages):
    """Pair names and ages using zip and return a list of tuples."""
    return [(n, a) for n, a in zip(names, ages)]


def flatten_2d_list(matrix):
    """Flatten a 2D list into a single list."""
    return [x for row in matrix for x in row]


def filter_even_numbers(numbers):
    """Return a new list containing only the even numbers."""
    return [n for n in numbers if n % 2 == 0]


# =============================================================================
# Rank 5 — Professional
# =============================================================================

def group_students_by_score(students):
    """
    Group students into low, medium, and high performance categories.
    """
    groups = {"low": [], "medium": [], "high": []}

    for name, score in students:
        if score < 60:
            groups["low"].append(name)
        elif score < 80:
            groups["medium"].append(name)
        else:
            groups["high"].append(name)

    return groups


def deduplicate_preserve_order(items):
    """
    Remove duplicates while preserving order of first appearance.
    """
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def sort_by_second_element(pairs):
    """
    Sort a list of (x, y) tuples by the second element y.
    """
    return sorted(pairs, key=lambda t: t[1])


def find_products_in_price_range(products, min_price, max_price):
    """
    Return products whose price is within the given range (inclusive).
    """
    return [
        (name, price)
        for name, price in products
        if min_price <= price <= max_price
    ]


# =============================================================================
# Optional Manual Testing
# =============================================================================

if __name__ == "__main__":
    # Simple self-tests (optional)
    print(create_number_list())
    print(first_and_last([5, 10, 20]))
    print(create_color_tuple())

    print(append_item(["milk"], "bread"))
    print(list_to_tuple([1, 2, 3]))
    print(tuple_to_list((4, 5, 6)))

    print(get_middle_slice([1, 2, 3, 4]))
    print(remove_all_occurrences([1, 2, 2, 3], 2))
    print(count_unique_items([1, 1, 2, 3, 3, 3]))

    print(pair_names_and_ages(["Alice", "Bob"], [30, 25]))
    print(flatten_2d_list([[1, 2], [3, 4]]))
    print(filter_even_numbers([1, 2, 3, 4, 5, 6]))

    print(
        group_students_by_score(
            [("Alice", 90), ("Bob", 70), ("Charlie", 50)]
        )
    )

    print(deduplicate_preserve_order([1, 2, 1, 3, 2, 4]))
    print(sort_by_second_element([("a", 3), ("b", 1), ("c", 2)]))

    print(
        find_products_in_price_range(
            [
                ("Keyboard", 50),
                ("Monitor", 150),
                ("Mouse", 25),
            ],
            30,
            150,
        )
    )
