"""
Python Variables - Complete Tutorial
=====================================

Welcome to the first module of Learning Python 2025!
This script teaches you everything about variables in Python.

Topics covered:
1. What are Variables?
2. Naming Rules
3. Best Practices
4. Data Types Examples
5. Practice Exercises
6. Mini-Project: Personal Information Card

Author: Learning_Python_2025
License: MIT
"""


def print_section(title):
    """Helper function to print section headers."""
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60 + "\n")


def section_1_what_are_variables():
    """Section 1: Introduction to Variables."""
    print_section("1. WHAT ARE VARIABLES?")
    
    print("A variable is a named container that stores data in your program.")
    print("Think of it as a labeled box where you can put information.\n")
    
    # Simple variable examples
    name = "Alice"
    age = 25
    height = 5.6
    is_student = True
    
    print("Basic variable examples:")
    print(f"  Name: {name} (type: {type(name).__name__})")
    print(f"  Age: {age} (type: {type(age).__name__})")
    print(f"  Height: {height} feet (type: {type(height).__name__})")
    print(f"  Is student: {is_student} (type: {type(is_student).__name__})")
    
    # Multiple assignment
    print("\nMultiple assignment:")
    x, y, z = 10, 20, 30
    print(f"  x = {x}, y = {y}, z = {z}")
    
    a = b = c = 100
    print(f"  a = {a}, b = {b}, c = {c} (same value to all)")


def section_2_naming_rules():
    """Section 2: Variable Naming Rules."""
    print_section("2. NAMING RULES")
    
    print("Python has specific rules for naming variables:\n")
    print("✅ MUST follow:")
    print("  1. Start with letter (a-z, A-Z) or underscore (_)")
    print("  2. Can contain letters, numbers, and underscores")
    print("  3. Cannot start with a number")
    print("  4. Cannot contain spaces or special characters")
    print("  5. Cannot be a Python keyword")
    print("  6. Case-sensitive (Name ≠ name)\n")
    
    # Valid examples
    user_name = "John"
    user1 = "Jane"
    _private_var = 42
    myVariable = "camelCase"
    MY_CONSTANT = 3.14
    
    print("Valid variable names created successfully!")
    
    # Demonstrating case sensitivity
    name = "Alice"
    Name = "Bob"
    NAME = "Charlie"
    print(f"\nCase sensitivity example:")
    print(f"  name = {name}")
    print(f"  Name = {Name}")
    print(f"  NAME = {NAME}")
    print("  All three are different variables!")


def section_3_best_practices():
    """Section 3: Best Practices."""
    print_section("3. BEST PRACTICES")
    
    print("Python naming conventions:\n")
    print("🎯 snake_case for variables and functions")
    print("   Examples: user_name, total_price, is_valid\n")
    print("🎯 UPPER_CASE for constants")
    print("   Examples: MAX_SIZE, PI, DATABASE_URL\n")
    print("🎯 Use descriptive names")
    print("   Good: student_age, total_score")
    print("   Bad: x, temp, data\n")
    
    # Good examples
    user_age = 30
    first_name = "Sarah"
    is_active = True
    MAX_ATTEMPTS = 3
    PI = 3.14159
    
    print("Good naming examples:")
    print(f"  user_age = {user_age}")
    print(f"  first_name = {first_name}")
    print(f"  MAX_ATTEMPTS = {MAX_ATTEMPTS}")
    
    # Poor examples (works but not recommended)
    x = 30
    a = "Sarah"
    print("\n⚠️  Poor naming (avoid these):")
    print(f"  x = {x}  (What does x represent?)")
    print(f"  a = {a}  (What is 'a'?)")


