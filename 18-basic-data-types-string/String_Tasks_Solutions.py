"""
Module 18 — Strings: Practice Task Solutions
--------------------------------------------

This file contains clean, readable solutions to all tasks in
String_Tasks.py. Multiple answers are always possible; these show
simple and professional approaches.

IMPORTANT:
Only read these solutions AFTER attempting the tasks yourself!
"""


# ---------------------------------------------------------------------------
# Rank 1 — Beginner
# ---------------------------------------------------------------------------

# Task 1.1
greeting = "Hello, World!"
print(greeting)

# Task 1.2
first_name = "Peyman"
last_name = "Miyandashti"
full_name = first_name + " " + last_name
print("Full name:", full_name)

# Task 1.3
city = "Mexicali"
print("Length of city name:", len(city))

# Task 1.4
name = "Arlette"
age = 47
print(f"{name} is {age} years old.")


# ---------------------------------------------------------------------------
# Rank 2 — Easy
# ---------------------------------------------------------------------------

# Task 2.1
language = "Python"
print("First character:", language[0])
print("Last character:", language[-1])

# Task 2.2
word = "Programming"
print("First 4:", word[:4])
print("Last 3:", word[-3:])

# Task 2.3
raw_name = "   peyman   "
clean_name = raw_name.strip().capitalize()
print("Clean name:", clean_name)

# Task 2.4  (interactive normally)
# user_word = input("Type a word: ")
# print("Lowercase:", user_word.lower())
# print("Uppercase:", user_word.upper())
print("Skipped interactive example for Task 2.4.")


# ---------------------------------------------------------------------------
# Rank 3 — Intermediate
# ---------------------------------------------------------------------------

# Task 3.1 (interactive normally)
# word = input("Enter a word: ")
# vowels = "aeiou"
# count = 0
# for ch in word.lower():
#     if ch in vowels:
#         count += 1
# print("Vowel count:", count)
print("Skipped interactive example for Task 3.1.")

# Task 3.2
sentence = "I like Java, but Java is not my favorite."
new_sentence = sentence.replace("Java", "Python")
print(new_sentence)

# Task 3.3 (interactive normally)
# full_name_input = input("Enter your full name: ")
# parts = full_name_input.split()
# print("Parts:", len(parts))
# print(parts)
print("Skipped interactive example for Task 3.3.")

# Task 3.4
message = """Hello!
Welcome to my Python practice.
Have a great day."""
print(message)


# ---------------------------------------------------------------------------
# Rank 4 — Advanced
# ---------------------------------------------------------------------------

# Task 4.1 (interactive normally)
# pwd = input("Create a password: ")
# length_ok = len(pwd) >= 8
# digit_ok = any(ch.isdigit() for ch in pwd)
# lower_ok = any(ch.islower() for ch in pwd)

# print("OK: at least 8 characters" if length_ok else "ERROR: too short")
# print("OK: contains a digit" if digit_ok else "ERROR: no digit found")
# print("OK: contains lowercase" if lower_ok else "ERROR: no lowercase letter")
print("Skipped interactive example for Task 4.1.")

# Task 4.2 (interactive normally)
# text = input("Enter a long text: ")
# if len(text) > 30:
#     preview = text[:30] + "..."
# else:
#     preview = text
# print("Preview:", preview)
print("Skipped interactive example for Task 4.2.")

# Task 4.3 (interactive normally)
# sentence = input("Enter a sentence: ").lower()
# word = input("Enter a word to search: ").lower()
# if word in sentence:
#     print("Found!")
# else:
#     print("Not found.")
print("Skipped interactive example for Task 4.3.")

# Task 4.4
data = "10,20,30,40,50"
parts = data.split(",")
numbers = [int(x) for x in parts]
print(numbers)


# ---------------------------------------------------------------------------
# Rank 5 — Professional
# ---------------------------------------------------------------------------

# Task 5.1
def format_product(name: str, price: float) -> str:
    return f"Product: {name} | Price: ${price:.2f}"

print(format_product("Keyboard", 599.9))


# Task 5.2
def sanitize_username(raw_username: str) -> str:
    cleaned = raw_username.strip().lower().replace(" ", "_")
    return cleaned

print(sanitize_username("  Peyman Nova  "))


# Task 5.3
def normalize_spaces(text: str) -> str:
    words = text.split()
    return " ".join(words)

print(normalize_spaces("Hello   world   from   Python"))


# Task 5.4
def to_sentence(words: list[str]) -> str:
    if not words:
        return ""

    sentence = " ".join(words)
    sentence = sentence.capitalize()

    if not sentence.endswith("."):
        sentence += "."

    return sentence

print(to_sentence(["python", "is", "fun"]))


# End of Solutions
