from sqlalchemy import Column, Text, Integer,String, Boolean,ForeignKey, DateTime
from sqlalchemy.orm  import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class TechnicalInstructor(Base):
    __tablename__ = "technical_instructors"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # One-to-many relationship: One TechnicalInstructor can have many Courses
    courses = relationship("Course", back_populates="instructor")

# Define the Student model
class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    # The foreign key to relate to the Course
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=True)

    # Each Student can have many Courses - (assuming direct enrollment in courses)
    courses = relationship("Course", back_populates="students")


# Define the Course model
class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    instructor_id = Column(Integer, ForeignKey('technical_instructors.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Define the relationship with TechnicalInstructor
    instructor = relationship("TechnicalInstructor", back_populates="courses")
    
    # Each Course can have many Students
    students = relationship("Student", back_populates="courses")



# The relationship here
# 1 - many => TechnicalInstructor - Course
# 1 - many => Student - Course