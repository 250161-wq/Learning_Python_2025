"""
NoneType_Notes.py
Module 21 — NoneType
Author: Peyman Miyandashti
Year: 2025

Comprehensive notes about Python’s NoneType — a special type with a single value: None.
None represents “no value,” “nothing here,” or “not yet defined.” It appears in many
real-world programs and is essential for writing clean, predictable, professional code.

In this module, I explore:
- What NoneType is and why it exists.
- How and when Python uses None automatically.
- How to check if something is None (correct and incorrect ways).
- Why None is falsy, but NOT the same as False or 0.
- How None is used in default arguments, missing data, and function results.

This file prepares me for the examples and tasks that follow.
"""


# ---------------------------------------------------------------------------
# 1. What Is None?
# ---------------------------------------------------------------------------
# None is a special built-in value in Python. It is the ONLY value of type NoneType.
# It represents the absence of a value.
# Examples:
# - A function that doesn’t return anything returns None automatically.
# - A variable that has not been assigned a meaningful value may use None.
# - Missing or unknown data is often represented with None.

nothing_here = None
print("The value of nothing_here is:", nothing_here)  # Output: None


# ---------------------------------------------------------------------------
# 2. Checking for None (the correct way)
# ---------------------------------------------------------------------------
# IMPORTANT: To check whether a value *is* None, always use:
#       value is None
# NOT:
#       value == None       (this works but is NOT recommended)
#
# Python identity comparison (is) is the correct way because there is only ONE None object.

x = None
print(x is None)   # True
print(x == None)   # True, but less Pythonic


# ---------------------------------------------------------------------------
# 3. None vs False vs 0 vs "" (empty string)
# ---------------------------------------------------------------------------
# None is a falsy value, which means bool(None) evaluates to False.
# But None is NOT the same as:
# - False
# - 0
# - ""
# - []
# - {}
#
# They all evaluate to False in a boolean context, but they represent DIFFERENT meanings.

print(bool(None))  # False
print(None == False)  # False
print(None == 0)      # False


# ---------------------------------------------------------------------------
# 4. When Python Returns None Automatically
# ---------------------------------------------------------------------------
# If a function does not explicitly return a value, Python returns None.

def greet():
    print("Hello!")  # No return statement

result = greet()
print("The function returned:", result)  # Output: None


# ---------------------------------------------------------------------------
# 5. Using None in Default Function Arguments
# ---------------------------------------------------------------------------
# None is commonly used as a default argument to represent:
# - no value provided
# - optional parameters

def send_message(text, recipient=None):
    if recipient is None:
        print("No recipient specified — sending broadcast message:", text)
    else:
        print(f"Sending to {recipient}: {text}")

send_message("Hello!")                # Uses None as default
send_message("Hello!", "Peyman")      # Uses real value


# ---------------------------------------------------------------------------
# 6. None as a Placeholder for Missing or Unknown Data
# ---------------------------------------------------------------------------

user_age = None      # Age not provided yet
price = 14.99        # Price is known

if user_age is None:
    print("User age is unknown.")
else:
    print("User age:", user_age)


# ---------------------------------------------------------------------------
# 7. Common Mistakes With None and How to Avoid Them
# ---------------------------------------------------------------------------
# ❌ Mistake 1: Using == instead of 'is' to compare with None
# ✔ Correct: if value is None:

# ❌ Mistake 2: Assuming None behaves like False in all cases
# ✔ None is falsy, but you should check explicitly for None when meaning matters.

# ❌ Mistake 3: Returning None unintentionally from a function
# ✔ Always make sure your function returns something meaningful.


# ---------------------------------------------------------------------------
# 8. None in Realistic Scenarios
# ---------------------------------------------------------------------------

# Example 1: Database or API might return None when data is missing
username = None
if username is None:
    print("No username found. Using guest mode.")

# Example 2: Function that returns None when something fails
def find_discount(user_status):
    if user_status == "premium":
        return 0.20
    return None   # No discount

discount = find_discount("regular")
if discount is None:
    print("No discount available.")
else:
    print("Discount:", discount)


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# None is extremely useful for:
# - representing missing data
# - identifying optional arguments
# - signaling failure or special cases
# - writing cleaner, more expressive logic
#
# Next Step:
# Continue with NoneType_Examples.py to see practical demonstrations.
