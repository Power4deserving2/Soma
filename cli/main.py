import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.setup import Session
from models.student import Student
from models.tutor import Tutor

def main_menu():
    print("\nWelcome to Soma 📚")
    print("1. View all students")
    print("2. View all tutors")
    print("3. Add a new student")  
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_students()
    elif choice == "2":
        view_tutors()
    elif choice == "3":
        add_student()
    elif choice == "0":
        print("Goodbye!")
        exit()
    else:
        print("Invalid choice.")
    
    main_menu()  # Loop back

def view_students():
    session = Session()
    students = session.query(Student).all()
    print("\nStudents:")
    for s in students:
        print(f"- {s.name}, Grade {s.grade_level}, School: {s.school_name}")
    session.close()

def view_tutors():
    session = Session()
    tutors = session.query(Tutor).all()
    print("\nTutors:")
    for t in tutors:
        print(f"- {t.name}, Subject: {t.subject}, School: {t.school_name}")
    session.close()

def add_student():
    session = Session()
    print("\nEnter student details:")
    name = input("Name: ")
    age = int(input("Age: "))
    school = input("School Name: ")
    grade = input("Grade Level: ")
    teacher = input("Teacher Name: ")

    new_student = Student(
        name=name,
        age=age,
        school_name=school,
        grade_level=grade,
        teacher_name=teacher
    )
    session.add(new_student)
    session.commit()
    session.close()
    print(f"\nStudent {name} added successfully!")

if __name__ == "__main__":
    main_menu()