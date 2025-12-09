"""
Module 38 — Ellipsis: Practice Exercises
Comprehensive practice with the Ellipsis object (...) in Python,
from beginner to more professional, production-style usage.

In this module I:
- Understand that ... is a real object named Ellipsis.
- Use Ellipsis as a placeholder in functions and classes.
- Use Ellipsis as a special sentinel value in APIs.
- Handle Ellipsis in custom __getitem__ for "multi-dimensional" access.
- Use Ellipsis in pattern matching and configuration examples.

Ranking system:
- Rank 1  -> Beginner: basic understanding of Ellipsis and type.
- Rank 2  -> Easy: using Ellipsis as a placeholder (to-do).
- Rank 3  -> Intermediate: Ellipsis as a sentinel default value.
- Rank 4  -> Advanced: handling Ellipsis in __getitem__.
- Rank 5  -> Professional: pattern matching and configuration tricks.

Author: Peyman Miyandashti
Date of Birth: 11/11/1983
ID Number: 250161
Year: 2025
"""

from __future__ import annotations
from typing import Any, List, Tuple, Dict, Optional, Iterable, Iterator, Union


# ===========================================================
# Rank 1 — Beginner
# What is Ellipsis?
# ===========================================================

print("Rank 1 — Beginner")

# Ellipsis is a built-in singleton object, just like None.
print("Ellipsis object:", Ellipsis)
print("Type of Ellipsis:", type(Ellipsis))
print("Ellipsis is Ellipsis:", Ellipsis is Ellipsis)

# You can also write it with dots:
dots = ...
print("dots is Ellipsis:", dots is Ellipsis)

print("-" * 50)


# ===========================================================
# Rank 2 — Easy
# Using Ellipsis as a placeholder (to-do)
# ===========================================================

print("Rank 2 — Easy")


def not_implemented_yet(x: int) -> int:
    """
    Example of using Ellipsis to mark code we will implement later.

    (In real projects, we usually raise NotImplementedError.)
    """
    # Placeholder: we haven't decided logic yet
    placeholder_logic = ...
    # Show that placeholder_logic is Ellipsis:
    print("placeholder_logic is Ellipsis:", placeholder_logic is Ellipsis)
    # For now, just return x unchanged.
    return x


result = not_implemented_yet(10)
print("Result of not_implemented_yet(10):", result)

# More realistic placeholder: use raise NotImplementedError, but show Ellipsis
def todo_example() -> None:
    """
    In code, sometimes people write ... to visually mark TODO sections.
    """
    ...
    # This function does nothing (pass), but shows the style.


todo_example()
print("-" * 50)


# ===========================================================
# Rank 3 — Intermediate
# Ellipsis as a sentinel default value
# ===========================================================

print("Rank 3 — Intermediate")

_SENTINEL = Ellipsis  # special unique value


def update_settings(
    settings: Dict[str, Any],
    *,
    username: Any = _SENTINEL,
    language: Any = _SENTINEL,
    theme: Any = _SENTINEL,
) -> Dict[str, Any]:
    """
    Update a settings dictionary.

    If a parameter is Ellipsis (the sentinel), we do NOT change that field.
    If a parameter is None or some other value, we DO update it.

    This way, we can distinguish:
    - "no change" (Ellipsis)
    - "set to None" (explicit None)
    """

    if username is not _SENTINEL:
        settings["username"] = username
    if language is not _SENTINEL:
        settings["language"] = language
    if theme is not _SENTINEL:
        settings["theme"] = theme
    return settings


user_settings = {"username": "pey", "language": "es", "theme": "light"}
print("Original settings:", user_settings)

# Change language only
update_settings(user_settings, language="en")
print("After language='en':", user_settings)

# Set theme to None (meaning: maybe auto theme)
update_settings(user_settings, theme=None)
print("After theme=None:", user_settings)

# Do not change anything (no arguments -> all Ellipsis)
update_settings(user_settings)
print("After no arguments:", user_settings)

print("-" * 50)


# ===========================================================
# Rank 4 — Advanced
# Handling Ellipsis in custom __getitem__
# ===========================================================

print("Rank 4 — Advanced")


