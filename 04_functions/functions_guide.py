"""
Module: Functions in Python
Description: Comprehensive guide to functions in Python

This module covers:
- Function definition and calling
- Parameters and arguments
- Return values
- Default parameters
- *args and **kwargs
- Lambda functions
- Scope and closures
- Decorators
- Recursion
"""


def demonstrate_basic_functions():
    """
    Demonstrates basic function definition and calling.
    
    Functions are reusable blocks of code that perform specific tasks.
    """
    print("=== Basic Functions ===")
    
    # Simple function without parameters
    def greet():
        """Prints a greeting message."""
        print("Hello, World!")
    
    greet()
    
    # Function with parameters
    def greet_person(name):
        """Prints a personalized greeting."""
        print(f"Hello, {name}!")
    
    greet_person("Alice")
    
    # Function with multiple parameters
    def add_numbers(a, b):
        """Adds two numbers and returns the result."""
        return a + b
    
    result = add_numbers(5, 3)
    print(f"5 + 3 = {result}")
    
    print()


def demonstrate_return_values():
    """
    Demonstrates different return value scenarios.
    """
    print("=== Return Values ===")
    
    # Single return value
    def square(x):
        """Returns the square of a number."""
        return x ** 2
    
    print(f"Square of 4: {square(4)}")
    
    # Multiple return values (tuple)
    def get_stats(numbers):
        """Returns min, max, and average of a list."""
        return min(numbers), max(numbers), sum(numbers) / len(numbers)
    
    data = [10, 20, 30, 40, 50]
    minimum, maximum, average = get_stats(data)
    print(f"Stats of {data}:")
    print(f"  Min: {minimum}, Max: {maximum}, Avg: {average}")
    
    # No return (returns None)
    def print_message(msg):
        """Prints a message without returning anything."""
        print(f"Message: {msg}")
    
    result = print_message("Test")
    print(f"Return value: {result}")
    
    print()


def demonstrate_default_parameters():
    """
    Demonstrates default parameter values.
    
    Default parameters allow function calls with fewer arguments.
    """
    print("=== Default Parameters ===")
    
    def greet(name, greeting="Hello"):
        """Greets a person with a customizable greeting."""
        print(f"{greeting}, {name}!")
    
    greet("Alice")  # Uses default greeting
    greet("Bob", "Hi")  # Custom greeting
    greet("Charlie", greeting="Hey")  # Named argument
    
    # Multiple defaults
    def create_profile(name, age=18, city="Unknown"):
        """Creates a user profile with some defaults."""
        return f"{name}, {age} years old, from {city}"
    
    print(create_profile("Alice"))
    print(create_profile("Bob", 25))
    print(create_profile("Charlie", 30, "New York"))
    
    print()


def demonstrate_args_kwargs():
    """
    Demonstrates *args and **kwargs for variable arguments.
    
    *args: Variable number of positional arguments
    **kwargs: Variable number of keyword arguments
    """
    print("=== *args and **kwargs ===")
    
    # *args - variable positional arguments
    def sum_all(*args):
        """Sums all provided numbers."""
        return sum(args)
    
    print(f"Sum of 1, 2, 3: {sum_all(1, 2, 3)}")
    print(f"Sum of 1, 2, 3, 4, 5: {sum_all(1, 2, 3, 4, 5)}")
    
    # **kwargs - variable keyword arguments
    def print_info(**kwargs):
        """Prints all key-value pairs."""
        for key, value in kwargs.items():
            print(f"  {key}: {value}")
    
    print("Person info:")
    print_info(name="Alice", age=25, city="New York")
    
    # Combined
    def flexible_function(*args, **kwargs):
        """Accepts any combination of arguments."""
        print(f"Positional args: {args}")
        print(f"Keyword args: {kwargs}")
    
    print("\nFlexible function:")
    flexible_function(1, 2, 3, name="Test", value=42)
    
    print()


def demonstrate_lambda_functions():
    """
    Demonstrates lambda functions (anonymous functions).
    
    Lambda functions are small, one-line functions without a name.
    """
    print("=== Lambda Functions ===")
    
    # Basic lambda
    square = lambda x: x ** 2
    print(f"Square of 5: {square(5)}")
    
    # Lambda with multiple arguments
    add = lambda x, y: x + y
    print(f"3 + 4 = {add(3, 4)}")
    
    # Lambda in sorted
    people = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 30},
        {"name": "Charlie", "age": 20}
    ]
    sorted_by_age = sorted(people, key=lambda x: x["age"])
    print(f"Sorted by age: {sorted_by_age}")
    
    # Lambda in map
    numbers = [1, 2, 3, 4, 5]
    squared = list(map(lambda x: x ** 2, numbers))
    print(f"Squared using map: {squared}")
    
    # Lambda in filter
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"Even numbers using filter: {even_numbers}")
    
    print()


