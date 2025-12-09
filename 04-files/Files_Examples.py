"""
Module 4 — Working with Files: Practical Examples
-------------------------------------------------

This file contains runnable examples showing how to read, write, append,
and process files in Python using professional patterns.

Concepts demonstrated:
- Reading entire files
- Reading line-by-line
- Writing and appending
- Safely handling missing files
- Using pathlib for file paths
- Parsing simple structured data
- Writing reusable file-handling functions
"""

from pathlib import Path


# ---------------------------------------------------------------------------
# Rank 1 — Beginner Examples
# ---------------------------------------------------------------------------

def example_1_read_entire_file(path: str) -> None:
    """
    Read and print the entire contents of a text file.
    """
    with open(path, "r") as f:
        content = f.read()
    print("--- File Content ---")
    print(content)


def example_2_read_line_by_line(path: str) -> None:
    """
    Read a file line-by-line.
    """
    with open(path, "r") as f:
        for line in f:
            print("Line:", line.strip())


def example_3_write_simple_file(path: str) -> None:
    """
    Create or overwrite a file with basic text content.
    """
    with open(path, "w") as f:
        f.write("Hello, file!\n")
        f.write("This is a test file.\n")
    print(f"File written: {path}")


# ---------------------------------------------------------------------------
# Rank 2 — Easy Examples
# ---------------------------------------------------------------------------

def example_4_append_to_file(path: str) -> None:
    """
    Append new lines to an existing file.
    """
    with open(path, "a") as f:
        f.write("Appending a new line.\n")
    print("Appended to file.")


def example_5_read_first_n_lines(path: str, n: int) -> None:
    """
    Read and print the first `n` lines of a file.
    """
    with open(path, "r") as f:
        for i in range(n):
            line = f.readline()
            if not line:
                break
            print(line.strip())


def example_6_file_exists(path: str) -> bool:
    """
    Return True if a file exists, using pathlib.
    """
    return Path(path).exists()


# ---------------------------------------------------------------------------
# Rank 3 — Intermediate Examples
# ---------------------------------------------------------------------------

def example_7_count_lines(path: str) -> int:
    """
    Count and return the number of lines in the file.
    """
    count = 0
    with open(path, "r") as f:
        for _ in f:
            count += 1
    return count


def example_8_extract_numbers(path: str) -> list[int]:
    """
    Read a file containing one number per line and return them as ints.

    Example file:
        10
        25
        7
        100
    """
    numbers = []
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if line.isdigit():
                numbers.append(int(line))
    return numbers


def example_9_parse_csv_simple(path: str) -> list[tuple[str, int]]:
    """
    Parse a simple CSV file without using external libraries.

    Example CSV format:
        Ana,25
        Bob,31
        Carla,28
    """
    results = []
    with open(path, "r") as f:
        for line in f:
            name, age = line.strip().split(",")
            results.append((name, int(age)))
    return results


# ---------------------------------------------------------------------------
# Rank 4 — Advanced Examples
# ---------------------------------------------------------------------------

def example_10_safe_read(path: str) -> str:
    """
    Safely read a file. Return an error message if missing.
    """
    try:
        with open(path, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "ERROR: File not found."
    except PermissionError:
        return "ERROR: Permission denied."


def example_11_write_lines(path: str, lines: list[str]) -> None:
    """
    Write a list of lines to a file using a clean loop.
    """
    with open(path, "w") as f:
        for line in lines:
            f.write(line + "\n")


def example_12_use_pathlib_read(path: str) -> str:
    """
    Read a file using pathlib.
    """
    p = Path(path)
    if p.exists():
        return p.read_text()
    return "ERROR: file not found."


# ---------------------------------------------------------------------------
# Rank 5 — Professional Examples
# ---------------------------------------------------------------------------

def example_13_generate_report(input_file: str, output_file: str) -> None:
    """
    Read an input text file and create a summary report file.

    The report includes:
    - Number of lines
    - Number of characters
    - First and last non-empty line

    This demonstrates a multi-step professional file workflow.
    """
    lines = []
    with open(input_file, "r") as f:
        for line in f:
            lines.append(line.rstrip("\n"))

    non_empty = [l for l in lines if l.strip()]

    report = [
        f"Total lines: {len(lines)}",
        f"Total characters: {sum(len(l) for l in lines)}",
        f"First non-empty line: {non_empty[0] if non_empty else '(none)'}",
        f"Last non-empty line:  {non_empty[-1] if non_empty else '(none)'}",
    ]

    with open(output_file, "w") as f:
        for item in report:
            f.write(item + "\n")

    print(f"Report generated: {output_file}")


def example_14_backup_file(path: str) -> str:
    """
    Create a backup copy of a file using pathlib.

    If path is: data.txt
    Backup: data.txt.bak
    """
    p = Path(path)
    backup = p.with_suffix(p.suffix + ".bak")

    if not p.exists():
        return "ERROR: original file does not exist."

    backup.write_text(p.read_text())
    return f"Backup created at {backup}"


def example_15_log_message(path: str, message: str) -> None:
    """
    Append a timestamped message to a log file.

    Demonstrates:
    - appending
    - string formatting
    - reusable utility pattern
    """
    from datetime import datetime

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(path, "a") as f:
        f.write(f"[{timestamp}] {message}\n")


# ---------------------------------------------------------------------------
# Demonstration Section (Optional Manual Testing)
# ---------------------------------------------------------------------------

def main():
    print("Example: Writing file...")
    example_3_write_simple_file("demo.txt")

    print("\nExample: Appending...")
    example_4_append_to_file("demo.txt")

    print("\nExample: Reading entire file...")
    example_1_read_entire_file("demo.txt")

    print("\nExample: Counting lines...")
    print(example_7_count_lines("demo.txt"))

    print("\nExample: Logging message...")
    example_15_log_message("log.txt", "This is a test log entry.")


if __name__ == "__main__":
    main()
