"""
Module: Data Types in Python
Description: Comprehensive guide to Python's built-in data types

This module covers:
- Numeric types (int, float, complex)
- String type and operations
- Boolean type
- List, Tuple, Set, Dictionary
- Type conversion
- None type
"""


def demonstrate_numeric_types():
    """
    Demonstrates numeric data types: int, float, and complex.
    
    Python supports three numeric types:
    - int: Whole numbers (unlimited precision)
    - float: Decimal numbers
    - complex: Complex numbers with real and imaginary parts
    """
    print("=== Numeric Types ===")
    
    # Integer
    integer_num = 42
    large_int = 123456789012345678901234567890
    print(f"Integer: {integer_num} (type: {type(integer_num).__name__})")
    print(f"Large Integer: {large_int}")
    
    # Float
    float_num = 3.14159
    scientific_notation = 1.5e-3  # 0.0015
    print(f"Float: {float_num} (type: {type(float_num).__name__})")
    print(f"Scientific: {scientific_notation}")
    
    # Complex
    complex_num = 3 + 4j
    print(f"Complex: {complex_num} (type: {type(complex_num).__name__})")
    print(f"Real part: {complex_num.real}, Imaginary part: {complex_num.imag}")
    
    # Arithmetic operations
    print(f"\nArithmetic: 10 + 3 = {10 + 3}")
    print(f"Division: 10 / 3 = {10 / 3}")
    print(f"Floor division: 10 // 3 = {10 // 3}")
    print(f"Modulo: 10 % 3 = {10 % 3}")
    print(f"Power: 2 ** 3 = {2 ** 3}")
    print()


def demonstrate_strings():
    """
    Demonstrates string data type and common operations.
    
    Strings are immutable sequences of characters.
    """
    print("=== String Type ===")
    
    # Different ways to create strings
    single_quote = 'Hello'
    double_quote = "World"
    triple_quote = """This is a
    multiline string"""
    
    print(f"Single quotes: {single_quote}")
    print(f"Double quotes: {double_quote}")
    print(f"Triple quotes: {triple_quote}")
    
    # String operations
    full_string = "Python Programming"
    print(f"\nOriginal: {full_string}")
    print(f"Length: {len(full_string)}")
    print(f"Uppercase: {full_string.upper()}")
    print(f"Lowercase: {full_string.lower()}")
    print(f"Replace: {full_string.replace('Python', 'Java')}")
    print(f"Split: {full_string.split()}")
    
    # String indexing and slicing
    print(f"\nIndexing: first char = '{full_string[0]}', last char = '{full_string[-1]}'")
    print(f"Slicing: first 6 chars = '{full_string[:6]}'")
    print(f"Slicing: last 11 chars = '{full_string[-11:]}'")
    
    # String formatting
    name = "Alice"
    age = 25
    print(f"\nFormatting: My name is {name} and I'm {age} years old")
    print()


def demonstrate_boolean():
    """
    Demonstrates boolean data type and logical operations.
    
    Boolean represents True or False values.
    """
    print("=== Boolean Type ===")
    
    is_python_fun = True
    is_difficult = False
    
    print(f"is_python_fun: {is_python_fun} (type: {type(is_python_fun).__name__})")
    print(f"is_difficult: {is_difficult}")
    
    # Logical operations
    print(f"\nAND: True and False = {True and False}")
    print(f"OR: True or False = {True or False}")
    print(f"NOT: not True = {not True}")
    
    # Comparison operations return boolean
    print(f"\nComparisons:")
    print(f"10 > 5 = {10 > 5}")
    print(f"10 == 10 = {10 == 10}")
    print(f"10 != 5 = {10 != 5}")
    
    # Truthy and Falsy values
    print(f"\nTruthy/Falsy:")
    print(f"bool(0) = {bool(0)}")
    print(f"bool(1) = {bool(1)}")
    print(f"bool('') = {bool('')}")
    print(f"bool('text') = {bool('text')}")
    print()


