"""
Module 23 — Generators: Practice Solutions
Solutions for all generator tasks from Module 23.

Author: Peyman Miyandashti
ID Number: 250161
Year: 2025
"""


# ===========================================================
# Rank 1 — Beginner
# Very simple generator that yields a sequence of integers
# ===========================================================

def count_up_to(n: int):
    """Yield numbers from 1 up to n (inclusive)."""
    for number in range(1, n + 1):
        yield number


def simple_fixed_numbers():
    """Yield [43, 47, 11] one by one."""
    pey_man_age = 43
    wife_age = 47
    favorite_number = 11

    yield pey_man_age
    yield wife_age
    yield favorite_number


# ===========================================================
# Rank 2 — Easy
# Generators using parameters and basic logic
# ===========================================================

def even_numbers_up_to(limit: int):
    """Yield all even numbers from 0 to limit (inclusive)."""
    for number in range(0, limit + 1):
        if number % 2 == 0:
            yield number


def age_progression(current_age: int, years: int):
    """
    Yield future ages, starting from current_age + 1,
    for a total of "years" ages.
    """
    for i in range(1, years + 1):
        yield current_age + i


# ===========================================================
# Rank 3 — Intermediate
# Generators with arithmetic operations and real contexts
# ===========================================================

def gaming_sessions_per_week(days_per_week: int, hours_per_day: int):
    """
    Yield gaming hours for each of 7 days.
    First days_per_week days -> hours_per_day.
    Remaining days -> 0.
    """
    for day_index in range(7):
        if day_index < days_per_week:
            yield hours_per_day
        else:
            yield 0


def yearly_car_ages(start_year: int, end_year: int, car_year: int):
    """
    Yield (year, age) from start_year to end_year (inclusive)
    for a car with model year "car_year".
    """
    for year in range(start_year, end_year + 1):
        age = year - car_year
        yield (year, age)


# ===========================================================
# Rank 4 — Advanced
# Chaining generators and using them for filtering
# ===========================================================

def upbc_semesters(start_year: int, end_year: int):
    """
    Yield semester codes "YYYY-1" and "YYYY-2" for each year.
    """
    for year in range(start_year, end_year + 1):
        for semester in (1, 2):
            yield f"{year}-{semester}"


def filter_even_semesters(semesters):
    """
    Yield only semester codes that end with "-2".
    """
    for sem in semesters:
        if sem.endswith("-2"):
            yield sem


def wow_level_generator(start_level: int, end_level: int, step: int = 1):
    """
    Yield levels from start_level to end_level (inclusive),
    increasing by step.
    """
    current = start_level
    while current <= end_level:
        yield current
        current += step


# ===========================================================
# Rank 5 — Professional
# Clean generator pipelines and composition
# ===========================================================

def generate_student_ids(start_id: int, count: int):
    """
    Yield "count" student IDs starting from "start_id".
    """
    current = start_id
    for _ in range(count):
        yield current
        current += 1


def tag_student_ids(student_ids, prefix: str):
    """
    Yield strings of the form f"{prefix}{id}" for each id.
    """
    for sid in student_ids:
        yield f"{prefix}{sid}"


def filter_ids_by_last_digit(tagged_ids, last_digit: int):
    """
    From strings like "UPBC-250161", yield only those where
    numeric part's last digit == last_digit.
    """
    for tagged in tagged_ids:
        # Assume prefix and number separated by '-'
        parts = tagged.split("-")
        if len(parts) != 2:
            # Skip malformed strings
            continue

        number_str = parts[1]
        try:
            number_int = int(number_str)
        except ValueError:
            # Skip non-integer IDs
            continue

        if number_int % 10 == last_digit:
            yield tagged


# ===========================================================
# Demo / manual testing
# ===========================================================

if __name__ == "__main__":
    print("== Rank 1 ==")
    print("count_up_to(5):", list(count_up_to(5)))
    print("simple_fixed_numbers():", list(simple_fixed_numbers()))
    print("-" * 40)

    print("== Rank 2 ==")
    print("even_numbers_up_to(10):", list(even_numbers_up_to(10)))
    print("age_progression(43, 5):", list(age_progression(43, 5)))
    print("-" * 40)

    print("== Rank 3 ==")
    print("gaming_sessions_per_week(3, 2):", list(gaming_sessions_per_week(3, 2)))
    print("yearly_car_ages(2024, 2027, 2024):", list(yearly_car_ages(2024, 2027, 2024)))
    print("-" * 40)

    print("== Rank 4 ==")
    all_semesters = list(upbc_semesters(2023, 2025))
    print("UPBC semesters 2023-2025:", all_semesters)
    print("Even semesters only:", list(filter_even_semesters(all_semesters)))
    print("wow_level_generator(1, 10, 3):", list(wow_level_generator(1, 10, 3)))
    print("-" * 40)

    print("== Rank 5 ==")
    ids = list(generate_student_ids(250161, 6))
    print("Generated IDs:", ids)

    tagged = list(tag_student_ids(ids, "UPBC-"))
    print("Tagged IDs:", tagged)

    filtered = list(filter_ids_by_last_digit(tagged, 1))
    print("Filtered IDs (last digit = 1):", filtered)
    print("-" * 40)
