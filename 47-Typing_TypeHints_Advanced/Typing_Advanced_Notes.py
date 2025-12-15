"""
Typing_Advanced_Notes.py
Module 47 — Typing & Type Hints (Advanced)
Author: Peyman Miyandashti
Year: 2025

This module explains advanced typing features in Python
using the typing module.
"""

from typing import (
    List, Dict, Tuple, Set,
    Union, Optional, Literal,
    Callable, TypeVar, Generic,
    Protocol, TypedDict
)

# ---------------------------------------------------------------------------
# 1. Why Advanced Typing?
# ---------------------------------------------------------------------------
# Advanced typing helps describe real constraints in code.
# It improves readability and tooling support.


# ---------------------------------------------------------------------------
# 2. Union and Optional
# ---------------------------------------------------------------------------

def parse_int(value: Union[str, int]) -> int:
    return int(value)

def find_user(user_id: int) -> Optional[str]:
    if user_id == 1:
        return "Admin"
    return None


# ---------------------------------------------------------------------------
# 3. Literal Types
# ---------------------------------------------------------------------------

def set_mode(mode: Literal["r", "w", "a"]) -> None:
    print("Mode:", mode)


# ---------------------------------------------------------------------------
# 4. Generic Collections
# ---------------------------------------------------------------------------

scores: List[int] = [90, 85, 100]
users: Dict[str, int] = {"Peyman": 43}
point: Tuple[int, int] = (10, 20)


# ---------------------------------------------------------------------------
# 5. Callable
# ---------------------------------------------------------------------------

def apply(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)


# ---------------------------------------------------------------------------
# 6. TypeVar and Generics
# ---------------------------------------------------------------------------

T = TypeVar("T")

def first_item(items: List[T]) -> T:
    return items[0]


# ---------------------------------------------------------------------------
# 7. Generic Classes
# ---------------------------------------------------------------------------

class Box(Generic[T]):
    def __init__(self, value: T):
        self.value = value

    def get(self) -> T:
        return self.value


# ---------------------------------------------------------------------------
# 8. Protocol (Structural Typing)
# ---------------------------------------------------------------------------

class Speaker(Protocol):
    def speak(self) -> str:
        ...


class Person:
    def speak(self) -> str:
        return "Hello"


def make_speak(entity: Speaker) -> None:
    print(entity.speak())


# ---------------------------------------------------------------------------
# 9. TypedDict
# ---------------------------------------------------------------------------

class UserData(TypedDict):
    name: str
    age: int


user: UserData = {"name": "Peyman", "age": 43}


# ---------------------------------------------------------------------------
# 10. Best Practices
# ---------------------------------------------------------------------------
# - Type for humans first
# - Avoid over-typing
# - Prefer clarity over complexity
# - Use typing to communicate intent


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# Advanced typing is a design tool.
# It helps write safer and more maintainable code.
#
# Next Step:
# Continue with Typing_Advanced_Examples.py
