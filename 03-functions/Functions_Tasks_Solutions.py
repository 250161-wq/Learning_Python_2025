"""
Module 3 — Functions: Practice Task Solutions
---------------------------------------------

These are clean, professional solutions to all tasks in
Functions_Tasks.py. Many tasks have multiple correct answers; the
solutions here focus on clarity, correctness, and good Python style.

IMPORTANT:
These solutions should only be viewed *after* attempting the tasks
independently.
"""


# ---------------------------------------------------------------------------
# Rank 1 — Beginner
# ---------------------------------------------------------------------------

def task_1_basic_greeting() -> None:
    print("Hello, world!")


def task_2_greet_user(name: str) -> None:
    print(f"Hello, {name}!")


def task_3_double_number(n: int) -> int:
    return n * 2


# ---------------------------------------------------------------------------
# Rank 2 — Easy
# ---------------------------------------------------------------------------

def task_4_full_name(first: str, last: str) -> str:
    return f"{first} {last}"


def task_5_add_three_numbers(a: float, b: float, c: float) -> float:
    return a + b + c


def task_6_greet_with_default(name: str = "Guest") -> str:
    return f"Hello, {name}!"


# ---------------------------------------------------------------------------
# Rank 3 — Intermediate
# ---------------------------------------------------------------------------

def task_7_count_even(numbers: list[int]) -> int:
    count = 0
    for n in numbers:
        if n % 2 == 0:
            count += 1
    return count


def task_8_calculate_average(values: list[float]) -> float:
    if not values:
        return 0.0
    total = 0.0
    for v in values:
        total += v
    return total / len(values)


def task_9_reverse_string(text: str) -> str:
    reversed_text = ""
    for ch in text:
        reversed_text = ch + reversed_text
    return reversed_text


# ---------------------------------------------------------------------------
# Rank 4 — Advanced
# ---------------------------------------------------------------------------

def task_10_filter_by_length(words: list[str], min_length: int) -> list[str]:
    result = []
    for word in words:
        if len(word) >= min_length:
            result.append(word)
    return result


def task_11_find_longest_word(words: list[str]) -> str | None:
    if not words:
        return None

    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


def task_12_safe_divide(a: float, b: float) -> float | None:
    if b == 0:
        return None
    return a / b


# ---------------------------------------------------------------------------
# Rank 5 — Professional
# ---------------------------------------------------------------------------

def task_13_letter_frequency(text: str) -> dict[str, int]:
    text = text.lower().replace(" ", "")
    freq: dict[str, int] = {}

    for ch in text:
        if ch not in freq:
            freq[ch] = 0
        freq[ch] += 1

    return freq


def task_14_create_user_profile(name: str, age: int, **extra) -> dict:
    profile = {"name": name, "age": age}
    for key, value in extra.items():
        profile[key] = value
    return profile


def task_15_apply_operation(numbers: list[float], func) -> list[float]:
    result = []
    for n in numbers:
        result.append(func(n))
    return result


# ---------------------------------------------------------------------------
# Manual Testing Area
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("--- Solution Tests ---")
    print(task_3_double_number(5))
    print(task_4_full_name("Peyman", "Miyandashti"))
    print(task_9_reverse_string("Python"))
    print(task_12_safe_divide(10, 2))
    print(task_13_letter_frequency("Hello World"))
    print(task_14_create_user_profile("Peyman", 43, role="admin"))
    print(task_15_apply_operation([1, 2, 3], lambda x: x * 10))
