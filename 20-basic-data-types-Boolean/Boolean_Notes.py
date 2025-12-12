"""
Module 20 — Basic Data Types: Boolean
Author: Peyman Miyandashti
Year: 2025

Comprehensive notes on Python's boolean type — the foundation of all logical 
decision-making in programming.

In this module, I explore what booleans are, how Python creates them, how they 
behave inside expressions, and how they control the flow of a program. 
Booleans are simple but extremely powerful. They allow programs to think, 
respond, and make choices.

Key Concepts Covered in This File:
- What a boolean is and why it matters.
- How to create and use boolean variables.
- Comparison operators (==, !=, <, >, <=, >=).
- Logical operators (and, or, not).
- Truthy and falsy values in Python.
- Real examples where booleans make decisions in programs.

Recommended Workflow:
Start with these notes, experiment with all examples inside this file, 
and prepare yourself for the examples and tasks that follow in the next files.
"""


# ---------------------------------------------------------------------------
# 1. What Is a Boolean?
# ---------------------------------------------------------------------------
# A boolean (bool) represents one of two possible values:
#   True  or  False
#
# Python uses booleans to make decisions — for example, inside if-statements,
# loops, validations, and game logic.

is_active = True
is_admin = False


# ---------------------------------------------------------------------------
# 2. Comparison Operators
# ---------------------------------------------------------------------------
# Comparison expressions ALWAYS return a boolean.
# They are one of the most common ways booleans are created in code.

x = 10
y = 20

equal_check = (x == y)       # False
not_equal = (x != y)         # True
greater_than = (y > x)       # True
less_or_equal = (x <= y)     # True


# ---------------------------------------------------------------------------
# 3. Logical Operators: and, or, not
# ---------------------------------------------------------------------------
# These allow combining multiple boolean expressions into more complex logic.
#   and  → True if both conditions are True
#   or   → True if at least one condition is True
#   not  → Flips True to False, and False to True

age = 17
has_permission = True

can_enter = (age >= 18) or has_permission  # True because permission is True
is_teen = (age >= 13) and (age <= 19)      # True
not_admin = not is_admin                   # True, since is_admin = False


# ---------------------------------------------------------------------------
# 4. Truthy and Falsy Values
# ---------------------------------------------------------------------------
# Python automatically interprets some non-boolean values as True or False.
#
# Falsy values (evaluated as False):
#   0, 0.0, "", [], {}, (), None, False
#
# Truthy values (evaluated as True):
#   Any non-empty collection, any number except zero, any object that is not None.

truthy_example = "Hello"
falsy_example = ""

print(bool(truthy_example))   # True
print(bool(falsy_example))    # False


# ---------------------------------------------------------------------------
# 5. Booleans in Realistic Scenarios
# ---------------------------------------------------------------------------

# Example 1: Checking login access
user_password = "1234"
input_password = "1234"

login_success = (input_password == user_password)
print("Login success:", login_success)

# Example 2: Discount eligibility
age = 65
is_student = False
eligible_for_discount = (age >= 60) or is_student
print("Eligible for discount:", eligible_for_discount)

# Example 3: Simple validation
name = "Peyman"
is_valid_name = (name != "") and (len(name) >= 3)
print("Name valid:", is_valid_name)


# ---------------------------------------------------------------------------
# 6. Final Notes
# ---------------------------------------------------------------------------
# Booleans appear everywhere in real code:
#   - Input validation
#   - Conditional logic
#   - Loops
#   - Error checking
#   - Game events
#   - User permissions
#
# Mastering booleans makes it easier to understand how programs make 
# decisions and react to different situations.

# Next Steps:
# Continue with Boolean_Examples.py to apply these ideas in small, practical snippets.
