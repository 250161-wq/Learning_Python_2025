"""
Module 16 — Python Modules
Examples File

This file contains practical examples showing how Python modules work:
importing, aliasing, creating custom modules, using built-in modules,
and understanding execution behavior.

Run this file directly to see all examples:
    python Modules_Examples.py
"""


# ---------------------------------------------------------------------------
# Rank 1 — Basic imports
# ---------------------------------------------------------------------------

def example_1_basic_import() -> None:
    """Importing a built-in module and using its functions."""
    print("Example 1 — Basic import")

    import math
    print("sqrt(25) =", math.sqrt(25))
    print("pi =", math.pi)
    print()


def example_2_import_specific_name() -> None:
    """Importing specific functions."""
    print("Example 2 — Importing specific names")

    from math import sin, pi
    print("sin(pi/2) =", sin(pi / 2))
    print()


# ---------------------------------------------------------------------------
# Rank 2 — Alias imports and namespace control
# ---------------------------------------------------------------------------

def example_3_alias_import() -> None:
    """Using import with an alias."""
    print("Example 3 — Alias import")

    import random as rnd
    print("Random number:", rnd.randint(1, 5))
    print()


def example_4_import_all() -> None:
    """Demonstration of wildcard imports (not recommended)."""
    print("Example 4 — Wildcard import demonstration")

    from math import *
    print("cos(0) =", cos(0))  # Works because cos() becomes available
    print("pi =", pi)
    print()


# ---------------------------------------------------------------------------
# Rank 3 — Creating & using your own module
# ---------------------------------------------------------------------------

# For demonstration, imagine a custom module file called:
#
#     helpers.py
#
# containing:
#     def greet(name):
#         return f"Hello, {name}!"
#
# This example shows how it would be imported.

def example_5_custom_module_import() -> None:
    """Illustrate importing a custom module (hypothetical example)."""
    print("Example 5 — Importing a custom module")

    # The actual file 'helpers.py' must exist in the same folder.
    try:
        import helpers  # This will work if helpers.py exists.
        print(helpers.greet("Nova"))
    except ModuleNotFoundError:
        print("helpers.py not found — create it to test this example.")
    print()


# ---------------------------------------------------------------------------
# Rank 4 — Using __name__ to control execution
# ---------------------------------------------------------------------------

def example_6_name_main_demo() -> None:
    """Show how __name__ behaves depending on execution."""
    print("Example 6 — __name__ demonstration")

    import name_demo_module  # hypothetical module

    print("Imported module __name__ =", name_demo_module.__name__)
    print()


# ---------------------------------------------------------------------------
# Rank 5 — Real-world module usage
# ---------------------------------------------------------------------------

import datetime
import os
import sys

def example_7_datetime_usage() -> None:
    """Using datetime module in real applications."""
    print("Example 7 — datetime module")

    now = datetime.datetime.now()
    print("Current time:", now)
    print("Year:", now.year)
    print()


def example_8_os_module() -> None:
    """Interacting with the operating system."""
    print("Example 8 — os module")

    print("Current directory:", os.getcwd())
    print("Files here:", os.listdir("."))
    print()


def example_9_sys_path() -> None:
    """Show where Python looks for modules."""
    print("Example 9 — sys.path exploration")

    print("Module search path:")
    for path in sys.path:
        print("  -", path)
    print()


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def main() -> None:
    """Run all example functions in sequence."""

    # Rank 1
    example_1_basic_import()
    example_2_import_specific_name()

    # Rank 2
    example_3_alias_import()
    example_4_import_all()

    # Rank 3
    example_5_custom_module_import()

    # Rank 4
    example_6_name_main_demo()

    # Rank 5
    example_7_datetime_usage()
    example_8_os_module()
    example_9_sys_path()


if __name__ == "__main__":
    main()
