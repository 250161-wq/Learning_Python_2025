"""
Module 12 — Conditionals (if, elif, else)
Professional Notes

This file explains how Python makes decisions using conditional statements.
Conditionals let a program choose different actions depending on values,
comparisons, and logical expressions. They are one of the most important
building blocks in programming.
"""

# ---------------------------------------------------------------------------
# 1. Introduction to Conditionals
# ---------------------------------------------------------------------------
# A conditional allows a program to run certain code only when a specific
# condition is True. If the condition is False, the program can choose to do
# something else.
#
# Python uses three main keywords for decision-making:
#   - if      → first condition to check
#   - elif    → additional conditions to test
#   - else    → fallback when no previous conditions are True
#
# Conditionals allow a program to “think” by evaluating expressions.


# ---------------------------------------------------------------------------
# 2. Basic if Statement
# ---------------------------------------------------------------------------
# Syntax:
#     if condition:
#         block of code
#
# Example:
age = 18
if age >= 18:
    print("You are an adult.")

# If the condition is True, the block runs. If not, Python skips it.


# ---------------------------------------------------------------------------
# 3. Adding else
# ---------------------------------------------------------------------------
# The else block runs only when all previous conditions are False.
#
password = "python123"
if password == "python123":
    print("Access granted.")
else:
    print("Access denied.")

# Only one of the two blocks will execute.


# ---------------------------------------------------------------------------
# 4. Adding elif (else + if)
# ---------------------------------------------------------------------------
# elif allows multiple different conditions to be checked in order.
#
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: D or below")

# Python checks conditions from top to bottom.
# Only the first True condition runs.


# ---------------------------------------------------------------------------
# 5. Comparison Operators
# ---------------------------------------------------------------------------
# Conditionals use comparison operators to evaluate values:
#
#   ==   equal to
#   !=   not equal to
#   >    greater than
#   <    less than
#   >=   greater or equal
#   <=   less or equal
#
# Example:
temperature = 32
if temperature < 0:
    print("Freezing!")
elif temperature < 20:
    print("Cold")
else:
    print("Warm")

# Comparisons always produce a Boolean value (True or False).


# ---------------------------------------------------------------------------
# 6. Logical Operators (and, or, not)
# ---------------------------------------------------------------------------
# Logical operators allow combining multiple conditions.
#
#   and   → both conditions must be True
#   or    → at least one condition must be True
#   not   → reverses a condition
#
# Examples:

age = 25
is_member = True

# Both must be True
if age >= 18 and is_member:
    print("Welcome to the club.")

# Either one can be True
if age < 18 or not is_member:
    print("Access restricted.")

# Reverse the condition
logged_in = False
if not logged_in:
    print("Please log in first.")


# ---------------------------------------------------------------------------
# 7. Nesting Conditionals
# ---------------------------------------------------------------------------
# A conditional can contain another conditional.
#
user = "admin"
password_ok = True

if user == "admin":
    if password_ok:
        print("Admin panel opened.")
    else:
        print("Wrong password.")
else:
    print("Unknown user.")

# Use nesting sparingly — too much nesting reduces readability.


# ---------------------------------------------------------------------------
# 8. Truthy and Falsy Values
# ---------------------------------------------------------------------------
# Python treats some values as True or False automatically.
#
# Falsy values:
#   0, 0.0
#   ""
#   []
#   {}
#   None
#   False
#
# Everything else is considered truthy.
#
# Example:
items = []

if not items:
    print("The list is empty.")
else:
    print("The list has items.")


# ---------------------------------------------------------------------------
# 9. Common Mistakes
# ---------------------------------------------------------------------------
# ❌ Using a single = instead of ==
#     if x = 5:   → INVALID
#
# ❌ Writing unreachable elif conditions
#     if x > 10:
#         ...
#     elif x > 5:  (this will never run if first is True)
#
# ❌ Overusing nested if statements instead of combining conditions
#
# ❌ Forgetting that indentation defines code blocks in Python


# ---------------------------------------------------------------------------
# 10. Best Practices
# ---------------------------------------------------------------------------
# ✔ Keep conditions simple and readable
# ✔ Use elif instead of long nested ifs
# ✔ Combine conditions with and/or when appropriate
# ✔ Use descriptive variable names
# ✔ Add comments when logic becomes complex
# ✔ Avoid deeply nested structures — refactor into functions


# ---------------------------------------------------------------------------
# 11. Summary
# ---------------------------------------------------------------------------
# In this module, I learned:
# - How to use if, elif, and else
# - How comparisons and logical operators work
# - How to write multiple decision branches
# - How to avoid common mistakes and keep logic clean
# - How conditionals appear in real-world applications
#
# End of Notes
