"""
Module 4 — Files: Practice Task Solutions
Clean, professional reference solutions for basic and intermediate file handling.

In this module I practice how to:

- Open files safely using `with open(...)` (context managers).
- Read files using `.read()`, `.readline()`, and `.readlines()`.
- Write and append text to files.
- Work with simple line-based data (logs, notes, lists).
- Handle common errors (like missing files) in a clean way.

I start from very simple tasks (Rank 1) and move toward more realistic,
"production-style" patterns (Rank 5).

These are **reference solutions**.  
In `Files_Tasks.py` I should first try to solve each task on my own, then come
here to compare style, structure, and best practices.
"""

from pathlib import Path


# ============================================================
# Rank 1 — Beginner
# Very simple reading/writing tasks to understand the basics.
# ============================================================

def write_hello_file(filename: str = "hello.txt") -> None:
    """
    Task (Rank 1):
    - Create a file called "hello.txt" (or the given filename).
    - Write the text: "Hello, Python files!" inside it.

    Notes:
    - Uses write mode "w" which overwrites the file if it exists.
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write("Hello, Python files!")


def read_hello_file(filename: str = "hello.txt") -> str:
    """
    Task (Rank 1):
    - Read the content of "hello.txt" and return it as a string.

    Returns:
        The content of the file.

    Notes:
    - Assumes the file already exists.
    """
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    return content


# ============================================================
# Rank 2 — Easy
# Work with multiple lines and simple list-to-file operations.
# ============================================================

def write_favorite_movies(filename: str, movies: list[str]) -> None:
    """
    Task (Rank 2):
    - Receive a list of movie titles.
    - Write each title on its own line in the file.

    Example:
        movies = ["Inception", "The Matrix", "Interstellar"]
        -> file content:
            Inception
            The Matrix
            Interstellar
    """
    with open(filename, "w", encoding="utf-8") as f:
        for movie in movies:
            f.write(f"{movie}\n")


def read_lines_strip(filename: str) -> list[str]:
    """
    Task (Rank 2):
    - Read all lines from the given file.
    - Return a list of strings with newline characters removed.

    Example:
        File lines:
            "Inception\\n"
            "The Matrix\\n"
        -> ["Inception", "The Matrix"]
    """
    cleaned_lines: list[str] = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            cleaned_lines.append(line.rstrip("\n"))
    return cleaned_lines


# ============================================================
# Rank 3 — Intermediate
# File transformations, simple summaries, and counters.
# ============================================================

def copy_text_file(source: str, target: str) -> None:
    """
    Task (Rank 3):
    - Copy the content from source file to target file.
    - Overwrite the target file if it already exists.

    This is a simple example of file-to-file operations.
    """
    with open(source, "r", encoding="utf-8") as src_file:
        content = src_file.read()

    with open(target, "w", encoding="utf-8") as dst_file:
        dst_file.write(content)


def count_lines_and_characters(filename: str) -> tuple[int, int]:
    """
    Task (Rank 3):
    - Read a text file.
    - Return a tuple: (number_of_lines, number_of_characters).

    Notes:
    - Characters include spaces and newline characters.
    """
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    num_lines = content.count("\n") + (1 if content else 0)
    num_chars = len(content)

    return num_lines, num_chars


def filter_non_empty_lines(source: str, target: str) -> None:
    """
    Task (Rank 3):
    - Read all lines from `source`.
    - Write only non-empty (non-blank) lines into `target`.

    Rules:
    - A line that only contains whitespace counts as empty.
    """
    with open(source, "r", encoding="utf-8") as src, open(
        target, "w", encoding="utf-8"
    ) as dst:
        for line in src:
            if line.strip():
                dst.write(line)


# ============================================================
# Rank 4 — Advanced
# Logs, append mode, and more structured text processing.
# ============================================================

def append_log_message(log_file: str, message: str) -> None:
    """
    Task (Rank 4):
    - Append a log message to a text log file.
    - Prepend each message with a numeric index based on current line count.

    Example:
        log_file content before:
            [1] Application started
        append_log_message(..., "User logged in")
        ->
            [1] Application started
            [2] User logged in
    """
    # Count existing lines (if file does not exist, count is 0).
    path = Path(log_file)
    current_count = 0
    if path.exists():
        with path.open("r", encoding="utf-8") as f:
            for _ in f:
                current_count += 1

    new_index = current_count + 1

    # Append new line with index.
    with path.open("a", encoding="utf-8") as f:
        f.write(f"[{new_index}] {message}\n")


def summarize_log_file(log_file: str) -> dict:
    """
    Task (Rank 4):
    - Read a simple log file where each line is a message.
    - Return a dictionary summary with:
        {
            "line_count": <int>,
            "first_line": <str | None>,
            "last_line": <str | None>,
        }

    If the file is empty or does not exist, all values should be 0 or None.
    """
    path = Path(log_file)
    if not path.exists():
        return {
            "line_count": 0,
            "first_line": None,
            "last_line": None,
        }

    lines: list[str] = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            # Keep original text but strip trailing newline for summary.
            lines.append(line.rstrip("\n"))

    if not lines:
        return {
            "line_count": 0,
            "first_line": None,
            "last_line": None,
        }

    return {
        "line_count": len(lines),
        "first_line": lines[0],
        "last_line": lines[-1],
    }


def merge_two_files(file_a: str, file_b: str, target: str) -> None:
    """
    Task (Rank 4):
    - Read the contents of file_a and file_b.
    - Write both into `target` with a separator line in between.

    Example separator:
        "-----\n"
    """
    with open(file_a, "r", encoding="utf-8") as fa:
        content_a = fa.read()

    with open(file_b, "r", encoding="utf-8") as fb:
        content_b = fb.read()

    separator = "\n-----\n"

    with open(target, "w", encoding="utf-8") as ft:
        ft.write(content_a)
        ft.write(separator)
        ft.write(content_b)


# ============================================================
# Rank 5 — Professional
# More "production-style" patterns: pathlib, helpers, simple error handling.
# ============================================================

def safe_read_file(path: str) -> str:
    """
    Task (Rank 5):
    - Safely read a text file.
    - If the file does not exist, return an empty string instead of crashing.

    This is closer to how real applications avoid unexpected exceptions.
    """
    file_path = Path(path)

    if not file_path.exists():
        # In a production scenario, we might log a warning here.
        return ""

    return file_path.read_text(encoding="utf-8")


def write_report(path: str, title: str, lines: list[str]) -> Path:
    """
    Task (Rank 5):
    - Create a simple "report" text file using pathlib.
    - The file should contain:
        - A title line
        - An underline made of '=' characters
        - One line per item from `lines`

    Example content:
        Daily Report
        ============
        Item 1
        Item 2
    """
    file_path = Path(path)

    header = f"{title}\n{'=' * len(title)}\n"
    body = "\n".join(lines)

    file_path.write_text(header + body, encoding="utf-8")
    return file_path


def read_config_key(path: str, key: str, default: str | None = None) -> str | None:
    """
    Task (Rank 5):
    - Read a simple "key=value" configuration file.
    - Return the value for the given key.
    - If the key is not found or the file does not exist, return `default`.

    Example config file:
        username=admin
        theme=dark
    """
    file_path = Path(path)

    if not file_path.exists():
        return default

    with file_path.open("r", encoding="utf-8") as f:
        for line in f:
            # Ignore comments and empty lines.
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue

            if "=" not in stripped:
                continue

            k, v = stripped.split("=", maxsplit=1)
            if k.strip() == key:
                return v.strip()

    return default


# ============================================================
# Optional: Quick manual test area
# (I can run this file directly to see some basic behavior.)
# ============================================================

if __name__ == "__main__":
    # Example quick tests (I can modify or remove these if I want).

    write_hello_file()
    print("Hello file content:", read_hello_file())

    write_favorite_movies("movies.txt", ["Inception", "The Matrix", "Interstellar"])
    print("Movies (stripped):", read_lines_strip("movies.txt"))

    copy_text_file("movies.txt", "movies_copy.txt")
    print("Movies copy line & char count:", count_lines_and_characters("movies_copy.txt"))

    append_log_message("app.log", "Application started")
    append_log_message("app.log", "User logged in")
    print("Log summary:", summarize_log_file("app.log"))

    report_path = write_report(
        "daily_report.txt",
        "Daily Report",
        ["Users: 15", "Errors: 0", "Status: OK"],
    )
    print("Report created at:", report_path)

    # Example config usage (for testing):
    # Create a small config file.
    sample_config = Path("config.ini")
    sample_config.write_text("username=admin\ntheme=dark\n", encoding="utf-8")
    print("Theme from config:", read_config_key("config.ini", "theme", default="light"))
