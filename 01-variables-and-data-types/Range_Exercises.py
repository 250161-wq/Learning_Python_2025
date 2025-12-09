"""
Module 18 — Range Type: Practice Exercises
Comprehensive practice with Python range objects, from beginner to
more professional, production-style usage.

In this module I:
- Practice how to create and use range() to generate sequences of integers.
- Start from very simple examples (Rank 1) and move toward
  more realistic, professional patterns (Rank 5).
- Focus only on the range type here. Integers were covered in Module 2,
  and other types have their own modules.

Ranking system:
- Rank 1  -> Beginner: very basic syntax and concepts.
- Rank 2  -> Easy: still simple, but combining two or more concepts.
- Rank 3  -> Intermediate: ranges with steps, lengths, and conversions.
- Rank 4  -> Advanced: using ranges to model real data and loops.
- Rank 5  -> Professional: clean, reusable functions that use ranges.

Author: Peyman Miyandashti
Date of Birth: 11/11/1983
ID Number: 250161
Year: 2025
"""

# Some base integer data (from your real life)
pey_man_age = 43
wife_age = 47
current_year = 2025
pey_man_birth_year = 1983
kia_sportage_year = 2024
hyundai_creta_year = 2018
favorite_number = 11


# ===========================================================
# Rank 1 — Beginner
# Creating simple ranges and converting to lists
# ===========================================================

print("Rank 1 — Beginner")

# A simple range from 0 to 4 (stop is exclusive)
basic_range = range(5)
print("basic_range:", basic_range)
print("basic_range as list:", list(basic_range))

# Range of Peyman's age from 0 up to (not including) his age
age_range = range(pey_man_age)
print("Age range from 0 to 42:", list(age_range))

# Range of years from birth year to current year (not including current_year)
years_lived_range = range(pey_man_birth_year, current_year)
print("Years lived (birth_year -> current_year-1):", list(years_lived_range))

print("-" * 50)


# ===========================================================
# Rank 2 — Easy
# Using ranges in for-loops with your personal data
# ===========================================================

print("Rank 2 — Easy")

print("Counting from 1 to your favorite number:")
for number in range(1, favorite_number + 1):
    print(number, end=" ")
print()  # new line

print("Listing every year of your 40s:")

start_age_40s = 40
end_age_40s = 50
for age in range(start_age_40s, end_age_40s):
    print(f"Age {age}")
    
# Difference between your age and your wife's age using range
print("Step-by-step difference from Peyman's age to wife's age:")
for age in range(pey_man_age, wife_age + 1):
    print("Age:", age)

print("-" * 50)


# ===========================================================
# Rank 3 — Intermediate
# Ranges with steps, len(), and conversions
# ===========================================================

print("Rank 3 — Intermediate")

# Every 2 years between Kia and Creta model years
print("Every 2nd year between Creta (2018) and Sportage (2024):")
for year in range(hyundai_creta_year, kia_sportage_year + 1, 2):
    print(year, end=" ")
print()

# Using len() with range
study_years_range = range(2023, current_year + 1)  # from 2023 to 2025
print("Study years range (2023 to 2025):", list(study_years_range))
print("Number of study years so far:", len(study_years_range))

# reverse range: count down from wife's age to Peyman's age
print("Counting down from wife's age to Peyman's age:")
for age in range(wife_age, pey_man_age - 1, -1):
    print(age, end=" ")
print()

# Use range to generate the first 10 multiples of Peyman's favorite number
multiples_of_fav = [favorite_number * n for n in range(1, 11)]
print("First 10 multiples of your favorite number 11:", multiples_of_fav)

print("-" * 50)


# ===========================================================
# Rank 4 — Advanced
# Using ranges to model time and indexing
# ===========================================================

print("Rank 4 — Advanced")

# Model Peyman's ages from birth until now in steps of 5 years
print("Peyman's age every 5 years from birth to now:")
for age in range(0, pey_man_age + 1, 5):
    year = pey_man_birth_year + age
    print(f"At age {age}, year was {year}")

print("-" * 20)

# Indexing with range and a list of games (example list)
games = ["World of Warcraft", "Diablo", "Overwatch", "StarCraft"]
print("Games list with positions (using range for indexes):")
for index in range(len(games)):
    print(f"Position {index}: {games[index]}")

print("-" * 20)

# Years Peyman and Arlette have been married (example: assume married at age 30)
married_start_age = 30
married_years_range = range(married_start_age, pey_man_age + 1)
print("Years of marriage (by Peyman's age, from 30 to now):")
for age in married_years_range:
    year = pey_man_birth_year + age
    print(f"Peyman's age {age} in year {year}")

print("-" * 50)


# ===========================================================
# Rank 5 — Professional
# Reusable functions that use range() for planning and analysis
# ===========================================================

def build_study_timeline(
    start_year: int,
    end_year: int,
    semesters_per_year: int
) -> list[dict]:
    """
    Build a study timeline using range().

    Each entry in the timeline is a dictionary with:
    - year: the calendar year
    - semester: 1..semesters_per_year
    - label: formatted string "Year-Semester"
    """
    timeline = []
    # range over each academic year
    for year in range(start_year, end_year + 1):
        # range over semesters inside each year
        for semester in range(1, semesters_per_year + 1):
            label = f"{year}-S{semester}"
            timeline.append(
                {
                    "year": year,
                    "semester": semester,
                    "label": label,
                }
            )
    return timeline


def build_age_projection(
    current_age: int,
    target_age: int,
    current_year: int
) -> list[tuple[int, int]]:
    """
    Use range() to project future ages and calendar years.

    Returns a list of (age, year) tuples from current_age up to target_age.
    """
    projection = []
    # The difference between age and year is constant:
    # year = current_year + (age - current_age)
    for age in range(current_age, target_age + 1):
        year = current_year + (age - current_age)
        projection.append((age, year))
    return projection


print("Rank 5 — Professional")

# Example: Peyman's study timeline at UPBC from 2023 to 2027, 2 semesters per year
pey_man_timeline = build_study_timeline(
    start_year=2023,
    end_year=2027,
    semesters_per_year=2,
)

print("Peyman's study timeline (first 8 entries):")
for entry in pey_man_timeline[:8]:
    print(entry)

print("-" * 20)

# Example: Age projection for Peyman from now (43) to 50
age_projection = build_age_projection(
    current_age=pey_man_age,
    target_age=50,
    current_year=current_year,
)

print("Peyman's age projection from 43 to 50:")
for age, year in age_projection:
    print(f"Age {age} in year {year}")

print("-" * 50)