class Matrix:
    """
    A tiny 2D matrix class that supports Ellipsis in indexing.

    - m[i, j]       -> single cell
    - m[i, :]       -> row slice
    - m[:, j]       -> column slice
    - m[..., j]     -> same as m[:, j]
    - m[i, ...]     -> same as m[i, :]

    We will represent data as a list of lists.
    """

    def __init__(self, rows: List[List[Any]]) -> None:
        self._rows = [list(r) for r in rows]
        if self._rows:
            width = len(self._rows[0])
            if any(len(r) != width for r in self._rows):
                raise ValueError("All rows must have the same length")

    @property
    def shape(self) -> Tuple[int, int]:
        if not self._rows:
            return (0, 0)
        return (len(self._rows), len(self._rows[0]))

    def __getitem__(self, key: Any) -> Any:
        """
        Support patterns:
        - m[i, j]
        - m[i, :]
        - m[:, j]
        - m[..., j]
        - m[i, ...]
        """
        if not isinstance(key, tuple) or len(key) != 2:
            raise TypeError("Matrix indices must be of the form m[row, col]")

        row_idx, col_idx = key

        num_rows, num_cols = self.shape

        # Convert Ellipsis to equivalent slices:
        if row_idx is Ellipsis:
            row_idx = slice(None)
        if col_idx is Ellipsis:
            col_idx = slice(None)

        # Row slice, column slice -> submatrix (list of lists)
        if isinstance(row_idx, slice) and isinstance(col_idx, slice):
            rows = range(*row_idx.indices(num_rows))
            cols = range(*col_idx.indices(num_cols))
            return [[self._rows[i][j] for j in cols] for i in rows]

        # Row slice, single column -> list
        if isinstance(row_idx, slice) and isinstance(col_idx, int):
            rows = range(*row_idx.indices(num_rows))
            return [self._rows[i][col_idx] for i in rows]

        # Single row, column slice -> list
        if isinstance(row_idx, int) and isinstance(col_idx, slice):
            cols = range(*col_idx.indices(num_cols))
            return [self._rows[row_idx][j] for j in cols]

        # Single row, single column -> cell
        if isinstance(row_idx, int) and isinstance(col_idx, int):
            return self._rows[row_idx][col_idx]

        raise TypeError("Unsupported index combination")

    def __repr__(self) -> str:
        return f"Matrix(shape={self.shape}, rows={self._rows!r})"


matrix_data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

m = Matrix(matrix_data)
print("Matrix m:", m)
print("m.shape:", m.shape)

print("m[0, 0]:", m[0, 0])
print("m[1, ...]:", m[1, ...])    # row 1, all columns
print("m[..., 2]:", m[..., 2])    # all rows, column 2
print("m[:, 1:3]:", m[:, 1:3])    # all rows, columns 1-2

print("-" * 50)


# ===========================================================
# Rank 5 — Professional
# Pattern matching and configuration tricks with Ellipsis
# ===========================================================

print("Rank 5 — Professional")


def describe_sequence(seq: Iterable[Any]) -> str:
    """
    Use structural pattern matching with Ellipsis to describe sequences.

    Requires Python 3.10+ for match/case syntax.
    """
    seq_list = list(seq)

    match seq_list:
        case [first, second, *rest] if rest:
            # At least 3 elements
            return f"Sequence with at least 3 elements, first={first!r}, second={second!r}"
        case [single]:
            return f"Sequence with a single element: {single!r}"
        case []:
            return "Empty sequence"
        case [*prefix, last]:
            # This pattern uses * and implicitly uses the idea of "..."
            return f"Sequence ending with {last!r}, length={len(seq_list)}"
        case _:
            return "Unknown sequence pattern"


print("describe_sequence([]):", describe_sequence([]))
print("describe_sequence([42]):", describe_sequence([42]))
print("describe_sequence([1, 2, 3, 4]):", describe_sequence([1, 2, 3, 4]))
print("describe_sequence(['a', 'b', 'c']):", describe_sequence(["a", "b", "c"]))


# Another Ellipsis trick: partial configuration
DEFAULT_CONFIG = {
    "host": "localhost",
    "port": 8000,
    "debug": False,
    "database": "school_db",
}


def merge_config(base: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
    """
    Merge two config dicts, where Ellipsis in override means:
    "keep the base value for this key".

    This allows us to explicitly write:
      {"host": "example.com", "database": ...}
    which means: change host, keep database from base.
    """
    result = dict(base)
    for key, value in override.items():
        if value is Ellipsis:
            # Keep base value (do nothing)
            continue
        result[key] = value
    return result


override_1 = {"host": "example.com", "database": ...}
override_2 = {"debug": True, "port": ...}

merged_1 = merge_config(DEFAULT_CONFIG, override_1)
merged_2 = merge_config(DEFAULT_CONFIG, override_2)

print("\nDEFAULT_CONFIG:", DEFAULT_CONFIG)
print("override_1:", override_1)
print("merged_1:", merged_1)
print("override_2:", override_2)
print("merged_2:", merged_2)

print("-" * 50)