def section_4_data_types():
    """Section 4: Data Types Examples."""
    print_section("4. DATA TYPES EXAMPLES")
    
    # 4.1 Numeric Types
    print("4.1 Numeric Types\n")
    age = 25
    price = 19.99
    complex_num = 3 + 4j
    
    print(f"  Integer: {age} (type: {type(age).__name__})")
    print(f"  Float: {price} (type: {type(price).__name__})")
    print(f"  Complex: {complex_num} (type: {type(complex_num).__name__})")
    
    # 4.2 String Type
    print("\n4.2 String Type\n")
    first_name = "John"
    last_name = "Doe"
    full_name = f"{first_name} {last_name}"
    
    print(f"  First name: {first_name}")
    print(f"  Last name: {last_name}")
    print(f"  Full name: {full_name}")
    print(f"  Uppercase: {full_name.upper()}")
    print(f"  Length: {len(full_name)} characters")
    
    # 4.3 Boolean Type
    print("\n4.3 Boolean Type\n")
    is_student = True
    is_employed = False
    age = 20
    is_adult = age >= 18
    
    print(f"  Is student: {is_student}")
    print(f"  Is employed: {is_employed}")
    print(f"  Is adult (age >= 18): {is_adult}")
    
    # 4.4 List Type
    print("\n4.4 List Type\n")
    fruits = ["apple", "banana", "orange", "grape"]
    numbers = [1, 2, 3, 4, 5]
    
    print(f"  Fruits: {fruits}")
    print(f"  First fruit: {fruits[0]}")
    print(f"  Last fruit: {fruits[-1]}")
    print(f"  List length: {len(fruits)}")
    
    # 4.5 Tuple Type
    print("\n4.5 Tuple Type\n")
    coordinates = (10, 20)
    rgb_color = (255, 128, 0)
    
    print(f"  Coordinates: {coordinates}")
    print(f"  RGB Color: {rgb_color}")
    print(f"  X coordinate: {coordinates[0]}")
    print(f"  Y coordinate: {coordinates[1]}")
    print("  Note: Tuples are immutable (cannot be changed)")
    
    # 4.6 Dictionary Type
    print("\n4.6 Dictionary Type\n")
    student = {
        "name": "Alice",
        "age": 20,
        "grade": "A",
        "is_enrolled": True
    }
    
    print(f"  Student: {student}")
    print(f"  Name: {student['name']}")
    print(f"  Age: {student['age']}")
    print(f"  Grade: {student['grade']}")
    
    # 4.7 Set Type
    print("\n4.7 Set Type\n")
    unique_numbers = {1, 2, 3, 4, 5}
    colors = {"red", "green", "blue"}
    numbers_with_duplicates = {1, 2, 2, 3, 3, 3, 4, 5, 5}
    
    print(f"  Unique numbers: {unique_numbers}")
    print(f"  Colors: {colors}")
    print(f"  With duplicates removed: {numbers_with_duplicates}")
    
    # 4.8 Type Conversion
    print("\n4.8 Type Conversion\n")
    str_num = "42"
    int_num = int(str_num)
    print(f"  String '{str_num}' to Integer: {int_num}")
    
    num = 100
    str_num = str(num)
    print(f"  Integer {num} to String: '{str_num}'")
    
    my_list = [1, 2, 3]
    my_tuple = tuple(my_list)
    print(f"  List {my_list} to Tuple: {my_tuple}")


def section_5_practice_exercises():
    """Section 5: Practice Exercises (with solutions)."""
    print_section("5. PRACTICE EXERCISES")
    
    print("Exercise 1: Basic Variable Assignment\n")
    favorite_book = "To Kill a Mockingbird"
    favorite_movie = "The Shawshank Redemption"
    favorite_song = "Bohemian Rhapsody"
    
    print("My Favorites:")
    print(f"  Book: {favorite_book}")
    print(f"  Movie: {favorite_movie}")
    print(f"  Song: {favorite_song}")
    
    print("\n" + "-" * 60)
    print("Exercise 2: Variable Swap\n")
    a = 5
    b = 10
    print(f"Before swap: a = {a}, b = {b}")
    
    # Python's elegant way to swap
    a, b = b, a
    print(f"After swap: a = {a}, b = {b}")
    
    print("\n" + "-" * 60)
    print("Exercise 3: Data Type Identification\n")
    var1 = 42
    var2 = 3.14
    var3 = "Hello"
    var4 = True
    var5 = [1, 2, 3]
    
    print(f"  var1 = {var1}, Type: {type(var1).__name__}")
    print(f"  var2 = {var2}, Type: {type(var2).__name__}")
    print(f"  var3 = {var3}, Type: {type(var3).__name__}")
    print(f"  var4 = {var4}, Type: {type(var4).__name__}")
    print(f"  var5 = {var5}, Type: {type(var5).__name__}")
    
    print("\n" + "-" * 60)
    print("Exercise 4: String Manipulation\n")
    first_name = "John"
    last_name = "Doe"
    full_name = f"{first_name} {last_name}"
    
    print(f"  Full name: {full_name}")
    print(f"  Uppercase: {full_name.upper()}")
    print(f"  Lowercase: {full_name.lower()}")
    print(f"  Title case: {full_name.title()}")
    
    print("\n" + "-" * 60)
    print("Exercise 5: List Operations\n")
    favorite_foods = ["Pizza", "Sushi", "Tacos", "Pasta", "Burgers"]
    print(f"  Original list: {favorite_foods}")
    
    favorite_foods.append("Ice Cream")
    print(f"  After adding: {favorite_foods}")
    
    favorite_foods.remove("Burgers")
    print(f"  After removing: {favorite_foods}")
    print(f"  Total favorite foods: {len(favorite_foods)}")
    
    print("\n" + "-" * 60)
    print("Exercise 6: Dictionary Creation\n")
    car = {
        "brand": "Toyota",
        "model": "Camry",
        "year": 2024,
        "color": "Silver"
    }
    
    print("  Car Information:")
    print(f"    Brand: {car['brand']}")
    print(f"    Model: {car['model']}")
    print(f"    Year: {car['year']}")
    print(f"    Color: {car['color']}")


