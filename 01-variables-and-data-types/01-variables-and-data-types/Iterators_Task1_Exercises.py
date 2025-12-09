"""
Module 19 — Iterators: Practice Exercises
Comprehensive practice with Python iterators, from beginner to
more professional, production-style usage.

In this module I:
- Practice how to create and use iterators with iter() and next().
- See how for-loops use iterators under the hood.
- Learn how to build custom iterator-style logic for real projects.

Ranking system:
- Rank 1  -> Beginner: very basic syntax and concepts.
- Rank 2  -> Easy: still simple, but mixing several iterator ideas.
- Rank 3  -> Intermediate: iterators with more complex data structures.
- Rank 4  -> Advanced: custom iterator-like behavior with classes.
- Rank 5  -> Professional: reusable iterator utilities for real data.

Author: Peyman Miyandashti
Date of Birth: 11/11/1983
ID Number: 250161
Year: 2025
"""

# Personal base data (we'll reuse this in several ranks)
pey_man_name = "Peyman Miyandashti"
pey_man_age = 43
wife_name = "Arlette Chong"
wife_age = 47

favorite_number = 11
favorite_game = "World of Warcraft"

home_cities = ["Tabriz", "Mexicali"]
car_models = ["Kia Sportage 2024 (Dark Gray)", "Hyundai Creta 2018"]

# ===========================================================
# Rank 1 — Beginner
# Basic iterators with lists and next()
# ===========================================================

print("Rank 1 — Beginner")

favorite_numbers = [favorite_number, 7, 3, 99]

print("Favorite numbers list:", favorite_numbers)

# Create an iterator from the list
numbers_iterator = iter(favorite_numbers)

# Get items one by one using next()
first_num = next(numbers_iterator)
second_num = next(numbers_iterator)

print("First number from iterator:", first_num)
print("Second number from iterator:", second_num)

# Continue consuming the iterator
third_num = next(numbers_iterator)
fourth_num = next(numbers_iterator)

print("Third number from iterator:", third_num)
print("Fourth number from iterator:", fourth_num)

print("-" * 50)


# ===========================================================
# Rank 2 — Easy
# Using iterators with range and safe next() using try/except
# ===========================================================

print("Rank 2 — Easy")

# Years Peyman has lived in different countries (simple example)
years_in_iran = 30
years_in_mexico = 13  # example value (not exact, just for practice)

years_lived = [("Iran", years_in_iran), ("Mexico", years_in_mexico)]

# Iterate with a for-loop (uses iterators internally)
print("Years lived in each country (for-loop):")
for country, years in years_lived:
    print(f"- {country}: {years} years")

# Manual iteration over a range using iter() and next()
print("\nCounting using an iterator over range(1, 6):")
counter_iterator = iter(range(1, 6))

while True:
    try:
        value = next(counter_iterator)
        print("Next value:", value)
    except StopIteration:
        print("Iterator is exhausted.")
        break

print("-" * 50)


# ===========================================================
# Rank 3 — Intermediate
# Iterators with more complex data: lists of dicts, enumerate, zip
# ===========================================================

print("Rank 3 — Intermediate")

# Create a list of family members as dictionaries
family_members = [
    {"name": pey_man_name, "age": pey_man_age, "role": "Student"},
    {"name": wife_name, "age": wife_age, "role": "Teacher"},
]

# Use an iterator explicitly on this list
family_iter = iter(family_members)

print("Iterating over family members with next():")
try:
    first_member = next(family_iter)
    print("First member:", first_member)

    second_member = next(family_iter)
    print("Second member:", second_member)

    # This next(next(...)) will raise StopIteration
    third_member = next(family_iter)
    print("Third member:", third_member)
except StopIteration:
    print("No more family members in iterator.")

# Use enumerate (which returns an iterator) in a for-loop
print("\nEnumerating family members:")
for index, member in enumerate(family_members, start=1):
    print(f"{index}. {member['name']} ({member['role']}) — {member['age']} years old")

# Use zip (also returns an iterator)
cities_lived = ["Tabriz", "Mexicali"]
years_in_each_city = [years_in_iran, years_in_mexico]

print("\nUsing zip iterator for cities and years:")
for city, years in zip(cities_lived, years_in_each_city):
    print(f"- {city}: {years} years")

print("-" * 50)


# ===========================================================
# Rank 4 — Advanced
# Custom iterator-like class (implements __iter__ and __next__)
# ===========================================================

print("Rank 4 — Advanced")


class GameSessionCountdown:
    """
    Simple custom iterator that counts down game sessions.

    Example use:
        countdown = GameSessionCountdown(total_sessions=3)
        for session in countdown:
            print(session)
    """

    def __init__(self, total_sessions: int):
        self.total_sessions = total_sessions
        self.current = total_sessions

    def __iter__(self):
        # An iterator must return itself from __iter__()
        return self

    def __next__(self):
        # Stop when current reaches 0
        if self.current <= 0:
            raise StopIteration
        session_number = self.current
        self.current -= 1
        return session_number


total_game_sessions = 5  # example: 5 sessions of World of Warcraft
countdown_iterator = GameSessionCountdown(total_game_sessions)

print(f"Counting down {total_game_sessions} game sessions:")
for session in countdown_iterator:
    print("Remaining sessions:", session)

print("-" * 50)


# ===========================================================
# Rank 5 — Professional
# Reusable iterator utilities (generator function + pipeline style)
# ===========================================================

print("Rank 5 — Professional")


def filter_adults(people):
    """
    Generator that yields only adults (age >= 18) from an iterable
    of dictionaries with 'age' keys.

    This is a reusable iterator-based utility.
    """
    for person in people:
        if person.get("age", 0) >= 18:
            yield person


def names_iterator(people):
    """
    Generator that yields names from an iterable of people dictionaries.
    """
    for person in people:
        yield person.get("name", "Unknown")


# Example dataset: small "social circle" around you
social_circle = [
    {"name": pey_man_name, "age": pey_man_age, "description": "IT student at UPBC"},
    {"name": wife_name, "age": wife_age, "description": "Teacher in Mexicali"},
    {"name": "Game Friend #1", "age": 17, "description": "WoW guild member"},
    {"name": "Game Friend #2", "age": 25, "description": "WoW healer"},
]

# Build an iterator pipeline:
# 1) filter_adults -> only adults
# 2) names_iterator -> get names only
adult_people_iterator = filter_adults(social_circle)
adult_names_iterator = names_iterator(adult_people_iterator)

print("Adult names in Peyman's social circle (iterator pipeline):")
for name in adult_names_iterator:
    print("- ", name)

# Another example: chunking an iterable into fixed-size pieces
def chunk_iterable(iterable, chunk_size: int):
    """
    Generator that yields chunks (lists) of size `chunk_size` from the iterable.
    Last chunk may be smaller.

    This kind of pattern is common in real data processing code.
    """
    iterator = iter(iterable)
    while True:
        chunk = []
        try:
            for _ in range(chunk_size):
                item = next(iterator)
                chunk.append(item)
        except StopIteration:
            if chunk:
                yield chunk
            break
        yield chunk


# Use chunk_iterable with a range of levels (like game levels)
print("\nChunking levels into groups of 4 using an iterator:")
levels = range(1, 17)  # pretend these are World of Warcraft levels
for group in chunk_iterable(levels, chunk_size=4):
    print("Group:", list(group))

print("-" * 50)
