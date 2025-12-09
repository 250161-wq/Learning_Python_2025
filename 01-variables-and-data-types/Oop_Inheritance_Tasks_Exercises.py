"""
Module 21 — Inheritance & OOP Patterns: Practice Tasks
Build on Module 20 (custom classes/objects) and practice:

- Class inheritance (child classes extending a base class)
- Method overriding (changing behavior in subclasses)
- Using super() to reuse base logic
- Special methods like __str__ for readable objects
- Polymorphism: different objects sharing a common interface

In these tasks, you will work with:
- A base Person class
- Student and Teacher subclasses
- A Gamer mixin-style behavior
- Car ownership modeled with classes

Author: Peyman Miyandashti
Date of Birth: 11/11/1983
ID Number: 250161
Year: 2025
"""

# ===========================================================
# Task 1 — Basic Inheritance
# Create a base class Person and a subclass Student
# ===========================================================

class Person:
    """
    TODO:
    - Add an __init__ method with parameters: name, age, country, city.
    - Save them as instance attributes (self.name, self.age, etc.).
    - Add a describe() method that returns a short string like:
      "Peyman (43) from Tabriz, Iran"
    """
    pass


class Student(Person):
    """
    TODO:
    - Inherit from Person.
    - Extend the __init__ to also accept:
      university, degree_program, student_id.
    - Use super().__init__(...) for the Person part.
    - Add a method study_summary() that returns something like:
      "Peyman studies INFORMATION TECHNOLOGY ENGINEERING AND DIGITAL INNOVATION at UPBC."
    """
    pass


def task_1_example():
    """
    TODO:
    - Create a Student object that represents:
        Name: Peyman Miyandashti
        Age: 43
        Country: Iran
        City: Tabriz
        University: Polytechnic Baja California University (UPBC)
        Degree: INFORMATION TECHNOLOGY ENGINEERING AND DIGITAL INNOVATION
        Student ID: 250161
    - Print:
        - person description
        - study summary
    """
    pass


# ===========================================================
# Task 2 — Teacher Subclass and Method Overriding
# ===========================================================

class Teacher(Person):
    """
    TODO:
    - Inherit from Person.
    - Add __init__ with:
        subject, school_name, years_experience.
    - Use super().__init__ for the common fields.
    - Override describe() so it returns:
      "Arlette Chong (47), Teacher of <subject> at <school>, from Mexicali, Mexico."
    """
    pass


def task_2_example():
    """
    TODO:
    - Create a Teacher object that represents your wife:
        Name: Arlette Chong
        Age: 47
        Country: Mexico
        City: Mexicali
        Subject: (for example) "Mathematics & Physics"
        School: "Secondary School in Mexicali"
        Years of experience: (choose an integer, e.g., 20)
    - Print the result of describe().
    """
    pass


# ===========================================================
# Task 3 — Car Class and Ownership
# ===========================================================

class Car:
    """
    TODO:
    - __init__(self, brand, model, year, color)
    - Save all to attributes.
    - Add a short_info() method that returns:
      "2024 Kia Sportage (Dark Gray)"
    """
    pass


class CarOwner(Person):
    """
    TODO:
    - Inherit from Person.
    - __init__ should accept a Person's info + a Car object.
    - Store the car as self.car.
    - Add a method car_description() that uses the Car.short_info()
      to return something like:
      "Peyman owns a 2024 Kia Sportage (Dark Gray)."
    """
    pass


def task_3_example():
    """
    TODO:
    - Create:
        - Peyman's Car:
            brand="Kia", model="Sportage", year=2024, color="Dark Gray"
        - CarOwner for Peyman using that car.
        - Arlette's Car:
            brand="Hyundai", model="Creta", year=2018, color="White" (or any color)
        - CarOwner for Arlette.
    - Print car_description() for both owners.
    """
    pass


# ===========================================================
# Task 4 — Gamer Behavior (Mixin-style)
# ===========================================================

class Gamer:
    """
    Represents gamer-related behavior.

    TODO:
    - __init__(self, favorite_game, hours_per_week)
    - Save both to attributes.
    - Add a method gaming_profile() that returns:
      "Favorite game: World OF War Craft, plays <hours_per_week> hours/week."
    """
    pass


class GamerStudent(Student, Gamer):
    """
    TODO:
    - Multiple inheritance: Student + Gamer.
    - __init__ should accept all parameters for Student AND:
        favorite_game, hours_per_week.
    - Call Student.__init__ and Gamer.__init__ explicitly
      (no need to use super() for this task).
    - Add a method full_profile() that combines:
        - describe() from Person/Student
        - study_summary()
        - gaming_profile()
      into a multi-line string.
    """
    pass


def task_4_example():
    """
    TODO:
    - Create a GamerStudent that represents Peyman:
        - Use your real info:
            name="Peyman Miyandashti"
            age=43
            country="Iran"
            city="Tabriz"
            university="Polytechnic Baja California University (UPBC)"
            degree_program="INFORMATION TECHNOLOGY ENGINEERING AND DIGITAL INNOVATION"
            student_id=250161
            favorite_game="World OF War Craft"
            hours_per_week (choose e.g. 10)
    - Print full_profile().
    """
    pass


# ===========================================================
# Task 5 — Special Methods and Polymorphism
# ===========================================================

class ProfileBase:
    """
    Abstract-style base for profiles.

    TODO:
    - Add a method summary(self) that raises NotImplementedError.
    - This will be overridden by subclasses.
    """
    def summary(self) -> str:
        raise NotImplementedError("Subclasses must implement summary().")


class StudentProfile(ProfileBase):
    """
    TODO:
    - __init__(self, student: Student)
    - Store the student instance.
    - Implement summary() to return something like:
      "Student: <name>, Age: <age>, Program: <degree_program>."
    """
    pass


class TeacherProfile(ProfileBase):
    """
    TODO:
    - __init__(self, teacher: Teacher)
    - Store the teacher instance.
    - Implement summary() to return something like:
      "Teacher: <name>, Subject: <subject>, School: <school_name>."
    """
    pass


def task_5_example():
    """
    TODO:
    - Create:
        - One Student representing Peyman.
        - One Teacher representing Arlette.
    - Wrap them into:
        - StudentProfile
        - TeacherProfile
    - Put both profiles into a list called profiles.
    - Loop over profiles and print profile.summary().
      (This is an example of polymorphism: different objects,
       same interface 'summary'.)
    """
    pass


# ===========================================================
# Main quick-test helper (you can use this while solving)
# ===========================================================

if __name__ == "__main__":
    print("Module 21 — Inheritance & OOP Patterns: TASKS")
    print("Run each task_*_example() after you complete it to test.")
