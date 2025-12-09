"""
Module 2 — Loops: Examples
--------------------------

This file contains small, focused examples that show how to use
loops in Python in a clean, professional way.

Covered in this file:
- Basic for-loops with lists and ranges
- while-loops with counters and conditions
- break and continue
- Looping with indexes using enumerate()
- Looping over dictionaries
- Nested loops
- Loop "patterns" used in real code

How to use this file:
- Run it directly:  python Loops_Examples.py
- Read the code and compare it with the terminal output.
- Modify values, lists, and conditions to see what changes.
"""


# ---------------------------------------------------------
# Rank 1 — Very basic loops
# ---------------------------------------------------------


def example_1_for_loop_over_list() -> None:
    """Print each student name from a simple list."""
    students = ["Ana", "Luis", "Pablo"]

    print("Example 1 — for-loop over a list")
    for student in students:
        print(f"- {student}")
    print()  # blank line for readability


def example_2_for_loop_with_range() -> None:
    """Use range() to repeat an action a specific number of times."""
    print("Example 2 — for-loop with range(1, 4)")
    for number in range(1, 4):
        print(f"Iteration number: {number}")
    print()


def example_3_while_loop_basic_counter() -> None:
    """Use a while-loop to count from 1 to 3."""
    print("Example 3 — basic while-loop with a counter")

    counter = 1
    while counter <= 3:
        print(f"Counter value: {counter}")
        counter += 1  # important to avoid an infinite loop

    print()


# ---------------------------------------------------------
# Rank 2 — Loops combining a few ideas
# ---------------------------------------------------------


def example_4_sum_numbers_with_for() -> None:
    """Sum numbers in a list using a for-loop."""
    print("Example 4 — summing numbers with a for-loop")

    numbers = [10, 5, 7, 3]
    total = 0

    for value in numbers:
        total += value

    print(f"Numbers: {numbers}")
    print(f"Total sum: {total}")
    print()


def example_5_while_loop_with_condition_flag() -> None:
    """
    Simulate a process that runs until a condition is met.

    Here we use a 'flag' variable (keep_running) to decide
    when to stop the loop. This pattern is common in real code.
    """
    print("Example 5 — while-loop with a condition flag")

    keep_running = True
    step = 0

    while keep_running:
        step += 1
        print(f"Processing step: {step}")

        if step >= 3:
            # Condition met, we stop the loop.
            keep_running = False

    print("Finished processing.\n")


# ---------------------------------------------------------
# Rank 3 — break, continue, and enumerate()
# ---------------------------------------------------------


def example_6_break_in_for_loop() -> None:
    """
    Use break to exit a loop early.

    We search for a target number in a list.
    """
    print("Example 6 — using 'break' in a for-loop")

    numbers = [4, 8, 15, 16, 23, 42]
    target = 16

    for number in numbers:
        print(f"Checking number: {number}")
        if number == target:
            print(f"Found target: {target}")
            break  # Exit the loop immediately

    print("Loop finished.\n")


def example_7_continue_in_for_loop() -> None:
    """
    Use continue to skip specific items in a loop.

    Here we skip negative numbers when calculating a sum.
    """
    print("Example 7 — using 'continue' in a for-loop")

    values = [10, -3, 5, -1, 7]
    total = 0

    for value in values:
        if value < 0:
            # Skip negative numbers.
            print(f"Skipping negative value: {value}")
            continue
        total += value

    print(f"Final sum of non-negative values: {total}\n")


def example_8_for_loop_with_enumerate() -> None:
    """
    Use enumerate() to get both index and value in a loop.

    This is more professional than manually managing an index.
    """
    print("Example 8 — for-loop with enumerate()")

    fruits = ["apple", "banana", "cherry"]

    for index, fruit in enumerate(fruits, start=1):
        print(f"{index}. {fruit}")

    print()


# ---------------------------------------------------------
# Rank 4 — Looping over dictionaries and nested loops
# ---------------------------------------------------------


def example_9_loop_over_dictionary_items() -> None:
    """
    Loop over key-value pairs in a dictionary.

    This pattern appears all the time in real projects.
    """
    print("Example 9 — looping over a dictionary")

    student_grades = {
        "Ana": 9.5,
        "Luis": 8.3,
        "Pablo": 7.9,
    }

    for name, grade in student_grades.items():
        print(f"Student: {name:5}  |  Grade: {grade}")

    print()


def example_10_nested_loops() -> None:
    """
    Use nested loops to combine items from two sequences.

    Here we build all possible (student, subject) pairs.
    """
    print("Example 10 — nested loops")

    students = ["Ana", "Luis"]
    subjects = ["Math", "Physics"]

    for student in students:
        for subject in subjects:
            print(f"{student} is enrolled in {subject}")

    print()


# ---------------------------------------------------------
# Rank 5 — More “production-style” loop patterns
# ---------------------------------------------------------


def example_11_filter_with_loop() -> None:
    """
    Filter a list using a loop.

    We create a new list that contains only the values
    that match a specific condition (value >= 10).
    """
    print("Example 11 — filtering values with a loop")

    raw_values = [3, 12, 7, 25, 10, 5]
    filtered_values = []

    for value in raw_values:
        if value >= 10:
            filtered_values.append(value)

    print(f"Raw values:       {raw_values}")
    print(f"Filtered (>= 10): {filtered_values}\n")


def example_12_search_pattern_with_boolean_result() -> None:
    """
    Implement a common pattern: check if a condition occurs at least once.

    We return a boolean that tells us if any value matches.
    """
    print("Example 12 — search pattern that returns a boolean")

    values = [2, 4, 6, 8, 9, 10]
    has_odd_number = False

    for value in values:
        if value % 2 != 0:
            has_odd_number = True
            break

    if has_odd_number:
        print("The list contains at least one odd number.")
    else:
        print("The list contains only even numbers.")

    print()


def example_13_loop_summary_report() -> None:
    """
    Combine several loop ideas to build a small summary report.

    - Count how many students passed.
    - Calculate the average grade.
    """
    print("Example 13 — loop-based summary report")

    student_grades = {
        "Ana": 9.5,
        "Luis": 6.8,
        "Pablo": 7.2,
        "Carla": 8.9,
    }

    passing_grade = 7.0
    total = 0.0
    passed_count = 0

    for name, grade in student_grades.items():
        total += grade
        if grade >= passing_grade:
            passed_count += 1
            status = "PASSED"
        else:
            status = "FAILED"

        print(f"{name:5} -> {grade:.1f} ({status})")

    average = total / len(student_grades)
    print(f"\nClass average: {average:.2f}")
    print(f"Students passed: {passed_count} / {len(student_grades)}\n")


# ---------------------------------------------------------
# Main entry point
# ---------------------------------------------------------


def main() -> None:
    """Run all examples in order."""
    # Rank 1
    example_1_for_loop_over_list()
    example_2_for_loop_with_range()
    example_3_while_loop_basic_counter()

    # Rank 2
    example_4_sum_numbers_with_for()
    example_5_while_loop_with_condition_flag()

    # Rank 3
    example_6_break_in_for_loop()
    example_7_continue_in_for_loop()
    example_8_for_loop_with_enumerate()

    # Rank 4
    example_9_loop_over_dictionary_items()
    example_10_nested_loops()

    # Rank 5
    example_11_filter_with_loop()
    example_12_search_pattern_with_boolean_result()
    example_13_loop_summary_report()


if __name__ == "__main__":
    main()
