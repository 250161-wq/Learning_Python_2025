"""
Module: Working with Files in Python
Description: Comprehensive guide to file operations in Python

This module covers:
- Reading and writing text files
- File modes and context managers
- Working with CSV files
- Working with binary files
- File and directory operations
- Error handling with files
- Best practices
"""

import os
import csv
import json
from pathlib import Path


def demonstrate_basic_file_operations():
    """
    Demonstrates basic file reading and writing operations.
    """
    print("=== Basic File Operations ===")
    
    # Writing to a file
    print("Writing to file...")
    with open("../data/sample.txt", "w") as file:
        file.write("Hello, World!\n")
        file.write("This is a test file.\n")
        file.write("Python file operations are easy!\n")
    print("  File written successfully")
    
    # Reading entire file
    print("\nReading entire file:")
    with open("../data/sample.txt", "r") as file:
        content = file.read()
        print(content)
    
    # Reading line by line
    print("Reading line by line:")
    with open("../data/sample.txt", "r") as file:
        for i, line in enumerate(file, 1):
            print(f"  Line {i}: {line.strip()}")
    
    print()


def demonstrate_file_modes():
    """
    Demonstrates different file opening modes.
    
    Common modes:
    - 'r': Read (default)
    - 'w': Write (overwrites)
    - 'a': Append
    - 'r+': Read and write
    - 'b': Binary mode
    """
    print("=== File Modes ===")
    
    # Write mode (overwrites)
    print("Write mode (w):")
    with open("../data/modes_test.txt", "w") as file:
        file.write("First line\n")
    print("  File created with 'First line'")
    
    # Append mode
    print("\nAppend mode (a):")
    with open("../data/modes_test.txt", "a") as file:
        file.write("Second line\n")
        file.write("Third line\n")
    print("  Added two more lines")
    
    # Read and display
    with open("../data/modes_test.txt", "r") as file:
        print("  Content:")
        for line in file:
            print(f"    {line.strip()}")
    
    print()


def demonstrate_context_managers():
    """
    Demonstrates why context managers (with statement) are important.
    
    Context managers ensure files are properly closed even if errors occur.
    """
    print("=== Context Managers ===")
    
    # Good practice: Using with statement
    print("Using context manager (recommended):")
    with open("../data/context_test.txt", "w") as file:
        file.write("Context managers automatically close files\n")
        file.write("Even if an error occurs!\n")
    print("  File automatically closed")
    
    # Alternative (not recommended)
    print("\nWithout context manager (not recommended):")
    file = open("../data/no_context.txt", "w")
    file.write("Need to manually close\n")
    file.close()
    print("  File manually closed")
    
    print()


def demonstrate_reading_methods():
    """
    Demonstrates different methods to read files.
    """
    print("=== Reading Methods ===")
    
    # Create sample file
    with open("../data/reading_test.txt", "w") as file:
        file.write("Line 1\n")
        file.write("Line 2\n")
        file.write("Line 3\n")
        file.write("Line 4\n")
    
    # read() - reads entire file
    print("Using read():")
    with open("../data/reading_test.txt", "r") as file:
        content = file.read()
        print(f"  Type: {type(content)}, Length: {len(content)}")
    
    # readline() - reads one line at a time
    print("\nUsing readline():")
    with open("../data/reading_test.txt", "r") as file:
        line1 = file.readline()
        line2 = file.readline()
        print(f"  First: {line1.strip()}")
        print(f"  Second: {line2.strip()}")
    
    # readlines() - reads all lines into a list
    print("\nUsing readlines():")
    with open("../data/reading_test.txt", "r") as file:
        lines = file.readlines()
        print(f"  Type: {type(lines)}, Count: {len(lines)}")
        print(f"  Lines: {[line.strip() for line in lines]}")
    
    print()


