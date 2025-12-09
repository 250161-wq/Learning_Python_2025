"""
Module 22 — Working With Files: Practice Exercises
Comprehensive practice with reading and writing files in Python,
from beginner to more professional, production-style usage.

In this module I:
- Practice how to create, read, and update text files.
- Start from very simple examples (Rank 1) and move toward
  more realistic, professional patterns (Rank 5).
- Use my real personal data (Peyman + Arlette, cars, study info, etc.)
  inside the files.

Ranking system:
- Rank 1  -> Beginner: very basic file writing and reading.
- Rank 2  -> Easy: append data and read line by line.
- Rank 3  -> Intermediate: use context managers and simple reports.
- Rank 4  -> Advanced: organize files in folders, use Path objects.
- Rank 5  -> Professional: reusable functions for file operations.

Author: Peyman Miyandashti
Date of Birth: 11/11/1983
ID Number: 250161
Year: 2025
"""

import os
from pathlib import Path

# Base directory where this module will create files
BASE_DIR = Path("module_22_files_output")
BASE_DIR.mkdir(exist_ok=True)

# Core personal data (integers/strings combined)
pey_name = "Peyman Miyandashti"
pey_age = 43
pey_country_from = "Iran"
pey_city_from = "Tabriz"
current_country = "Mexico"
current_city = "Mexicali"
university = "Polytechnic Baja California University (UPBC)"
degree_program = "Information Technology Engineering and Digital Innovation"

wife_name = "Arlette Chong"
wife_age = 47
pey_favorite_number = 11
pey_favorite_game = "World of Warcraft"
pey_favorite_color = "Red"

kia_model = "Kia Sportage"
kia_year = 2024
kia_color = "Dark Gray"

creta_model = "Hyundai Creta"
creta_year = 2018

# ===========================================================
# Rank 1 — Beginner
# Write and read a very simple text file
# ===========================================================

rank1_file = BASE_DIR / "rank1_basic_info.txt"

print("Rank 1 — Beginner")

# Write a simple line to a file (overwrite if it exists)
with open(rank1_file, "w", encoding="utf-8") as f:
    f.write("Hello from Module 22 (files)!\n")
    f.write(f"My name is {pey_name} and I am {pey_age} years old.\n")

# Read the whole file back and print it
with open(rank1_file, "r", encoding="utf-8") as f:
    content = f.read()

print(f"Created file: {rank1_file}")
print("File content:")
print(content)
print("-" * 50)


# ===========================================================
# Rank 2 — Easy
# Append to an existing file and read line by line
# ===========================================================

rank2_file = BASE_DIR / "rank2_location.txt"

print("Rank 2 — Easy")

# First, create the file with initial content
with open(rank2_file, "w", encoding="utf-8") as f:
    f.write("Original home:\n")
    f.write(f"- Country: {pey_country_from}\n")
    f.write(f"- City: {pey_city_from}\n")

# Now append new lines about current location
with open(rank2_file, "a", encoding="utf-8") as f:
    f.write("\nCurrent home:\n")
    f.write(f"- Country: {current_country}\n")
    f.write(f"- City: {current_city}\n")

# Read line by line
print(f"Created/updated file: {rank2_file}")
print("Reading line by line:")
with open(rank2_file, "r", encoding="utf-8") as f:
    for line in f:
        # strip() just removes the newline for cleaner printing
        print("LINE ->", line.strip())

print("-" * 50)


# ===========================================================
# Rank 3 — Intermediate
# Create a small text "report" using context managers
# ===========================================================

rank3_file = BASE_DIR / "rank3_study_report.txt"

print("Rank 3 — Intermediate")

study_year_start = 2023
current_year = 2025
years_studying = current_year - study_year_start

