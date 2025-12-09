"""
Module 10 — Modules & Packages: Practical Examples
--------------------------------------------------

This file demonstrates:
- Creating and importing modules
- Using packages
- Understanding __init__.py
- Absolute vs relative imports
- Avoiding circular imports
- Real-world project structure

Examples progress from Rank 1 → Rank 5.
"""


# ============================================================================
# Rank 1 — Beginner: Basic Modules
# ============================================================================

def example_1_basic_module_usage():
    """
    Simulate importing from a separate module.
    Imagine math_utils.py contains:
        def add(a, b): return a + b
    """
    import math  # real module
    print("sqrt(16) =", math.sqrt(16))


def example_2_import_specific_function():
    """
    Simulate:
        from math_utils import add
    """
    from math import factorial
    print("factorial(5) =", factorial(5))


def example_3_import_with_alias():
    """
    Using aliases for modules:
        import math as m
    """
    import math as m
    print("m.pi =", m.pi)


# ============================================================================
# Rank 2 — Easy: Creating and Using Your Own Modules
# ============================================================================

# Simulated "local module"
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b


def example_4_use_local_functions():
    """Using functions that would normally be in another .py module."""
    print("add:", add(10, 3))
    print("subtract:", subtract(10, 3))


def example_5_sys_path():
    """Show Python's module search path."""
    import sys
    print("\nModule search path:")
    for path in sys.path:
        print("  ", path)


# ============================================================================
# Rank 3 — Intermediate: Packages & __init__.py
# ============================================================================

def example_6_package_simulation():
    """
    Simulates a package structure:

    mypackage/
        __init__.py  → defines: from .math_utils import add
        math_utils.py → function add()

    import mypackage
    mypackage.add(2, 3)
    """

    # Simulated package API:
    class FakePackage:
        def add(self, a, b):
            return a + b

    pkg = FakePackage()
    print("Package-level add:", pkg.add(2, 3))


def example_7_relative_vs_absolute_imports():
    """
    Demonstrates conceptual difference between imports.
    """
    print("Absolute import example: from math import sqrt")
    print("Relative import example: from .helpers import clean_data (inside package)")


# ============================================================================
# Rank 4 — Advanced: Subpackages & Project Structure
# ============================================================================

def example_8_subpackage_concept():
    """
    Simulate a subpackage structure:

    project/
        data/
            processing/
                cleaner.py

    import project.data.processing.cleaner
    """
    print("Subpackages allow deep organization like project.data.processing.cleaner")


def example_9_absolute_relative_imports():
    """
    Show why absolute imports are recommended.
    """
    print("Absolute imports avoid confusion and circular imports.")
    print("Example: from app.utils.formatters import format_name")


def example_10_circular_import_fix():
    """
    Explain how to fix circular imports by restructuring code.
    """
    print("Fix circular imports by:")
    print(" - moving shared logic to a helper module")
    print(" - or importing inside functions")


# ============================================================================
# Rank 5 — Professional: Real Project Architecture
# ============================================================================

def example_11_professional_project_structure():
    """
    Show a real-world Python project structure.
    """
    print("""
Example layout:

my_project/
    src/
        my_project/
            __init__.py
            main.py
            utils/
                __init__.py
                date_utils.py
            models/
                __init__.py
                user.py
    tests/
        test_user.py
""")


def example_12_internal_public_api():
    """
    Show how __all__ controls public API.
    """
    print("""
__all__ = ["add", "subtract"]

Means ONLY these functions are exported when doing:
    from mymodule import *
""")


def example_13_namespace_packages():
    """
    Demonstrates large-scale packaging.
    """
    print("Namespace packages allow splitting one logical package across multiple folders.")


# ---------------------------------------------------------------------------
# Run All Examples
# ---------------------------------------------------------------------------

def main():
    print("\n--- Rank 1 ---")
    example_1_basic_module_usage()
    example_2_import_specific_function()
    example_3_import_with_alias()

    print("\n--- Rank 2 ---")
    example_4_use_local_functions()
    example_5_sys_path()

    print("\n--- Rank 3 ---")
    example_6_package_simulation()
    example_7_relative_vs_absolute_imports()

    print("\n--- Rank 4 ---")
    example_8_subpackage_concept()
    example_9_absolute_relative_imports()
    example_10_circular_import_fix()

    print("\n--- Rank 5 ---")
    example_11_professional_project_structure()
    example_12_internal_public_api()
    example_13_namespace_packages()


if __name__ == "__main__":
    main()
