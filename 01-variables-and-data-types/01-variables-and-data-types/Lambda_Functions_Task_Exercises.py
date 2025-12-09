# Filename: Lambda_Functions_Exercises.py

"""
Module 31 — Lambda Functions: Practice Exercises
Comprehensive practice with Python lambda (anonymous) functions, from beginner to
more professional, production-style usage.

In this module I:
- Practice how to create and use lambda functions for simple one-line operations.
- Use lambda together with built-in functions like sorted(), map(), filter().
- Build small, realistic examples where lambdas make the code shorter and cleaner.
- See how lambdas can be used as "small behavior" in dictionaries (dispatch tables).

Ranking system:
- Rank 1  -> Beginner: very basic lambda syntax and concepts.
- Rank 2  -> Easy: combining lambdas with simple lists and built-in functions.
- Rank 3  -> Intermediate: using lambdas as key functions for sorting and selection.
- Rank 4  -> Advanced: using lambdas inside data structures and small utilities.
- Rank 5  -> Professional: using lambdas in a clean, readable "dispatch" style.

Author: Peyman Miyandashti
Date of Birth: 11/11/1983
ID Number: 250161
Year: 2025
"""

print("=== Module 31 — Lambda Functions: Practice Exercises ===")
print()


# ===========================================================
# Rank 1 — Beginner
# Simple lambdas as tiny one-line functions
# ===========================================================

print("Rank 1 — Beginner")

# 1) Lambda that adds 10 to a number.
add_ten = lambda n: n + 10

# 2) Lambda that returns the length of a string.
string_length = lambda s: len(s)

# 3) Lambda that returns the square of a number.
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

print("Rank 2 — Easy")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 1) Use map + lambda to create a new list with each number doubled.
doubled_numbers = list(map(lambda n: n * 2, numbers))

# 2) Use filter + lambda to keep only even numbers.
even_numbers = list(filter(lambda n: n % 2 == 0, numbers))

# 3) Use map + lambda to convert numbers to formatted strings.
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

print("Rank 3 — Intermediate")

students = [
    ("Alice", 8.5, 3),   # (name, grade, absences)
    ("Bob", 6.9, 0),
    ("Carlos", 9.3, 1),
    ("Diana", 7.5, 5),
    ("Elena", 9.3, 0),
]

# 1) Sort students by grade (ascending) using a lambda as the key.
students_sorted_by_grade = sorted(students, key=lambda s: s[1])

# 2) Sort students by number of absences (ascending).
students_sorted_by_absences = sorted(students, key=lambda s: s[2])

# 3) Sort by grade (descending), then by name (ascending) using a tuple key.
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

print("Rank 4 — Advanced")

# 1) A list of operations (each item: (description, lambda)).
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

# 2) A helper that takes a lambda and applies it to all items.
def apply_to_list(values, func):
    """
    Apply a function (often a lambda) to each item in a list
    and return a new list with the results.
    """
    return [func(v) for v in values]


temperatures_c = [18.0, 21.5, 25.0, 30.0]
# Convert Celsius to Fahrenheit: F = C * 9/5 + 32
temperatures_f = apply_to_list(temperatures_c, lambda c: c * 9 / 5 + 32)

print("Temperatures in °C:", temperatures_c)
print("Temperatures in °F:", temperatures_f)
print("-" * 50)


# ===========================================================
# Rank 5 — Professional
# Lambda-based dispatch table (command -> small behavior)
# ===========================================================

print("Rank 5 — Professional")

# A small calculator using lambdas in a "dispatch table".
calculator = {
    "add":      lambda a, b: a + b,
    "subtract": lambda a, b: a - b,
    "multiply": lambda a, b: a * b,
    "divide":   lambda a, b: a / b if b != 0 else float("inf"),
}

def calculate(op_name: str, a: float, b: float) -> float:
    """
    Perform a calculation using a small lambda-based dispatch table.

    - op_name: "add", "subtract", "multiply", or "divide"
    - a, b: numbers to operate on
    """
    operation = calculator.get(op_name)
    if operation is None:
        raise ValueError(f"Unknown operation: {op_name!r}")
    return operation(a, b)


a, b = 10, 4
for op in ("add", "subtract", "multiply", "divide"):
    result = calculate(op, a, b)
    print(f"{op.capitalize():9} {a} and {b} -> {result}")

print()

# You can extend this dispatch table with new behaviors very easily:
calculator["power"] = lambda a, b: a ** b

print("Added new operation: 'power'")
print(f"power({a}, {b}) ->", calculate("power", a, b))

print("-" * 50)
print("=== End of Module 31 — Lambda Functions (Exercises) ===")
