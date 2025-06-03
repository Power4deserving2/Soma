from database.setup import Base, engine
from models.student import Student
from models.tutor import Tutor
from models.assignment import Assignment
from models.submission import Submission  # <-- Add this

Base.metadata.create_all(engine)
print("Tables created successfully.")