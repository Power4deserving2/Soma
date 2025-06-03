from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database.setup import Base
from datetime import datetime

class Submission(Base):
    __tablename__ = 'submissions'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    assignment_id = Column(Integer, ForeignKey('assignments.id'))
    score = Column(Integer)
    submitted_at = Column(DateTime, default=datetime.utcnow)

    # Optional relationships (not required for now)
    student = relationship("Student", backref="submissions")
    assignment = relationship("Assignment", backref="submissions")

    def __repr__(self):
        return f"<Submission(student_id={self.student_id}, score={self.score})>"