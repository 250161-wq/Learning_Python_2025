"""
Module 11 — Virtual Environments & Dependencies
Professional Notes

This file explains what virtual environments are, why they matter, and how to
use them correctly in real Python projects. The goal is to build a solid,
practical understanding of environment isolation and dependency management.
"""

# ---------------------------------------------------------------------------
# 1. What Is a Virtual Environment?
# ---------------------------------------------------------------------------
# A virtual environment is a self-contained Python workspace.
# Each project gets its own environment with its own installed packages.
#
# Why this matters:
# - Avoids conflicts between projects that require different package versions.
# - Keeps your system Python clean.
# - Makes your project reproducible on any computer.
#
# In practice, every professional Python project uses a virtual environment.


# ---------------------------------------------------------------------------
# 2. Creating a Virtual Environment (venv)
# ---------------------------------------------------------------------------
# Python includes a built-in module called `venv` for creating environments.
#
# Basic command (Windows, macOS, Linux):
#     python -m venv .venv
#
# This creates a folder named `.venv` containing:
# - A private Python interpreter
# - A private `pip` installer
# - Local site-packages folder
#
# Best practice:
# - Name the environment folder `.venv` and keep it inside the project root.
# - Add `.venv/` to your .gitignore so it is NOT pushed to GitHub.


# ---------------------------------------------------------------------------
# 3. Activating and Deactivating Environments
# ---------------------------------------------------------------------------
# Activation makes the environment's Python and pip the default in your terminal.
#
# Windows (PowerShell):
#     .venv\Scripts\Activate.ps1
#
# Windows (Command Prompt):
#     .venv\Scripts\activate.bat
#
# macOS / Linux:
#     source .venv/bin/activate
#
# Deactivate the environment with:
#     deactivate
#
# When active, your terminal may show something like:
#     (.venv) C:\project>
# which confirms that Python and pip are coming from the environment.


# ---------------------------------------------------------------------------
# 4. Installing Packages with pip
# ---------------------------------------------------------------------------
# Once the environment is active, you use pip to install dependencies.
#
# Examples:
#     pip install requests
#     pip install numpy
#
# Upgrade a package:
#     pip install --upgrade requests
#
# Uninstall a package:
#     pip uninstall requests
#
# List installed packages:
#     pip list
#
# Show which version of pip you’re using:
#     pip --version
#
# NOTE: Only packages inside `.venv` are modified.


# ---------------------------------------------------------------------------
# 5. requirements.txt — Freezing Dependencies
# ---------------------------------------------------------------------------
# A requirements file is a simple list of all dependencies in your project.
# It allows someone else (or future you) to recreate the same environment.
#
# Generate the file:
#     pip freeze > requirements.txt
#
# Typical example contents:
#     requests==2.32.0
#     numpy==1.26.4
#
# Rebuild the environment later:
#     pip install -r requirements.txt
#
# This ensures consistency across machines, deployments, and collaborators.


# ---------------------------------------------------------------------------
# 6. Removing and Re-Creating Environments
# ---------------------------------------------------------------------------
# If your environment breaks or becomes messy, the solution is simple:
# 1. Delete the `.venv` folder.
# 2. Recreate it:
#        python -m venv .venv
# 3. Activate it.
# 4. Reinstall everything from the requirements file:
#        pip install -r requirements.txt
#
# This workflow is extremely common in real projects.


# ---------------------------------------------------------------------------
# 7. Best Practices for Virtual Environments
# ---------------------------------------------------------------------------
# ✔ Create a new environment for every project.
# ✔ Never install packages globally unless absolutely necessary.
# ✔ Keep `.venv/` out of version control (add it to `.gitignore`).
# ✔ Always generate a `requirements.txt` before sharing a project.
# ✔ Prefer clear version pinning when working on long-term projects.
# ✔ Name your environment folder consistently (.venv is the standard).
#
# Following these habits will save hours of debugging and prevent dependency
# conflicts that frustrate even experienced developers.


# ---------------------------------------------------------------------------
# 8. Summary
# ---------------------------------------------------------------------------
# In this module, I learned how to:
# - Create and activate virtual environments
# - Install, upgrade, and remove dependencies with pip
# - Use requirements.txt to freeze and restore environments
# - Fix environment problems by rebuilding from scratch
# - Follow professional best practices for dependency management
#
# These skills form the foundation of real-world Python development.
#
# End of Notes