def demonstrate_csv_operations():
    """
    Demonstrates working with CSV files.
    
    CSV (Comma-Separated Values) is a common format for tabular data.
    """
    print("=== CSV Operations ===")
    
    # Writing CSV
    print("Writing CSV file:")
    csv_file = "../data/students.csv"
    
    with open(csv_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age", "Grade"])  # Header
        writer.writerow(["Alice", 20, "A"])
        writer.writerow(["Bob", 21, "B"])
        writer.writerow(["Charlie", 19, "A"])
    print("  CSV file created")
    
    # Reading CSV
    print("\nReading CSV file:")
    with open(csv_file, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"  {row}")
    
    # Using DictReader
    print("\nUsing DictReader:")
    with open(csv_file, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"  {row['Name']} is {row['Age']} years old, grade: {row['Grade']}")
    
    # Using DictWriter
    print("\nUsing DictWriter:")
    with open("../data/products.csv", "w", newline="") as file:
        fieldnames = ["Product", "Price", "Stock"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerow({"Product": "Apple", "Price": 1.50, "Stock": 100})
        writer.writerow({"Product": "Banana", "Price": 0.75, "Stock": 150})
    print("  Products CSV created")
    
    print()


def demonstrate_file_paths():
    """
    Demonstrates working with file paths using pathlib.
    
    pathlib provides an object-oriented way to work with file paths.
    """
    print("=== File Paths with pathlib ===")
    
    # Current directory
    current_dir = Path.cwd()
    print(f"Current directory: {current_dir}")
    
    # Creating paths
    data_dir = Path("../data")
    file_path = data_dir / "test.txt"
    print(f"File path: {file_path}")
    
    # Path properties
    print(f"\nPath properties:")
    print(f"  Name: {file_path.name}")
    print(f"  Suffix: {file_path.suffix}")
    print(f"  Parent: {file_path.parent}")
    print(f"  Absolute: {file_path.absolute()}")
    
    # Check existence
    print(f"\nExists: {file_path.exists()}")
    
    # Create file
    file_path.write_text("Created using pathlib")
    print(f"After creation - Exists: {file_path.exists()}")
    
    # Read file
    content = file_path.read_text()
    print(f"Content: {content}")
    
    print()


def demonstrate_directory_operations():
    """
    Demonstrates directory operations.
    """
    print("=== Directory Operations ===")
    
    # Create directory
    test_dir = Path("../data/test_directory")
    test_dir.mkdir(exist_ok=True)
    print(f"Created directory: {test_dir}")
    
    # List files in directory
    print("\nFiles in data directory:")
    data_dir = Path("../data")
    for item in data_dir.iterdir():
        file_type = "DIR" if item.is_dir() else "FILE"
        print(f"  [{file_type}] {item.name}")
    
    # Find specific files
    print("\nCSV files in data directory:")
    for csv_file in data_dir.glob("*.csv"):
        print(f"  {csv_file.name}")
    
    print()


def demonstrate_error_handling():
    """
    Demonstrates error handling with file operations.
    """
    print("=== Error Handling ===")
    
    # File not found
    print("Handling FileNotFoundError:")
    try:
        with open("nonexistent.txt", "r") as file:
            content = file.read()
    except FileNotFoundError:
        print("  Error: File does not exist!")
    
    # Permission error (simulate)
    print("\nHandling PermissionError:")
    try:
        with open("../data/test_write.txt", "w") as file:
            file.write("Test")
        # Try to write to a read-only file (in a real scenario)
        print("  File operations successful")
    except PermissionError:
        print("  Error: Permission denied!")
    
    # Generic exception handling
    print("\nGeneric exception handling:")
    filename = "../data/safe_test.txt"
    try:
        with open(filename, "r") as file:
            content = file.read()
            print(f"  Successfully read: {len(content)} characters")
    except FileNotFoundError:
        print(f"  Creating new file: {filename}")
        with open(filename, "w") as file:
            file.write("New file created")
    except Exception as e:
        print(f"  Unexpected error: {e}")
    
    print()


def demonstrate_binary_files():
    """
    Demonstrates working with binary files.
    """
    print("=== Binary File Operations ===")
    
    # Write binary data
    print("Writing binary file:")
    binary_data = bytes([65, 66, 67, 68, 69])  # ASCII: ABCDE
    with open("../data/binary_test.bin", "wb") as file:
        file.write(binary_data)
    print(f"  Written: {binary_data}")
    
    # Read binary data
    print("\nReading binary file:")
    with open("../data/binary_test.bin", "rb") as file:
        data = file.read()
        print(f"  Read: {data}")
        print(f"  As text: {data.decode('ascii')}")
    
    print()


# EXERCISES
def exercise_1():
    """
    Exercise 1: Log File Writer
    
    TODO: Create a function that writes log entries to a file
    - Each entry should have timestamp
    - Append to existing log
    - Format: [TIMESTAMP] MESSAGE
    """
    print("=== Exercise 1: Log File Writer ===")
    
    from datetime import datetime
    
    def write_log(message, log_file="../data/app.log"):
        """Writes a timestamped log entry."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"
        
        with open(log_file, "a") as file:
            file.write(log_entry)
    
    # Test the function
    write_log("Application started")
    write_log("User logged in")
    write_log("Data processed successfully")
    
    print("Log entries written:")
    with open("../data/app.log", "r") as file:
        for line in file:
            print(f"  {line.strip()}")
    
    print()


def exercise_2():
    """
    Exercise 2: CSV Data Analyzer
    
    TODO: Read the students.csv file and:
    - Calculate average age
    - Count grade distribution
    - Find youngest and oldest student
    """
    print("=== Exercise 2: CSV Data Analyzer ===")
    
    csv_file = "../data/students.csv"
    
    students = []
    with open(csv_file, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({
                "name": row["Name"],
                "age": int(row["Age"]),
                "grade": row["Grade"]
            })
    
    # Average age
    avg_age = sum(s["age"] for s in students) / len(students)
    print(f"Average age: {avg_age:.1f}")
    
    # Grade distribution
    from collections import Counter
    grades = [s["grade"] for s in students]
    distribution = Counter(grades)
    print(f"Grade distribution: {dict(distribution)}")
    
    # Youngest and oldest
    youngest = min(students, key=lambda s: s["age"])
    oldest = max(students, key=lambda s: s["age"])
    print(f"Youngest: {youngest['name']} ({youngest['age']})")
    print(f"Oldest: {oldest['name']} ({oldest['age']})")
    
    print()


def exercise_3():
    """
    Exercise 3: File Backup
    
    TODO: Create a function that:
    - Reads a file
    - Creates a backup with .bak extension
    - Preserves original content
    """
    print("=== Exercise 3: File Backup ===")
    
    def backup_file(filename):
        """Creates a backup of a file."""
        source = Path(filename)
        if not source.exists():
            print(f"  Error: {filename} does not exist")
            return
        
        backup = source.with_suffix(source.suffix + ".bak")
        content = source.read_text()
        backup.write_text(content)
        print(f"  Backup created: {backup.name}")
    
    # Create test file and backup
    test_file = "../data/important.txt"
    with open(test_file, "w") as file:
        file.write("Important data that needs backup\n")
    
    backup_file(test_file)
    
    # Verify backup
    backup_path = Path(test_file).with_suffix(".txt.bak")
    if backup_path.exists():
        print(f"  Backup verified: {backup_path.read_text().strip()}")
    
    print()


def exercise_4():
    """
    Exercise 4: Word Counter
    
    TODO: Create a function that:
    - Reads a text file
    - Counts total words
    - Finds most common words
    - Counts lines and characters
    """
    print("=== Exercise 4: Word Counter ===")
    
    # Create sample text file
    sample_text = """Python is a great programming language.
Python is easy to learn and powerful.
Many developers love Python for its simplicity.
Python has a large community."""
    
    with open("../data/sample_text.txt", "w") as file:
        file.write(sample_text)
    
    def analyze_text(filename):
        """Analyzes text file statistics."""
        with open(filename, "r") as file:
            lines = file.readlines()
        
        # Basic stats
        num_lines = len(lines)
        num_chars = sum(len(line) for line in lines)
        
        # Word analysis
        words = []
        for line in lines:
            words.extend(line.lower().split())
        
        num_words = len(words)
        
        # Most common words
        from collections import Counter
        word_freq = Counter(words)
        most_common = word_freq.most_common(5)
        
        return {
            "lines": num_lines,
            "characters": num_chars,
            "words": num_words,
            "most_common": most_common
        }
    
    stats = analyze_text("../data/sample_text.txt")
    print(f"Lines: {stats['lines']}")
    print(f"Characters: {stats['characters']}")
    print(f"Words: {stats['words']}")
    print("Most common words:")
    for word, count in stats["most_common"]:
        print(f"  {word}: {count}")
    
    print()


def exercise_5():
    """
    Exercise 5: Configuration File Handler
    
    TODO: Create functions to:
    - Save configuration as JSON
    - Load configuration from JSON
    - Update specific settings
    """
    print("=== Exercise 5: Configuration Handler ===")
    
    def save_config(config, filename="../data/config.json"):
        """Saves configuration to JSON file."""
        with open(filename, "w") as file:
            json.dump(config, file, indent=2)
    
    def load_config(filename="../data/config.json"):
        """Loads configuration from JSON file."""
        try:
            with open(filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
    
    def update_config(key, value, filename="../data/config.json"):
        """Updates a specific configuration setting."""
        config = load_config(filename)
        config[key] = value
        save_config(config, filename)
    
    # Test the functions
    initial_config = {
        "app_name": "MyApp",
        "version": "1.0.0",
        "debug": True,
        "max_users": 100
    }
    
    save_config(initial_config)
    print("Initial config saved")
    
    loaded = load_config()
    print(f"Loaded config: {loaded}")
    
    update_config("version", "1.0.1")
    update_config("debug", False)
    print("\nAfter updates:")
    print(f"Updated config: {load_config()}")
    
    print()


if __name__ == "__main__":
    """
    Main execution block - runs all demonstrations and exercises.
    """
    # Ensure data directory exists
    Path("../data").mkdir(exist_ok=True)
    
    print("=" * 60)
    print("FILE OPERATIONS IN PYTHON - COMPLETE GUIDE")
    print("=" * 60)
    print()
    
    # Run all demonstrations
    demonstrate_basic_file_operations()
    demonstrate_file_modes()
    demonstrate_context_managers()
    demonstrate_reading_methods()
    demonstrate_csv_operations()
    demonstrate_file_paths()
    demonstrate_directory_operations()
    demonstrate_error_handling()
    demonstrate_binary_files()
    
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
    print("END OF FILE OPERATIONS MODULE")
    print("=" * 60)
