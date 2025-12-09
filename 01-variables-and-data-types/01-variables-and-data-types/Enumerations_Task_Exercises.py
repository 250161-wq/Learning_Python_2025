"""
Module 26 — Enumerations (Enums) — Practice Tasks
Practice using Python enumerations (Enum, IntEnum, auto, IntFlag)
with real-world style examples.

In this module you:
- Learn how to define and use Enum and IntEnum.
- Practice using auto() for automatic values.
- Practice using IntFlag for bitwise permission-style enums.
- Use small helper functions that work with enums.

Ranking system for tasks:
- Rank 1  -> Beginner: basic enums and attributes.
- Rank 2  -> Easy: using enums in functions and simple logic.
- Rank 3  -> Intermediate: mapping enums to data and small utilities.
- Rank 4  -> Advanced: using auto() and more structured enums.
- Rank 5  -> Professional: IntFlag / permissions style patterns.

Author: Peyman Miyandashti
Date of Birth: 11/11/1983
ID Number: 250161
Year: 2025
"""

from enum import Enum, IntEnum, auto, IntFlag


# ===========================================================
# Rank 1 — Beginner
# Basic Enum with Peyman's favorite season and color
# ===========================================================

class Season(Enum):
    """
    Simple enum for seasons of the year.

    TODO:
    - Add four members: SPRING, SUMMER, FALL, WINTER
      (values can be strings like "spring", "summer", etc. or integers)
    """
    # Example:
    # SPRING = "spring"
    # ...
    pass


class FavoriteColor(Enum):
    """
    Simple enum for colors.

    Peyman likes red, and his Kia Sportage is dark gray.

    TODO:
    - Add RED
    - Add DARK_GRAY
    - Add at least one more color you like
    """
    pass


def describe_favorite_color(color: FavoriteColor) -> str:
    """
    Return a short human-readable description of the given FavoriteColor.

    TODO:
    - If color is FavoriteColor.RED -> return "Peyman's favorite color is red."
    - If color is FavoriteColor.DARK_GRAY -> return "Dark gray like Peyman's Kia Sportage."
    - Otherwise, return a generic message using color.name.
    """
    # TODO: implement this function
    raise NotImplementedError("Implement describe_favorite_color")


# ===========================================================
# Rank 2 — Easy
# IntEnum for education years at university
# ===========================================================

class StudyYear(IntEnum):
    """
    Integer enum representing the year of study at university.

    TODO:
    - FIRST_YEAR = 1
    - SECOND_YEAR = 2
    - THIRD_YEAR = 3
    - FOURTH_YEAR = 4

    (You can add more if you want.)
    """
    pass


def years_until_graduation(current_year: StudyYear, total_years: int = 4) -> int:
    """
    Calculate how many years are left until graduation.

    Example:
    - If total_years = 4 and current_year = StudyYear.SECOND_YEAR (2)
      then result = 2.

    TODO:
    - Use integer math with current_year (an IntEnum, so it's an int).
    - Make sure result is never negative (use max(remaining, 0)).
    """
    # TODO: implement this function
    raise NotImplementedError("Implement years_until_graduation")


# ===========================================================
# Rank 3 — Intermediate
# Enums for countries and gaming preferences
# ===========================================================

class Country(Enum):
    """
    Peyman is from Iran (Tabriz) and now lives in Mexico (Mexicali).

    TODO:
    - IRAN
    - MEXICO
    (You can assign simple string codes like "IR" and "MX".)
    """
    pass


class GameGenre(Enum):
    """
    Basic game genres. Peyman's favorite game is World of Warcraft (RPG/MMO).

    TODO:
    - RPG
    - MMO
    - FPS
    - STRATEGY
    - OTHER
    """
    pass


def get_country_description(country: Country) -> str:
    """
    Return a short description of the country enum.

    TODO:
    - If Country.IRAN -> mention Tabriz and origin.
    - If Country.MEXICO -> mention Mexicali and current residence.
    - Use country.name for a generic fallback.
    """
    # TODO: implement this function
    raise NotImplementedError("Implement get_country_description")


def is_wow_favorite(genre: GameGenre) -> bool:
    """
    Check if the given game genre matches Peyman's favorite style
    (World of Warcraft style).

    TODO:
    - Return True if genre is RPG or MMO.
    - Otherwise return False.
    """
    # TODO: implement this function
    raise NotImplementedError("Implement is_wow_favorite")


# ===========================================================
# Rank 4 — Advanced
# auto() usage and combining enums with small "profiles"
# ===========================================================

class CarBrand(Enum):
    """
    Car brands for Peyman and Arlette.

    TODO:
    - KIA
    - HYUNDAI
    - OTHER

    You can choose whatever values you like, for example strings:
    KIA = "Kia"
    HYUNDAI = "Hyundai"
    """
    pass


class CarOwner(Enum):
    """
    Use auto() to assign values automatically.

    TODO:
    - PEYMAN
    - ARLETTE
    """
    # Example:
    # PEYMAN = auto()
    # ARLETTE = auto()
    pass


def build_car_profile(owner: CarOwner, brand: CarBrand, year: int) -> dict:
    """
    Build a small dictionary describing a car.

    TODO:
    - Create a dict with keys:
        "owner"  -> owner.name
        "brand"  -> brand.name
        "year"   -> year
    - Return that dictionary.
    """
    # TODO: implement this function
    raise NotImplementedError("Implement build_car_profile")


# ===========================================================
# Rank 5 — Professional
# IntFlag for permissions (like small role system)
# ===========================================================

class Permission(IntFlag):
    """
    Example of IntFlag (bitwise permissions).

    TODO:
    - READ = 1
    - WRITE = 2
    - EXECUTE = 4

    Combined permissions should be possible, e.g. READ | WRITE.
    """
    pass


def has_write_permission(perms: Permission) -> bool:
    """
    Check if the given Permission set includes WRITE.

    TODO:
    - Use bitwise check with Permission.WRITE.
    - Return True if WRITE is present, otherwise False.
    """
    # TODO: implement this function
    raise NotImplementedError("Implement has_write_permission")


def has_full_permissions(perms: Permission) -> bool:
    """
    Check if the given Permission set includes READ, WRITE, and EXECUTE.

    TODO:
    - You can compare perms with Permission.READ | Permission.WRITE | Permission.EXECUTE
      or use bitwise logic.
    """
    # TODO: implement this function
    raise NotImplementedError("Implement has_full_permissions")


# ===========================================================
# Optional: quick manual test area
# You can comment/uncomment this block while you work.
# ===========================================================

if __name__ == "__main__":
    print("Module 26 — Enumerations (Tasks)")
    print("Run your own tests here after you implement the TODOs.")
