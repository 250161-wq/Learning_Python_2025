"""
Module 17 — Exceptions (try/except)
Practice File: exceptions_tasks.py

Goal:
- Learn how to use try/except, else, finally.
- Learn how to handle common errors:
  * ZeroDivisionError
  * ValueError
  * TypeError
  * FileNotFoundError
  * KeyError
- Learn how to create and raise your own exceptions.

IMPORTANT:
- Do NOT just read. TYPE the code and experiment.
- For each TASK, follow the TODO comments.
- You can add print() to see what is happening.

Author: Peyman Miyandashti
Year: 2025
Repository: Learning_Python_2025
"""


# ===========================================================
# TASK 1 — Basic try/except with division
# Handle ZeroDivisionError
# ===========================================================

def task1_division():
    """
    TODO:
    1. Ask the user for a number (as input).
    2. Try to divide 100 by that number.
    3. Use try/except to:
       - Catch ZeroDivisionError if the user types 0.
       - Print a friendly error message.
    4. If everything is ok, print the result.
    """
    # Write your code here
    pass


# ===========================================================
# TASK 2 — Converting input to int (ValueError)
# ===========================================================

def task2_convert_age():
    """
    Scenario:
    Peyman wants to convert a string to an integer age.

    TODO:
    1. Ask the user: "Enter your age: "
    2. Try to convert it to int.
    3. If the user types something NOT numeric (like 'hello'),
       a ValueError will happen.
    4. Use try/except to:
       - Catch ValueError.
       - Print: "Please enter a valid number for age."
    5. If conversion works, print:
       "In 10 years, you will be <age + 10> years old."
    """
    # Write your code here
    pass


# ===========================================================
# TASK 3 — Working with a file (FileNotFoundError)
# ===========================================================

def task3_read_profile_file():
    """
    Scenario:
    You want to read a file called 'peyman_profile.txt'.

    TODO:
    1. Use try/except when opening the file:
          open("peyman_profile.txt", "r")
    2. Catch FileNotFoundError and print:
          "File not found. Please create 'peyman_profile.txt' first."
    3. If the file exists:
       - Read the contents.
       - Print the text.
    4. Add a finally block that prints:
          "Done trying to read the file."
    """
    # Write your code here
    pass


# ===========================================================
# TASK 4 — List index out of range (IndexError)
# ===========================================================

def task4_list_index():
    """
    Scenario:
    You have a list of Peyman's favorite numbers.

    favorites = [11, 7, 3]

    TODO:
    1. Create the list above.
    2. Ask the user: "Enter an index (0, 1, or 2): "
    3. Convert the input to int.
    4. Use try/except to:
       - Try to print favorites[index]
       - Catch IndexError and print:
         "Index out of range! Please choose 0, 1, or 2."
       - Catch ValueError (if user types something not a number) and print:
         "Please enter a number for the index."
    """
    # Write your code here
    pass


# ===========================================================
# TASK 5 — Dictionary and KeyError
# ===========================================================

def task5_profile_dict():
    """
    Scenario:
    Peyman has a small profile stored in a dictionary.

    profile = {
        "name": "Peyman Miyandashti",
        "age": 43,
        "city": "Mexicali",
        "country": "Mexico",
    }

    TODO:
    1. Create the profile dict above (you can add more keys if you want).
    2. Ask the user: "Which field do you want to see? (name/age/city/country): "
    3. Use try/except to:
       - Try to print profile[user_field]
       - Catch KeyError and print:
         "That field does not exist in the profile."
    4. Optionally, show the user all valid keys when there is an error.
    """
    # Write your code here
    pass


# ===========================================================
# TASK 6 — Safe division function (try/except/else/finally)
# ===========================================================

def safe_divide(a, b):
    """
    TODO:
    1. Use try/except to divide a by b.
    2. Catch ZeroDivisionError and print:
       "You cannot divide by zero."
       Then return None.
    3. Use else to:
       - Print "Division successful."
       - Return the result.
    4. Use finally to print:
       "Finished safe_divide operation."
    """
    # Write your code here
    pass


