"""
Module 25 — Context Managers: Solutions
Using with, __enter__/__exit__, and contextlib to manage resources safely.

In this module I:
- Practice how to use context managers with files and other resources.
- Learn how to build my own context managers (class-based and decorator-based).
- Use context managers to make my code cleaner, safer, and more "professional".

Ranking system:
- Rank 1  -> Beginner: basic "with" usage (files, simple examples).
- Rank 2  -> Easy: add a bit of logic around the context (logs, printing).
- Rank 3  -> Intermediate: custom class-based context managers.
- Rank 4  -> Advanced: contextlib.contextmanager and combining contexts.
- Rank 5  -> Professional: reusable patterns that protect resources and handle errors.

Author: Peyman Miyandashti
Date of Birth: 11/11/1983
ID Number: 250161
Year: 2025
"""

from __future__ import annotations

import os
import time
from contextlib import contextmanager


# ===========================================================
# Rank 1 — Beginner
# Simple file context manager usage
# ===========================================================

def write_and_read_note_solved(file_path: str) -> str:
    """
    Task 1 (Solution):
    - Use a context manager (with open) to write a short note about Peyman.
    - Then use another context manager to read it back and return the content.
    """
    note_text = (
        "Student: Peyman Miyandashti\n"
        "Age: 43\n"
        "University: Polytechnic Baja California University (UPBC)\n"
        "Degree: Information Technology Engineering and Digital Innovation\n"
    )

    # Write the note
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(note_text)

    # Read the note
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    return content


# ===========================================================
# Rank 2 — Easy
# Logging with a simple context manager wrapper
# ===========================================================

@contextmanager
def logging_open_solved(file_path: str, mode: str):
    """
    Task 2 (Solution):
    A thin wrapper around open that prints simple logs
    when entering and leaving the context.
    """
    print(f"[LOG] Opening file: {file_path!r} with mode {mode!r}")
    f = open(file_path, mode, encoding="utf-8")
    try:
        yield f
    finally:
        print(f"[LOG] Closing file: {file_path!r}")
        f.close()


def demo_logging_open_solved(file_path: str) -> str:
    """
    Use logging_open_solved to append a short line about Peyman's hobby
    and then read the full content.
    """
    hobby_line = "Hobby: Playing games (favorite game: World of Warcraft)\n"

    with logging_open_solved(file_path, "a") as f:
        f.write(hobby_line)

    with logging_open_solved(file_path, "r") as f:
        return f.read()


# ===========================================================
# Rank 3 — Intermediate
# Custom class-based context manager (CodeTimer)
# ===========================================================