def demonstrate_lists():
    """
    Demonstrates list data type and operations.
    
    Lists are mutable, ordered sequences that can contain any type.
    """
    print("=== List Type ===")
    
    # Creating lists
    numbers = [1, 2, 3, 4, 5]
    mixed = [1, "two", 3.0, True, [5, 6]]
    empty_list = []
    
    print(f"Numbers list: {numbers}")
    print(f"Mixed list: {mixed}")
    print(f"Empty list: {empty_list}")
    
    # List operations
    fruits = ["apple", "banana", "cherry"]
    print(f"\nOriginal: {fruits}")
    
    # Adding elements
    fruits.append("date")
    print(f"After append: {fruits}")
    
    fruits.insert(1, "blueberry")
    print(f"After insert: {fruits}")
    
    # Removing elements
    fruits.remove("banana")
    print(f"After remove: {fruits}")
    
    popped = fruits.pop()
    print(f"After pop: {fruits}, popped: {popped}")
    
    # Accessing elements
    print(f"\nFirst fruit: {fruits[0]}")
    print(f"Last fruit: {fruits[-1]}")
    print(f"Slice [1:3]: {fruits[1:3]}")
    
    # List methods
    numbers = [3, 1, 4, 1, 5, 9, 2]
    print(f"\nNumbers: {numbers}")
    print(f"Sorted: {sorted(numbers)}")
    print(f"Sum: {sum(numbers)}")
    print(f"Max: {max(numbers)}")
    print(f"Count of 1: {numbers.count(1)}")
    print()


def demonstrate_tuples():
    """
    Demonstrates tuple data type and operations.
    
    Tuples are immutable, ordered sequences.
    """
    print("=== Tuple Type ===")
    
    # Creating tuples
    coordinates = (10, 20)
    single_element = (42,)  # Note the comma!
    mixed_tuple = (1, "two", 3.0)
    
    print(f"Coordinates: {coordinates} (type: {type(coordinates).__name__})")
    print(f"Single element: {single_element}")
    print(f"Mixed tuple: {mixed_tuple}")
    
    # Tuple operations (limited since immutable)
    print(f"\nFirst coordinate: {coordinates[0]}")
    print(f"Last coordinate: {coordinates[-1]}")
    
    # Tuple unpacking
    x, y = coordinates
    print(f"Unpacked: x={x}, y={y}")
    
    # Tuples are immutable
    print("\nNote: Tuples cannot be modified after creation")
    print()


def demonstrate_sets():
    """
    Demonstrates set data type and operations.
    
    Sets are unordered collections of unique elements.
    """
    print("=== Set Type ===")
    
    # Creating sets
    numbers = {1, 2, 3, 4, 5}
    unique_letters = set("hello")  # {'h', 'e', 'l', 'o'}
    
    print(f"Numbers set: {numbers}")
    print(f"Unique letters: {unique_letters}")
    
    # Set operations
    set_a = {1, 2, 3, 4}
    set_b = {3, 4, 5, 6}
    
    print(f"\nSet A: {set_a}")
    print(f"Set B: {set_b}")
    print(f"Union: {set_a | set_b}")
    print(f"Intersection: {set_a & set_b}")
    print(f"Difference: {set_a - set_b}")
    print(f"Symmetric difference: {set_a ^ set_b}")
    
    # Adding and removing
    numbers = {1, 2, 3}
    numbers.add(4)
    print(f"\nAfter add: {numbers}")
    numbers.remove(2)
    print(f"After remove: {numbers}")
    print()


def demonstrate_dictionaries():
    """
    Demonstrates dictionary data type and operations.
    
    Dictionaries are unordered collections of key-value pairs.
    """
    print("=== Dictionary Type ===")
    
    # Creating dictionaries
    person = {
        "name": "Alice",
        "age": 25,
        "city": "New York"
    }
    
    print(f"Person dictionary: {person}")
    
    # Accessing values
    print(f"\nName: {person['name']}")
    print(f"Age: {person.get('age')}")
    print(f"Country: {person.get('country', 'Not specified')}")
    
    # Adding/updating
    person["email"] = "alice@example.com"
    person["age"] = 26
    print(f"\nUpdated: {person}")
    
    # Dictionary methods
    print(f"\nKeys: {list(person.keys())}")
    print(f"Values: {list(person.values())}")
    print(f"Items: {list(person.items())}")
    
    # Iterating
    print("\nIterating:")
    for key, value in person.items():
        print(f"  {key}: {value}")
    print()


