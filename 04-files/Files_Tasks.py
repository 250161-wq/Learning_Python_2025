"""
Module 4 — Files: Practice Tasks
--------------------------------

This file contains practice tasks for working with files in Python.

In this module I practice how to:
- Open files safely for reading and writing.
- Read full files, individual lines, and line-by-line streams.
- Write and append text to files.
- Work with simple structured text files (like line-based logs).
- Combine file operations with basic data processing.

IMPORTANT:
- This file is for MY solutions. I should try to solve each task myself.
- The corresponding solutions are in: Files_Tasks_Solutions.py
- I can run this file and call individual task functions while I practice.

Ranking system (difficulty levels)
----------------------------------
- Rank 1 → Beginner: very simple file operations (open, write, read).
- Rank 2 → Easy: combine reading, writing, and simple processing.
- Rank 3 → Intermediate: work with multi-line files and derived results.
- Rank 4 → Advanced: more realistic file processing / mini utilities.
- Rank 5 → Professional: small “real-world style” tasks with clearer structure.

How to use this file
--------------------
- Pick a rank that matches how confident I feel.
- Choose a task, read the docstring and comments carefully.
- Implement the code where it says:  # TODO: Write your code here
- I can comment out or remove raise NotImplementedError once I implement it.
"""


# ---------------------------------------------------------------------------
# RANK 1 — BEGINNER
# Very small tasks: open, write, read basic text files.
# ---------------------------------------------------------------------------

def task_r1_01_write_hello_file():
    """
    Task R1-01 — Write a simple greeting file

    Requirements:
    - Create (or overwrite) a file named "hello.txt" in the current folder.
    - Write a single line of text into the file, for example: "Hello from Python!".
    - Close the file properly (use a context manager: `with open(...) as f:`).

    After implementing:
    - Open the file in a text editor or from the terminal to verify the content.
    """
    # TODO: Write your code here
    raise NotImplementedError


def task_r1_02_read_hello_file():
    """
    Task R1-02 — Read a greeting from a file

    Requirements:
    - Open the file "hello.txt" created in task_r1_01_write_hello_file.
    - Read the full content of the file.
    - Print the content to the console (using print()).
    - If the file does not exist, handle the error gracefully and print a friendly message.

    Hint:
    - Use try/except to handle FileNotFoundError.
    """
    # TODO: Write your code here
    raise NotImplementedError


def task_r1_03_write_multiple_lines():
    """
    Task R1-03 — Write multiple lines to a file

    Requirements:
    - Create (or overwrite) a file named "shopping_list.txt".
    - Write several items to the file, each item on its own line, for example:
        milk
        bread
        eggs
    - Use a context manager (`with open(...) as f:`).

    Optional:
    - Store the items in a Python list first, then write the list to the file.
    """
    # TODO: Write your code here
    raise NotImplementedError


# ---------------------------------------------------------------------------
# RANK 2 — EASY
# Read line by line, append content, and do small, simple processing.
# ---------------------------------------------------------------------------

def task_r2_01_read_lines_into_list():
    """
    Task R2-01 — Read all lines into a Python list

    Requirements:
    - Read the file "shopping_list.txt" created earlier.
    - Strip the newline characters from each line.
    - Store all cleaned items in a Python list called `items`.
    - Print the list to verify the result.

    Example output:
    ['milk', 'bread', 'eggs']
    """
    # TODO: Write your code here
    raise NotImplementedError


def task_r2_02_append_item_to_file():
    """
    Task R2-02 — Append a new line to an existing file

    Requirements:
    - Open "shopping_list.txt" in append mode.
    - Ask the user for a new item using input().
    - Append the new item as a new line at the end of the file.
    - Close the file properly.

    Bonus:
    - After appending, optionally print a confirmation message like:
      "Item '<name>' added to shopping_list.txt".
    """
    # TODO: Write your code here
    raise NotImplementedError


def task_r2_03_count_lines_in_file():
    """
    Task R2-03 — Count how many lines a file has

    Requirements:
    - Ask the user for a filename (e.g., "shopping_list.txt").
    - Try to open the file for reading.
    - Count how many lines the file has.
    - Print: "The file '<filename>' has <N> lines."
    - If the file does not exist, print a clear error message.

    Hint:
    - Use a for loop over the file object: for line in file: ...
    """
    # TODO: Write your code here
    raise NotImplementedError


# ---------------------------------------------------------------------------
# RANK 3 — INTERMEDIATE
# Work with simple structured content and do some processing.
# ---------------------------------------------------------------------------

def task_r3_01_save_usernames():
    """
    Task R3-01 — Save multiple usernames to a file

    Requirements:
    - Ask the user how many usernames they want to enter (an integer).
    - For each username:
      - Use input() to read the username.
      - Immediately write it to a file named "usernames.txt", one per line.
    - Use a context manager for the file.

    Bonus:
    - Ignore empty usernames (if the user just presses Enter, do not write it).
    """
    # TODO: Write your code here
    raise NotImplementedError


