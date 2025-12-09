"""
Module 5 — Lists & Tuples: Practice Exercises
Structured practice on Python's list and tuple types, from beginner to
more professional, production-style usage.

In this module I:
- Create, read, update, and delete elements from lists.
- Use common list operations: indexing, slicing, appending, inserting,
  removing, sorting, and copying.
- Understand tuples as ordered, immutable sequences.
- Use tuples for fixed structures (coordinates, records, return values).
- Practice iterating over lists and tuples in clean, readable ways.
- Work up from simple list/tuple tasks (Rank 1) to more realistic,
  professional-style use cases (Rank 5).

Ranking system:
- Rank 1  -> Beginner: very basic syntax and concepts.
- Rank 2  -> Easy: still simple, but combining two or more concepts.
- Rank 3  -> Intermediate: more operations in a single example.
- Rank 4  -> Advanced: more realistic, closer to real projects.
- Rank 5  -> Professional: cleaner design, better structure, and
             more “real-world” style tasks.

⚠️ Important:
- This file is for **my own practice**.
- I should try to implement each task on my own before checking the
  corresponding solutions in `Lists_Tuples_Tasks_Solutions.py`.
- I do NOT need to finish all tasks in one session. I can gradually
  move from lower ranks to higher ranks as I feel more confident.
"""

# =============================================================================
# Rank 1 — Beginner
# Very basic list and tuple creation and reading values.
# =============================================================================


def create_number_list():
    """
    Task:
        Return a list containing at least five integer numbers of my choice.

    Requirements:
        - The return value MUST be a list of integers.
        - I can choose any integers (e.g., [1, 2, 3, 4, 5]).

    Return:
        list[int]: A list of at least 5 integers.
    """
    # TODO: Replace [] with a list of at least five integers.
    return []


def first_and_last(elements):
    """
    Task:
        Given a list called `elements`, return a tuple with:
        - The first element
        - The last element

    Requirements:
        - Assume `elements` has at least 1 element.
        - Use list indexing to access the first and last elements.

    Example:
        first_and_last([10, 20, 30]) -> (10, 30)

    Args:
        elements (list): A non-empty list.

    Return:
        tuple: A tuple containing (first_element, last_element).
    """
    # TODO: Implement using indexing.
    return (None, None)


def create_color_tuple():
    """
    Task:
        Create and return a tuple of at least three color names
        (as strings), for example: ("red", "green", "blue").

    Requirements:
        - The return value MUST be a tuple.
        - All elements should be strings.

    Return:
        tuple[str, ...]: A tuple of color names.
    """
    # TODO: Replace () with a tuple of at least three color strings.
    return ()


# =============================================================================
# Rank 2 — Easy
# Simple operations with indexing, appending, and basic conversions.
# =============================================================================


def append_item(shopping_list, item):
    """
    Task:
        Add the given `item` to the end of `shopping_list` and return
        the updated list.

    Requirements:
        - Modify the list by appending the item.
        - Return the same list after modification.

    Example:
        append_item(["milk"], "bread") -> ["milk", "bread"]

    Args:
        shopping_list (list): A list of items (strings).
        item (str): A new item to add.

    Return:
        list: The updated list including the new item.
    """
    # TODO: Use list.append(...) and then return the list.
    return shopping_list


def list_to_tuple(values):
    """
    Task:
        Convert a list called `values` to a tuple and return the tuple.

    Requirements:
        - Do NOT modify the original list.
        - Use the built-in `tuple()` constructor.

    Example:
        list_to_tuple([1, 2, 3]) -> (1, 2, 3)

    Args:
        values (list): Any list.

    Return:
        tuple: A tuple containing the same elements as `values`.
    """
    # TODO: Return tuple(values)
    return ()


def tuple_to_list(values):
    """
    Task:
        Convert a tuple called `values` to a list and return the list.

    Requirements:
        - Do NOT modify the original tuple.
        - Use the built-in `list()` constructor.

    Example:
        tuple_to_list((1, 2, 3)) -> [1, 2, 3]

    Args:
        values (tuple): Any tuple.

    Return:
        list: A list containing the same elements as `values`.
    """
    # TODO: Return list(values)
    return []


# =============================================================================
# Rank 3 — Intermediate
# Slicing, searching, removing, counting, and simple transformations.
# =============================================================================


def get_middle_slice(numbers):
    """
    Task:
        Given a list of numbers, return a new list that contains all
        elements except the first and the last.

    Requirements:
        - Use list slicing.
        - If the list has fewer than 3 elements, return an empty list.

    Examples:
        get_middle_slice([1, 2, 3, 4]) -> [2, 3]
        get_middle_slice([10, 20]) -> []

    Args:
        numbers (list[int | float]): List of numeric values.

    Return:
        list: A new list containing all elements except the first & last.
    """
    # TODO: Implement using slicing.
    return []


def remove_all_occurrences(values, target):
    """
    Task:
        Return a NEW list where all occurrences of `target`
        are removed from the original `values` list.

    Requirements:
        - Do NOT modify the original list in-place.
        - Create a new list that excludes all elements equal to `target`.
        - Use a loop or a list comprehension.

    Example:
        remove_all_occurrences([1, 2, 2, 3], 2) -> [1, 3]

    Args:
        values (list): List with any type of elements.
        target: Value to remove from the list.

    Return:
        list: A new list without any elements equal to `target`.
    """
    # TODO: Build a new list without the target.
    return []


def count_unique_items(values):
    """
    Task:
        Count how many unique items exist in the list `values`.

    Requirements:
        - Two items are considered the same if they are `==`.
        - You may use a `set` or any other approach.
        - Return an integer representing the number of distinct elements.

    Example:
        count_unique_items([1, 1, 2, 3]) -> 3

    Args:
        values (list): List of hashable elements.

    Return:
        int: Number of unique elements in the list.
    """
    # TODO: Implement using set(...) or another method.
    return 0


