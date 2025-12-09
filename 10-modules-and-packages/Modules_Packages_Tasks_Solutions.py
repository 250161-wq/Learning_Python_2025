"""
Modules_Packages_Tasks_Solutions.py

Module 10 — Modules & Packages: Practice Exercises — SOLUTIONS
Example reference solutions for all tasks in this module.

IMPORTANT:
- These are just one set of possible solutions.
- In many places, your own solutions may look a bit different but still
  be correct.
- For tasks that require multiple files, this file shows example contents
  for those files under clear comments like "File: helpers.py".
"""

# ---------------------------------------------------------------------------
# RANK 1 — BEGINNER
# Basic imports and simple reusable functions
# ---------------------------------------------------------------------------

# Task 1 — My first custom module
# --------------------------------
# File: helpers.py
def greet(name: str) -> str:
    """Return a friendly greeting message."""
    return f"Hello, {name}! Welcome to Learning_Python_2025."


# File: demo_helpers.py
def demo_helpers_task1() -> None:
    """
    Example of using the helpers module.

    In your real project, this would live in demo_helpers.py:

        import helpers

        message = helpers.greet("Peyman")
        print(message)
    """
    # Here we just simulate the behavior by calling greet directly.
    message = greet("Peyman")
    print(message)


# Task 2 — Import with an alias
# ------------------------------
# File: demo_helpers_alias.py
def demo_helpers_task2() -> None:
    """
    Example of alias import.

    Real file example (demo_helpers_alias.py):

        import helpers as hp

        message = hp.greet("Arlette")
        print(message)
    """
    # Simulated here in this single file:
    hp = __import__("__main__")  # not for real projects; just to show the idea
    # In a real project you'd do: import helpers as hp
    # and then: hp.greet("Arlette")
    message = greet("Arlette")
    print(message)


# Task 3 — Using from-import
# ---------------------------
# File: from_import_demo.py
def demo_from_import_task3() -> None:
    """
    Example of from-import usage.

    Real file example (from_import_demo.py):

        from helpers import greet

        print(greet("World"))

    Notes:
    - `from helpers import greet` lets you call greet() directly.
    - This can be more convenient for frequent use of a single function.
    - But in larger projects, it may become confusing if you don't know
      where greet() comes from.
    """
    # Simulated call:
    print(greet("World"))


# Task 4 — A module with constants
# ---------------------------------
# File: config.py
APP_NAME = "Learning_Python_2025"
VERSION = "1.0"
DEBUG = True


# File: config_demo.py
def demo_config_task4() -> None:
    """
    Example of using a config module.

    Real file (config_demo.py):

        import config

        print("App name:", config.APP_NAME)
        print("Version:", config.VERSION)
        print("Debug mode:", config.DEBUG)
    """
    print("App name:", APP_NAME)
    print("Version:", VERSION)
    print("Debug mode:", DEBUG)


# ---------------------------------------------------------------------------
# RANK 2 — EASY
# Multiple modules working together
# ---------------------------------------------------------------------------

# Task 5 — Splitting math utilities into a module
# -----------------------------------------------
# File: math_utils.py
def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def average(numbers: list[float]) -> float:
    if not numbers:
        raise ValueError("numbers list cannot be empty")
    return sum(numbers) / len(numbers)


# File: math_demo.py
def demo_math_task5() -> None:
    """
    Example of using math_utils.

    Real file (math_demo.py):

        import math_utils

        print("Add 2 + 3:", math_utils.add(2, 3))
        print("Subtract 10 - 4:", math_utils.subtract(10, 4))
        print("Average of [1, 2, 3, 4]:", math_utils.average([1, 2, 3, 4]))
    """
    print("Add 2 + 3:", add(2, 3))
    print("Subtract 10 - 4:", subtract(10, 4))
    print("Average of [1, 2, 3, 4]:", average([1, 2, 3, 4]))


