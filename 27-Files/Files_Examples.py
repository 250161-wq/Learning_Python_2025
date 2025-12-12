"""
Files_Examples.py
Module 27 — Working with Files
Author: Peyman Miyandashti
Year: 2025

This file contains practical examples showing:
- Reading files
- Writing files
- Appending to files
- Looping through file lines
- Handling missing files
- Using 'with' for safety

NOTE:
These examples use sample filenames. Replace them with real paths if needed.
"""


# ---------------------------------------------------------------------------
# Example 1: Writing to a file (creates or overwrites)
# ---------------------------------------------------------------------------

with open("example_write.txt", "w") as f:
    f.write("Hello, Peyman!\n")
    f.write("This file was written using Python.\n")


# ---------------------------------------------------------------------------
# Example 2: Reading an entire file
# ---------------------------------------------------------------------------

with open("example_write.txt", "r") as f:
    content = f.read()
    print("File content:\n", content)


# ---------------------------------------------------------------------------
# Example 3: Appending to an existing file
# ---------------------------------------------------------------------------

with open("example_write.txt", "a") as f:
    f.write("This is an appended line.\n")


# ---------------------------------------------------------------------------
# Example 4: Reading line by line
# ---------------------------------------------------------------------------

with open("example_write.txt", "r") as f:
    print("Reading line by line:")
    for line in f:
        print("Line:", line.strip())


# ---------------------------------------------------------------------------
# Example 5: Using readline() and readlines()
# ---------------------------------------------------------------------------

with open("example_write.txt", "r") as f:
    first_line = f.readline()
    all_lines = f.readlines()

print("First line:", first_line.strip())
print("Remaining lines:", [line.strip() for line in all_lines])


# ---------------------------------------------------------------------------
# Example 6: Writing numbers to a file
# ---------------------------------------------------------------------------

numbers = [100, 200, 300, 400]

with open("numbers.txt", "w") as f:
    for num in numbers:
        f.write(str(num) + "\n")


# ---------------------------------------------------------------------------
# Example 7: Reading numeric values back from file
# ---------------------------------------------------------------------------

with open("numbers.txt", "r") as f:
    nums_read = [int(line) for line in f]

print("Numbers read:", nums_read)


# ---------------------------------------------------------------------------
# Example 8: Safe file opening with try/except
# ---------------------------------------------------------------------------

try:
    with open("maybe_exists.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File 'maybe_exists.txt' not found — handled safely.")


# ---------------------------------------------------------------------------
# Example 9: Writing and reading a log file
# ---------------------------------------------------------------------------

with open("log.txt", "a") as log:
    log.write("New log entry: Program executed successfully.\n")

with open("log.txt", "r") as log:
    print("Log file content:")
    print(log.read())


# ---------------------------------------------------------------------------
# Example 10: Using file paths (relative)
# ---------------------------------------------------------------------------

with open("folder_example.txt", "w") as f:
    f.write("This file is in a relative path.\n")

with open("folder_example.txt", "r") as f:
    print("Relative file content:", f.read())


# ---------------------------------------------------------------------------
# Example 11: Overwriting vs appending demonstration
# ---------------------------------------------------------------------------

with open("overwrite_demo.txt", "w") as f:
    f.write("First write.\n")

with open("overwrite_demo.txt", "w") as f:
    f.write("This overwrites the previous content.\n")

with open("overwrite_demo.txt", "a") as f:
    f.write("This is appended, not overwritten.\n")

with open("overwrite_demo.txt", "r") as f:
    print("Overwrite/appending result:\n", f.read())