# =============================================================================
# Rank 4 — Advanced
# Working with nested lists/tuples and combined structures.
# =============================================================================


def pair_names_and_ages(names, ages):
    """
    Task:
        Given a list of names and a list of ages (same length),
        create a list of (name, age) tuples.

    Requirements:
        - Use the built-in `zip()` function.
        - Each element in the result should be a tuple: (name, age).
        - If `names` and `ages` have different lengths, only pair until
          the shortest list ends (this is how `zip()` behaves).

    Example:
        pair_names_and_ages(["Alice", "Bob"], [30, 25])
            -> [("Alice", 30), ("Bob", 25)]

    Args:
        names (list[str]): List of names.
        ages (list[int]): List of ages.

    Return:
        list[tuple[str, int]]: List of (name, age) tuples.
    """
    # TODO: Use zip(...) and build a list of tuples.
    return []


def flatten_2d_list(matrix):
    """
    Task:
        Given a 2D list `matrix` (a list of lists), flatten it into
        a single list containing all the inner elements in order.

    Requirements:
        - Use nested loops OR a list comprehension.
        - Assume each element of `matrix` is itself a list.

    Example:
        flatten_2d_list([[1, 2], [3, 4]]) -> [1, 2, 3, 4]

    Args:
        matrix (list[list]): 2D list.

    Return:
        list: A flattened list with all inner elements.
    """
    # TODO: Implement flattening logic.
    return []


def filter_even_numbers(numbers):
    """
    Task:
        From a list of integers `numbers`, return a NEW list containing
        only the even numbers.

    Requirements:
        - Do NOT modify the original list.
        - Use a loop or a list comprehension.
        - Even number condition: number % 2 == 0.

    Example:
        filter_even_numbers([1, 2, 3, 4]) -> [2, 4]

    Args:
        numbers (list[int]): List of integers.

    Return:
        list[int]: New list with only even integers.
    """
    # TODO: Filter even numbers.
    return []


# =============================================================================
# Rank 5 — Professional
# More realistic, “production-style” tasks using lists and tuples.
# =============================================================================


def group_students_by_score(students):
    """
    Task:
        Given a list of (name, score) tuples, group students into three
        categories based on their score:

        - "low"    : score < 60
        - "medium" : 60 <= score < 80
        - "high"   : score >= 80

        Return a dictionary with keys "low", "medium", "high",
        and each value is a list of student names in that category.

    Requirements:
        - Input: list[tuple[str, int | float]]
        - Output: dict[str, list[str]]
        - Ensure every key ("low", "medium", "high") exists in the result,
          even if its list is empty.

    Example:
        students = [("Alice", 90), ("Bob", 70), ("Charlie", 50)]
        group_students_by_score(students) ->
            {
                "low": ["Charlie"],
                "medium": ["Bob"],
                "high": ["Alice"]
            }

    Args:
        students (list[tuple[str, int | float]]):
            Tuples of (student_name, score).

    Return:
        dict[str, list[str]]: Grouped student names by score range.
    """
    # TODO: Implement grouping logic using lists and tuples.
    return {
        "low": [],
        "medium": [],
        "high": [],
    }


def deduplicate_preserve_order(items):
    """
    Task:
        Remove duplicate elements from the list `items` while preserving
        the original order of the first occurrence of each element.

    Requirements:
        - Return a NEW list with duplicates removed.
        - Preserve the order of first appearances.
        - Do NOT use any external libraries.

    Example:
        deduplicate_preserve_order([1, 2, 1, 3, 2]) -> [1, 2, 3]

    Args:
        items (list): List with possible duplicates.

    Return:
        list: New list with duplicates removed, order preserved.
    """
    # TODO: Track seen elements and build a new list.
    return []


def sort_by_second_element(pairs):
    """
    Task:
        Given a list of 2-element tuples `pairs`, return a NEW list
        sorted by the second element in each tuple.

    Requirements:
        - Do NOT modify the original list.
        - Use the built-in `sorted()` function.
        - Use a `key` function or `lambda` to access the second element.

    Example:
        sort_by_second_element([("a", 3), ("b", 1), ("c", 2)])
            -> [("b", 1), ("c", 2), ("a", 3)]

    Args:
        pairs (list[tuple]):
            Each element is expected to be a 2-element tuple.

    Return:
        list[tuple]: New list sorted by the second element.
    """
    # TODO: Use sorted(pairs, key=...)
    return []


def find_products_in_price_range(products, min_price, max_price):
    """
    Task:
        Given a list of product tuples and a price range, return a NEW
        list with products whose price is within the range (inclusive).

        Each product is represented as a tuple:
            (product_name, price)

    Requirements:
        - Include products where min_price <= price <= max_price.
        - Do NOT modify the original list.
        - Use a loop or a list comprehension.

    Example:
        products = [
            ("Keyboard", 50),
            ("Monitor", 150),
            ("Mouse", 25),
        ]
        find_products_in_price_range(products, 30, 150) ->
            [("Keyboard", 50), ("Monitor", 150)]

    Args:
        products (list[tuple[str, int | float]]): Product tuples.
        min_price (int | float): Minimum price (inclusive).
        max_price (int | float): Maximum price (inclusive).

    Return:
        list[tuple[str, int | float]]:
            New list of products in the specified price range.
    """
    # TODO: Filter products based on the given price range.
    return []


if __name__ == "__main__":
    # Optional: I can use this block to do quick manual tests
    # while I am working through the tasks.
    pass