def task_r3_02_filter_long_usernames():
    """
    Task R3-02 — Read and filter usernames

    Requirements:
    - Read the file "usernames.txt".
    - Build a new list with only usernames that have length >= 5 characters.
    - Print:
      - The total number of usernames.
      - The number of "long" usernames (length >= 5).
      - The list of "long" usernames.

    Optional:
    - Write the long usernames to a new file named "usernames_long.txt".
    """
    # TODO: Write your code here
    raise NotImplementedError


def task_r3_03_copy_file():
    """
    Task R3-03 — Make a simple copy of a text file

    Requirements:
    - Ask the user for a source filename (e.g., "shopping_list.txt").
    - Ask the user for a destination filename (e.g., "shopping_list_copy.txt").
    - Read the full content from the source file.
    - Write the same content into the destination file.
    - Handle the case when the source file does not exist.

    Hint:
    - Use try/except around the open() call for the source file.
    """
    # TODO: Write your code here
    raise NotImplementedError


# ---------------------------------------------------------------------------
# RANK 4 — ADVANCED
# Slightly more realistic processing: logs, reports, simple “tools”.
# ---------------------------------------------------------------------------

def task_r4_01_analyze_temperature_log():
    """
    Task R4-01 — Analyze a simple temperature log

    Scenario:
    - You have a text file called "temperatures.txt".
    - Each line contains a single temperature as a float, for example:
        21.5
        19.0
        23.2
        18.7

    Requirements:
    - Read all temperatures from the file into a list of floats.
    - Calculate:
      - The number of readings.
      - The minimum temperature.
      - The maximum temperature.
      - The average temperature.
    - Print a small report to the console, for example:

        Temperature report:
        - Readings: 4
        - Min: 18.7
        - Max: 23.2
        - Average: 20.6

    Assumptions:
    - You can assume the file exists and contains valid numbers (for now).
    """
    # TODO: Write your code here
    raise NotImplementedError


def task_r4_02_clean_text_file():
    """
    Task R4-02 — Clean up a messy text file

    Scenario:
    - You have a file "raw_notes.txt" with many empty lines and lines
      that contain only spaces or tabs.

    Requirements:
    - Read all lines from "raw_notes.txt".
    - Remove:
      - Completely empty lines.
      - Lines that contain only whitespace (spaces / tabs / newlines).
    - Write the cleaned lines into a new file called "clean_notes.txt".
    - Ensure that the resulting file has no leading/trailing blank lines.

    Hint:
    - Use line.strip() to check if a line is "empty".
    """
    # TODO: Write your code here
    raise NotImplementedError


def task_r4_03_merge_two_files():
    """
    Task R4-03 — Merge the content of two files

    Requirements:
    - Ask the user for two input filenames (file_a and file_b).
    - Ask for an output filename (merged_filename).
    - Create the output file and write:
      - All lines from file_a.
      - Followed by a separator line, for example: "-----\\n".
      - All lines from file_b.
    - Handle the case when one of the input files does not exist by printing
      a clear error message and not creating the output file.

    Hint:
    - You can nest try/except blocks or handle both files in a single try block.
    """
    # TODO: Write your code here
    raise NotImplementedError


# ---------------------------------------------------------------------------
# RANK 5 — PROFESSIONAL
# More “real-world style” utilities with clearer structure.
# ---------------------------------------------------------------------------

def task_r5_01_log_messages_with_timestamps():
    """
    Task R5-01 — Simple logging utility with timestamps

    Scenario:
    - You want to log small text messages to a file with timestamps.

    Requirements:
    - Ask the user for a log message using input().
    - If the user enters a non-empty message:
      - Open (or create) a file called "app.log" in *append* mode.
      - Write one line in the format:
          [YYYY-MM-DD HH:MM:SS] message goes here
      - Close the file.

    Hints:
    - Use the datetime module:
        from datetime import datetime
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    Optional:
    - Put the logging logic into a helper function like `log_message(message)`.
    """
    # TODO: Write your code here
    raise NotImplementedError


def task_r5_02_search_in_file():
    """
    Task R5-02 — Search for a word in a text file

    Scenario:
    - You want a small tool that searches for a word inside a text file.

    Requirements:
    - Ask the user for:
      - The filename to search in.
      - The word (or fragment) to look for.
    - Open the file and read it line by line.
    - For each line that contains the search word (case-sensitive is fine):
      - Print the line number (starting at 1) and the line content.
    - At the end, print how many matches were found.

    Example output:
        Found 3 matching lines:
        Line 2: This is a test line.
        Line 5: Another test is here.
        Line 8: Final test case.

    Error handling:
    - If the file does not exist, print a friendly error message.
    """
    # TODO: Write your code here
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Optional: small helper to quickly test individual tasks while learning.
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    """
    This block is optional and can be used while practicing.

    Example:
    - Temporarily call one of the task functions here to test it:
        task_r1_01_write_hello_file()
    - Then run this file:
        python Files_Tasks.py
    - Comment out or change the function calls as needed.
    """
    # Example (commented out so nothing runs by default):
    # task_r1_01_write_hello_file()
    pass