def task6_test_safe_divide():
    """
    TODO:
    1. Call safe_divide(100, 0)
    2. Call safe_divide(100, 4)
    3. Print the results of each call.
    """
    # Write your code here
    pass


# ===========================================================
# TASK 7 — Multiple exceptions in one block
# ===========================================================

def task7_multiple_exceptions():
    """
    Scenario:
    The user should type a number. You want to calculate 100 / number
    and also use it as an index in a short list.

    numbers = [10, 20, 30]

    TODO:
    1. Create the list above.
    2. Ask the user: "Enter a number: "
    3. Use try/except to do this:
       - Convert input to int.
       - Compute 100 / user_number.
       - Access numbers[user_number].
    4. Catch these exceptions separately:
       - ValueError  -> print: "You must type a number."
       - ZeroDivisionError -> print: "Cannot divide by zero."
       - IndexError  -> print: "Index is out of range for the list."
    5. Optionally, use a generic:
         except Exception as e:
             print("Unexpected error:", e)
    """
    # Write your code here
    pass


# ===========================================================
# TASK 8 — Custom validation + raising ValueError
# ===========================================================

def validate_age(age):
    """
    TODO:
    1. If age < 0 or age > 120:
         - raise ValueError("Age must be between 0 and 120.")
    2. Otherwise, just return age.
    """
    # Write your code here
    pass


def task8_test_validate_age():
    """
    TODO:
    1. Call validate_age(43)  -> should be OK (Peyman's age).
    2. Call validate_age(-5)  -> should raise ValueError.
    3. Wrap the calls in try/except to catch ValueError and print the message.
    """
    # Write your code here
    pass


# ===========================================================
# TASK 9 — Creating your own exception class
# ===========================================================

class InvalidCarYearError(Exception):
    """
    Custom exception for invalid car year.
    Example:
    Peyman's car is Kia Sportage 2024 (valid)
    Arlette's car is Hyundai Creta 2018 (valid)
    """

    # TODO (optional): You can customize this class later if you want.
    pass


def check_car_year(year):
    """
    TODO:
    1. If year < 1990 or year > 2025:
         - raise InvalidCarYearError("Car year is not in the valid range.")
    2. Otherwise, return year.
    """
    # Write your code here
    pass


def task9_test_check_car_year():
    """
    TODO:
    1. Call check_car_year(2024)  -> OK (Peyman's Kia Sportage).
    2. Call check_car_year(2018)  -> OK (Arlette's Hyundai Creta).
    3. Call check_car_year(1800)  -> Should raise InvalidCarYearError.
    4. Use try/except to catch InvalidCarYearError and print the message.
    """
    # Write your code here
    pass


# ===========================================================
# TASK 10 — Combining everything in one mini program
# ===========================================================

def task10_mini_profile_program():
    """
    Scenario:
    Build a small "Peyman profile checker" that uses several exceptions.

    TODO (step by step):
    1. Ask the user for:
       - age (int)
       - car year (int)
    2. Use:
       - validate_age(age)
       - check_car_year(car_year)
       inside a try block.
    3. Catch:
       - ValueError from validate_age
       - InvalidCarYearError from check_car_year
    4. If everything is OK (no exception):
       - Print a nice message like:
         "Profile looks good! Age: <age>, Car year: <car_year>"
    5. Use finally to print:
         "Finished checking Peyman's profile."
    """
    # Write your code here
    pass


# ===========================================================
# RUN SOME TASKS FOR TESTING (OPTIONAL)
# ===========================================================

if __name__ == "__main__":
    print("Module 17 — Exceptions (try/except) Tasks")
    print("Run each task function manually while you practice.")
    # Example: uncomment these as you complete them:
    # task1_division()
    # task2_convert_age()
    # task3_read_profile_file()
    # task4_list_index()
    # task5_profile_dict()
    # task6_test_safe_divide()
    # task7_multiple_exceptions()
    # task8_test_validate_age()
    # task9_test_check_car_year()
    # task10_mini_profile_program()
