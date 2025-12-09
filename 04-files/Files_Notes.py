"""
Module 4 — Working with Files: Notes & Explanations
---------------------------------------------------

This module introduces how Python reads, writes, and manipulates files.
File handling is a critical skill for real-world programming: data
processing, logging, configuration management, automation, reporting, etc.

Python provides simple and powerful tools for working with files:
- The built-in `open()` function
- Context managers (`with`)
- File modes: read, write, append, update
- Reading techniques: full file, line-by-line, chunks
- Writing and appending text
- Safe file handling using try/except
- Modern path handling with the `pathlib` library
"""


# ---------------------------------------------------------------------------
# 1. What Is a File?
# ---------------------------------------------------------------------------
"""
A file is a container for data stored on disk. Files can contain text,
numbers, logs, structured data (CSV, JSON), or binary content (images,
audio, etc.).

Python treats files as *streams* of data that we can read or write.
Before interacting with a file, Python must open it — this creates a
file object that provides methods to:
- read
- write
- iterate through lines
- close the file when finished
"""


# ---------------------------------------------------------------------------
# 2. The open() Function
# ---------------------------------------------------------------------------
"""
Basic syntax:

    file = open("filename.txt", "mode")

Common modes:
- "r"  → read (default)
- "w"  → write (overwrite file)
- "a"  → append (add to end of file)
- "r+" → read + write
- "w+" → write + read (overwrites file)
- "a+" → append + read

IMPORTANT:
Always close files after opening them, or use a context manager (`with`)
which closes the file automatically.
"""

# Example: opening and closing a file manually
# file = open("example.txt", "r")
# content = file.read()
# file.close()


# ---------------------------------------------------------------------------
# 3. Using Context Managers (with open(...))
# ---------------------------------------------------------------------------
"""
The BEST and most professional way to work with files in Python is using
a context manager. It guarantees:
- The file is closed automatically.
- Errors inside the block do not leave the file open.
"""

# Example:
# with open("data.txt", "r") as f:
#     text = f.read()
# print(text)


# ---------------------------------------------------------------------------
# 4. Reading Files
# ---------------------------------------------------------------------------
"""
Python provides several ways to read file contents.
"""


# 4.1 read(): read entire file at once
# -----------------------------------------------------
# Example:
# with open("notes.txt", "r") as f:
#     content = f.read()
# print(content)


# 4.2 readline(): read one line at a time
# -----------------------------------------------------
# Example:
# with open("notes.txt", "r") as f:
#     line = f.readline()
#     print("First line:", line)


# 4.3 readlines(): read all lines into a list
# -----------------------------------------------------
# Example:
# with open("notes.txt", "r") as f:
#     lines = f.readlines()
# print(lines)


# 4.4 Loop through a file
# -----------------------------------------------------
# Example:
# with open("notes.txt", "r") as f:
#     for line in f:
#         print("Line:", line.strip())


# ---------------------------------------------------------------------------
# 5. Writing Files
# ---------------------------------------------------------------------------
"""
Writing to files uses mode "w" (overwrite) or "a" (append).

- "w": creates a new file or clears existing content
- "a": adds content to the end of the file
"""


# Example: write text
# with open("output.txt", "w") as f:
#     f.write("Hello, file!\n")
#     f.write("Writing more text.\n")


# Example: append text
# with open("output.txt", "a") as f:
#     f.write("Adding a new line.\n")


# ---------------------------------------------------------------------------
# 6. Reading and Writing Structured Data (simple parsing)
# ---------------------------------------------------------------------------
"""
Many real-world files contain structured data — logs, CSV-like lines,
lists of values, key/value pairs, etc.

Example file example.csv:
    Alice,24
    Bob,30
    Charlie,28

We can parse this easily:
"""

# Example:
# with open("example.csv", "r") as f:
#     for line in f:
#         name, age = line.strip().split(",")
#         print(name, "is", age)


# ---------------------------------------------------------------------------
# 7. Using pathlib for File Paths (Professional Best Practice)
# ---------------------------------------------------------------------------
"""
Instead of working with raw strings like "folder/data.txt",
professionals use the `pathlib` library:

- It makes file paths OS-independent.
- It provides clean methods for reading/writing.

Example:
"""

from pathlib import Path

# file_path = Path("data") / "notes.txt"
# if file_path.exists():
#     text = file_path.read_text()
#     print(text)


# ---------------------------------------------------------------------------
# 8. Error Handling with try/except
# ---------------------------------------------------------------------------
"""
Files may not exist or may be locked, so error handling is important.

Example:
"""

def read_file_safe(path: str) -> str:
    """Return file contents or an error message if file not found."""
    try:
        with open(path, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "Error: File does not exist."
    except PermissionError:
        return "Error: Permission denied."


# ---------------------------------------------------------------------------
# 9. Writing Utility Functions for Reuse
# ---------------------------------------------------------------------------
"""
Here are some professional examples of reusable file helper functions.
"""


def write_lines(path: str, lines: list[str]) -> None:
    """Write a list of lines to a file, one per line."""
    with open(path, "w") as f:
        for line in lines:
            f.write(line + "\n")


def append_line(path: str, text: str) -> None:
    """Append a single line to a file."""
    with open(path, "a") as f:
        f.write(text + "\n")


def count_lines(path: str) -> int:
    """Return the number of lines in a file."""
    with open(path, "r") as f:
        return sum(1 for _ in f)


# ---------------------------------------------------------------------------
# 10. Summary
# ---------------------------------------------------------------------------
"""
In this module I learned:

- How to open files safely using `open()` and context managers
- The difference between read(), readline(), readlines()
- How to write and append text to files
- How to loop through files efficiently
- How to parse simple structured text data
- How to use pathlib for modern, clean file handling
- How to handle file-related errors properly
- How to write reusable file utility functions

Next steps:
- Practice these concepts in Files_Examples.py
- Complete the exercises in Files_Tasks.py
"""
