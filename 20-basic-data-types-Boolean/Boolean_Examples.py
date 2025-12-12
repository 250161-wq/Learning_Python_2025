"""
Boolean_Examples.py
Module 20 — Basic Data Types: Boolean
Author: Peyman Miyandashti
Year: 2025

This file contains small, practical examples demonstrating how booleans work
in real Python code. Each example is focused, easy to test, and designed to
build intuition about boolean expressions, comparisons, and logical operators.

These examples prepare me for the tasks in the next file.
"""

# ---------------------------------------------------------------------------
# Example 1: Basic Boolean Variables
# ---------------------------------------------------------------------------

is_logged_in = True
is_admin = False

print("Logged in:", is_logged_in)
print("Admin user:", is_admin)


# ---------------------------------------------------------------------------
# Example 2: Comparison Expressions
# ---------------------------------------------------------------------------

temperature = 30

print("Is it hot?", temperature > 25)       # True
print("Is it freezing?", temperature <= 0)  # False
print("Is it exactly 30?", temperature == 30)  # True


# ---------------------------------------------------------------------------
# Example 3: Multiple Conditions with 'and'
# ---------------------------------------------------------------------------

age = 16
has_parent_permission = True

can_watch_movie = (age >= 18) and has_parent_permission
print("Can watch movie:", can_watch_movie)   # False


# ---------------------------------------------------------------------------
# Example 4: Multiple Conditions with 'or'
# ---------------------------------------------------------------------------

is_vip = False
has_ticket = True

can_enter_event = is_vip or has_ticket
print("Can enter event:", can_enter_event)   # True


# ---------------------------------------------------------------------------
# Example 5: Using 'not'
# ---------------------------------------------------------------------------

is_blocked = False
print("User allowed?", not is_blocked)      # True


# ---------------------------------------------------------------------------
# Example 6: Truthy and Falsy Values
# ---------------------------------------------------------------------------

username = ""
email = "peyman@example.com"

print("Username provided?", bool(username))   # False
print("Email provided?", bool(email))         # True


# ---------------------------------------------------------------------------
# Example 7: Using Booleans in Input Validation
# ---------------------------------------------------------------------------

score = 87
passed_exam = (score >= 60)

print("Did the student pass?", passed_exam)   # True


# ---------------------------------------------------------------------------
# Example 8: Login Check Example
# ---------------------------------------------------------------------------

correct_password = "python123"
entered_password = "python123"

login_ok = (entered_password == correct_password)
print("Login status:", login_ok)


# ---------------------------------------------------------------------------
# Example 9: Range Checking with Booleans
# ---------------------------------------------------------------------------

height = 1.72   # meters
is_typical_height = (1.50 <= height <= 1.90)

print("Height in typical range?", is_typical_height)


# ---------------------------------------------------------------------------
# Example 10: Combining Logic in a Realistic Scenario
# ---------------------------------------------------------------------------

has_id = True
has_age = True
age = 19

can_buy_ticket = has_id and has_age and (age >= 18)
print("Ticket purchase allowed:", can_buy_ticket)
