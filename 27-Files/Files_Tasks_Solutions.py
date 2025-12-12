"""
Files_Tasks_Solutions.py
Module 27 — Working with Files
Author: Peyman Miyandashti
Year: 2025

Solutions to all file-handling exercises.
Use this file ONLY after completing the tasks yourself.
"""


# ---------------------------------------------------------------------------
# ⭐ RANK 1 — BEGINNER
# ---------------------------------------------------------------------------

# 1.
with open("task1.txt", "w") as f:
    f.write("Peyman Miyandashti")

# 2.
with open("task1.txt", "r") as f:
    print(f.read())

# 3.
with open("hello.txt", "w") as f:
    f.write("Hello World!\n")
    f.write("Welcome to Python.\n")

with open("hello.txt", "r") as f:
    print(f.read())

# 4.
with open("hello.txt", "a") as f:
    f.write("New line added.\n")

# 5.
with open("hello.txt", "r") as f:
    for line in f:
        print(line.strip())


# ---------------------------------------------------------------------------
# ⭐ RANK 2 — EASY
# ---------------------------------------------------------------------------

# 6.
with open("numbers.txt", "w") as f:
    for i in range(1, 6):
        f.write(str(i) + "\n")

# 7.
with open("numbers.txt", "r") as f:
    nums = [int(line) for line in f]

# 8.
with open("numbers.txt", "a") as f:
    f.write("99\n")

# 9.
names = ["Luis", "Ana", "Jorge"]
with open("names.txt", "w") as f:
    for name in names:
        f.write(name + "\n")

# 10.
with open("names.txt", "r") as f:
    for i, name in enumerate(f, start=1):
        print(f"Line {i}: {name.strip()}")


# ---------------------------------------------------------------------------
# ⭐ RANK 3 — INTERMEDIATE
# ---------------------------------------------------------------------------

# 11.
try:
    with open("missing.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found!")

# 12.
def write_lines(filename, lines):
    with open(filename, "w") as f:
        for line in lines:
            f.write(line + "\n")

# 13.
def read_lines(filename):
    with open(filename, "r") as f:
        return [line.strip() for line in f]

# 14.
with open("fruits.txt", "w") as f:
    f.write("apple\nbanana\nmango\n")

with open("fruits.txt", "r") as f:
    for fruit in f:
        if "a" in fruit.lower():
            print(fruit.strip())

# 15.
def copy_file(src, dst):
    with open(src, "r") as f_src:
        data = f_src.read()
    with open(dst, "w") as f_dst:
        f_dst.write(data)


# ---------------------------------------------------------------------------
# ⭐ RANK 4 — ADVANCED
# ---------------------------------------------------------------------------

# 16.
with open("grades.txt", "w") as f:
    f.write("Luis:90\nAna:85\nJorge:100\n")

with open("grades.txt", "r") as f:
    for line in f:
        name, grade = line.strip().split(":")
        print(f"{name} has {grade}")

# 17.
new_lines = []
with open("grades.txt", "r") as f:
    for line in f:
        name, grade = line.strip().split(":")
        grade = max(int(grade), 90)
        new_lines.append(f"{name}:{grade}")

with open("grades.txt", "w") as f:
    for l in new_lines:
        f.write(l + "\n")

# 18.
with open("paragraph.txt", "r") as f:
    text = f.read()
word_count = len(text.split())
print("Word count:", word_count)

# 19.
def filter_lines(filename, keyword, output):
    with open(filename, "r") as f_src, open(output, "w") as f_out:
        for line in f_src:
            if keyword.lower() in line.lower():
                f_out.write(line)

# 20.
with open("names.txt", "r") as f_src, open("names_upper.txt", "w") as f_out:
    for line in f_src:
        f_out.write(line.strip().upper() + "\n")


# ---------------------------------------------------------------------------
# ⭐ RANK 5 — PROFESSIONAL
# ---------------------------------------------------------------------------

# 21.
from datetime import datetime

def log(msg):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("app.log", "a") as f:
        f.write(f"[{timestamp}] {msg}\n")

# 22.
def save_user(username, age):
    with open("users.csv", "a") as f:
        f.write(f"{username},{age}\n")

# 23.
def load_users():
    users = []
    try:
        with open("users.csv", "r") as f:
            for line in f:
                name, age = line.strip().split(",")
                users.append((name, int(age)))
    except FileNotFoundError:
        return []
    return users

# 24.
def add_item(item):
    with open("database.txt", "a") as f:
        f.write(item + "\n")

def get_all_items():
    try:
        with open("database.txt", "r") as f:
            return [line.strip() for line in f]
    except FileNotFoundError:
        return []

# 25.
def update_price_file(filename, percent):
    updated = []
    with open(filename, "r") as f:
        for line in f:
            product, price = line.strip().split(":")
            new_price = int(price) + int(price) * (percent / 100)
            updated.append(f"{product}:{int(new_price)}")

    with open(filename, "w") as f:
        for line in updated:
            f.write(line + "\n")
