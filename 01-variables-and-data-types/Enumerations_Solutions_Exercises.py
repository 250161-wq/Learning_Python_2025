"""
Module 26 — Enumerations (Enums) — Solutions
Complete reference implementation for enumeration practice.

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
    SPRING = "spring"
    SUMMER = "summer"
    FALL = "fall"
    WINTER = "winter"


class FavoriteColor(Enum):
    RED = "red"
    DARK_GRAY = "dark_gray"
    BLUE = "blue"       # extra example
    WHITE = "white"     # extra example (Peyman is white-skinned)


def describe_favorite_color(color: FavoriteColor) -> str:
    if color is FavoriteColor.RED:
        return "Peyman's favorite color is red."
    elif color is FavoriteColor.DARK_GRAY:
        return "Dark gray like Peyman's 2024 Kia Sportage."
    else:
        return f"Selected color is {color.name.lower()}."


# ===========================================================
# Rank 2 — Easy
# IntEnum for education years at university
# ===========================================================

class StudyYear(IntEnum):
    FIRST_YEAR = 1
    SECOND_YEAR = 2
    THIRD_YEAR = 3
    FOURTH_YEAR = 4


def years_until_graduation(current_year: StudyYear, total_years: int = 4) -> int:
    remaining = total_years - int(current_year)
    return max(remaining, 0)


# ===========================================================
# Rank 3 — Intermediate
# Enums for countries and gaming preferences
# ===========================================================

class Country(Enum):
    IRAN = "IR"
    MEXICO = "MX"


class GameGenre(Enum):
    RPG = "rpg"
    MMO = "mmo"
    FPS = "fps"
    STRATEGY = "strategy"
    OTHER = "other"


def get_country_description(country: Country) -> str:
    if country is Country.IRAN:
        return "Peyman is originally from Tabriz, Iran."
    elif country is Country.MEXICO:
        return "Peyman currently lives in Mexicali, Baja California, Mexico."
    else:
        return f"Country: {country.name}"


def is_wow_favorite(genre: GameGenre) -> bool:
    # World of Warcraft is a MMORPG: RPG + MMO
    return genre in (GameGenre.RPG, GameGenre.MMO)


# ===========================================================
# Rank 4 — Advanced
# auto() usage and combining enums with small "profiles"
# ===========================================================

class CarBrand(Enum):
    KIA = "Kia"
    HYUNDAI = "Hyundai"
    OTHER = "Other"


class CarOwner(Enum):
    PEYMAN = auto()
    ARLETTE = auto()


def build_car_profile(owner: CarOwner, brand: CarBrand, year: int) -> dict:
    profile = {
        "owner": owner.name,  # "PEYMAN" or "ARLETTE"
        "brand": brand.name,  # enum name, not value -> "KIA", "HYUNDAI"
        "year": year,
    }
    return profile


# ===========================================================
# Rank 5 — Professional
# IntFlag for permissions (like small role system)
# ===========================================================

class Permission(IntFlag):
    READ = 1
    WRITE = 2
    EXECUTE = 4


def has_write_permission(perms: Permission) -> bool:
    return bool(perms & Permission.WRITE)


def has_full_permissions(perms: Permission) -> bool:
    full = Permission.READ | Permission.WRITE | Permission.EXECUTE
    return (perms & full) == full


# ===========================================================
# Demo usage (optional)
# ===========================================================

if __name__ == "__main__":
    print("Module 26 — Enumerations (Solutions Demo)")
    print("-" * 50)

    # Rank 1 demo
    print("Season example:", Season.FALL, Season.FALL.value)
    color_msg = describe_favorite_color(FavoriteColor.RED)
    print("Color message:", color_msg)
    print("-" * 50)

    # Rank 2 demo
    print("Current year of study:", StudyYear.SECOND_YEAR)
    print("Years until graduation:", years_until_graduation(StudyYear.SECOND_YEAR))
    print("-" * 50)

    # Rank 3 demo
    print(get_country_description(Country.IRAN))
    print(get_country_description(Country.MEXICO))
    print("Is RPG WoW style?:", is_wow_favorite(GameGenre.RPG))
    print("Is FPS WoW style?:", is_wow_favorite(GameGenre.FPS))
    print("-" * 50)

    # Rank 4 demo
    peyman_car = build_car_profile(CarOwner.PEYMAN, CarBrand.KIA, 2024)
    arlette_car = build_car_profile(CarOwner.ARLETTE, CarBrand.HYUNDAI, 2018)
    print("Peyman's car profile:", peyman_car)
    print("Arlette's car profile:", arlette_car)
    print("-" * 50)

    # Rank 5 demo
    perms = Permission.READ | Permission.WRITE
    print("Permissions:", perms)
    print("Has write?:", has_write_permission(perms))
    print("Has full?:", has_full_permissions(perms))
    full_perms = Permission.READ | Permission.WRITE | Permission.EXECUTE
    print("Full permissions:", full_perms, "Has full?:", has_full_permissions(full_perms))
