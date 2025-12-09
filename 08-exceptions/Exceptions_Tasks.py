"""
Module 8 — Exceptions: Practice Exercises
-----------------------------------------

This file contains structured practice tasks for learning Python
exception handling.

Tasks progress from beginner to professional difficulty.

I should:
- Implement each function myself.
- NOT look at solutions until I finish.
- Write clean, readable code.
- Move from Rank 1 → Rank 5 at my own pace.
"""


# =============================================================================
# Rank 1 — Beginner
# =============================================================================

def divide_numbers(a, b):
    """
    Task:
        Use try/except to divide two numbers.
        Return a friendly message if division fails.

    Cases to handle:
        - ZeroDivisionError
        - TypeError

    Return:
        float | str
    """
    # TODO: Implement basic try/except.
    pass


def safe_int_convert(value):
    """
    Task:
        Convert `value` to an integer.
        If conversion fails, return the message:
            "Invalid integer"

    Exception:
        ValueError

    Return:
        int | str
    """
    # TODO: Convert inside try.
    pass


def open_file_basic(filename):
    """
    Task:
        Try to open a file and read one line.
        If the file does not exist, return:
            "File not found"

    Exceptions:
        FileNotFoundError

    Return:
        str
    """
    # TODO: Use try/except.
    pass


# =============================================================================
# Rank 2 — Easy
# =============================================================================

def read_list_index(values, index):
    """
    Task:
        Read the element at `index` of list `values`.
        If index is invalid, return:
            "Index out of range"

    Exceptions:
        IndexError

    Return:
        Any | str
    """
    # TODO: Add try/except.
    pass


def dict_safe_get(data, key):
    """
    Task:
        Access data[key] safely.
        If the key is missing, return:
            "Key not found"

    Exceptions:
        KeyError

    Return:
        Any | str
    """
    # TODO: Implement exception handling.
    pass


def convert_multiple(values):
    """
    Task:
        Given a list of values, convert each to int.
        If a conversion fails, append:
            "invalid"

    Example:
        convert_multiple(["10", "xx", 25])
            -> [10, "invalid", 25]

    Exceptions:
        ValueError
        TypeError

    Return:
        list
    """
    # TODO: Loop + try/except.
    pass


# =============================================================================
# Rank 3 — Intermediate
# =============================================================================

def safe_file_read(filename):
    """
    Task:
        Use try / except / else / finally.

        Behavior:
            - TRY opening the file
            - EXCEPT if missing: return "Missing file"
            - ELSE: return file contents
            - FINALLY: print "File operation complete"

    Return:
        str
    """
    # TODO: Proper structure with all blocks.
    pass


def validate_positive_number(value):
    """
    Task:
        Convert value to int.
        If invalid, return:
            "Invalid number"
        If number <= 0, return:
            "Must be positive"
        Else return the number.

    Exceptions:
        ValueError
        TypeError

    Return:
        int | str
    """
    # TODO: try conversion + validate.
    pass


def safe_division_with_message(a, b):
    """
    Task:
        Divide a / b safely.
        If any exception occurs, return a string message:
            "Error: <message>"

    Example:
        safe_division_with_message(10, 0)
            -> "Error: division by zero"

    Exceptions:
        ZeroDivisionError
        TypeError

    Return:
        float | str
    """
    # TODO: Use exception object to capture message.
    pass


# =============================================================================
# Rank 4 — Advanced
# =============================================================================

def raise_if_negative(number):
    """
    Task:
        If number < 0, RAISE a ValueError with message:
            "Negative number provided"

        Otherwise return True.
    """
    # TODO: Use raise ValueError(...)
    pass


def ensure_string(value):
    """
    Task:
        If value is not a string, raise TypeError.
        If string is empty, raise ValueError.
        Otherwise return the string uppercased.

    Exceptions:
        TypeError
        ValueError

    Return:
        str
    """
    # TODO: Perform validations.
    pass


def divide_and_log(a, b):
    """
    Task:
        Perform a division inside try.
        If error happens, re-raise the exception with a NEW message:
            "Failed division operation"

        Hint:
            Use: raise NewError(...) from original_error
    """
    # TODO: Use chained exceptions.
    pass


# =============================================================================
# Rank 5 — Professional
# =============================================================================

def process_user_record(record):
    """
    Task:
        A realistic data-validation task.

        record = {
            "name": <string>,
            "age": <int>,
            "email": <string>
        }

        Requirements:
            - name must be a non-empty string
            - age must be a positive integer
            - email must contain '@'

        If ANY validation fails:
            return "Invalid record: <reason>"

        Otherwise:
            return "Record OK"

    Exceptions to consider:
        KeyError
        TypeError
        ValueError
    """
    # TODO: Extract keys safely + validate data + return messages.
    pass


def safe_workflow_step(step_func):
    """
    Task:
        Accept a function `step_func` that may raise errors.

        Behavior:
            - Try running step_func()
            - If it succeeds, return "Step OK"
            - If it fails, return:
                  "Step failed: <error message>"

        Exceptions:
            Exception (general)

    Return:
        str
    """
    # TODO: Run inside try, catch Exception.
    pass


def batch_process(values):
    """
    Task:
        For each item in `values`, try converting to int.

        Return a dictionary:
            {
                "success": [list of ints],
                "failed": [list of items that could not convert]
            }

        Use professional structured exception handling.

    Exceptions:
        ValueError
        TypeError
    """
    # TODO: Build dict + try conversion inside loop.
    pass


# =============================================================================
# Optional Testing Area
# =============================================================================

if __name__ == "__main__":
    pass