def demonstrate_scope():
    """
    Demonstrates variable scope: local, enclosing, global, built-in (LEGB).
    """
    print("=== Variable Scope ===")
    
    global_var = "I'm global"
    
    def outer_function():
        enclosing_var = "I'm in enclosing scope"
        
        def inner_function():
            local_var = "I'm local"
            print(f"Local: {local_var}")
            print(f"Enclosing: {enclosing_var}")
            print(f"Global: {global_var}")
        
        inner_function()
    
    outer_function()
    
    # Modifying global variable
    def modify_global():
        global global_var
        global_var = "Modified global"
    
    print(f"Before: {global_var}")
    modify_global()
    print(f"After: {global_var}")
    
    print()


def demonstrate_closures():
    """
    Demonstrates closures - functions that remember enclosing scope.
    """
    print("=== Closures ===")
    
    def make_multiplier(n):
        """Returns a function that multiplies by n."""
        def multiplier(x):
            return x * n
        return multiplier
    
    times_2 = make_multiplier(2)
    times_3 = make_multiplier(3)
    
    print(f"5 * 2 = {times_2(5)}")
    print(f"5 * 3 = {times_3(5)}")
    
    # Counter closure
    def make_counter():
        """Returns a counter function."""
        count = 0
        
        def counter():
            nonlocal count
            count += 1
            return count
        
        return counter
    
    counter1 = make_counter()
    counter2 = make_counter()
    
    print(f"Counter1: {counter1()}, {counter1()}, {counter1()}")
    print(f"Counter2: {counter2()}, {counter2()}")
    
    print()


def demonstrate_decorators():
    """
    Demonstrates decorators - functions that modify other functions.
    """
    print("=== Decorators ===")
    
    # Simple decorator
    def uppercase_decorator(func):
        """Decorator that uppercases the result."""
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result.upper()
        return wrapper
    
    @uppercase_decorator
    def greet(name):
        return f"hello, {name}"
    
    print(greet("alice"))
    
    # Timing decorator
    import time
    
    def timer_decorator(func):
        """Decorator that times function execution."""
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"  {func.__name__} took {end - start:.6f} seconds")
            return result
        return wrapper
    
    @timer_decorator
    def slow_function():
        time.sleep(0.1)
        return "Done"
    
    print(slow_function())
    
    print()


def demonstrate_recursion():
    """
    Demonstrates recursive functions - functions that call themselves.
    """
    print("=== Recursion ===")
    
    # Factorial
    def factorial(n):
        """Calculates factorial using recursion."""
        if n <= 1:
            return 1
        return n * factorial(n - 1)
    
    print(f"Factorial of 5: {factorial(5)}")
    
    # Fibonacci
    def fibonacci(n):
        """Calculates nth Fibonacci number."""
        if n <= 1:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)
    
    print(f"First 10 Fibonacci numbers:")
    fib_numbers = [fibonacci(i) for i in range(10)]
    print(f"  {fib_numbers}")
    
    # Sum of list
    def sum_list(numbers):
        """Sums a list using recursion."""
        if not numbers:
            return 0
        return numbers[0] + sum_list(numbers[1:])
    
    print(f"Sum of [1,2,3,4,5]: {sum_list([1, 2, 3, 4, 5])}")
    
    print()


def demonstrate_function_annotations():
    """
    Demonstrates function annotations (type hints).
    """
    print("=== Function Annotations ===")
    
    def greet(name: str, age: int) -> str:
        """
        Greets a person with type hints.
        
        Args:
            name: Person's name
            age: Person's age
            
        Returns:
            Greeting message
        """
        return f"Hello {name}, you are {age} years old"
    
    result = greet("Alice", 25)
    print(result)
    print(f"Annotations: {greet.__annotations__}")
    
    print()


# EXERCISES
def exercise_1():
    """
    Exercise 1: Temperature Converter
    
    TODO: Create functions to convert:
    - Celsius to Fahrenheit
    - Fahrenheit to Celsius
    - Test with various temperatures
    """
    print("=== Exercise 1: Temperature Converter ===")
    
    # Your code here
    def celsius_to_fahrenheit(celsius):
        """Converts Celsius to Fahrenheit."""
        return (celsius * 9/5) + 32
    
    def fahrenheit_to_celsius(fahrenheit):
        """Converts Fahrenheit to Celsius."""
        return (fahrenheit - 32) * 5/9
    
    temps_c = [0, 100, 25, -40]
    print("Celsius to Fahrenheit:")
    for temp in temps_c:
        print(f"  {temp}°C = {celsius_to_fahrenheit(temp):.2f}°F")
    
    temps_f = [32, 212, 77, -40]
    print("\nFahrenheit to Celsius:")
    for temp in temps_f:
        print(f"  {temp}°F = {fahrenheit_to_celsius(temp):.2f}°C")
    
    print()


