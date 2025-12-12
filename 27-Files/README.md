Module 27 — Working with Files (Reading & Writing)

Author: Peyman Miyandashti
Year: 2025

In this module, I learn how Python works with external files, including:

Text files (.txt)

Data files (CSV-like text)

Log files

Config files

Any readable or writable plain-text files

Reading and writing files is one of the most useful capabilities in Python.
It allows programs to save data permanently, load information, store logs, process documents, and interact with the operating system.

By the end of this module, I should feel completely comfortable:

Opening files safely

Writing text into files

Reading file contents

Appending new data

Looping over lines

Handling missing files safely

Using the best practices for file management

This module also prepares me for future topics like JSON, CSV, APIs, data analysis, and advanced file handling.

Key Learning Objectives

By completing this module, I will be able to:

🔹 Open files using Python’s built-in open()

Understand modes like:

"r" → read

"w" → write (overwrites!)

"a" → append (adds to file)

"r+" → read & write

"rb" / "wb" → binary modes

🔹 Read content from text files

read() → entire file

readline() → one line

readlines() → list of lines

Iterating with for line in file:

🔹 Write content into files

Create or overwrite files with "w".

🔹 Append content without destroying the file

Add new lines or logs using "a".

🔹 Use the with statement (best practice)

Ensures the file closes automatically — safe and clean.

🔹 Handle missing files with try/except

Avoid crashes when files are not found.

🔹 Work with relative and absolute paths

Organize files safely inside projects.

Module File Structure
Files_Notes.py

Concepts, explanations, modes, examples, good habits, safety, and best practices.

Files_Examples.py

Short, practical examples for reading, writing, and appending.

Files_Tasks.py

Beginner → professional practice exercises.

Files_Tasks_Solutions.py

Clean and professional solutions.

Exercise Difficulty Framework (Ranking System)
⭐ Rank 1 — Beginner

Basic reading and writing of small text files.

⭐ Rank 2 — Easy

Line-by-line processing, appending, file creation.

⭐ Rank 3 — Intermediate

Combining operations, safe error handling, multiple files.

⭐ Rank 4 — Advanced

Reading structured text, splitting, filtering, rewriting content.

⭐ Rank 5 — Professional

Mini-systems that manage logs, user data, or simplified databases.

Recommended Study Workflow

Start with Files_Notes.py and learn how file operations work.

Run and modify Files_Examples.py to learn by practice.

Complete all exercises in Files_Tasks.py — do NOT check solutions yet.

Review Files_Tasks_Solutions.py to confirm your understanding and adopt professional patterns.

File handling is a critical skill — learning this module brings you closer to real software development and data engineering.
