"""
Module: Variables Basics
Description: Learn the fundamentals of variables in Python

This module covers:
- Variable declaration and assignment
- Variable naming conventions
- Variable types and dynamic typing
- Multiple assignment
- Variable reassignment
"""


def demonstrate_basic_variables():
    """
    Demonstrates basic variable declaration and assignment.
    
    Variables in Python don't need explicit type declarations.
    The type is inferred from the value assigned.
    """
    # Basic variable assignment
    name = "Alice"
    age = 25
    height = 5.6
    is_student = True
    
    print("=== Basic Variables ===")
    print(f"Name: {name} (type: {type(name).__name__})")
    print(f"Age: {age} (type: {type(age).__name__})")
    print(f"Height: {height} (type: {type(height).__name__})")
    print(f"Is Student: {is_student} (type: {type(is_student).__name__})")
    print()


def demonstrate_naming_conventions():
    """
    Demonstrates Python variable naming conventions.
    
    Good naming conventions:
    - Use lowercase with underscores (snake_case)
    - Start with letter or underscore
    - Be descriptive and meaningful
    - Avoid Python keywords
    """
    print("=== Naming Conventions ===")
    
    # Good variable names (snake_case)
    first_name = "John"
    user_age = 30
    total_count = 100
    
    # Constants (UPPERCASE)
    MAX_USERS = 1000
    PI = 3.14159
    
    # Private variables (leading underscore)
    _internal_value = 42
    
    print(f"first_name: {first_name}")
    print(f"user_age: {user_age}")
    print(f"total_count: {total_count}")
    print(f"MAX_USERS: {MAX_USERS}")
    print(f"PI: {PI}")
    print(f"_internal_value: {_internal_value}")
    print()


def demonstrate_multiple_assignment():
    """
    Demonstrates multiple variable assignment techniques.
    
    Python allows assigning values to multiple variables simultaneously.
    """
    print("=== Multiple Assignment ===")
    
    # Multiple variables in one line
    x, y, z = 1, 2, 3
    print(f"x={x}, y={y}, z={z}")
    
    # Same value to multiple variables
    a = b = c = 10
    print(f"a={a}, b={b}, c={c}")
    
    # Unpacking a list
    numbers = [5, 10, 15]
    first, second, third = numbers
    print(f"first={first}, second={second}, third={third}")
    
    # Swapping variables
    m, n = 100, 200
    print(f"Before swap: m={m}, n={n}")
    m, n = n, m
    print(f"After swap: m={m}, n={n}")
    print()


def demonstrate_dynamic_typing():
    """
    Demonstrates Python's dynamic typing feature.
    
    Variables can change type during execution.
    """
    print("=== Dynamic Typing ===")
    
    # Variable changing types
    variable = 42
    print(f"variable = {variable} (type: {type(variable).__name__})")
    
    variable = "Now I'm a string"
    print(f"variable = {variable} (type: {type(variable).__name__})")
    
    variable = [1, 2, 3]
    print(f"variable = {variable} (type: {type(variable).__name__})")
    
    variable = True
    print(f"variable = {variable} (type: {type(variable).__name__})")
    print()


def demonstrate_variable_scope():
    """
    Demonstrates variable scope concepts.
    
    Variables can be local or global depending on where they're defined.
    """
    print("=== Variable Scope ===")
    
    global_var = "I'm global"
    
    def inner_function():
        local_var = "I'm local"
        print(f"Inside function - global_var: {global_var}")
        print(f"Inside function - local_var: {local_var}")
    
    inner_function()
    print(f"Outside function - global_var: {global_var}")
    # print(local_var)  # This would cause an error!
    print()


# EXERCISES
def exercise_1():
    """
    Exercise 1: Create variables for a person's profile
    
    TODO: Create variables for:
    - Full name
    - Email address
    - Phone number
    - Years of experience
    - Is employed (boolean)
    
    Then print them in a formatted way.
    """
    print("=== Exercise 1: Person Profile ===")
    
    # Your code here
    full_name = "Jane Doe"
    email = "jane.doe@example.com"
    phone = "+1-555-0123"
    years_experience = 5
    is_employed = True
    
    print(f"Profile:")
    print(f"  Name: {full_name}")
    print(f"  Email: {email}")
    print(f"  Phone: {phone}")
    print(f"  Experience: {years_experience} years")
    print(f"  Employed: {'Yes' if is_employed else 'No'}")
    print()


def exercise_2():
    """
    Exercise 2: Variable swap challenge
    
    TODO: Swap the values of three variables in a circular manner
    a -> b, b -> c, c -> a
    """
    print("=== Exercise 2: Circular Swap ===")
    
    a = "Apple"
    b = "Banana"
    c = "Cherry"
    
    print(f"Before: a={a}, b={b}, c={c}")
    
    # Your code here (try to do it in one line!)
    a, b, c = c, a, b
    
    print(f"After: a={a}, b={b}, c={c}")
    print()


def exercise_3():
    """
    Exercise 3: Calculate and store results
    
    TODO: Create variables for different measurements and calculate:
    - Perimeter of a rectangle (2 * length + 2 * width)
    - Area of a rectangle (length * width)
    - Store the results in appropriately named variables
    """
    print("=== Exercise 3: Rectangle Calculations ===")
    
    # Your code here
    length = 10
    width = 5
    
    perimeter = 2 * length + 2 * width
    area = length * width
    
    print(f"Rectangle dimensions: {length} x {width}")
    print(f"Perimeter: {perimeter}")
    print(f"Area: {area}")
    print()


if __name__ == "__main__":
    """
    Main execution block - runs all demonstrations and exercises.
    """
    print("=" * 60)
    print("VARIABLES IN PYTHON - COMPLETE GUIDE")
    print("=" * 60)
    print()
    
    # Run all demonstrations
    demonstrate_basic_variables()
    demonstrate_naming_conventions()
    demonstrate_multiple_assignment()
    demonstrate_dynamic_typing()
    demonstrate_variable_scope()
    
    # Run all exercises
    print("=" * 60)
    print("EXERCISES")
    print("=" * 60)
    print()
    
    exercise_1()
    exercise_2()
    exercise_3()
    
    print("=" * 60)
    print("END OF VARIABLES MODULE")
    print("=" * 60)
