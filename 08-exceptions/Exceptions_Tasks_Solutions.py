"""
Module 8 — Exceptions: Task Solutions
-------------------------------------

This file contains clean, professional solutions for all tasks from
Exceptions_Tasks.py.

Covers:
- Basic try/except
- Specific exception handling
- else/finally usage
- Raising exceptions
- Validation patterns
- Exception chaining
- Professional workflow design
"""


# =============================================================================
# Rank 1 — Beginner
# =============================================================================

def divide_numbers(a, b):
    """Safely divide two numbers."""
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Inputs must be numbers"


def safe_int_convert(value):
    """Convert to int or return friendly error."""
    try:
        return int(value)
    except ValueError:
        return "Invalid integer"


def open_file_basic(filename):
    """Open a file and read one line, handle missing file."""
    try:
        with open(filename, "r") as f:
            return f.readline().strip()
    except FileNotFoundError:
        return "File not found"


# =============================================================================
# Rank 2 — Easy
# =============================================================================

def read_list_index(values, index):
    """Return value at index or fallback message."""
    try:
        return values[index]
    except IndexError:
        return "Index out of range"


def dict_safe_get(data, key):
    """Safely get key from dictionary."""
    try:
        return data[key]
    except KeyError:
        return "Key not found"


def convert_multiple(values):
    """
    Convert each item to int.
    Replace failed conversions with "invalid".
    """
    result = []
    for v in values:
        try:
            result.append(int(v))
        except (ValueError, TypeError):
            result.append("invalid")
    return result


# =============================================================================
# Rank 3 — Intermediate
# =============================================================================

def safe_file_read(filename):
    """Demonstrate full try/except/else/finally structure."""
    try:
        f = open(filename, "r")
    except FileNotFoundError:
        return "Missing file"
    else:
        content = f.read()
        f.close()
        return content
    finally:
        print("File operation complete")


def validate_positive_number(value):
    """
    Convert to int and ensure it is > 0.
    """
    try:
        num = int(value)
    except (ValueError, TypeError):
        return "Invalid number"

    if num <= 0:
        return "Must be positive"

    return num


def safe_division_with_message(a, b):
    """
    Return "Error: <message>" when any exception occurs.
    """
    try:
        return a / b
    except Exception as e:
        return f"Error: {e}"


# =============================================================================
# Rank 4 — Advanced
# =============================================================================

def raise_if_negative(number):
    """Raise ValueError if number < 0."""
    if number < 0:
        raise ValueError("Negative number provided")
    return True


def ensure_string(value):
    """
    Validate a string.
    - Must be a string
    - Must be non-empty
    """
    if not isinstance(value, str):
        raise TypeError("Value must be a string")
    if value == "":
        raise ValueError("String cannot be empty")

    return value.upper()


def divide_and_log(a, b):
    """
    Perform a division and re-raise errors with a new message.
    """
    try:
        return a / b
    except Exception as original_error:
        raise RuntimeError("Failed division operation") from original_error


# =============================================================================
# Rank 5 — Professional
# =============================================================================

def process_user_record(record):
    """
    Validate a user record with multiple fields.
    Return detailed error messages.
    """
    try:
        name = record["name"]
        age = record["age"]
        email = record["email"]
    except KeyError as e:
        return f"Invalid record: missing field {e}"

    # Validate name
    if not isinstance(name, str):
        return "Invalid record: name must be a string"
    if len(name) == 0:
        return "Invalid record: name cannot be empty"

    # Validate age
    try:
        age_value = int(age)
    except (ValueError, TypeError):
        return "Invalid record: age must be an integer"
    if age_value <= 0:
        return "Invalid record: age must be positive"

    # Validate email
    if not isinstance(email, str):
        return "Invalid record: email must be a string"
    if "@" not in email:
        return "Invalid record: invalid email format"

    return "Record OK"


def safe_workflow_step(step_func):
    """
    Execute a workflow step and catch all exceptions.
    """
    try:
        step_func()
        return "Step OK"
    except Exception as e:
        return f"Step failed: {e}"


def batch_process(values):
    """
    Convert each item to int.
    Track successes and failures in separate lists.
    """
    result = {"success": [], "failed": []}

    for v in values:
        try:
            result["success"].append(int(v))
        except (ValueError, TypeError):
            result["failed"].append(v)

    return result


# =============================================================================
# Optional Self-Test
# =============================================================================

if __name__ == "__main__":
    print(divide_numbers(10, 0))
    print(safe_int_convert("abc"))
    print(open_file_basic("missing.txt"))

    print(read_list_index([1,2,3], 5))
    print(dict_safe_get({"a":1}, "b"))
    print(convert_multiple(["10", "xx", 30]))

    print(validate_positive_number("-5"))
    print(safe_division_with_message(10, 0))

    try:
        raise_if_negative(-2)
    except Exception as e:
        print("Caught:", e)

    print(process_user_record({"name": "Peyman", "age": 43, "email": "p@example.com"}))
    print(batch_process(["10", "x", 25]))