class CodeTimer:
    """
    Task 3 (Solution):
    Class-based context manager that measures how long a block of code takes.

    Usage:
        with CodeTimer("calculate_something") as t:
            # do work
        print(t.elapsed)
    """

    def __init__(self, label: str = "block"):
        self.label = label
        self.start = None
        self.end = None
        self.elapsed = None

    def __enter__(self) -> "CodeTimer":
        self.start = time.perf_counter()
        print(f"[TIMER] Starting {self.label!r}...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        self.end = time.perf_counter()
        self.elapsed = self.end - self.start
        print(f"[TIMER] Finished {self.label!r} in {self.elapsed:.6f} seconds")

        # Do not suppress exceptions
        return False


def simulate_upbc_assignment_solved() -> int:
    """
    Use CodeTimer to "simulate" work:
    - pretend Peyman is doing a UPBC assignment that sums numbers.
    Returns the result of the calculation to prove we did some work.
    """
    with CodeTimer("UPBC assignment: sum 1..1_000_000"):
        total = 0
        for i in range(1, 200_000):
            total += i

    return total


# ===========================================================
# Rank 4 — Advanced
# contextlib.contextmanager + temporary working directory
# ===========================================================

@contextmanager
def temporary_working_directory_solved(path: str):
    """
    Task 4 (Solution):
    Temporarily change the current working directory.

    - Save the old working directory.
    - Change to the new one.
    - Yield control to the with-block.
    - Restore the old working directory afterward (even if there's an error).
    """
    old_cwd = os.getcwd()
    print(f"[CWD] Changing from {old_cwd!r} to {path!r}")
    os.makedirs(path, exist_ok=True)
    os.chdir(path)
    try:
        yield
    finally:
        print(f"[CWD] Reverting to {old_cwd!r}")
        os.chdir(old_cwd)


def create_student_report_in_temp_dir_solved(temp_dir: str, filename: str) -> str:
    """
    Use temporary_working_directory_solved to create a report file in a
    temporary directory. Returns the absolute path to the created file.
    """
    report_text = (
        "=== STUDENT REPORT ===\n"
        "Name: Peyman Miyandashti\n"
        "Age: 43\n"
        "Current city: Mexicali, Baja California, Mexico\n"
        "Origin: Tabriz, Iran\n"
        "Car: Kia Sportage 2024 (Dark Gray)\n"
        "Favorite number: 11\n"
    )

    with temporary_working_directory_solved(temp_dir):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(report_text)
        created_path = os.path.abspath(filename)

    # At this point, working directory has been restored
    return created_path


# ===========================================================
# Rank 5 — Professional
# Robust context manager that guarantees cleanup and handles errors
# ===========================================================

class SafeGameSession:
    """
    Task 5 (Solution):

    A professional-style context manager that simulates a "game session"
    for Peyman (World of Warcraft). It guarantees that the progress is saved
    even if an exception happens inside the with-block.

    Parameters:
        player_name: name of the player
        game_name: game being played
    """

    def __init__(self, player_name: str, game_name: str):
        self.player_name = player_name
        self.game_name = game_name
        self.session_active = False

    def __enter__(self) -> "SafeGameSession":
        self.session_active = True
        print(f"[GAME] Starting session for {self.player_name!r} in {self.game_name!r}...")
        return self

    def save_progress(self):
        """
        Simulate saving progress.
        In a real project, this would write to a database or file.
        """
        print(f"[GAME] Saving progress for {self.player_name!r} in {self.game_name!r}...")

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        # Always save progress when leaving the context
        self.save_progress()
        self.session_active = False

        if exc_type is not None:
            print(f"[GAME] An error occurred: {exc_type.__name__}: {exc_val}")
            print("[GAME] Progress saved safely. Cleaning up session.")

            # Return False so the exception is not suppressed.
            return False

        print("[GAME] Session ended normally. Progress saved.")
        return False  # do not suppress exceptions


def demo_safe_game_session_solved(raise_error: bool = False) -> None:
    """
    Demonstrate SafeGameSession with and without an error.
    """
    with SafeGameSession("Peyman", "World of Warcraft"):
        print("[GAME] Playing some epic raid with Arlette watching as a teacher of life 😄")
        if raise_error:
            # Simulate a bug or crash
            raise RuntimeError("Connection lost during boss fight!")


# ===========================================================
# Simple demo runner
# ===========================================================

def _run_demo():
    print("=== Module 25 — Context Managers (Solutions Demo) ===")

    # Rank 1
    print("\n[DEMO] Rank 1 — write_and_read_note_solved")
    note_content = write_and_read_note_solved("pey_man_note.txt")
    print(note_content)

    # Rank 2
    print("\n[DEMO] Rank 2 — demo_logging_open_solved")
    all_text = demo_logging_open_solved("pey_man_note.txt")
    print(all_text)

    # Rank 3
    print("\n[DEMO] Rank 3 — simulate_upbc_assignment_solved")
    total = simulate_upbc_assignment_solved()
    print("Sum result:", total)

    # Rank 4
    print("\n[DEMO] Rank 4 — create_student_report_in_temp_dir_solved")
    created_path = create_student_report_in_temp_dir_solved(
        temp_dir="temp_reports",
        filename="pey_man_report.txt",
    )
    print("Report created at:", created_path)

    # Rank 5
    print("\n[DEMO] Rank 5 — demo_safe_game_session_solved (normal)")
    demo_safe_game_session_solved(raise_error=False)

    print("\n[DEMO] Rank 5 — demo_safe_game_session_solved (with error)")
    try:
        demo_safe_game_session_solved(raise_error=True)
    except RuntimeError as e:
        print("[DEMO] Caught RuntimeError outside context manager:", e)


if __name__ == "__main__":
    _run_demo()