def section_6_mini_project():
    """Section 6: Mini-Project - Personal Information Card."""
    print_section("6. MINI-PROJECT: PERSONAL INFORMATION CARD")
    
    # Sample data for the personal information card
    full_name = "Alex Johnson"
    age = 25
    city = "San Francisco"
    country = "USA"
    occupation = "Software Developer"
    
    hobbies = ["Reading", "Hiking", "Photography", "Coding"]
    skills = ["Python", "JavaScript", "Data Analysis", "Problem Solving"]
    
    contact_info = {
        "email": "alex.johnson@example.com",
        "github": "github.com/alexj",
        "linkedin": "linkedin.com/in/alexjohnson"
    }
    
    education = {
        "degree": "Bachelor of Science in Computer Science",
        "institution": "Stanford University",
        "year": 2023
    }
    
    years_of_experience = 2
    favorite_language = "Python"
    is_available = True
    
    # Display the information card
    print("=" * 50)
    print(" " * 15 + "PERSONAL INFORMATION CARD")
    print("=" * 50)
    print(f"\n👤 Name: {full_name}")
    print(f"🎂 Age: {age} years old")
    print(f"📍 Location: {city}, {country}")
    print(f"💼 Occupation: {occupation}")
    print(f"⏱️  Experience: {years_of_experience} years")
    print(f"💻 Favorite Language: {favorite_language}")
    print(f"✅ Available for opportunities: {is_available}")
    
    print(f"\n🎯 Hobbies:")
    for i, hobby in enumerate(hobbies, 1):
        print(f"   {i}. {hobby}")
    
    print(f"\n💡 Skills:")
    for i, skill in enumerate(skills, 1):
        print(f"   {i}. {skill}")
    
    print(f"\n📧 Contact Information:")
    print(f"   Email: {contact_info['email']}")
    print(f"   GitHub: {contact_info['github']}")
    print(f"   LinkedIn: {contact_info['linkedin']}")
    
    print(f"\n🎓 Education:")
    print(f"   Degree: {education['degree']}")
    print(f"   Institution: {education['institution']}")
    print(f"   Year: {education['year']}")
    
    print("\n" + "=" * 50)
    print(" " * 10 + "Thank you for viewing my profile!")
    print("=" * 50)
    
    # Bonus statistics
    print("\n📊 Profile Statistics:")
    print(f"   Total hobbies: {len(hobbies)}")
    print(f"   Total skills: {len(skills)}")
    print(f"   Contact methods: {len(contact_info)}")
    print(f"   Profile completeness: 100%")


def main():
    """Main function to run all sections."""
    print("\n" + "=" * 60)
    print("  PYTHON VARIABLES - COMPLETE TUTORIAL")
    print("  Learning_Python_2025 - Module 01")
    print("=" * 60)
    
    # Run all sections
    section_1_what_are_variables()
    section_2_naming_rules()
    section_3_best_practices()
    section_4_data_types()
    section_5_practice_exercises()
    section_6_mini_project()
    
    # Conclusion
    print("\n" + "=" * 60)
    print("  🎉 CONGRATULATIONS!")
    print("=" * 60)
    print("\nYou've completed the Variables tutorial!")
    print("\nYou now know:")
    print("  ✅ What variables are and how to use them")
    print("  ✅ Variable naming rules and conventions")
    print("  ✅ Best practices for writing clean code")
    print("  ✅ Different data types in Python")
    print("  ✅ How to work with various data structures")
    print("  ✅ Type conversion between different types")
    print("  ✅ How to build a practical mini-project")
    print("\nNext Steps:")
    print("  1. Practice creating variables in your own projects")
    print("  2. Experiment with different data types")
    print("  3. Move on to the next module in Learning_Python_2025")
    print("\nHappy Coding! 🐍\n")


if __name__ == "__main__":
    main()
