"""
Module: Loops in Python
Description: Comprehensive guide to loop constructs in Python

This module covers:
- For loops
- While loops
- Loop control statements (break, continue, pass)
- Nested loops
- List comprehensions
- Loop patterns and best practices
"""


def demonstrate_for_loops():
    """
    Demonstrates for loop usage with different iterables.
    
    For loops iterate over sequences (lists, strings, ranges, etc.).
    """
    print("=== For Loops ===")
    
    # Basic for loop with list
    fruits = ["apple", "banana", "cherry"]
    print("Iterating over list:")
    for fruit in fruits:
        print(f"  {fruit}")
    
    # For loop with range
    print("\nIterating with range(5):")
    for i in range(5):
        print(f"  Index: {i}")
    
    # For loop with range and start, stop, step
    print("\nRange with start, stop, step - range(0, 10, 2):")
    for i in range(0, 10, 2):
        print(f"  {i}", end=" ")
    print()
    
    # Iterating over string
    print("\nIterating over string:")
    for char in "Python":
        print(f"  {char}", end=" ")
    print()
    
    # Using enumerate for index and value
    print("\nUsing enumerate:")
    for index, fruit in enumerate(fruits):
        print(f"  {index}: {fruit}")
    
    print()


def demonstrate_while_loops():
    """
    Demonstrates while loop usage.
    
    While loops continue executing while a condition is True.
    """
    print("=== While Loops ===")
    
    # Basic while loop
    print("Counting down from 5:")
    count = 5
    while count > 0:
        print(f"  {count}")
        count -= 1
    print("  Blastoff!")
    
    # While loop with user input simulation
    print("\nWhile loop with condition:")
    number = 1
    while number < 100:
        number *= 2
        print(f"  {number}", end=" ")
    print()
    
    # While True with break
    print("\nWhile True with break:")
    counter = 0
    while True:
        counter += 1
        print(f"  Iteration {counter}")
        if counter >= 3:
            print("  Breaking out!")
            break
    
    print()


def demonstrate_loop_control():
    """
    Demonstrates loop control statements: break, continue, pass.
    
    - break: Exit the loop immediately
    - continue: Skip to next iteration
    - pass: Do nothing (placeholder)
    """
    print("=== Loop Control Statements ===")
    
    # Break statement
    print("Break example - find first even number:")
    numbers = [1, 3, 5, 7, 8, 9, 10, 11]
    for num in numbers:
        if num % 2 == 0:
            print(f"  First even number: {num}")
            break
    
    # Continue statement
    print("\nContinue example - skip odd numbers:")
    for num in range(10):
        if num % 2 != 0:
            continue
        print(f"  {num}", end=" ")
    print()
    
    # Pass statement
    print("\nPass example - placeholder:")
    for i in range(3):
        if i == 1:
            pass  # TODO: Implement later
        else:
            print(f"  Processing {i}")
    
    print()


def demonstrate_nested_loops():
    """
    Demonstrates nested loops for working with multi-dimensional data.
    """
    print("=== Nested Loops ===")
    
    # Simple multiplication table
    print("Multiplication table (3x3):")
    for i in range(1, 4):
        for j in range(1, 4):
            print(f"{i * j:3d}", end=" ")
        print()
    
    # Pattern printing
    print("\nPattern printing:")
    for i in range(1, 6):
        for j in range(i):
            print("*", end=" ")
        print()
    
    # Working with 2D list
    print("\n2D list iteration:")
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    for row in matrix:
        for item in row:
            print(f"{item:2d}", end=" ")
        print()
    
    print()


def demonstrate_loop_with_else():
    """
    Demonstrates loop else clause.
    
    The else clause executes if the loop completes normally (no break).
    """
    print("=== Loop with Else Clause ===")
    
    # For loop with else - number found
    print("Searching for number 5:")
    numbers = [1, 2, 3, 4, 5, 6]
    for num in numbers:
        if num == 5:
            print(f"  Found {num}!")
            break
    else:
        print("  Number not found")
    
    # For loop with else - number not found
    print("\nSearching for number 10:")
    for num in numbers:
        if num == 10:
            print(f"  Found {num}!")
            break
    else:
        print("  Number not found (else clause executed)")
    
    # While loop with else
    print("\nWhile loop with else:")
    count = 0
    while count < 3:
        print(f"  Count: {count}")
        count += 1
    else:
        print("  Loop completed normally")
    
    print()


def demonstrate_list_comprehensions():
    """
    Demonstrates list comprehensions - concise way to create lists.
    
    List comprehensions provide a more Pythonic way to create lists.
    """
    print("=== List Comprehensions ===")
    
    # Basic list comprehension
    squares = [x**2 for x in range(10)]
    print(f"Squares: {squares}")
    
    # With condition
    even_squares = [x**2 for x in range(10) if x % 2 == 0]
    print(f"Even squares: {even_squares}")
    
    # String operations
    fruits = ["apple", "banana", "cherry"]
    uppercase_fruits = [fruit.upper() for fruit in fruits]
    print(f"Uppercase: {uppercase_fruits}")
    
    # Nested list comprehension
    matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
    print(f"Matrix: {matrix}")
    
    # Dictionary comprehension
    squares_dict = {x: x**2 for x in range(5)}
    print(f"Squares dict: {squares_dict}")
    
    # Set comprehension
    unique_lengths = {len(fruit) for fruit in fruits}
    print(f"Unique lengths: {unique_lengths}")
    
    print()


