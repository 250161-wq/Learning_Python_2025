"""
Module 10 — Modules & Packages: Notes & Explanations
----------------------------------------------------

Modules and packages allow Python programs to be organized into multiple
files and directories. This is essential for building clean, maintainable,
scalable, REAL applications.

In this module, I will learn:
- What modules are
- What packages are
- How imports work
- How to structure real projects
- How to avoid common pitfalls like circular imports
"""


# ============================================================================
# 1. What Is a Module?
# ============================================================================

"""
A module is simply a Python file ending in .py.

Example:
    math_utils.py

A module may contain:
    - variables
    - functions
    - classes

To use a module:
    import math_utils
    result = math_utils.add(5, 3)
"""

# Simple example module content:

def add(a, b):
    return a + b


# ============================================================================
# 2. Importing Modules
# ============================================================================

"""
Different ways to import:

1. import module_name
       module_name.function()

2. from module_name import function
       function()

3. from module_name import *
       BAD PRACTICE (pollutes namespace)

4. import module_name as alias
       import math as m
       m.sqrt(9)
"""


# ============================================================================
# 3. The Module Search Path
# ============================================================================

"""
When Python imports, it looks in:

1. The current directory
2. PYTHONPATH
3. Site-packages
4. Standard library

You can check the search path:

    import sys
    print(sys.path)
"""

import sys
module_search_path = sys.path


# ============================================================================
# 4. What Is a Package?
# ============================================================================

"""
A package is a folder containing Python modules AND an __init__.py file.

Example:
    utilities/
        __init__.py
        math_utils.py
        string_utils.py

Without __init__.py, Python will NOT treat the folder as a package.
"""


# ============================================================================
# 5. Importing from Packages
# ============================================================================

"""
Absolute import (recommended):
    from utilities.math_utils import add

Relative import (inside package):
    from .math_utils import add
"""


# ============================================================================
# 6. __init__.py — What Is It For?
# ============================================================================

"""
__init__.py can be empty OR can define what is loaded when the package
is imported.

Example __init__.py:
    from .math_utils import add
    from .string_utils import capitalize

Now:
    import utilities
    utilities.add(2, 3)
"""

# Example of package-like behavior inside one file:
__all__ = ["add"]


# ============================================================================
# 7. Subpackages
# ============================================================================

"""
Packages can contain subpackages:

project/
    data/
        processing/
            __init__.py
            cleaner.py
    utils/
        __init__.py
        formatting.py

Importing:
    from project.data.processing.cleaner import clean_data
"""


# ============================================================================
# 8. Absolute vs Relative Imports
# ============================================================================

"""
Absolute import (recommended):
    from project.utils.formatting import fmt

Relative import:
    from .utils import fmt
    from ..common import helper

Relative imports ONLY work inside packages.
"""


# ============================================================================
# 9. Avoiding Circular Imports
# ============================================================================

"""
Circular import example:

file A imports B
file B imports A

→ Causes ImportError or partial initialization.

BEST PRACTICES:
✔ Move shared code into a third module
✔ Import inside functions (lazy import)
✔ Simplify module relations
"""


# ============================================================================
# 10. Real Project Structure (Professional)
# ============================================================================

"""
Recommended layout:

my_project/
    src/
        my_project/
            __init__.py
            main.py
            utils/
                __init__.py
                helpers.py
            models/
                __init__.py
                user.py
    tests/
        test_user.py
    README.md
    requirements.txt
    pyproject.toml

This structure is used in professional Python projects.
"""


# ============================================================================
# 11. Using Modules to Organize Logic
# ============================================================================

"""
Example:

calculator/
    add.py
    subtract.py
    multiply.py

main.py:
    from calculator.add import add
    from calculator.subtract import subtract
"""

# Example functions you might split into modules:

def multiply(a, b):
    return a * b


# ============================================================================
# 12. Packages as Libraries
# ============================================================================

"""
Python packages can be installed and reused.

To create installable packages:
- Use pyproject.toml
- Use setuptools
- Publish on PyPI
(advanced topic, but useful to know)
"""


# ============================================================================
# 13. Summary of Best Practices
# ============================================================================

"""
✔ Keep modules small and focused
✔ Prefer absolute imports for clarity
✔ Use __all__ to control public API
✔ Avoid circular imports
✔ Use packages to group related logic
✔ Maintain a clean project structure
✔ Do not use 'from x import *'
"""


# ============================================================================
# 14. Summary
# ============================================================================

"""
In this module I learned:

- What modules are
- What packages are
- How imports work
- How to structure real Python projects
- How to use __init__.py
- What subpackages are
- How to avoid circular imports
- How to build real project architectures

Next:
    Run Modules_Packages_Examples.py for practical demonstrations.
    Complete the practice tasks in Modules_Packages_Tasks.py.
"""
