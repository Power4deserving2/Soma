from database.setup import Base, engine
from models.student import Student

Base.metadata.create_all(engine)
print("Tables created successfully.")