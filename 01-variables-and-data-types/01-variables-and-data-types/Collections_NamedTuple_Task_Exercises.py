"""
Module 27 — Named Tuples: Practice Exercises
Professional skill-building with Python's namedtuple from simple usage to
clean production-style patterns.

In this module I:
- Learn what a namedtuple is and why it’s used
- Practice creating namedtuples in several ways
- Access fields by name instead of index
- Use methods like _replace(), _asdict()
- Compare namedtuples with classes and dictionaries
"""

from collections import namedtuple

# ------------------------------------------
# Task 1: Create a simple namedtuple
# Create a namedtuple called Car with fields: brand, model, year.
# Then create one sample Car instance.
# ------------------------------------------



# ------------------------------------------
# Task 2: Accessing values by name
# Using your Car instance, print the brand and year using dot notation.
# ------------------------------------------



# ------------------------------------------
# Task 3: _replace() method
# Replace the model of the car with a new model using _replace().
# ------------------------------------------



# ------------------------------------------
# Task 4: _asdict() method
# Convert your Car instance to a dictionary using _asdict().
# ------------------------------------------



# ------------------------------------------
# Task 5: Namedtuple for coordinates
# Create a namedtuple called Point with fields x, y.
# Create two points and print their coordinates.
# ------------------------------------------



# ------------------------------------------
# Task 6: Namedtuple for students
# Create a namedtuple Student with fields:
# name, grade, passed (boolean)
# Create 3 students and print their info cleanly.
# ------------------------------------------



# ------------------------------------------
# Task 7: Comparison
# Compare two Student namedtuples and print whether they are equal.
# ------------------------------------------



# ------------------------------------------
# Task 8: Using namedtuple inside a list
# Create a list of Car objects and loop through them, printing brand + model.
# ------------------------------------------



# ------------------------------------------
# Task 9: Default values
# Create a namedtuple with default values:
# Book(title, author, year=2025)
# Create a Book only using title + author.
# ------------------------------------------



# ------------------------------------------
# Task 10: Nested namedtuples (advanced)
# Create a namedtuple Engine(hp, type)
# Create a namedtuple FullCar(brand, model, engine)
# Create a FullCar with a nested Engine and print horsepower.
# ------------------------------------------
