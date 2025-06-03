from database.setup import Base, engine
from models.student import Student
from models.tutor import Tutor
from models.assignment import Assignment  # <-- Add this line

Base.metadata.create_all(engine)
print("Tables created successfully.")