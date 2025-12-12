"""
Files_Notes.py
Module 27 — Working with Files
Author: Peyman Miyandashti
Year: 2025

This module explains how Python reads, writes, and manages files on disk.
File handling is essential for saving data, loading data, processing documents,
creating logs, and interacting with the operating system.

In this file, I cover:
- How to open files
- File access modes (r, w, a, etc.)
- Reading files safely
- Writing and appending text
- Using 'with' for automatic cleanup
- Handling missing files with try/except
- Best practices for file operations
"""


# ---------------------------------------------------------------------------
# 1. What Is File Handling?
# ---------------------------------------------------------------------------
# File handling allows a Python program to:
# - read text from a file
# - write text to a file
# - save results permanently
# - load data from previous runs
#
# Python uses the built-in open() function to interact with files.


# ---------------------------------------------------------------------------
# 2. File Modes
# ---------------------------------------------------------------------------
# open("filename", "mode")
#
# Common modes:
#   "r"  → read (file must exist)
#   "w"  → write (creates file or overwrites existing!)
#   "a"  → append (write at end of file)
#
# Read + write:
#   "r+" → read and write (file must exist)
#   "w+" → write and read (overwrites!)
#   "a+" → append and read
#
# Binary modes (for images, bytes, etc.):
#   "rb" → read binary
#   "wb" → write binary
#   "ab" → append binary


# ---------------------------------------------------------------------------
# 3. Reading Files
# ---------------------------------------------------------------------------
# read()       → returns entire file as a single string
# readline()   → returns one line at a time
# readlines()  → returns a list of lines
#
# Example text file content:
#   line1
#   line2
#   line3

# Example (commented):
# file = open("example.txt", "r")
# content = file.read()
# print(content)
# file.close()


# ---------------------------------------------------------------------------
# 4. Best Practice: Use the 'with' Statement
# ---------------------------------------------------------------------------
# Using 'with' automatically closes the file, even if errors happen.

# Example (commented):
# with open("example.txt", "r") as file:
#     text = file.read()
#     print(text)


# ---------------------------------------------------------------------------
# 5. Writing to Files
# ---------------------------------------------------------------------------
# "w" mode overwrites the file completely!

# Example (commented):
# with open("notes.txt", "w") as f:
#     f.write("Hello, World!\n")
#     f.write("This is Peyman's Python file.\n")


# ---------------------------------------------------------------------------
# 6. Appending to Files
# ---------------------------------------------------------------------------
# "a" mode adds new content at the END of the file without deleting anything.

# Example (commented):
# with open("notes.txt", "a") as f:
#     f.write("Another line added.\n")


# ---------------------------------------------------------------------------
# 7. Reading Files Line by Line
# ---------------------------------------------------------------------------
# The most memory-efficient way to process large files.

# Example (commented):
# with open("data.txt", "r") as f:
#     for line in f:
#         print("Line:", line.strip())


# ---------------------------------------------------------------------------
# 8. Handling Missing Files
# ---------------------------------------------------------------------------
# If a file does not exist, "open(..., 'r')" will crash.
# Use try/except to avoid errors.

# Example:
try:
    with open("file_that_might_not_exist.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found — safe handling.")


# ---------------------------------------------------------------------------
# 9. File Paths
# ---------------------------------------------------------------------------
# Files can be accessed with:
# - relative paths (same folder)
# - absolute paths (full location)
#
# Example relative path:
#   "folder/data.txt"
#
# Example absolute path:
#   "C:/Users/Peyman/Documents/data.txt"


# ---------------------------------------------------------------------------
# 10. Writing and Reading Lists of Data
# ---------------------------------------------------------------------------

# Writing:
# with open("scores.txt", "w") as f:
#     for score in [90, 85, 100]:
#         f.write(str(score) + "\n")

# Reading:
# with open("scores.txt", "r") as f:
#     scores = [int(line) for line in f]


# ---------------------------------------------------------------------------
# 11. Best Practices Summary
# ---------------------------------------------------------------------------
# ✔ Always use 'with' for file operations
# ✔ Be careful with "w" mode — it deletes old content
# ✔ Use "a" mode for logs or incremental writes
# ✔ Use try/except when opening unknown files
# ✔ Use meaningful filenames
# ✔ Clean and strip() lines when processing
# ✔ Separate reading and writing logic for clarity


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# File handling is one of the most important skills in Python.
# It allows programs to store information, reload data, process documents,
# manage logs, and perform real-world tasks outside of memory.
#
# Next Step:
# Continue with Files_Examples.py to see practical demonstrations.
