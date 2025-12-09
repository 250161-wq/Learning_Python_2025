"""
Module 21 — Inheritance & OOP Patterns: Solutions

This file contains one possible set of solutions for the tasks in:
    oop_inheritance_tasks.py

Author: Peyman Miyandashti
ID Number: 250161
Year: 2025
"""

# ===========================================================
# Task 1 — Basic Inheritance
# ===========================================================

class Person:
    def __init__(self, name: str, age: int, country: str, city: str) -> None:
        self.name = name
        self.age = age
        self.country = country
        self.city = city

    def describe(self) -> str:
        return f"{self.name} ({self.age}) from {self.city}, {self.country}"


class Student(Person):
    def __init__(
        self,
        name: str,
        age: int,
        country: str,
        city: str,
        university: str,
        degree_program: str,
        student_id: int,
    ) -> None:
        super().__init__(name=name, age=age, country=country, city=city)
        self.university = university
        self.degree_program = degree_program
        self.student_id = student_id

    def study_summary(self) -> str:
        return (
            f"{self.name} studies {self.degree_program} "
            f"at {self.university} (ID: {self.student_id})."
        )


def task_1_example():
    peyman_student = Student(
        name="Peyman Miyandashti",
        age=43,
        country="Iran",
        city="Tabriz",
        university="Polytechnic Baja California University (UPBC)",
        degree_program="INFORMATION TECHNOLOGY ENGINEERING AND DIGITAL INNOVATION",
        student_id=250161,
    )

    print("Task 1 Example")
    print(peyman_student.describe())
    print(peyman_student.study_summary())
    print("-" * 50)


# ===========================================================
# Task 2 — Teacher Subclass and Method Overriding
# ===========================================================

class Teacher(Person):
    def __init__(
        self,
        name: str,
        age: int,
        country: str,
        city: str,
        subject: str,
        school_name: str,
        years_experience: int,
    ) -> None:
        super().__init__(name=name, age=age, country=country, city=city)
        self.subject = subject
        self.school_name = school_name
        self.years_experience = years_experience

    def describe(self) -> str:
        return (
            f"{self.name} ({self.age}), Teacher of {self.subject} at "
            f"{self.school_name}, from {self.city}, {self.country} "
            f"with {self.years_experience} years of experience."
        )


def task_2_example():
    arlette_teacher = Teacher(
        name="Arlette Chong",
        age=47,
        country="Mexico",
        city="Mexicali",
        subject="Mathematics & Physics",
        school_name="Secondary School in Mexicali",
        years_experience=20,
    )

    print("Task 2 Example")
    print(arlette_teacher.describe())
    print("-" * 50)


# ===========================================================
# Task 3 — Car Class and Ownership
# ===========================================================

class Car:
    def __init__(self, brand: str, model: str, year: int, color: str) -> None:
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def short_info(self) -> str:
        return f"{self.year} {self.brand} {self.model} ({self.color})"


class CarOwner(Person):
    def __init__(
        self,
        name: str,
        age: int,
        country: str,
        city: str,
        car: Car,
    ) -> None:
        super().__init__(name=name, age=age, country=country, city=city)
        self.car = car

    def car_description(self) -> str:
        return f"{self.name} owns a {self.car.short_info()}."


def task_3_example():
    peyman_car = Car(
        brand="Kia",
        model="Sportage",
        year=2024,
        color="Dark Gray",
    )
    arlette_car = Car(
        brand="Hyundai",
        model="Creta",
        year=2018,
        color="White",
    )

    peyman_owner = CarOwner(
        name="Peyman Miyandashti",
        age=43,
        country="Iran",
        city="Tabriz",
        car=peyman_car,
    )

    arlette_owner = CarOwner(
        name="Arlette Chong",
        age=47,
        country="Mexico",
        city="Mexicali",
        car=arlette_car,
    )

    print("Task 3 Example")
    print(peyman_owner.car_description())
    print(arlette_owner.car_description())
    print("-" * 50)


# ===========================================================
# Task 4 — Gamer Behavior (Mixin-style)
# ===========================================================

class Gamer:
    def __init__(self, favorite_game: str, hours_per_week: int) -> None:
        self.favorite_game = favorite_game
        self.hours_per_week = hours_per_week

    def gaming_profile(self) -> str:
        return (
            f"Favorite game: {self.favorite_game}, "
            f"plays {self.hours_per_week} hours/week."
        )


class GamerStudent(Student, Gamer):
    def __init__(
        self,
        name: str,
        age: int,
        country: str,
        city: str,
        university: str,
        degree_program: str,
        student_id: int,
        favorite_game: str,
        hours_per_week: int,
    ) -> None:
        Student.__init__(
            self,
            name=name,
            age=age,
            country=country,
            city=city,
            university=university,
            degree_program=degree_program,
            student_id=student_id,
        )
        Gamer.__init__(
            self,
            favorite_game=favorite_game,
            hours_per_week=hours_per_week,
        )

    def full_profile(self) -> str:
        return (
            f"{self.describe()}\n"
            f"{self.study_summary()}\n"
            f"{self.gaming_profile()}"
        )


def task_4_example():
    peyman_gamer_student = GamerStudent(
        name="Peyman Miyandashti",
        age=43,
        country="Iran",
        city="Tabriz",
        university="Polytechnic Baja California University (UPBC)",
        degree_program="INFORMATION TECHNOLOGY ENGINEERING AND DIGITAL INNOVATION",
        student_id=250161,
        favorite_game="World OF War Craft",
        hours_per_week=10,
    )

    print("Task 4 Example")
    print(peyman_gamer_student.full_profile())
    print("-" * 50)


# ===========================================================
# Task 5 — Special Methods and Polymorphism
# ===========================================================

class ProfileBase:
    def summary(self) -> str:
        raise NotImplementedError("Subclasses must implement summary().")


class StudentProfile(ProfileBase):
    def __init__(self, student: Student) -> None:
        self.student = student

    def summary(self) -> str:
        return (
            f"Student: {self.student.name}, Age: {self.student.age}, "
            f"Program: {self.student.degree_program}."
        )


class TeacherProfile(ProfileBase):
    def __init__(self, teacher: Teacher) -> None:
        self.teacher = teacher

    def summary(self) -> str:
        return (
            f"Teacher: {self.teacher.name}, Subject: {self.teacher.subject}, "
            f"School: {self.teacher.school_name}."
        )


def task_5_example():
    peyman = Student(
        name="Peyman Miyandashti",
        age=43,
        country="Iran",
        city="Tabriz",
        university="Polytechnic Baja California University (UPBC)",
        degree_program="INFORMATION TECHNOLOGY ENGINEERING AND DIGITAL INNOVATION",
        student_id=250161,
    )

    arlette = Teacher(
        name="Arlette Chong",
        age=47,
        country="Mexico",
        city="Mexicali",
        subject="Mathematics & Physics",
        school_name="Secondary School in Mexicali",
        years_experience=20,
    )

    profiles = [
        StudentProfile(peyman),
        TeacherProfile(arlette),
    ]

    print("Task 5 Example")
    for profile in profiles:
        print(profile.summary())
    print("-" * 50)


# ===========================================================
# Quick test
# ===========================================================

if __name__ == "__main__":
    print("Module 21 — Inheritance & OOP Patterns: SOLUTIONS\n")
    task_1_example()
    task_2_example()
    task_3_example()
    task_4_example()
    task_5_example()
