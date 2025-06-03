import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.setup import Session
from models.student import Student
from models.tutor import Tutor

def main_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nWelcome to Soma 📚")
    print("1. View all students")
    print("2. View all tutors")
    print("3. Add a new student")
    print("4. Add a new tutor")
    print("5. Add a new assignment")
    print("6. Submit an assignment")
    print("7. View all submissions")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_students()
    elif choice == "2":
        view_tutors()
    elif choice == "3":
        add_student()
    elif choice == "4":
        add_tutor()
    elif choice == "5":
        add_assignment()
    elif choice == "6":
        submit_assignment()
    elif choice == "7":
        view_submissions()
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

def add_tutor():
    session = Session()
    print("\nEnter tutor details:")
    name = input("Name: ")
    subject = input("Subject: ")
    school = input("School Name: ")

    new_tutor = Tutor(
        name=name,
        subject=subject,
        school_name=school
    )
    session.add(new_tutor)
    session.commit()
    session.close()
    print(f"\nTutor {name} added successfully!")

def add_assignment():
    session = Session()
    print("\nEnter assignment details:")
    title = input("Title: ")
    content = input("Content: ")
    grade = input("Grade Level: ")
    
    # Show tutors to choose from
    tutors = session.query(Tutor).all()
    print("\nAvailable Tutors:")
    for tutor in tutors:
        print(f"{tutor.id}: {tutor.name} ({tutor.subject})")

    tutor_id = int(input("Enter Tutor ID to assign this: "))

    new_assignment = Assignment(
        title=title,
        content=content,
        grade_level=grade,
        tutor_id=tutor_id
    )

    session.add(new_assignment)
    session.commit()
    session.close()
    print(f"\nAssignment '{title}' added successfully!")

def submit_assignment():
    session = Session()

    # List students
    students = session.query(Student).all()
    print("\nStudents:")
    for s in students:
        print(f"{s.id}: {s.name}, Grade {s.grade_level}")

    student_id = int(input("Enter student ID: "))

    # List assignments
    assignments = session.query(Assignment).all()
    print("\nAssignments:")
    for a in assignments:
        print(f"{a.id}: {a.title} (Grade {a.grade_level})")

    assignment_id = int(input("Enter assignment ID: "))
    score = int(input("Enter score (0-100): "))

    submission = Submission(
        student_id=student_id,
        assignment_id=assignment_id,
        score=score
    )

    session.add(submission)
    session.commit()
    session.close()
    print("\nSubmission recorded successfully.")

def view_submissions():
    session = Session()
    submissions = session.query(Submission).all()

    print("\nSubmissions:")
    for sub in submissions:
        student = session.query(Student).get(sub.student_id)
        assignment = session.query(Assignment).get(sub.assignment_id)
        print(f"- {student.name} submitted '{assignment.title}' | Score: {sub.score} | Date: {sub.submitted_at.strftime('%Y-%m-%d')}")
    
    session.close()

if __name__ == "__main__":
    main_menu()