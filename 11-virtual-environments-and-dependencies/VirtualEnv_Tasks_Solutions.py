"""
Module 11 — Virtual Environments & Dependencies
Practice Task Solutions

This file contains clear, professional solutions to all exercises found in
VirtualEnv_Tasks.py. Multiple answers are possible, but these represent standard
and recommended practices used in real Python development.

Only read these after attempting the tasks yourself.
"""

# ---------------------------------------------------------------------------
# Rank 1 — Beginner
# ---------------------------------------------------------------------------

# Task 1.1
# Command to create a virtual environment:
# python -m venv .venv

# Task 1.2
# Activation commands:
# Windows PowerShell: .venv\\Scripts\\Activate.ps1
# Windows CMD:        .venv\\Scripts\\activate.bat
# macOS/Linux:        source .venv/bin/activate

# Task 1.3
# Virtual environments isolate dependencies for each project so that
# different projects can use different package versions without conflicts.
# They keep your system Python clean and make projects reproducible.


# ---------------------------------------------------------------------------
# Rank 2 — Easy
# ---------------------------------------------------------------------------

# Task 2.1
# pip install requests

# Task 2.2
# pip list

# Task 2.3
# pip uninstall numpy

# Task 2.4
# pip install --upgrade flask


# ---------------------------------------------------------------------------
# Rank 3 — Intermediate
# ---------------------------------------------------------------------------

# Task 3.1
# pip freeze > requirements.txt

# Task 3.2
# pip install -r requirements.txt

# Task 3.3
# Running "pip install -r requirements.txt" installs the exact versions of all
# packages listed in the file. This ensures that any machine can recreate the
# same environment, which is essential for collaboration, deployment, and long-
# term maintenance of a project.


# ---------------------------------------------------------------------------
# Rank 4 — Advanced
# ---------------------------------------------------------------------------

# Task 4.1
# Steps to rebuild an environment:
# 1. Delete the .venv folder.
# 2. Create a new environment: python -m venv .venv
# 3. Activate the environment.
# 4. Install dependencies: pip install -r requirements.txt

# Task 4.2
# Example scenario:
# A data science project may need numpy==1.26 while a legacy app requires
# numpy==1.20 because newer versions break compatibility. Virtual environments
# allow each project to use its own version without conflict.

# Task 4.3
# The .venv folder is large and machine-specific. It contains binaries,
# compiled files, and platform-dependent paths. Uploading it to GitHub is
# unnecessary and causes huge repositories. Instead, share only
# requirements.txt so others can rebuild the environment.


# ---------------------------------------------------------------------------
# Rank 5 — Professional
# ---------------------------------------------------------------------------

# Task 5.1
# Full project setup workflow:
# 1. Create a new project folder.
# 2. Open a terminal inside the folder.
# 3. Create a virtual environment: python -m venv .venv
# 4. Activate the environment.
# 5. Install required packages using pip.
# 6. Freeze dependencies: pip freeze > requirements.txt
# 7. Add .venv/ to .gitignore.
# 8. Push the project (without .venv) to GitHub.

# Task 5.2
# Steps to run a received project:
# 1. Navigate to the project folder.
# 2. Create a new environment: python -m venv .venv
# 3. Activate the environment.
# 4. Install dependencies: pip install -r requirements.txt
# 5. Run the project script normally: python script_name.py

# Task 5.3
# Installing globally affects the entire system and may break other projects.
# Installing inside a virtual environment isolates dependencies so changes do
# not interfere with any other project. Global installs are risky and should
# be avoided unless absolutely necessary.


# End of Solutions
