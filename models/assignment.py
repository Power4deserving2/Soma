from sqlalchemy import Column, Integer, String, ForeignKey
from database.setup import Base

class Assignment(Base):
    __tablename__ = 'assignments'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    grade_level = Column(String)
    tutor_id = Column(Integer, ForeignKey('tutors.id'))

    def __repr__(self):
        return f"<Assignment(title='{self.title}', grade='{self.grade_level}')>"