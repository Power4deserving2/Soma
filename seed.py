from database.setup import Session
from models.student import Student
from models.tutor import Tutor
from models.assignment import Assignment
from models.submission import Submission

session = Session()

# Create tutors
tutor1 = Tutor(name="Mr. Okello", subject="Math", school_name="Green Valley")
tutor2 = Tutor(name="Ms. Achieng", subject="Science", school_name="Blue Hill")

# Create students
student1 = Student(name="Brian", age=13, school_name="Green Valley", grade_level="6", teacher_name="Mr. Okello")
student2 = Student(name="Sharon", age=14, school_name="Blue Hill", grade_level="7", teacher_name="Ms. Achieng")

# Create assignments
assignment1 = Assignment(title="Fractions", content="Solve the set of fraction problems", grade_level="6", tutor_id=1)
assignment2 = Assignment(title="Plant Cells", content="Label plant cell diagram", grade_level="7", tutor_id=2)

# Create submissions
submission1 = Submission(student_id=1, assignment_id=1, score=85)
submission2 = Submission(student_id=2, assignment_id=2, score=92)

# Add everything
session.add_all([tutor1, tutor2, student1, student2, assignment1, assignment2, submission1, submission2])
session.commit()
session.close()

print("Seed data inserted successfully.")