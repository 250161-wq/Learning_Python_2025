"""
Module 3 — Functions: Practice Tasks
------------------------------------

This file contains structured exercises designed to build practical skill
with Python functions. Each task increases in complexity through the
Rank 1 → Rank 5 progression.

I should attempt each task on my own before looking at the
Functions_Tasks_Solutions.py file.

RANKING SYSTEM
- Rank 1 — Beginner: basic function definitions & arguments
- Rank 2 — Easy: simple logic & return values
- Rank 3 — Intermediate: multi-step functions
- Rank 4 — Advanced: problem-solving with reusable functions
- Rank 5 — Professional: clean, production-style patterns
"""


# ---------------------------------------------------------------------------
# Rank 1 — Beginner
# ---------------------------------------------------------------------------

def task_1_basic_greeting() -> None:
    """
    Define a function that prints:
        "Hello, world!"

    Then call the function.
    """
    pass


def task_2_greet_user(name: str) -> None:
    """
    Print:
        "Hello, <name>!"
    Example:
        task_2_greet_user("Peyman") -> Hello, Peyman!
    """
    pass


def task_3_double_number(n: int) -> int:
    """
    Return the double of the number n.
    Example:
        task_3_double_number(4) -> 8
    """
    pass


# ---------------------------------------------------------------------------
# Rank 2 — Easy
# ---------------------------------------------------------------------------

def task_4_full_name(first: str, last: str) -> str:
    """
    Return a formatted full name: "<first> <last>".
    Example:
        task_4_full_name("Peyman", "Miyandashti")
    """
    pass


def task_5_add_three_numbers(a: float, b: float, c: float) -> float:
    """
    Return the sum of a + b + c.
    """
    pass


def task_6_greet_with_default(name: str = "Guest") -> str:
    """
    Return a greeting string.
    Example:
        task_6_greet_with_default() -> "Hello, Guest!"
        task_6_greet_with_default("Peyman") -> "Hello, Peyman!"
    """
    pass


# ---------------------------------------------------------------------------
# Rank 3 — Intermediate
# ---------------------------------------------------------------------------

def task_7_count_even(numbers: list[int]) -> int:
    """
    Return how many even numbers appear in the list.
    Example:
        task_7_count_even([1,2,3,4]) -> 2
    """
    pass


def task_8_calculate_average(values: list[float]) -> float:
    """
    Return the average of the values in the list.
    If the list is empty, return 0.0.
    """
    pass


def task_9_reverse_string(text: str) -> str:
    """
    Return the reverse of the string.
    Example:
        "python" -> "nohtyp"
    """
    pass


# ---------------------------------------------------------------------------
# Rank 4 — Advanced
# ---------------------------------------------------------------------------

def task_10_filter_by_length(words: list[str], min_length: int) -> list[str]:
    """
    Return a list of words whose length is >= min_length.

    Example:
        task_10_filter_by_length(["hi", "python", "go"], 3)
        -> ["python"]
    """
    pass


def task_11_find_longest_word(words: list[str]) -> str | None:
    """
    Return the longest word in the list.
    If the list is empty, return None.

    Example:
        ["apple", "banana", "kiwi"] -> "banana"
    """
    pass


def task_12_safe_divide(a: float, b: float) -> float | None:
    """
    Return a / b.
    If b is 0, return None instead of raising an error.
    """
    pass


# ---------------------------------------------------------------------------
# Rank 5 — Professional
# ---------------------------------------------------------------------------

def task_13_letter_frequency(text: str) -> dict[str, int]:
    """
    Return a dictionary mapping each letter to its frequency.

    Example:
        "hello"
        -> {"h":1, "e":1, "l":2, "o":1}

    Ignore spaces.
    Treat letters case-insensitively (convert text to lowercase).
    """
    pass


def task_14_create_user_profile(name: str, age: int, **extra) -> dict:
    """
    Return a user profile dictionary.

    Required keys:
        - "name": name
        - "age": age

    Extra keyword arguments should be included as well.

    Example:
        task_14_create_user_profile("Peyman", 43, role="admin")
        -> {"name":"Peyman","age":43,"role":"admin"}
    """
    pass


def task_15_apply_operation(numbers: list[float], func) -> list[float]:
    """
    Apply a function `func` to each number in the list and return the result.

    Example:
        def square(x): return x*x
        task_15_apply_operation([1,2,3], square)
        -> [1, 4, 9]

    This demonstrates higher-order functions.
    """
    pass


# Manual testing area (optional)
if __name__ == "__main__":
    # You can call your tasks here while developing them.
    pass