def demonstrate_type_conversion():
    """
    Demonstrates type conversion between different data types.
    """
    print("=== Type Conversion ===")
    
    # String to number
    str_num = "42"
    int_num = int(str_num)
    float_num = float(str_num)
    print(f"String '{str_num}' -> int: {int_num}, float: {float_num}")
    
    # Number to string
    number = 123
    str_number = str(number)
    print(f"Number {number} -> string: '{str_number}'")
    
    # List to tuple, set
    my_list = [1, 2, 3, 2, 1]
    my_tuple = tuple(my_list)
    my_set = set(my_list)
    print(f"\nList {my_list}")
    print(f"To tuple: {my_tuple}")
    print(f"To set: {my_set} (duplicates removed)")
    
    # Dictionary to list
    my_dict = {"a": 1, "b": 2}
    keys_list = list(my_dict.keys())
    values_list = list(my_dict.values())
    print(f"\nDict keys: {keys_list}")
    print(f"Dict values: {values_list}")
    print()


def demonstrate_none_type():
    """
    Demonstrates the None type.
    
    None represents the absence of a value.
    """
    print("=== None Type ===")
    
    nothing = None
    print(f"Value: {nothing} (type: {type(nothing).__name__})")
    
    # Common use cases
    def might_return_value(condition):
        if condition:
            return "Value"
        return None
    
    result = might_return_value(False)
    if result is None:
        print("No value returned")
    
    # Checking for None
    print(f"\nIs None: {result is None}")
    print(f"Is not None: {result is not None}")
    print()


# EXERCISES
def exercise_1():
    """
    Exercise 1: Create a student record
    
    TODO: Create a dictionary with student information:
    - Name, age, grades (list), is_enrolled (bool)
    - Add a new grade to the list
    - Calculate average grade
    """
    print("=== Exercise 1: Student Record ===")
    
    # Your code here
    student = {
        "name": "Bob Smith",
        "age": 20,
        "grades": [85, 90, 78, 92],
        "is_enrolled": True
    }
    
    print(f"Student: {student['name']}")
    print(f"Grades: {student['grades']}")
    
    # Add new grade
    student['grades'].append(88)
    print(f"Updated grades: {student['grades']}")
    
    # Calculate average
    average = sum(student['grades']) / len(student['grades'])
    print(f"Average grade: {average:.2f}")
    print()


def exercise_2():
    """
    Exercise 2: Set operations
    
    TODO: Given two sets of course enrollments, find:
    - Students in both courses
    - Students in only one course
    - All unique students
    """
    print("=== Exercise 2: Set Operations ===")
    
    # Your code here
    python_students = {"Alice", "Bob", "Charlie", "David"}
    java_students = {"Charlie", "David", "Eve", "Frank"}
    
    print(f"Python students: {python_students}")
    print(f"Java students: {java_students}")
    
    both_courses = python_students & java_students
    only_python = python_students - java_students
    all_students = python_students | java_students
    
    print(f"In both courses: {both_courses}")
    print(f"Only in Python: {only_python}")
    print(f"All unique students: {all_students}")
    print()


def exercise_3():
    """
    Exercise 3: Type conversion challenge
    
    TODO: Convert between types and handle the data appropriately
    - Convert a string of numbers to a list of integers
    - Find unique numbers using a set
    - Store frequency count in a dictionary
    """
    print("=== Exercise 3: Type Conversion ===")
    
    # Your code here
    numbers_string = "1 2 3 2 4 5 3 6 1 4"
    
    # Convert to list of integers
    numbers_list = [int(x) for x in numbers_string.split()]
    print(f"List: {numbers_list}")
    
    # Get unique numbers
    unique_numbers = set(numbers_list)
    print(f"Unique: {unique_numbers}")
    
    # Count frequency
    frequency = {}
    for num in numbers_list:
        frequency[num] = frequency.get(num, 0) + 1
    print(f"Frequency: {frequency}")
    print()


if __name__ == "__main__":
    """
    Main execution block - runs all demonstrations and exercises.
    """
    print("=" * 60)
    print("DATA TYPES IN PYTHON - COMPLETE GUIDE")
    print("=" * 60)
    print()
    
    # Run all demonstrations
    demonstrate_numeric_types()
    demonstrate_strings()
    demonstrate_boolean()
    demonstrate_lists()
    demonstrate_tuples()
    demonstrate_sets()
    demonstrate_dictionaries()
    demonstrate_type_conversion()
    demonstrate_none_type()
    
    # Run all exercises
    print("=" * 60)
    print("EXERCISES")
    print("=" * 60)
    print()
    
    exercise_1()
    exercise_2()
    exercise_3()
    
    print("=" * 60)
    print("END OF DATA TYPES MODULE")
    print("=" * 60)