def demonstrate_loop_patterns():
    """
    Demonstrates common loop patterns and best practices.
    """
    print("=== Common Loop Patterns ===")
    
    # Iterating over multiple lists with zip
    print("Using zip:")
    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]
    for name, age in zip(names, ages):
        print(f"  {name} is {age} years old")
    
    # Iterating in reverse
    print("\nReverse iteration:")
    for num in reversed(range(5)):
        print(f"  {num}", end=" ")
    print()
    
    # Iterating with sorted
    print("\nSorted iteration:")
    fruits = ["banana", "apple", "cherry"]
    for fruit in sorted(fruits):
        print(f"  {fruit}", end=" ")
    print()
    
    # Sum and accumulation
    print("\nAccumulation pattern:")
    numbers = [1, 2, 3, 4, 5]
    total = 0
    for num in numbers:
        total += num
    print(f"  Sum: {total}")
    
    # Finding maximum
    print("\nFinding maximum:")
    numbers = [3, 7, 2, 9, 1]
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    print(f"  Maximum: {max_num}")
    
    print()


# EXERCISES
def exercise_1():
    """
    Exercise 1: FizzBuzz
    
    TODO: Print numbers 1 to 30, but:
    - Print "Fizz" for multiples of 3
    - Print "Buzz" for multiples of 5
    - Print "FizzBuzz" for multiples of both
    """
    print("=== Exercise 1: FizzBuzz ===")
    
    # Your code here
    for i in range(1, 31):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
    print("\n")


def exercise_2():
    """
    Exercise 2: Prime Number Finder
    
    TODO: Find all prime numbers between 1 and 50
    A prime number is only divisible by 1 and itself
    """
    print("=== Exercise 2: Prime Numbers ===")
    
    # Your code here
    primes = []
    for num in range(2, 51):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    
    print(f"Prime numbers: {primes}")
    print(f"Count: {len(primes)}")
    print()


def exercise_3():
    """
    Exercise 3: List Processing
    
    TODO: Given a list of numbers:
    - Create a new list with only even numbers
    - Calculate sum of all numbers
    - Find average
    - Use list comprehension where possible
    """
    print("=== Exercise 3: List Processing ===")
    
    # Your code here
    numbers = [12, 7, 23, 45, 8, 16, 31, 50, 9, 14]
    
    print(f"Original: {numbers}")
    
    # Even numbers using list comprehension
    even_numbers = [num for num in numbers if num % 2 == 0]
    print(f"Even numbers: {even_numbers}")
    
    # Sum
    total = sum(numbers)
    print(f"Sum: {total}")
    
    # Average
    average = total / len(numbers)
    print(f"Average: {average:.2f}")
    print()


def exercise_4():
    """
    Exercise 4: Pattern Challenge
    
    TODO: Create a pyramid pattern with numbers
    Example:
        1
       121
      12321
     1234321
    """
    print("=== Exercise 4: Number Pyramid ===")
    
    # Your code here
    n = 4
    for i in range(1, n + 1):
        # Print spaces
        print(" " * (n - i), end="")
        
        # Print ascending numbers
        for j in range(1, i + 1):
            print(j, end="")
        
        # Print descending numbers
        for j in range(i - 1, 0, -1):
            print(j, end="")
        
        print()
    print()


def exercise_5():
    """
    Exercise 5: Dictionary from Lists
    
    TODO: Create a dictionary from two lists using a loop
    - Keys: student names
    - Values: their grades
    - Calculate class average
    """
    print("=== Exercise 5: Student Grades ===")
    
    # Your code here
    students = ["Alice", "Bob", "Charlie", "David", "Eve"]
    grades = [85, 92, 78, 95, 88]
    
    # Create dictionary
    student_grades = {}
    for student, grade in zip(students, grades):
        student_grades[student] = grade
    
    print("Student Grades:")
    for student, grade in student_grades.items():
        print(f"  {student}: {grade}")
    
    # Calculate average
    class_average = sum(student_grades.values()) / len(student_grades)
    print(f"\nClass Average: {class_average:.2f}")
    print()


if __name__ == "__main__":
    """
    Main execution block - runs all demonstrations and exercises.
    """
    print("=" * 60)
    print("LOOPS IN PYTHON - COMPLETE GUIDE")
    print("=" * 60)
    print()
    
    # Run all demonstrations
    demonstrate_for_loops()
    demonstrate_while_loops()
    demonstrate_loop_control()
    demonstrate_nested_loops()
    demonstrate_loop_with_else()
    demonstrate_list_comprehensions()
    demonstrate_loop_patterns()
    
    # Run all exercises
    print("=" * 60)
    print("EXERCISES")
    print("=" * 60)
    print()
    
    exercise_1()
    exercise_2()
    exercise_3()
    exercise_4()
    exercise_5()
    
    print("=" * 60)
    print("END OF LOOPS MODULE")
    print("=" * 60)
