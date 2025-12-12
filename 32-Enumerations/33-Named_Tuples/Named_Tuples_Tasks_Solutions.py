"""
Named_Tuples_Tasks_Solutions.py
Module 33 — Named Tuples
Author: Peyman Miyandashti
Year: 2025

This file contains clean and professional solutions
for the named tuple exercises in this module.
"""

from collections import namedtuple

# ---------------------------------------------------------------------------
# Rank 1 — Beginner
# ---------------------------------------------------------------------------

# Task 1 Solution
Book = namedtuple("Book", ["title", "author", "year"])


# Task 2 Solution
book1 = Book("Clean Code", "Robert C. Martin", 2008)

print(book1.title)
print(book1.author)
print(book1.year)


# ---------------------------------------------------------------------------
# Rank 2 — Easy
# ---------------------------------------------------------------------------

# Task 3 Solution
def describe_book(book: Book):
    return f"'{book.title}' by {book.author} ({book.year})"


print(describe_book(book1))


# Task 4 Solution
print(book1[0])      # title
print(book1[1])      # author
print(book1.year)    # year (by name)


# ---------------------------------------------------------------------------
# Rank 3 — Intermediate
# ---------------------------------------------------------------------------

# Task 5 Solution
Employee = namedtuple("Employee", ["name", "role", "salary"])

emp1 = Employee("Peyman", "Engineer", 50000)

def give_raise(employee: Employee):
    new_salary = int(employee.salary * 1.10)
    return employee._replace(salary=new_salary)


emp2 = give_raise(emp1)
print(emp2)


# Task 6 Solution
employee_dict = emp2._asdict()
print(employee_dict)


# ---------------------------------------------------------------------------
# Rank 4 — Advanced
# ---------------------------------------------------------------------------

# Task 7 Solution
Person = namedtuple("Person", ["name", "age", "country"])
Person.__new__.__defaults__ = ("Unknown",)

p1 = Person("Alice", 30)
p2 = Person("Bob", 25, "Mexico")

print(p1)
print(p2)


# Task 8 Solution
Student = namedtuple("Student", ["name", "grade"])

def get_student():
    return Student("Arlette", 95)

student = get_student()
print(student.name, student.grade)


# ---------------------------------------------------------------------------
# Rank 5 — Professional
# ---------------------------------------------------------------------------

# Task 9 Solution
# Old tuple approach:
# user = ("admin", True)

User = namedtuple("User", ["role", "active"])
user = User("admin", True)

if user.role == "admin" and user.active:
    print("Admin access granted")


# Task 10 Solution
Record = namedtuple("Record", ["id", "value"])

records = [
    Record(1, 100),
    Record(2, 200),
    Record(3, 300)
]

for record in records:
    print(f"ID: {record.id}, Value: {record.value}")


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# These solutions show how named tuples:
# - improve readability
# - provide immutability
# - replace simple tuples and small classes
#
# Next Step:
# Move on to the next module when ready.
