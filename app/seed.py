from faker import Faker
fake = Faker()

from config import *
from models import Tm, Student


for _ in range(20):
    student = Student(name=fake.name(), age=fake.pyint(), course=fake.text(), tm_id = 1)
    session.add(student)
    session.commit()