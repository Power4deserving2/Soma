from sqlalchemy import Column, Integer, String
from database.setup import Base

class Tutor(Base):
    __tablename__ = 'tutors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    subject = Column(String)
    school_name = Column(String)

    def __repr__(self):
        return f"<Tutor(name='{self.name}', subject='{self.subject}')>"