# Task 6 — Importing selected names
# ---------------------------------
def demo_math_task6() -> None:
    """
    Example of importing selected functions.

    Real file (math_demo_selected.py):

        from math_utils import add, average

        print(add(3, 5))
        print(average([10, 20, 30]))

        # The line below would cause a NameError, because subtract is not imported:
        # print(subtract(10, 3))

        # Explanation:
        # Only `add` and `average` are imported into the current namespace.
        # The name `subtract` does not exist here, so Python cannot find it.
    """
    from math_utils import add as add_func, average as avg_func  # example style

    print(add_func(3, 5))
    print(avg_func([10, 20, 30]))
    # We DO NOT call subtract here to avoid raising an error in this demo.


# Task 7 — Namespaces and dir()
# ------------------------------
def demo_namespace_task7() -> None:
    """
    Demonstrates dir() on a module and on the current namespace.
    In a real file (namespace_demo.py):

        import math_utils
        from helpers import greet

        print("dir(math_utils):")
        print(dir(math_utils))

        print("\\ndir() in this file:")
        print(dir())

    Example explanation (summary):

    - dir(math_utils):
        Shows names defined inside the math_utils module, such as:
        ['add', 'average', 'subtract', '__doc__', '__name__', ...]
    - dir():
        Shows all names currently available in the current module
        (variables, functions, imported names, etc.). It is different
        because it also includes local variables defined in this file.
    """
    import math_utils
    from helpers import greet as greet_func  # noqa: F401  (used to show in dir)

    print("dir(math_utils):")
    print(dir(math_utils))

    print("\ndir() in this file:")
    print(dir())


# ---------------------------------------------------------------------------
# RANK 3 — INTERMEDIATE
# Working with packages (folders) and __init__.py
# ---------------------------------------------------------------------------

# Task 8 — Creating a simple package
# ----------------------------------
# Imagine the following structure:
#
# utilities/
#   __init__.py
#   strings.py
#   numbers.py
#
# Below are example contents for those files.

# File: utilities/strings.py
def to_title_case(text: str) -> str:
    """Convert text to title case."""
    return text.title()


def shorten(text: str, max_length: int) -> str:
    """
    Shorten the text to at most max_length characters.

    If the text is longer than max_length, it is truncated and '...' is added
    (only if max_length > 3).
    """
    if max_length <= 3:
        return text[:max_length]
    if len(text) <= max_length:
        return text
    return text[: max_length - 3] + "..."


# File: utilities/numbers.py
def clamp(value: float, min_value: float, max_value: float) -> float:
    """Clamp value between min_value and max_value."""
    return max(min_value, min(value, max_value))


def percent(part: float, whole: float) -> float:
    """
    Return the percentage (0–100) that 'part' represents of 'whole'.
    """
    if whole == 0:
        raise ValueError("whole cannot be zero")
    return (part / whole) * 100.0


# File: utilities/__init__.py
# (example content)
# from .strings import to_title_case, shorten
# from .numbers import clamp, percent
#
# __all__ = ["to_title_case", "shorten", "clamp", "percent"]


# Task 9 — Importing from a package
# ---------------------------------
def demo_package_task9() -> None:
    """
    Example of using the utilities package.

    Real file (package_demo.py):

        from utilities import strings, numbers

        title = strings.to_title_case("learning python with nova")
        pct = numbers.percent(25, 80)

        print("Title case result:", title)
        print("Percent result:", pct)
    """
    title = to_title_case("learning python with nova")
    pct = percent(25, 80)

    print("Title case result:", title)
    print("Percent result:", pct)


# Task 10 — Using aliases for submodules
# --------------------------------------
def demo_package_task10() -> None:
    """
    Example of using aliases for submodules.

    Real file:

        from utilities import strings as str_utils
        from utilities import numbers as num_utils

        title = str_utils.to_title_case("learning python with nova")
        pct = num_utils.percent(25, 80)

        print("Title case result:", title)
        print("Percent result:", pct)

        # Comments:
        # - Aliases can make long module names shorter and easier to type.
        # - But too many or unclear aliases can make code harder to read,
        #   because it's not obvious which module 'str_utils' refers to.
    """
    # Here we just simulate:
    str_utils = __import__("__main__")  # not for real projects
    num_utils = str_utils
    title = to_title_case("learning python with nova")
    pct = percent(25, 80)
    print("Title case result:", title)
    print("Percent result:", pct)


