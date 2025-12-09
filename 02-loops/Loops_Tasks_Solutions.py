"""
Module 2 — Loops: Practice Task Solutions
-----------------------------------------

This file contains clean, professional solutions to all loop exercises
from Loops_Tasks.py. Multiple solutions are possible; these demonstrate
clear, readable approaches suitable for beginners and intermediate
Python learners.

IMPORTANT:
I should only read these solutions AFTER attempting each task on my own.
"""


# ---------------------------------------------------------------------------
# Rank 1 — Beginner
# ---------------------------------------------------------------------------

def task_1_print_1_to_10():
    for i in range(1, 11):
        print(i)


def task_2_print_characters(text: str):
    for ch in text:
        print(ch)


def task_3_repeat_message(message: str, times: int):
    for _ in range(times):
        print(message)


# ---------------------------------------------------------------------------
# Rank 2 — Easy
# ---------------------------------------------------------------------------

def task_4_sum_1_to_n(n: int) -> int:
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def task_5_count_vowels(text: str) -> int:
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count


def task_6_countdown(start: int) -> None:
    for i in range(start, -1, -1):
        print(i)


# ---------------------------------------------------------------------------
# Rank 3 — Intermediate
# ---------------------------------------------------------------------------

def task_7_filter_positive(numbers: list[int]) -> list[int]:
    result = []
    for n in numbers:
        if n > 0:
            result.append(n)
    return result


def task_8_first_index_of(value: int, numbers: list[int]) -> int | None:
    for index, number in enumerate(numbers):
        if number == value:
            return index
    return None


def task_9_contains_digit(text: str) -> bool:
    for ch in text:
        if ch.isdigit():
            return True
    return False


# ---------------------------------------------------------------------------
# Rank 4 — Advanced
# ---------------------------------------------------------------------------

def task_10_unique_values(numbers: list[int]) -> list[int]:
    unique = []
    for value in numbers:
        if value not in unique:
            unique.append(value)
    return unique


def task_11_pair_sums(numbers: list[int]) -> list[int]:
    result = []
    if len(numbers) < 2:
        return result

    for i in range(len(numbers) - 1):
        pair_sum = numbers[i] + numbers[i + 1]
        result.append(pair_sum)

    return result


def task_12_multiplication_table(n: int) -> list[list[int]]:
    table = []
    for row in range(1, n + 1):
        row_values = []
        for col in range(1, n + 1):
            row_values.append(row * col)
        table.append(row_values)
    return table


# ---------------------------------------------------------------------------
# Rank 5 — Professional
# ---------------------------------------------------------------------------

def task_13_all_substrings(text: str) -> list[str]:
    substrings = []
    length = len(text)

    for start in range(length):
        for end in range(start + 1, length + 1):
            substrings.append(text[start:end])

    return substrings


def task_14_group_by_length(words: list[str]) -> dict[int, list[str]]:
    groups: dict[int, list[str]] = {}

    for word in words:
        size = len(word)
        if size not in groups:
            groups[size] = []
        groups[size].append(word)

    return groups


def task_15_is_prime(n: int) -> bool:
    # Quick rejections
    if n <= 1:
        return False
    if n == 2:
        return True

    # Check divisors
    for divisor in range(2, int(n**0.5) + 1):
        if n % divisor == 0:
            return False

    return True


# ---------------------------------------------------------------------------
# Manual Testing Section
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("Testing solutions...")

    print(task_1_print_1_to_10())
    print(task_4_sum_1_to_n(10))
    print(task_7_filter_positive([-3, 0, 5, 9]))
    print(task_12_multiplication_table(3))
    print(task_15_is_prime(29))
