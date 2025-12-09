"""
Module 10 — Modules & Packages: Practice Exercises
Structured, progressive practice with Python modules and packages.

In this module I:
- Practice creating my own modules and importing them in different ways.
- Learn how to organize code into packages (folders with __init__.py).
- Use import styles: `import module`, `from module import name`, and aliases.
- Work with the special variable `__name__` and the "main script" pattern.
- Get used to a more professional project layout where code is split across files.

Ranking system:
- Rank 1  -> Beginner: Very small, focused exercises on the basics of imports.
- Rank 2  -> Easy: Slightly bigger tasks combining more than one import idea.
- Rank 3  -> Intermediate: Multi-file exercises and small utilities.
- Rank 4  -> Advanced: More realistic mini-project structure with packages.
- Rank 5  -> Professional: Clean, production-style patterns for reusable code.

IMPORTANT:
- This file only describes the tasks.
- I should solve them in separate files inside this same module folder.
- I should NOT look at `Modules_Packages_Tasks_Solutions.py` until I have
  tried to solve the exercises on my own.
"""

# ---------------------------------------------------------------------------
# RANK 1 — BEGINNER
# Basic imports and simple reusable functions
# ---------------------------------------------------------------------------

# Task 1 — My first custom module
# --------------------------------
# 1. Create a new file in this folder called helpers.py.
# 2. Inside helpers.py define a function:
#       def greet(name: str) -> str:
#           """Return a friendly greeting message."""
#           ...
# 3. In a separate file (for example, demo_helpers.py), import helpers and:
#       - Call helpers.greet("Peyman") and print the result.
# 4. Run demo_helpers.py to verify that the import works.


# Task 2 — Import with an alias
# ------------------------------
# 1. In demo_helpers.py (or a new file), import helpers using an alias:
#       import helpers as hp
# 2. Call the greet function using the alias:
#       hp.greet("Arlette")
# 3. Print the returned message and confirm that the code runs correctly.


# Task 3 — Using from-import
# ---------------------------
# 1. In a new file (for example, from_import_demo.py), write:
#       from helpers import greet
# 2. Call greet("World") and print the message.
# 3. Compare this style with `import helpers` and note:
#       - What is more convenient?
#       - What can be confusing in larger projects?


# Task 4 — A module with constants
# ---------------------------------
# 1. Create a new file config.py in this folder.
# 2. Define a few constants, for example:
#       APP_NAME = "Learning_Python_2025"
#       VERSION = "1.0"
#       DEBUG = True
# 3. In a separate file (config_demo.py), import config and print:
#       - config.APP_NAME
#       - config.VERSION
#       - config.DEBUG


# ---------------------------------------------------------------------------
# RANK 2 — EASY
# Multiple modules working together
# ---------------------------------------------------------------------------

# Task 5 — Splitting math utilities into a module
# -----------------------------------------------
# 1. Create a file math_utils.py.
# 2. Add at least three functions, for example:
#       - add(a, b)
#       - subtract(a, b)
#       - average(numbers: list[float]) -> float
# 3. In a separate file (math_demo.py):
#       - Import math_utils.
#       - Use each function with sample values.
#       - Print the results in a clear way (labels + values).


# Task 6 — Importing selected names
# ---------------------------------
# 1. In math_demo.py (or another file), change the import to:
#       from math_utils import add, average
# 2. Use only add and average in this file.
# 3. Try to call subtract(...) and observe the error.
# 4. Add a comment explaining why Python cannot find subtract in this context.


# Task 7 — Namespaces and dir()
# ------------------------------
# 1. In a file (namespace_demo.py), write:
#       import math_utils
#       from helpers import greet
# 2. Use dir(math_utils) to inspect what is inside that module.
# 3. Use dir() with no arguments to see what names exist in the current file.
# 4. Print the outputs and add comments at the bottom explaining:
#       - What you see in dir(math_utils).
#       - What you see in dir() and why it is different.


# ---------------------------------------------------------------------------
# RANK 3 — INTERMEDIATE
# Working with packages (folders) and __init__.py
# ---------------------------------------------------------------------------

# Task 8 — Creating a simple package
# ----------------------------------
# 1. Inside this module folder (10-modules-and-packages), create a subfolder:
#       utilities/
# 2. Inside utilities/ create an empty file called:
#       __init__.py
# 3. Now create two modules inside utilities/:
#       - strings.py
#       - numbers.py
# 4. In strings.py define at least two functions, for example:
#       - to_title_case(text: str) -> str
#       - shorten(text: str, max_length: int) -> str
# 5. In numbers.py define at least two functions, for example:
#       - clamp(value: float, min_value: float, max_value: float) -> float
#       - percent(part: float, whole: float) -> float


# Task 9 — Importing from a package
# ---------------------------------
# 1. Create a new file package_demo.py in 10-modules-and-packages.
# 2. In package_demo.py:
#       - Import strings and numbers like this:
#             from utilities import strings, numbers
#       - Call strings.to_title_case("learning python with nova")
#       - Call numbers.percent(25, 80)
# 3. Print the results with clear labels (for example:
#       "Title case result:", ...
#       "Percent result:", ...
# 4. Run package_demo.py to verify that the imports work correctly.


