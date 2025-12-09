"""
Module 19 — Iterators: Practice Exercises (Solutions)
Complete solutions for iterator practice, from beginner to
more professional, production-style usage.

Author: Peyman Miyandashti
Date of Birth: 11/11/1983
ID Number: 250161
Year: 2025
"""

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

# Task 1 solution
for number in favorite_numbers:
    print("Number:", number)

pey_man_letters = list(pey_man_name)

# Task 2 solution
for ch in pey_man_letters[:5]:
    print("Letter:", ch)

print("-" * 50)


# ===========================================================
# Rank 2 — Easy
# Using iter() and next(), and working with range()
# ===========================================================

print("Rank 2 — Easy")

levels_to_complete = range(1, 6)

# Task 3 solution
levels_iterator = iter(levels_to_complete)

# Task 4 solution
level1 = next(levels_iterator)
level2 = next(levels_iterator)
level3 = next(levels_iterator)

print("First three levels (using next):", level1, level2, level3)

# Task 5 solution
for level in levels_iterator:
    print("Remaining level:", level)

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

# Task 6 solution
for key, value in profile_dict.items():
    print(f"key: {key} -> value: {value}")

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

# Task 7 solution
for owner, car_info in cars_by_owner.items():
    print(f"Owner: {owner}")
    print(f"  Model: {car_info['model']}")
    print(f"  Color: {car_info['color']}")
    print(f"  Year: {car_info['year']}")

print("-" * 50)


# ===========================================================
# Rank 4 — Advanced
# Custom iterator class + generator function
# ===========================================================

print("Rank 4 — Advanced")

class CountdownToGraduation:
    """
    Custom iterator that counts from current_age up to target_age.
    """

    def __init__(self, current_age: int, target_age: int):
        self.current_age = current_age
        self.target_age = target_age
        self.current = current_age

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.target_age:
            raise StopIteration
        age_to_return = self.current
        self.current += 1
        return age_to_return


# Task 11 solution
pey_man_countdown = CountdownToGraduation(current_age=pey_man_age, target_age=48)

# Task 12 solution
for age in pey_man_countdown:
    print("Age in countdown:", age)


def world_of_warcraft_sessions(weeks: int):
    """
    Generator that yields (week_number, total_hours) for Peyman's play time.
    2 hours/day * 5 days/week = 10 hours/week.
    """
    hours_per_day = 2
    days_per_week = 5

    for week_number in range(1, weeks + 1):
        total_hours = hours_per_day * days_per_week
        yield week_number, total_hours


# Task 14 solution
for week_number, hours in world_of_warcraft_sessions(3):
    print(f"Week {week_number}: {hours} hours played")

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
    Simple generator that yields all (course_name, grade) pairs.
    """
    for course_name, grade in records:
        yield course_name, grade


def filtered_grade_iterator(records, min_grade):
    """
    Generator that yields only (course_name, grade) where grade >= min_grade.
    """
    for course_name, grade in records:
        if grade >= min_grade:
            yield course_name, grade


# Task 17 solution
for course_name, grade in filtered_grade_iterator(student_grades, 90):
    print(f"High grade - {course_name}: {grade}")

print("-" * 50)
