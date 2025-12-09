"""
Module 11 — Virtual Environments & Dependencies
Examples File

This file contains small, focused demonstrations of how to work with virtual
environments, install packages, create requirements files, and rebuild a project
environment. These examples are meant to be read, not executed directly inside
Python, because most commands run in a terminal (PowerShell, CMD, or Bash).

Each example shows a real workflow used in professional Python development.
"""

# ---------------------------------------------------------------------------
# Rank 1 — Beginner Examples
# Basic environment creation and activation concepts.
# ---------------------------------------------------------------------------


def example_1_create_environment():
    """
    Demonstrates how to create a virtual environment using `venv`.

    Terminal commands (not Python code):

        python -m venv .venv

    This creates a `.venv` folder in the project directory.
    """
    print("Example 1 — Create a virtual environment (see comments above).")


def example_2_activate_environment():
    """
    Demonstrates how to activate a virtual environment.

    Windows PowerShell:
        .venv\\Scripts\\Activate.ps1

    Windows CMD:
        .venv\\Scripts\\activate.bat

    macOS / Linux:
        source .venv/bin/activate

    After activation, your terminal shows a prefix like:
        (.venv)
    """
    print("Example 2 — Activate the environment (see comments above).")


# ---------------------------------------------------------------------------
# Rank 2 — Installing and managing packages
# ---------------------------------------------------------------------------


def example_3_install_packages():
    """
    Shows how to install packages using pip.

    Terminal commands:

        pip install requests
        pip install numpy

    View installed packages:
        pip list

    Verify installation:
        python -c "import requests; import numpy; print('OK')"
    """
    print("Example 3 — Install packages with pip (see comments above).")


def example_4_uninstall_and_upgrade():
    """
    Demonstrates upgrading and uninstalling packages.

    Upgrade a package:
        pip install --upgrade requests

    Uninstall a package:
        pip uninstall requests
    """
    print("Example 4 — Uninstall or upgrade packages (see comments above).")


# ---------------------------------------------------------------------------
# Rank 3 — requirements.txt workflows
# ---------------------------------------------------------------------------


def example_5_freeze_requirements():
    """
    Shows how to create a requirements file.

    Command:
        pip freeze > requirements.txt

    This file lists all installed packages and versions.
    It is essential for sharing or deploying a project.
    """
    print("Example 5 — Freeze dependencies into requirements.txt.")


def example_6_install_from_requirements():
    """
    Demonstrates restoring an environment using requirements.txt.

    Command:
        pip install -r requirements.txt
    """
    print("Example 6 — Install dependencies from requirements.txt.")


# ---------------------------------------------------------------------------
# Rank 4 — Deleting and rebuilding environments
# ---------------------------------------------------------------------------


def example_7_rebuild_environment():
    """
    Full rebuild workflow — very common in real projects.

    Steps:
        1. Delete the `.venv` folder manually.
        2. Create a new environment:
               python -m venv .venv
        3. Activate the environment.
        4. Reinstall packages:
               pip install -r requirements.txt
    """
    print("Example 7 — Rebuild an environment from scratch.")


# ---------------------------------------------------------------------------
# Rank 5 — Professional workflow example
# ---------------------------------------------------------------------------


def example_8_full_workflow():
    """
    Demonstrates a complete, realistic project setup:

        # 1. Create the environment
        python -m venv .venv

        # 2. Activate it
        .venv\\Scripts\\Activate.ps1         (Windows PowerShell)
        source .venv/bin/activate            (macOS/Linux)

        # 3. Install dependencies
        pip install flask requests numpy

        # 4. Generate requirements.txt
        pip freeze > requirements.txt

        # 5. Run project code
        python app.py

        # 6. Send your project to GitHub WITHOUT the .venv folder
        #    (because environments should not be pushed to version control)

    This is the same workflow used by most professional developers.
    """
    print("Example 8 — Full virtual environment workflow.")


# ---------------------------------------------------------------------------
# Run all examples
# ---------------------------------------------------------------------------


def main():
    """Run all demonstration examples."""
    example_1_create_environment()
    example_2_activate_environment()
    example_3_install_packages()
    example_4_uninstall_and_upgrade()
    example_5_freeze_requirements()
    example_6_install_from_requirements()
    example_7_rebuild_environment()
    example_8_full_workflow()


if __name__ == "__main__":
    main()