def exercise_2():
    """
    Exercise 2: List Statistics
    
    TODO: Create a function that takes a list and returns:
    - Mean, median, and mode
    - Use appropriate error handling
    """
    print("=== Exercise 2: List Statistics ===")
    
    # Your code here
    def calculate_statistics(numbers):
        """Calculates mean, median, and mode."""
        if not numbers:
            return None, None, None
        
        # Mean
        mean = sum(numbers) / len(numbers)
        
        # Median
        sorted_nums = sorted(numbers)
        n = len(sorted_nums)
        if n % 2 == 0:
            median = (sorted_nums[n//2 - 1] + sorted_nums[n//2]) / 2
        else:
            median = sorted_nums[n//2]
        
        # Mode (simple version)
        from collections import Counter
        count = Counter(numbers)
        mode = count.most_common(1)[0][0]
        
        return mean, median, mode
    
    data = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7]
    mean, median, mode = calculate_statistics(data)
    print(f"Data: {data}")
    print(f"Mean: {mean:.2f}")
    print(f"Median: {median}")
    print(f"Mode: {mode}")
    print()


def exercise_3():
    """
    Exercise 3: Password Validator
    
    TODO: Create a function that validates a password:
    - At least 8 characters
    - Contains uppercase and lowercase
    - Contains at least one digit
    - Contains at least one special character
    """
    print("=== Exercise 3: Password Validator ===")
    
    # Your code here
    def validate_password(password):
        """Validates password strength."""
        if len(password) < 8:
            return False, "Too short (minimum 8 characters)"
        
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(not c.isalnum() for c in password)
        
        if not has_upper:
            return False, "Missing uppercase letter"
        if not has_lower:
            return False, "Missing lowercase letter"
        if not has_digit:
            return False, "Missing digit"
        if not has_special:
            return False, "Missing special character"
        
        return True, "Strong password"
    
    test_passwords = [
        "weak",
        "StrongPass1!",
        "nodigits!",
        "NOLOWER1!",
        "NoSpecial1"
    ]
    
    for pwd in test_passwords:
        valid, message = validate_password(pwd)
        status = "✓" if valid else "✗"
        print(f"  {status} '{pwd}': {message}")
    
    print()


def exercise_4():
    """
    Exercise 4: Decorator Practice
    
    TODO: Create a decorator that:
    - Logs function calls with arguments
    - Counts how many times a function is called
    """
    print("=== Exercise 4: Logging Decorator ===")
    
    # Your code here
    def call_logger(func):
        """Decorator that logs function calls."""
        count = 0
        
        def wrapper(*args, **kwargs):
            nonlocal count
            count += 1
            print(f"  Call #{count}: {func.__name__}{args}")
            result = func(*args, **kwargs)
            print(f"    Returned: {result}")
            return result
        
        return wrapper
    
    @call_logger
    def add(a, b):
        return a + b
    
    add(2, 3)
    add(5, 7)
    add(10, 20)
    print()


def exercise_5():
    """
    Exercise 5: Recursive Directory Size
    
    TODO: Create a recursive function to calculate:
    - Sum of all numbers in a nested list
    - Handle lists of any depth
    """
    print("=== Exercise 5: Recursive Sum ===")
    
    # Your code here
    def recursive_sum(data):
        """Recursively sums all numbers in nested list."""
        total = 0
        for item in data:
            if isinstance(item, list):
                total += recursive_sum(item)
            else:
                total += item
        return total
    
    nested_list = [1, [2, 3, [4, 5]], 6, [7, [8, 9]]]
    result = recursive_sum(nested_list)
    print(f"Nested list: {nested_list}")
    print(f"Sum: {result}")
    print()


if __name__ == "__main__":
    """
    Main execution block - runs all demonstrations and exercises.
    """
    print("=" * 60)
    print("FUNCTIONS IN PYTHON - COMPLETE GUIDE")
    print("=" * 60)
    print()
    
    # Run all demonstrations
    demonstrate_basic_functions()
    demonstrate_return_values()
    demonstrate_default_parameters()
    demonstrate_args_kwargs()
    demonstrate_lambda_functions()
    demonstrate_scope()
    demonstrate_closures()
    demonstrate_decorators()
    demonstrate_recursion()
    demonstrate_function_annotations()
    
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
    print("END OF FUNCTIONS MODULE")
    print("=" * 60)
