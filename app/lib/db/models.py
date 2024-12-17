from flask_sqlalchemy import SQLAlchemy  
from datetime import datetime  

db = SQLAlchemy()  

class Task(db.Model):  
    __tablename__ = 'tasks'  
    
    id = db.Column(db.Integer, primary_key=True)  
    title = db.Column(db.String, nullable=False)  
    description = db.Column(db.String)  
    due_date = db.Column(db.Date, nullable=False)  
    priority = db.Column(db.String, nullable=False)  # Low, Medium, High  
    status = db.Column(db.Boolean, default=False)  # False for Incomplete  

    def __repr__(self):  
        return f"<Task {self.title}>"