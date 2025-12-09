"""
Module 8 — Exceptions: Notes & Explanations
-------------------------------------------

Exceptions allow Python programs to respond to unexpected situations
WITHOUT crashing. Exception handling is one of the most important
skills for building safe, reliable, real-world software.

In this module I will learn:
- What exceptions are
- How errors propagate
- How to use try / except / else / finally
- How to catch specific exceptions
- How to raise exceptions intentionally
- How to write clean and professional error-handling code
"""


# ---------------------------------------------------------------------------
# 1. What Is an Exception?
# ---------------------------------------------------------------------------
"""
An exception is an event that interrupts normal program execution.

Examples:
    - Dividing by zero
    - Converting invalid input to int
    - Accessing a missing key in a dictionary
    - Opening a file that doesn’t exist

Without handling the exception, the program will CRASH.
"""


# ---------------------------------------------------------------------------
# 2. Basic try / except
# ---------------------------------------------------------------------------
"""
Structure:

    try:
        code that may fail
    except:
        what to do if it fails

Example:
"""

def divide_basic(a, b):
    try:
        return a / b
    except:
        return "Error occurred!"


# ---------------------------------------------------------------------------
# 3. Catching Specific Exceptions (Best Practice)
# ---------------------------------------------------------------------------
"""
Catching ALL exceptions is usually bad.

Better:

    try:
        risky_code
    except ZeroDivisionError:
        handle it
    except ValueError:
        handle it differently

This gives professional, predictable behavior.
"""

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero!"
    except TypeError:
        return "Inputs must be numbers!"


# ---------------------------------------------------------------------------
# 4. Using else and finally
# ---------------------------------------------------------------------------
"""
else:
    Runs ONLY if no exception occurs.

finally:
    Runs ALWAYS (useful for cleanup tasks).

Example:
"""

def read_file_example(filename):
    try:
        f = open(filename, "r")
    except FileNotFoundError:
        return "File not found."
    else:
        content = f.read()
        return content
    finally:
        print("Finished attempt to read file.")


# ---------------------------------------------------------------------------
# 5. The raise Statement (Raising Exceptions Intentionally)
# ---------------------------------------------------------------------------
"""
I can throw an exception when something is invalid.

    raise ValueError("Age must be positive")

This is EXTREMELY useful in real apps to validate data.
"""

def validate_age(age):
    if age < 0:
        raise ValueError("Age must be positive.")
    return True


# ---------------------------------------------------------------------------
# 6. Handling Multiple Exceptions Together
# ---------------------------------------------------------------------------
"""
Multiple exceptions can be grouped:

    except (TypeError, ValueError):
        handle both

This prevents duplicate code blocks.
"""

def parse_int(value):
    try:
        return int(value)
    except (TypeError, ValueError):
        return "Invalid integer."


# ---------------------------------------------------------------------------
# 7. Exception Hierarchy (Advanced Concept)
# ---------------------------------------------------------------------------
"""
Most exceptions inherit from BaseException → Exception.

Common ones:
- ValueError
- TypeError
- KeyError
- IndexError
- FileNotFoundError
- ZeroDivisionError

We usually catch child classes, not the root ones.
"""


# ---------------------------------------------------------------------------
# 8. Avoiding Bare except (VERY IMPORTANT)
# ---------------------------------------------------------------------------
"""
NEVER do this:

    try:
        something
    except:
        pass

Why? Because it hides ALL types of errors, even KeyboardInterrupt.

Professional rule:
CATCH ONLY WHAT YOU EXPECT.
"""


# ---------------------------------------------------------------------------
# 9. Real-World Example: Safe User Input
# ---------------------------------------------------------------------------

def get_user_number(text):
    """
    Try converting user input to an integer safely.
    """
    try:
        return int(text)
    except ValueError:
        return "Please enter a valid number."


# ---------------------------------------------------------------------------
# 10. Real-World Example: Validating Data
# ---------------------------------------------------------------------------

def process_order(quantity):
    """
    Validate order quantity before processing.
    """
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")
    return f"Order accepted for {quantity} items."


# ---------------------------------------------------------------------------
# 11. Using try/except with Dictionaries
# ---------------------------------------------------------------------------

def safe_lookup(data, key):
    """
    Return value for key, or a message if missing.
    """
    try:
        return data[key]
    except KeyError:
        return "Key not found."


# ---------------------------------------------------------------------------
# 12. Summary of Best Practices
# ---------------------------------------------------------------------------
"""
✔ Catch specific exceptions (ZeroDivisionError, ValueError, etc.)
✔ Use try ONLY around the code that may fail
✔ Use else when code should run only if no exceptions occur
✔ Use finally for cleanup logic
✔ Raise exceptions intentionally for invalid data
✔ Avoid bare except
✔ Write clean, readable error-handling code
"""


# ---------------------------------------------------------------------------
# 13. Summary
# ---------------------------------------------------------------------------
"""
In this module I learned:

- How exceptions work and why they matter
- How to use try/except effectively
- How to handle specific exceptions
- How to use else/finally
- How to raise exceptions
- How to design safer, more robust programs

Next:
    Run Exceptions_Examples.py to see exceptions in action.
    Then complete the challenges in Exceptions_Tasks.py.
"""
