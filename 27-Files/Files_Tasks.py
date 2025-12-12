"""
Files_Tasks.py
Module 27 — Working with Files
Author: Peyman Miyandashti
Year: 2025

Practice exercises for mastering Python file handling.
Tasks progress from simple file reading/writing (Rank 1)
to professional-level file processing systems (Rank 5).

Instructions:
- Complete all tasks BEFORE checking the solutions.
- Use the 'with' statement whenever possible.
- Use safe and clean file-handling patterns.
"""


# ---------------------------------------------------------------------------
# ⭐ RANK 1 — BEGINNER
# Basic reading and writing.
# ---------------------------------------------------------------------------

# 1. Create a file "task1.txt" and write your name inside it.

# 2. Read "task1.txt" and print its contents.

# 3. Create a file "hello.txt" and write:
#       Hello World!
#       Welcome to Python.
#    Then read it back.

# 4. Append the text "New line added." to "hello.txt".

# 5. Read "hello.txt" line by line and print each line with strip().


# ---------------------------------------------------------------------------
# ⭐ RANK 2 — EASY
# Appending, reading lists, writing sets of values.
# ---------------------------------------------------------------------------

# 6. Write the numbers 1–5 to "numbers.txt", one per line.

# 7. Read "numbers.txt" into a list of integers.

# 8. Append the number 99 to "numbers.txt".

# 9. Write a list of names (at least 3 names) to "names.txt".

# 10. Read "names.txt" and print:
#       Line 1: <name>
#       Line 2: <name>
#       ...


# ---------------------------------------------------------------------------
# ⭐ RANK 3 — INTERMEDIATE
# File checks, error handling, multiple operations.
# ---------------------------------------------------------------------------

# 11. Try reading a file called "missing.txt".
#       If it doesn't exist, print: "File not found!"

# 12. Write a function write_lines(filename, lines) that:
#       - writes each string in `lines` to the file (one per line)

# 13. Write a function read_lines(filename) that:
#       - returns a list of lines stripped of whitespace

# 14. Create a file "fruits.txt" with: apple, banana, mango (one per line)
#       Then read it and print only the fruits containing the letter 'a'.

# 15. Write a function copy_file(src, dst) that copies all text
#       from src to dst.


# ---------------------------------------------------------------------------
# ⭐ RANK 4 — ADVANCED
# Filtering, rewriting files, structured text processing.
# ---------------------------------------------------------------------------

# 16. Create a file "grades.txt" with:
#       Luis:90
#       Ana:85
#       Jorge:100
#     Read it and print "<name> has <grade>".

# 17. Rewrite "grades.txt" so grades below 90 are raised to 90.

# 18. Read a file "paragraph.txt" and print the number of words it contains.

# 19. Write a function filter_lines(filename, keyword, output) that:
#       - writes ONLY the lines containing keyword into output file

# 20. Read "names.txt" and create a new file "names_upper.txt"
#       where every name is uppercase.


# ---------------------------------------------------------------------------
# ⭐ RANK 5 — PROFESSIONAL
# Real-world mini-systems using files.
# ---------------------------------------------------------------------------

# 21. Create a log system:
#       - Write a function log(msg) that appends timestamp + msg to "app.log".

# 22. Create a function save_user(username, age):
#       - Writes "username,age" to "users.csv" (append mode).

# 23. Create a function load_users() that reads "users.csv" and returns:
#       [("username1", age1), ("username2", age2), ...]

# 24. Build a simple text database:
#       - Write add_item(item) → appends item to "database.txt"
#       - Write get_all_items() → returns all items as list

# 25. Create a function update_price_file(filename, percent):
#       - File format example:
#             Keyboard:750
#             Mouse:250
#       - Increase every price by <percent>
#       - Rewrite the file with updated prices
