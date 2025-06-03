from database.setup import Base, engine
from models.student import Student
from models.tutor import Tutor  # <-- Add this line

Base.metadata.create_all(engine)
print("Tables created successfully.")