with open(rank3_file, "w", encoding="utf-8") as f:
    f.write("Student Study Report\n")
    f.write("====================\n")
    f.write(f"Name: {pey_name}\n")
    f.write(f"Age: {pey_age}\n")
    f.write(f"University: {university}\n")
    f.write(f"Degree: {degree_program}\n")
    f.write(f"Started in: {study_year_start}\n")
    f.write(f"Current year: {current_year}\n")
    f.write(f"Years studying so far: {years_studying}\n")
    f.write("\nPersonal preferences:\n")
    f.write(f"- Favorite color: {pey_favorite_color}\n")
    f.write(f"- Favorite game: {pey_favorite_game}\n")
    f.write(f"- Favorite number: {pey_favorite_number}\n")

print(f"Created report file: {rank3_file}")
print("Report preview (first 5 lines):")
with open(rank3_file, "r", encoding="utf-8") as f:
    for i, line in enumerate(f):
        if i >= 5:
            break
        print(line.strip())
print("-" * 50)


# ===========================================================
# Rank 4 — Advanced
# Use folders and Path objects to organize multiple files
# ===========================================================

print("Rank 4 — Advanced")

cars_dir = BASE_DIR / "cars"
cars_dir.mkdir(exist_ok=True)

kia_file = cars_dir / "kia_sportage.txt"
creta_file = cars_dir / "hyundai_creta.txt"

with open(kia_file, "w", encoding="utf-8") as f:
    f.write("Car Profile\n")
    f.write("===========\n")
    f.write(f"Owner: {pey_name}\n")
    f.write(f"Model: {kia_model}\n")
    f.write(f"Year: {kia_year}\n")
    f.write(f"Color: {kia_color}\n")

with open(creta_file, "w", encoding="utf-8") as f:
    f.write("Car Profile\n")
    f.write("===========\n")
    f.write(f"Owner: {wife_name}\n")
    f.write(f"Model: {creta_model}\n")
    f.write(f"Year: {creta_year}\n")

# Loop over all .txt files inside cars_dir and show a summary
print(f"Car files created in folder: {cars_dir}")
for path in cars_dir.glob("*.txt"):
    print(f"- Found file: {path.name}")
    # Just read the first 2 lines as a quick summary
    with open(path, "r", encoding="utf-8") as f:
        first_line = f.readline().strip()
        second_line = f.readline().strip()
    print("  Summary:", first_line, "|", second_line)

print("-" * 50)


# ===========================================================
# Rank 5 — Professional
# Reusable helper functions for file operations
# ===========================================================

print("Rank 5 — Professional")


def save_profile_to_file(profile: dict, filepath: Path) -> None:
    """
    Save a simple key/value profile to a text file.

    Each line looks like:
    key=value
    """
    with open(filepath, "w", encoding="utf-8") as f:
        for key, value in profile.items():
            f.write(f"{key}={value}\n")


def load_profile_from_file(filepath: Path) -> dict:
    """
    Load a simple key/value profile from a text file
    where each line is key=value.

    Lines without '=' are ignored.
    """
    profile = {}
    if not filepath.exists():
        return profile

    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if "=" not in line or not line:
                continue
            key, value = line.split("=", 1)
            profile[key] = value
    return profile


# Build a profile dict using Peyman + Arlette information
profile_data = {
    "pey_name": pey_name,
    "pey_age": str(pey_age),   # store as string in the text file
    "wife_name": wife_name,
    "wife_age": str(wife_age),
    "from_country": pey_country_from,
    "from_city": pey_city_from,
    "current_country": current_country,
    "current_city": current_city,
    "university": university,
    "degree_program": degree_program,
    "favorite_game": pey_favorite_game,
    "favorite_color": pey_favorite_color,
    "favorite_number": str(pey_favorite_number),
    "kia_model": kia_model,
    "kia_year": str(kia_year),
    "creta_model": creta_model,
    "creta_year": str(creta_year),
}

profile_file = BASE_DIR / "rank5_profile.txt"

# Save the profile to a file
save_profile_to_file(profile_data, profile_file)
print(f"Saved profile to: {profile_file}")

# Load it back and print the loaded dict
loaded_profile = load_profile_from_file(profile_file)
print("Loaded profile dictionary:")

for key, value in loaded_profile.items():
    print(f"- {key:16} -> {value}")

print("-" * 50)
