"""
Module 31 — Lambda Functions: Practice Exercises
Comprehensive practice with Python lambda functions, from beginner to
more professional, production-style usage.

In this module I:
- Practice how to create and use anonymous functions (lambda).
- Start from very simple examples (Rank 1) and move toward
  more realistic, professional patterns (Rank 5).
- Combine lambda with built-in functions like map, filter, and sorted.

Ranking system:
- Rank 1  -> Beginner: very basic syntax and concepts.
- Rank 2  -> Easy: still simple, but combining two or more concepts.
- Rank 3  -> Intermediate: lambdas with sorting and conditionals.
- Rank 4  -> Advanced: lambdas inside other functions and data structures.
- Rank 5  -> Professional: patterns that could appear in real projects.

Author: Peyman Miyandashti
Date of Birth: 11/11/1983
ID Number: 250161
Year: 2025
"""

# ===========================================================
# Rank 1 — Beginner
# Basic lambda syntax vs normal function
# ===========================================================

print("Rank 1 — Beginner")

# Normal function
def add_numbers(a: int, b: int) -> int:
    return a + b

# Lambda function (anonymous, assigned to a variable)
add_lambda = lambda a, b: a + b  # type: ignore[assignment]

result_normal = add_numbers(5, 7)
result_lambda = add_lambda(5, 7)

print("Normal function result:", result_normal)
print("Lambda function result:", result_lambda)

# Single-argument lambda
square = lambda x: x * x  # type: ignore[assignment]
print("Square of 6 using lambda:", square(6))
print("-" * 50)


# ===========================================================
# Rank 2 — Easy
# Using lambda with map() and filter()
# ===========================================================

print("Rank 2 — Easy")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Double each number using map + lambda
doubled = list(map(lambda x: x * 2, numbers))
print("Original numbers:", numbers)
print("Doubled numbers:", doubled)

# Keep only even numbers using filter + lambda
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)

# Convert to strings using map + lambda
labels = list(map(lambda x: f"Number: {x}", numbers))
print("Labels:", labels)
print("-" * 50)


# ===========================================================
# Rank 3 — Intermediate
# Lambdas as sort keys and small inline logic
# ===========================================================

print("Rank 3 — Intermediate")

students = [
    ("Ana", 18, 9.1),
    ("Luis", 15, 8.5),
    ("Peyman", 16, 9.8),
    ("Carla", 17, 7.9),
]

print("Original students list:")
print(students)

# Sort by age using lambda as key
students_by_age = sorted(students, key=lambda s: s[1])
print("\nStudents sorted by age:")
print(students_by_age)

# Sort by grade (descending) using lambda
students_by_grade_desc = sorted(students, key=lambda s: s[2], reverse=True)
print("\nStudents sorted by grade (descending):")
print(students_by_grade_desc)

# Use lambda with a conditional expression
grade_status = list(
    map(
        lambda s: (s[0], "PASS" if s[2] >= 8.0 else "FAIL"),
        students,
    )
)
print("\nStudent grade status (using lambda with condition):")
print(grade_status)
print("-" * 50)


# ===========================================================
# Rank 4 — Advanced
# Functions that return lambdas and dictionaries of lambdas
# ===========================================================

print("Rank 4 — Advanced")


def make_multiplier(factor: int):
    """
    Return a lambda that multiplies any number by 'factor'.

    This is a simple example of a closure: the lambda remembers
    the value of 'factor' even after make_multiplier finishes.
    """
    return lambda x: x * factor


double = make_multiplier(2)
triple = make_multiplier(3)
times_ten = make_multiplier(10)

print("Double 7:", double(7))
print("Triple 7:", triple(7))
print("Times ten 7:", times_ten(7))

# Dictionary of operations using lambdas
operations = {
    "add": lambda a, b: a + b,
    "sub": lambda a, b: a - b,
    "mul": lambda a, b: a * b,
    "div": lambda a, b: a / b if b != 0 else float("inf"),
}

a, b = 10, 4
print("\nUsing dictionary of lambda operations:")
for name, op in operations.items():
    result = op(a, b)
    print(f"{name.upper():<4} -> op({a}, {b}) = {result}")

print("-" * 50)


# ===========================================================
# Rank 5 — Professional
# Using lambdas in small, reusable processing pipelines
# ===========================================================

print("Rank 5 — Professional")

from typing import Callable, List, Dict, Any

Student = Dict[str, Any]

students_data: List[Student] = [
    {"name": "Peyman", "math": 95, "physics": 92},
    {"name": "Ana", "math": 88, "physics": 79},
    {"name": "Luis", "math": 72, "physics": 85},
    {"name": "Carla", "math": 91, "physics": 87},
]


# Step 1: Build a small reusable "pipeline" of transformations
# Each step is a lambda that receives a list of students and returns a list.
PipelineStep = Callable[[List[Student]], List[Student]]

compute_average: PipelineStep = lambda data: [  # type: ignore[assignment]
    {
        **s,
        "average": (s["math"] + s["physics"]) / 2,
    }
    for s in data
]

keep_only_high_achievers: PipelineStep = lambda data: [  # type: ignore[assignment]
    s for s in data if s["average"] >= 85
]

sort_by_average_desc: PipelineStep = lambda data: sorted(  # type: ignore[assignment]
    data,
    key=lambda s: s["average"],
    reverse=True,
)

# Step 2: Run the pipeline
pipeline: List[PipelineStep] = [
    compute_average,
    keep_only_high_achievers,
    sort_by_average_desc,
]

processed_students = students_data
for step in pipeline:
    processed_students = step(processed_students)

# Step 3: Pretty-print the result
print("Processed high-achiever students (using lambda pipeline):")
for idx, s in enumerate(processed_students, start=1):
    print(
        f"{idx}. {s['name']:<10} | "
        f"Math: {s['math']:<3} | Physics: {s['physics']:<3} | "
        f"Average: {s['average']:.2f}"
    )

print("-" * 50)
