# Filename: Lambda_Functions_Solutions.py

"""
Module 31 — Lambda Functions: Solutions
Complete reference solutions for the lambda function practice exercises.

This file mirrors the structure of Lambda_Functions_Exercises.py,
but here the focus is on clear, correct implementations that you can
compare with your own answers.

Author: Peyman Miyandashti
Date of Birth: 11/11/1983
ID Number: 250161
Year: 2025
"""

print("=== Module 31 — Lambda Functions: Solutions ===")
print()


# ===========================================================
# Rank 1 — Beginner
# Simple lambdas as tiny one-line functions
# ===========================================================

print("Rank 1 — Beginner (Solutions)")

add_ten = lambda n: n + 10
string_length = lambda s: len(s)
square = lambda x: x * x

number = 7
text = "Lambda"

print("add_ten(7):", add_ten(number))
print('string_length("Lambda"):', string_length(text))
print("square(7):", square(number))
print("-" * 50)


# ===========================================================
# Rank 2 — Easy
# Lambdas with map(), filter(), and basic list transformations
# ===========================================================

print("Rank 2 — Easy (Solutions)")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

doubled_numbers = list(map(lambda n: n * 2, numbers))
even_numbers = list(filter(lambda n: n % 2 == 0, numbers))
number_labels = list(map(lambda n: f"Number: {n}", numbers))

print("Original numbers:", numbers)
print("Doubled numbers:", doubled_numbers)
print("Even numbers:", even_numbers)
print("Number labels:", number_labels)
print("-" * 50)


# ===========================================================
# Rank 3 — Intermediate
# Lambdas as key functions for sorting and selection
# ===========================================================

print("Rank 3 — Intermediate (Solutions)")

students = [
    ("Alice", 8.5, 3),
    ("Bob", 6.9, 0),
    ("Carlos", 9.3, 1),
    ("Diana", 7.5, 5),
    ("Elena", 9.3, 0),
]

students_sorted_by_grade = sorted(students, key=lambda s: s[1])
students_sorted_by_absences = sorted(students, key=lambda s: s[2])
students_sorted_grade_desc_name = sorted(
    students,
    key=lambda s: (-s[1], s[0])
)

print("Original students list:")
for s in students:
    print(" ", s)

print("\nStudents sorted by grade (ascending):")
for s in students_sorted_by_grade:
    print(" ", s)

print("\nStudents sorted by absences (ascending):")
for s in students_sorted_by_absences:
    print(" ", s)

print("\nStudents sorted by grade (desc), then name (asc):")
for s in students_sorted_grade_desc_name:
    print(" ", s)

print("-" * 50)


# ===========================================================
# Rank 4 — Advanced
# Lambdas inside data structures and small helpers
# ===========================================================

print("Rank 4 — Advanced (Solutions)")

operations = [
    ("Square", lambda x: x * x),
    ("Cube", lambda x: x * x * x),
    ("Half", lambda x: x / 2),
    ("Double plus one", lambda x: x * 2 + 1),
]

value = 5
print(f"Applying operations to value={value}:")
for description, func in operations:
    result = func(value)
    print(f" - {description:15} -> {result}")

print()

def apply_to_list(values, func):
    """
    Apply a function (often a lambda) to each item in a list
    and return a new list with the results.
    """
    return [func(v) for v in values]


temperatures_c = [18.0, 21.5, 25.0, 30.0]
temperatures_f = apply_to_list(temperatures_c, lambda c: c * 9 / 5 + 32)

print("Temperatures in °C:", temperatures_c)
print("Temperatures in °F:", temperatures_f)
print("-" * 50)


# ===========================================================
# Rank 5 — Professional
# Lambda-based dispatch table (command -> small behavior)
# ===========================================================

print("Rank 5 — Professional (Solutions)")

calculator = {
    "add":      lambda a, b: a + b,
    "subtract": lambda a, b: a - b,
    "multiply": lambda a, b: a * b,
    "divide":   lambda a, b: a / b if b != 0 else float("inf"),
}

def calculate(op_name: str, a: float, b: float) -> float:
    operation = calculator.get(op_name)
    if operation is None:
        raise ValueError(f"Unknown operation: {op_name!r}")
    return operation(a, b)


a, b = 10, 4
for op in ("add", "subtract", "multiply", "divide"):
    result = calculate(op, a, b)
    print(f"{op.capitalize():9} {a} and {b} -> {result}")

print()

calculator["power"] = lambda a, b: a ** b

print("Added new operation: 'power'")
print(f"power({a}, {b}) ->", calculate("power", a, b))

print("-" * 50)
print("=== End of Module 31 — Lambda Functions (Solutions) ===")
