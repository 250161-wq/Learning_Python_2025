"""
NoneType_Examples.py
Module 21 — NoneType
Author: Peyman Miyandashti
Year: 2025

This file contains practical, easy-to-understand examples showing how None
appears in real Python code. Each example is focused and demonstrates a 
specific behavior or best practice related to NoneType.
"""


# ---------------------------------------------------------------------------
# Example 1: Basic None Assignment
# ---------------------------------------------------------------------------

value = None
print("Value is:", value)  # None


# ---------------------------------------------------------------------------
# Example 2: Checking if a Variable Is None
# ---------------------------------------------------------------------------

user_name = None

if user_name is None:
    print("No user name provided.")
else:
    print("User name:", user_name)


# ---------------------------------------------------------------------------
# Example 3: Function That Implicitly Returns None
# ---------------------------------------------------------------------------

def welcome_message():
    print("Welcome!")  # No return statement → returns None automatically

result = welcome_message()
print("Function returned:", result)  # None


# ---------------------------------------------------------------------------
# Example 4: Function with None as Default Argument
# ---------------------------------------------------------------------------

def greet(text, recipient=None):
    if recipient is None:
        print("Broadcast:", text)
    else:
        print(f"Message to {recipient}: {text}")

greet("Hello everyone!")
greet("Hello Peyman!", "Peyman")


# ---------------------------------------------------------------------------
# Example 5: None Used to Represent Missing Data
# ---------------------------------------------------------------------------

temperature = None

if temperature is None:
    print("Temperature data not available.")
else:
    print("Temperature is:", temperature)


# ---------------------------------------------------------------------------
# Example 6: Checking Function Results Against None
# ---------------------------------------------------------------------------

def get_discount(user_type):
    if user_type == "vip":
        return 0.25
    return None  # No discount for regular users

discount = get_discount("regular")

if discount is None:
    print("No discount applied.")
else:
    print("Discount:", discount)


# ---------------------------------------------------------------------------
# Example 7: None Is Falsy in Boolean Context
# ---------------------------------------------------------------------------

value = None

if value:
    print("This will NOT run.")
else:
    print("None is considered False in conditions.")


# ---------------------------------------------------------------------------
# Example 8: Difference Between None and Empty Values
# ---------------------------------------------------------------------------

empty_list = []
empty_string = ""
nothing_here = None

print("Empty list is truthy?", bool(empty_list))   # False
print("Empty string is truthy?", bool(empty_string))  # False
print("None is truthy?", bool(nothing_here))          # False

# Even though all three are falsy, they represent DIFFERENT meanings.


# ---------------------------------------------------------------------------
# Example 9: Using None as a Reset or Clear Operation
# ---------------------------------------------------------------------------

status = "READY"
print("Status:", status)

# Now reset it
status = None
print("Status after reset:", status)


# ---------------------------------------------------------------------------
# Example 10: None Returned From a Loop That Doesn't Find a Match
# ---------------------------------------------------------------------------

def find_first_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            return num
    return None   # No even number found

result = find_first_even([1, 3, 5, 7])
print("First even number found:", result)
