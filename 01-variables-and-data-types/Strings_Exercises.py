"""
Module 1 — String Variables: Practice Exercises
Comprehensive practice with Python string variables, from beginner to
more professional, production-style usage.

In this module I:
- Practice how to create, modify, and use string variables.
- Start from very simple examples (Rank 1) and move toward
  more realistic, professional patterns (Rank 5).
- Focus only on the string type here. Other variable types will get
  their own practice files later.

Ranking system:
- Rank 1  -> Beginner: very basic syntax and concepts.
- Rank 2  -> Easy: still simple, but combining two or more concepts.
- Rank 3  -> Intermediate: more operations in a single example.
- Rank 4  -> Advanced: closer to how strings are used in real projects.
- Rank 5  -> Professional: clean, reusable, and readable patterns.

Author: Peyman Miyandashti
Date of Birth: 11/11/1983
ID Number: 250161
Year: 2025
"""

# ===========================================================
# Rank 1 — Beginner
# Simple string creation and printing
# ===========================================================

first_name = "Peyman"
last_name = "Miyandashti"

print("Rank 1 — Beginner")
print("First name:", first_name)
print("Last name:", last_name)
print("Full name:", first_name + " " + last_name)
print("-" * 50)


# ===========================================================
# Rank 2 — Easy
# Concatenation, f-strings, and basic string info
# ===========================================================

city = "Vancouver"
country = "Canada"

full_location = city + ", " + country           # concatenation
location_message = f"I live in {city}, {country}."  # f-string

print("Rank 2 — Easy")
print("Location message:", location_message)
print("Number of characters in city:", len(city))
print("First letter of city:", city[0])
print("Last letter of country:", country[-1])
print("-" * 50)


# ===========================================================
# Rank 3 — Intermediate
# Slicing, methods (upper/lower/replace), and cleaning input
# ===========================================================

raw_username = "   peyMan_250161   "   # string with spaces and odd casing
clean_username = raw_username.strip()  # remove spaces at both ends
normalized_username = clean_username.lower()  # make it lowercase

welcome_message = f"Welcome, {normalized_username}!"
shouting_message = welcome_message.upper()
fixed_message = shouting_message.replace("WELCOME", "HELLO")

print("Rank 3 — Intermediate")
print("Raw username:", repr(raw_username))
print("Clean username:", repr(clean_username))
print("Normalized username:", normalized_username)
print("Welcome message:", welcome_message)
print("Shouting message:", shouting_message)
print("Fixed message:", fixed_message)

# Slicing example (take only first part before underscore)
user_prefix = normalized_username.split("_")[0]
print("User prefix (before underscore):", user_prefix)
print("-" * 50)


# ===========================================================
# Rank 4 — Advanced
# Splitting, joining, and building formatted text blocks
# ===========================================================

skills_text = "python, networking, automation, linux"
skills_list = [skill.strip().title() for skill in skills_text.split(",")]

skills_bullet_list = "\n".join(f"- {skill}" for skill in skills_list)

profile_template = (
    f"Developer Profile\n"
    f"-----------------\n"
    f"Name: {first_name} {last_name}\n"
    f"ID: {250161}\n"
    f"Main Skills:\n{skills_bullet_list}\n"
)

print("Rank 4 — Advanced")
print(profile_template)
print("-" * 50)


# ===========================================================
# Rank 5 — Professional
# Reusable function that builds nicely formatted messages
# (uses f-strings, alignment, and multi-line strings)
# ===========================================================

def build_student_report(
    student_name: str,
    module_name: str,
    score: float,
    passed: bool
) -> str:
    """
    Build a formatted report string for a student.

    This function is an example of how strings are used in
    real-world projects: reusable, readable, and easy to test.
    """
    status = "PASSED ✅" if passed else "FAILED ❌"

    # Format score to 2 decimal places and align labels
    report = (
        "Student Report\n"
        "==============\n"
        f"{'Name:':15} {student_name}\n"
        f"{'Module:':15} {module_name}\n"
        f"{'Score:':15} {score:.2f}\n"
        f"{'Status:':15} {status}\n"
    )
    return report


print("Rank 5 — Professional")
report_string = build_student_report(
    student_name="Peyman Miyandashti",
    module_name="Module 1 — Variables and Data Types",
    score=96.75,
    passed=True,
)
print(report_string)
print("-" * 50)

