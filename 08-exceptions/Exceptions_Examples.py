"""
Module 8 — Exceptions: Practical Examples
-----------------------------------------

This file contains runnable examples demonstrating real-world exception
handling patterns.

Examples are grouped by difficulty from Rank 1 → Rank 5.
"""


# ---------------------------------------------------------------------------
# Rank 1 — Beginner Examples
# ---------------------------------------------------------------------------

def example_1_basic_try_except():
    """Simple try/except demonstration."""
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Cannot divide by zero!")


def example_2_basic_conversion():
    """Handle invalid integer conversion."""
    user_input = "abc"
    try:
        num = int(user_input)
    except ValueError:
        print("Invalid number!")


# ---------------------------------------------------------------------------
# Rank 2 — Easy Examples
# ---------------------------------------------------------------------------

def example_3_multiple_exceptions():
    """Catching different types of errors."""
    values = [10, 0, "hello"]

    for v in values:
        try:
            print(100 / v)
        except ZeroDivisionError:
            print("Cannot divide by zero!")
        except TypeError:
            print("Invalid type — must be a number!")


def example_4_else_finally():
    """Using else and finally."""
    try:
        number = int("25")
    except ValueError:
        print("Invalid number!")
    else:
        print("Conversion successful:", number)
    finally:
        print("Finished processing.")


# ---------------------------------------------------------------------------
# Rank 3 — Intermediate Examples
# ---------------------------------------------------------------------------

def example_5_file_handling():
    """Handle missing file errors gracefully."""
    filename = "missing_file.txt"
    try:
        f = open(filename, "r")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    else:
        print(f.read())
        f.close()
    finally:
        print("File operation attempted.")


def example_6_safe_dict_lookup():
    """Demonstrate KeyError handling."""
    data = {"name": "Peyman", "age": 43}
    key = "email"

    try:
        print("Email:", data[key])
    except KeyError:
        print("Key does not exist!")


def example_7_safe_input_conversion(value):
    """Convert a value to int with safe fallback."""
    try:
        num = int(value)
    except (ValueError, TypeError):
        print("Invalid input value:", value)
    else:
        print("Converted to:", num)


# ---------------------------------------------------------------------------
# Rank 4 — Advanced Examples
# ---------------------------------------------------------------------------

def example_8_raise_custom_exception():
    """Show how to raise custom errors."""
    age = -5
    try:
        if age < 0:
            raise ValueError("Age cannot be negative!")
    except ValueError as e:
        print("Error:", e)


def example_9_validate_data():
    """Using raise inside validation logic."""
    def validate_username(name):
        if not isinstance(name, str):
            raise TypeError("Username must be a string.")
        if len(name) < 3:
            raise ValueError("Username must be at least 3 characters long.")
        return True

    try:
        validate_username("Al")
    except Exception as e:
        print("Validation failed:", e)


def example_10_exception_chaining():
    """Show how one exception can cause another."""
    try:
        try:
            int("abc")
        except ValueError as original_error:
            raise RuntimeError("Conversion failed!") from original_error
    except RuntimeError as e:
        print("Chained error:", e)


# ---------------------------------------------------------------------------
# Rank 5 — Professional Examples
# ---------------------------------------------------------------------------

def example_11_safe_division(a, b):
    """Professional safe-division with detailed messages."""
    try:
        result = a / b
    except ZeroDivisionError:
        return "Division error: cannot divide by zero."
    except TypeError:
        return "Type error: inputs must be numbers."
    else:
        return f"Result = {result}"
    finally:
        print("Division attempt complete.")


def example_12_process_order(quantity):
    """A realistic example with validation + exception handling."""
    try:
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
    except ValueError as e:
        print("Order error:", e)
    else:
        print(f"Order accepted for {quantity} items.")


def example_13_robust_workflow():
    """
    A simulated workflow:
    - read data
    - validate data
    - process data
    Each part can throw different exceptions.
    """

    def read_data():
        raise FileNotFoundError("Data file is missing.")

    def validate_data(data):
        if data != "EXPECTED":
            raise ValueError("Invalid data format.")

    try:
        data = read_data()
        validate_data(data)
    except FileNotFoundError as e:
        print("Workflow failed (missing file):", e)
    except ValueError as e:
        print("Workflow failed (bad data):", e)
    else:
        print("Workflow completed successfully!")
    finally:
        print("Workflow ended.")


# ---------------------------------------------------------------------------
# Demonstration Section
# ---------------------------------------------------------------------------

def main():
    print("--- Rank 1 ---")
    example_1_basic_try_except()
    example_2_basic_conversion()

    print("\n--- Rank 2 ---")
    example_3_multiple_exceptions()
    example_4_else_finally()

    print("\n--- Rank 3 ---")
    example_5_file_handling()
    example_6_safe_dict_lookup()
    example_7_safe_input_conversion("123")
    example_7_safe_input_conversion("abc")

    print("\n--- Rank 4 ---")
    example_8_raise_custom_exception()
    example_9_validate_data()
    example_10_exception_chaining()

    print("\n--- Rank 5 ---")
    print(example_11_safe_division(10, 2))
    print(example_11_safe_division(10, 0))
    example_12_process_order(5)
    example_12_process_order(-1)
    example_13_robust_workflow()


if __name__ == "__main__":
    main()