# Task 10 — Using aliases for submodules
# --------------------------------------
# 1. In package_demo.py (or a new file), try:
#       from utilities import strings as str_utils
#       from utilities import numbers as num_utils
# 2. Use str_utils.to_title_case(...) and num_utils.percent(...).
# 3. Add comments in the file explaining:
#       - Why aliases can improve readability.
#       - When aliases might make code harder to understand.


# ---------------------------------------------------------------------------
# RANK 4 — ADVANCED
# The __name__ variable and “main script” pattern
# ---------------------------------------------------------------------------

# Task 11 — Understanding __name__
# --------------------------------
# 1. Create a new file name_demo.py.
# 2. Inside it, write code that:
#       - Prints the value of __name__.
#       - Has a function main() that prints "Running name_demo.main()".
#       - Uses the pattern:
#             if __name__ == "__main__":
#                 main()
# 3. Run name_demo.py directly (python name_demo.py) and observe the output.
# 4. Then import name_demo from another file (for example, import_demo.py)
#    and call:
#       import name_demo
# 5. Observe what runs automatically on import and what does NOT run.
# 6. Add comments summarizing your observations.


# Task 12 — A “tool” module with a main guard
# -------------------------------------------
# 1. Create a file text_tool.py.
# 2. Implement at least two functions, for example:
#       - count_words(text: str) -> int
#       - find_words_with_letter(text: str, letter: str) -> list[str]
# 3. Add a main() function that:
#       - Uses input() to ask the user for some text.
#       - Prints the word count.
# 4. Protect main() with:
#       if __name__ == "__main__":
#           main()
# 5. Test both:
#       - Running text_tool.py directly.
#       - Importing text_tool in another file and using the functions there
#         without triggering main() automatically.


# Task 13 — Reorganizing existing code into modules
# -------------------------------------------------
# 1. Take one of your previous modules (for example, loops or functions).
# 2. Choose a file where you have several related functions.
# 3. Move those functions into a new module:
#       - For example, put all “string utility” functions in a file called
#         string_utils.py.
# 4. Update the original file so it imports these functions from string_utils
#    instead of defining them inline.
# 5. Run the code and confirm everything still works.
# 6. Add comments explaining if the new structure feels clearer and why.


# ---------------------------------------------------------------------------
# RANK 5 — PROFESSIONAL
# Small “library-style” structure with modules and packages
# ---------------------------------------------------------------------------

# Task 14 — Designing a tiny “library”
# ------------------------------------
# 1. In the 10-modules-and-packages folder, design a mini-library, for example:
#       - A "reporting" library that prepares formatted strings.
#       - A "finance" library for very simple budget calculations.
#       - A "text analytics" library for working with text.
# 2. Create a new package folder, for example:
#       reporting/
# 3. Inside reporting/ create:
#       - __init__.py
#       - core.py      (main logic)
#       - formatters.py (functions that format output as strings)
# 4. Implement at least:
#       - 2–3 functions in core.py
#       - 2–3 functions in formatters.py
# 5. In __init__.py, import and re-export a few key functions so that a user
#    could write:
#       from reporting import generate_summary
#    instead of:
#       from reporting.core import generate_summary


# Task 15 — Creating a clean public API for the package
# -----------------------------------------------------
# 1. Decide which functions from your new package are “public” (for users)
#    and which are “internal” (helpers).
# 2. In __init__.py, only expose the public functions by importing them:
#       from .core import generate_summary
#       from .formatters import format_currency
# 3. Optionally define __all__ in __init__.py:
#       __all__ = ["generate_summary", "format_currency"]
# 4. In a separate file (reporting_demo.py):
#       - Import using:
#             from reporting import generate_summary, format_currency
#       - Use these functions with some example data.
# 5. Add comments explaining:
#       - Why it is helpful to have a small, clean public API.
#       - How this pattern prepares you for real-world packages on PyPI.


# Task 16 — Documenting your mini-library
# ---------------------------------------
# 1. Create a file REPORTING_NOTES.md or reporting_usage.md in this folder.
# 2. Write a short, clear documentation section that explains:
#       - What the package does.
#       - How to install/use it in a project (for now, just mention that it
#         lives inside this repository).
#       - Example import statements and basic usage.
# 3. Make sure the style and tone match the professional style of this repo.


# Task 17 — Reflecting on modules & packages
# ------------------------------------------
# 1. In a file reflection_modules_packages.md, answer questions like:
#       - What was confusing at first about modules and imports?
#       - What started to feel more natural after completing these tasks?
#       - How do modules and packages make large projects easier to maintain?
# 2. Keep the reflection short (5–10 sentences) but honest and specific.
# 3. This reflection is only for you. It helps track your progress and
#    prepares you for larger projects later.