# ---------------------------------------------------------------------------
# RANK 4 — ADVANCED
# The __name__ variable and “main script” pattern
# ---------------------------------------------------------------------------

# Task 11 — Understanding __name__
# --------------------------------
# File: name_demo.py
def main_name_demo() -> None:
    print("Running name_demo.main()")


# This simulates the code that would be in name_demo.py:
if __name__ == "__main__":
    # When you run "python name_demo.py", __name__ == "__main__"
    # In this file, this block will run when Modules_Packages_Tasks_Solutions.py
    # is executed directly, but not when imported as a module.
    main_name_demo()


def demo_import_name_demo_task11() -> None:
    """
    Example of importing name_demo from another file.

    Real file (import_demo.py):

        import name_demo

        # When importing:
        # - The top-level print(__name__) in name_demo.py runs.
        # - The code under "if __name__ == '__main__':" does NOT run,
        #   because in that context __name__ == "name_demo", not "__main__".

    Summary of observations:
    - When you run a file directly, its __name__ becomes "__main__".
    - When you import a file, its __name__ is the module name.
    - The pattern with if __name__ == "__main__" allows us to have
      code that only runs when the file is executed directly.
    """
    # Here we don't actually re-import, but the explanation above covers it.
    pass


# Task 12 — A “tool” module with a main guard
# -------------------------------------------
# File: text_tool.py
def count_words(text: str) -> int:
    """Return the number of words in text."""
    words = text.split()
    return len(words)


def find_words_with_letter(text: str, letter: str) -> list[str]:
    """Return list of words containing the given letter (case-insensitive)."""
    letter_lower = letter.lower()
    words = text.split()
    return [w for w in words if letter_lower in w.lower()]


def main_text_tool() -> None:
    """
    Simple command-line interface for text_tool.

    Real file:

        if __name__ == "__main__":
            main()
    """
    user_text = input("Enter some text: ")
    print("Word count:", count_words(user_text))


# In text_tool.py, you would typically have:
# if __name__ == "__main__":
#     main()


# Task 13 — Reorganizing existing code into modules
# -------------------------------------------------
# This task is mainly about refactoring your own previous code.
# Below is a generic example of how a string_utils module might look.

# File: string_utils.py (example)
def to_upper(text: str) -> str:
    return text.upper()


def to_lower(text: str) -> str:
    return text.lower()


def add_exclamation(text: str) -> str:
    return text + "!"


# Original file (for example, functions_demo.py) might change from:
#
#   def to_upper(text): ...
#   def to_lower(text): ...
#   def add_exclamation(text): ...
#
# To:
#
#   from string_utils import to_upper, to_lower, add_exclamation
#
#   def demo():
#       print(to_upper("hello"))
#       print(to_lower("HELLO"))
#       print(add_exclamation("Hi Nova"))
#
# Comments (reflection):
# - Moving these functions into string_utils.py makes them reusable in
#   multiple files.
# - The original file becomes smaller and focused on using the utilities
#   instead of defining them.
# - This structure is clearer when your project grows.


# ---------------------------------------------------------------------------
# RANK 5 — PROFESSIONAL
# Small “library-style” structure with modules and packages
# ---------------------------------------------------------------------------

# Task 14 — Designing a tiny “library”
# ------------------------------------
# Example: "reporting" mini-library.

# Directory structure:
#
# reporting/
#   __init__.py
#   core.py
#   formatters.py
#
# Below are example contents.

# File: reporting/core.py
def generate_summary(numbers: list[float]) -> dict:
    """
    Generate a simple numeric summary (count, total, average).
    """
    count = len(numbers)
    total = sum(numbers)
    average_value = total / count if count else 0.0
    return {
        "count": count,
        "total": total,
        "average": average_value,
    }


def generate_comparison(current: float, previous: float) -> dict:
    """
    Compare current and previous values in a very simple way.
    """
    change = current - previous
    percent_change = (change / previous * 100.0) if previous else 0.0
    return {
        "current": current,
        "previous": previous,
        "change": change,
        "percent_change": percent_change,
    }


