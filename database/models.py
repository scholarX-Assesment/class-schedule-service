from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base

class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    subject = Column(String, index=True)
    contact_no = Column(String, index=True)

class Class(Base):
    __tablename__ = "classes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location = Column(String, index=True)

class ClassSchedule(Base):
    __tablename__ = "class_schedules"

    id = Column(Integer, primary_key=True, index=True)
    class_name = Column(String, index=True)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), index=True)
    room_number = Column(String, index=True)
    time_slot = Column(String, index=True)

    teacher = relationship("Teacher")
    class_ = relationship("Class")