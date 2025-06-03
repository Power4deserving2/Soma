from sqlalchemy import Column, Integer, String
from database.setup import Base

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    school_name = Column(String)
    grade_level = Column(String)
    teacher_name = Column(String)

    def __repr__(self):
        return f"<Student(name='{self.name}', grade='{self.grade_level}')>"