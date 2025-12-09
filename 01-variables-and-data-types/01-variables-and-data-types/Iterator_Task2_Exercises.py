"""
Module 19 — Iterators: Practice Exercises
Comprehensive practice with Python iterators and iterable objects, from beginner
to more professional, production-style usage.

In this module I:
- Practice how to use iterators with lists, ranges, and dictionaries.
- Learn the difference between iterables and iterators.
- Use iter(), next(), custom iterator classes, and generator functions.
- Start from very simple examples (Rank 1) and move toward more realistic,
  professional patterns (Rank 5).

Ranking system:
- Rank 1  -> Beginner: basic for-loops over iterables.
- Rank 2  -> Easy: use iter() and next(), and simple ranges.
- Rank 3  -> Intermediate: iterate over dictionaries and nested data.
- Rank 4  -> Advanced: write custom iterator classes and generators.
- Rank 5  -> Professional: clean, reusable iterator-based utilities.

Author: Peyman Miyandashti
Date of Birth: 11/11/1983
ID Number: 250161
Year: 2025
"""

# Personal base data (used in tasks)
pey_man_age = 43
wife_age = 47
favorite_number = 11

pey_man_name = "Peyman Miyandashti"
wife_name = "Arlette Chong"
favorite_game = "World of Warcraft"

pey_man_city_origin = "Tabriz"
pey_man_country_origin = "Iran"
current_city = "Mexicali"
current_state = "Baja California"
current_country = "Mexico"

pey_man_car = "Kia Sportage 2024"
wife_car = "Hyundai Creta 2018"


# ===========================================================
# Rank 1 — Beginner
# Basic iteration over lists and strings
# ===========================================================

print("Rank 1 — Beginner")

favorite_numbers = [favorite_number, 7, 3, 5]

# TODO 1:
# Use a for-loop to print each number in favorite_numbers
# Example output format: "Number: 11"
for number in favorite_numbers:
    # Replace 'pass' with a print that shows each number
    pass

pey_man_letters = list(pey_man_name)

# TODO 2:
# Use a for-loop to print only the first 5 characters of pey_man_name
# HINT: you can loop over a slice pey_man_letters[:5]
for ch in pey_man_letters[:5]:
    # Replace 'pass' with a print that shows each character
    pass

print("-" * 50)


# ===========================================================
# Rank 2 — Easy
# Using iter() and next(), and working with range()
# ===========================================================

print("Rank 2 — Easy")

# A simple range iterator for game levels Peyman wants to complete
# (pretend these are level numbers)
levels_to_complete = range(1, 6)  # 1 to 5

# TODO 3:
# Create an iterator from levels_to_complete using iter()
levels_iterator = None  # Replace None with iter(...)

# TODO 4:
# Use next() three times to get the first three level numbers.
# Store them in level1, level2, level3.
level1 = None  # Replace with next(levels_iterator)
level2 = None  # Replace with next(levels_iterator)
level3 = None  # Replace with next(levels_iterator)

print("First three levels (using next):", level1, level2, level3)

# TODO 5:
# Use a for-loop to print the remaining levels from levels_iterator
# (whatever is left after three calls to next()).
for level in []:  # Replace [] with the correct iterator
    # Replace 'pass' with a print that shows the remaining levels
    pass

print("-" * 50)


# ===========================================================
# Rank 3 — Intermediate
# Iterating over dictionaries and nested structures
# ===========================================================

print("Rank 3 — Intermediate")

profile_dict = {
    "name": pey_man_name,
    "age": pey_man_age,
    "city": current_city,
    "country": current_country,
    "favorite_game": favorite_game,
    "favorite_number": favorite_number,
}

# TODO 6:
# Iterate over profile_dict.items() and print:
# "key: <key> -> value: <value>"
for key, value in profile_dict.items():
    # Replace 'pass' with a print using the format above
    pass

cars_by_owner = {
    "Peyman": {
        "model": pey_man_car,
        "color": "Dark Gray",
        "year": 2024,
    },
    "Arlette": {
        "model": wife_car,
        "color": "White",  # example
        "year": 2018,
    },
}

# TODO 7:
# Use nested iteration to print each owner and their car info.
# Example:
# Owner: Peyman
#   Model: Kia Sportage 2024
#   Color: Dark Gray
#   Year: 2024
for owner, car_info in cars_by_owner.items():
    # Replace 'pass' with prints that follow the example format.
    pass

print("-" * 50)


# ===========================================================
# Rank 4 — Advanced
# Custom iterator class + generator function
# ===========================================================

print("Rank 4 — Advanced")

class CountdownToGraduation:
    """
    Custom iterator that counts down years until graduation from
    Peyman's current age to a target graduation age.
    """

    def __init__(self, current_age: int, target_age: int):
        # TODO 8:
        # Store current_age and target_age as instance attributes.
        # Also create a 'current' attribute to track the current age
        # in the countdown.
        pass

    def __iter__(self):
        # TODO 9:
        # Return self, because this object is its own iterator.
        pass

    def __next__(self):
        """
        Each call to next() should:
        - If current age is greater than target age: raise StopIteration.
        - Otherwise: return the current age and then increase it by 1.
        """
        # TODO 10:
        # Implement the logic described in the docstring.
        pass


# TODO 11:
# Create an instance of CountdownToGraduation for Peyman, from his
# current age (pey_man_age) to a target age of 48.
pey_man_countdown = None  # Replace None with CountdownToGraduation(...)

# TODO 12:
# Use a for-loop to iterate over pey_man_countdown and print
# "Age in countdown: <age>"
# for age in pey_man_countdown:
#     print("Age in countdown:", age)


def world_of_warcraft_sessions(weeks: int):
    """
    Generator function that yields total hours played each week.

    Assume Peyman plays 2 hours per day, 5 days per week (same as before).
    For week_number in range(1, weeks + 1), yield (week_number, hours).
    """
    hours_per_day = 2
    days_per_week = 5

    # TODO 13:
    # Use a for-loop with range(1, weeks + 1) and yield
    # (week_number, total_hours_for_that_week).
    pass


# TODO 14:
# Use a for-loop to consume world_of_warcraft_sessions(3) and print:
# "Week <n>: <hours> hours played"
# for week_number, hours in world_of_warcraft_sessions(3):
#     print(f"Week {week_number}: {hours} hours played")

print("-" * 50)


# ===========================================================
# Rank 5 — Professional
# Iterator-based utility functions working with real data
# ===========================================================

print("Rank 5 — Professional")

student_grades = [
    ("Python Basics", 95),
    ("Networking", 88),
    ("Linux", 91),
    ("Discrete Math", 84),
    ("Databases", 90),
]


def grade_iterator(records):
    """
    TODO 15:
    Turn this function into a generator that:

    - Takes a list of (course_name, grade) tuples.
    - Yields only those (course_name, grade) where grade >= min_grade.
      (You will add min_grade in the next task.)

    For now, just leave it as a simple placeholder.
    """
    # Replace 'pass' in the solution file with a real generator.
    pass


def filtered_grade_iterator(records, min_grade):
    """
    TODO 16:
    Implement a generator that:
    - Iterates over 'records'.
    - Yields only (course_name, grade) where grade >= min_grade.
    """
    # Replace 'pass' in the solution file with real logic.
    pass


# TODO 17:
# Use filtered_grade_iterator(student_grades, 90) and print only
# the courses where Peyman scored 90 or more.
# Example:
# "High grade - Python Basics: 95"
for course_name, grade in []:  # Replace [] with the generator call
    # Replace 'pass' with a print using the example format.
    pass

print("-" * 50)
