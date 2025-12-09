"""
Module 25 — Context Managers: Practice Exercises
Comprehensive practice with Python context managers, from beginner to
professional, production-style usage.

In this module I:
- Learn how `with` statements work.
- Create my own context managers using classes.
- Create context managers using the @contextlib.contextmanager decorator.
- Use context managers for file operations, timers, and resource cleanup.
- Integrate real data from Peyman's life (UPBC, games, Mexicali, etc.)

Ranking system:
- Rank 1  -> Beginner: basic use of with + file handling.
- Rank 2  -> Easy: custom context manager (class-based).
- Rank 3  -> Intermediate: contextlib.contextmanager.
- Rank 4  -> Advanced: timing, profiling, and logging behavior.
- Rank 5  -> Professional: reusable context manager utilities.

Author: Peyman Miyandashti
Date of Birth: 11/11/1983
ID Number: 250161
Year: 2025
"""

import time
from contextlib import contextmanager
from pathlib import Path

BASE_DIR = Path("module_25_output")
BASE_DIR.mkdir(exist_ok=True)

PEYMAN_NAME = "Peyman Miyandashti"
CITY = "Mexicali"
UNIVERSITY = "UPBC"
GAME = "World of Warcraft"
FAVORITE_NUMBER = 11

# ===========================================================
# Rank 1 — Beginner
# Basic file writing with a with-statement
# ===========================================================

def rank1_demo():
    print("Rank 1 — Beginner")

    file_path = BASE_DIR / "rank1_basic.txt"

    # Using with to safely handle files
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("Hello, this is Module 25 — Context Managers!\n")
        f.write(f"My name is {PEYMAN_NAME}.\n")
        f.write(f"I live in {CITY}.\n")

    # No need to close — context manager handles that
    print(f"Wrote beginner file: {file_path}")
    print("-" * 50)


# ===========================================================
# Rank 2 — Easy
# Create a simple class-based context manager
# ===========================================================

class MessageBlock:
    """
    A simple context manager that prints a message before and after a block.
    """

    def __init__(self, title: str):
        self.title = title

    def __enter__(self):
        print(f"--- Entering: {self.title} ---")
        return self  # Not required, but common

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"--- Exiting: {self.title} ---")
        # Returning False means errors will not be suppressed
        return False


def rank2_demo():
    print("Rank 2 — Easy")

    with MessageBlock("Peyman's Study Session"):
        print(f"{PEYMAN_NAME} is studying at {UNIVERSITY}")
        print(f"Favorite number is {FAVORITE_NUMBER}")

    print("-" * 50)


# ===========================================================
# Rank 3 — Intermediate
# Use @contextmanager to create lightweight context managers
# ===========================================================

@contextmanager
def study_timer(module_name: str):
    """
    A context manager that measures how long Peyman studies a module.
    """
    start = time.perf_counter()
    print(f"Starting study for {module_name}...")
    try:
        yield
    finally:
        end = time.perf_counter()
        print(f"Finished studying {module_name}. Time spent: {end - start:.2f} seconds")


def rank3_demo():
    print("Rank 3 — Intermediate")

    with study_timer("Module 25 — Context Managers"):
        # simulate study time
        time.sleep(1.2)

    print("-" * 50)


# ===========================================================
# Rank 4 — Advanced
# Context manager for event logging + resource handling
# ===========================================================

class EventLogger:
    """
    A context manager for logging actions to a file.

    Useful for:
    - tracking study sessions
    - tracking gaming sessions
    - monitoring long tasks
    """

    def __init__(self, logfile: Path):
        self.logfile = logfile

    def __enter__(self):
        self.file = open(self.logfile, "a", encoding="utf-8")
        self.file.write("\n=== NEW SESSION STARTED ===\n")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.file.write(f"ERROR: {exc_type.__name__}: {exc_val}\n")
        self.file.write("=== SESSION ENDED ===\n")
        self.file.close()
        return False  # Do not swallow exceptions


def rank4_demo():
    print("Rank 4 — Advanced")

    log_path = BASE_DIR / "study_log.txt"

    with EventLogger(log_path) as log:
        log.write(f"Peyman studied at {UNIVERSITY}.\n")
        log.write(f"Favorite game: {GAME}\n")
        log.write(f"City: {CITY}\n")

    print(f"Wrote advanced log file to: {log_path}")
    print("-" * 50)


# ===========================================================
# Rank 5 — Professional
# Reusable, professional-grade context managers
# ===========================================================

@contextmanager
def temporary_change_directory(path: Path):
    """
    Temporarily change the working directory.
    Useful in automation & file-handling scripts.
    """
    import os
    old_dir = Path.cwd()
    try:
        print(f"Changing directory to {path}")
        os.chdir(path)
        yield
    finally:
        os.chdir(old_dir)
        print(f"Returned to original directory: {old_dir}")


@contextmanager
def suppress_errors(*exceptions):
    """
    Suppress specific exceptions (like try/except but cleaner).
    """
    try:
        yield
    except exceptions as e:
        print(f"Suppressed error: {e}")


def rank5_demo():
    print("Rank 5 — Professional")

    # Example 1 — safely changing directories
    with temporary_change_directory(BASE_DIR):
        print("Inside BASE_DIR... files here:")
        for p in Path(".").iterdir():
            print(" -", p)

    # Example 2 — suppressing specific errors
    with suppress_errors(ZeroDivisionError):
        print("Trying division by zero (will be suppressed)...")
        x = 10 / 0  # suppressed

    print("Continuing after suppressed error...")
    print("-" * 50)


# ===========================================================
# Main Runner
# ===========================================================

if __name__ == "__main__":
    rank1_demo()
    rank2_demo()
    rank3_demo()
    rank4_demo()
    rank5_demo()