def generate_text_report(title: str, summary: dict) -> str:
    """
    Create a plain-text report from a title and summary dict.
    """
    lines = [
        f"Report: {title}",
        f"Count  : {summary.get('count', 0)}",
        f"Total  : {summary.get('total', 0)}",
        f"Average: {summary.get('average', 0.0):.2f}",
    ]
    return "\n".join(lines)


# File: reporting/formatters.py
def format_currency(amount: float, currency_symbol: str = "$") -> str:
    """
    Format a number as a currency string, e.g. $1,234.56
    """
    return f"{currency_symbol}{amount:,.2f}"


def format_percentage(value: float) -> str:
    """
    Format a number as a percentage string, e.g. 12.34%
    """
    return f"{value:.2f}%"


def format_summary(summary: dict) -> str:
    """
    Format a summary dict as a nice multi-line string.
    """
    lines = [
        f"Count: {summary.get('count', 0)}",
        f"Total: {summary.get('total', 0)}",
        f"Average: {summary.get('average', 0.0):.2f}",
    ]
    return "\n".join(lines)


# File: reporting/__init__.py
# Example public API:
#
# from .core import generate_summary, generate_comparison, generate_text_report
# from .formatters import format_currency, format_percentage, format_summary
#
# __all__ = [
#     "generate_summary",
#     "generate_comparison",
#     "generate_text_report",
#     "format_currency",
#     "format_percentage",
#     "format_summary",
# ]


# Task 15 — Creating a clean public API for the package
# -----------------------------------------------------
def demo_reporting_task15() -> None:
    """
    Example usage as if __init__.py exposes:

        from reporting import generate_summary, format_currency

    Real file (reporting_demo.py):

        from reporting import generate_summary, format_currency

        data = [10, 20, 30]
        summary = generate_summary(data)
        total_formatted = format_currency(summary["total"])

        print("Summary:", summary)
        print("Total (formatted):", total_formatted)

        # Comments:
        # - A small, clean public API is easier for users of your package.
        # - They don't need to know about internal helper functions or the
        #   exact file structure, only the key functions they should import.
        # - This pattern is very similar to what real-world packages on PyPI do.
    """
    data = [10, 20, 30]
    summary = generate_summary(data)
    total_formatted = format_currency(summary["total"])
    print("Summary:", summary)
    print("Total (formatted):", total_formatted)


# Task 16 — Documenting your mini-library
# ---------------------------------------
REPORTING_USAGE_MD_EXAMPLE = """
# Reporting Mini-Library

This mini-library provides simple tools for generating numeric summaries and
formatting them for display.

## Where it lives

Right now, it lives inside this repository in the `reporting/` folder.
You can use it in any of your Python files inside this project.

## Basic usage

Example:

    from reporting import generate_summary, format_currency

    data = [10, 20, 30, 40]
    summary = generate_summary(data)
    print(summary)  # {'count': 4, 'total': 100, 'average': 25.0}

    total_as_currency = format_currency(summary["total"])
    print(total_as_currency)  # e.g. "$100.00"

This matches the professional style and structure used in the rest of the
Learning_Python_2025 repository.
"""


# Task 17 — Reflecting on modules & packages
# ------------------------------------------
REFLECTION_MODULES_PACKAGES_EXAMPLE = """
At first, modules and imports were confusing because I was not sure how Python
found files or why some imports failed with ImportError. After practicing with
simple modules like helpers.py and math_utils.py, imports started to feel more
natural. Creating packages with __init__.py helped me understand how larger
libraries are organized. I can see that splitting code into modules and
packages makes big projects easier to read, test, and maintain. It also
encourages me to think about what should be public for users and what should
stay internal as implementation detail.
"""


# Optional: small demo runner (you can ignore this if you like)
def _run_basic_demos() -> None:
    print("--- Demo: helpers / greet ---")
    demo_helpers_task1()
    print("\n--- Demo: math_utils ---")
    demo_math_task5()
    print("\n--- Demo: utilities package ---")
    demo_package_task9()
    print("\n--- Demo: reporting ---")
    demo_reporting_task15()


if __name__ == "__main__":
    # You can run this file directly to see some demos.
    _run_basic_demos()
