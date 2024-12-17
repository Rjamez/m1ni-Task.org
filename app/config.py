from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

from models import TechnicalInstructor, Student, Course


engine =  create_engine("sqlite:///school.sqlite")


# create a session
Session =  sessionmaker(bind=engine)
session = Session()