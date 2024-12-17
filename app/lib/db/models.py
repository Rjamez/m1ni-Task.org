from flask_sqlalchemy import SQLAlchemy  
from datetime import datetime  
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import func

db = SQLAlchemy()  

class Task(db.Model):  
    __tablename__ = 'tasks'  
    
    id = db.Column(db.Integer, primary_key=True)  
    title = db.Column(db.String, nullable=False)  
    description = db.Column(db.String)  
    due_date = db.Column(db.Date, nullable=False)  
    priority = db.Column(db.String, nullable=False)  # Low, Medium, High  
    status = db.Column(db.Boolean, default=False)  # False for Incomplete  
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):  
        return f"<Task {self.title}>"

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'due_date': self.due_date,
            'priority': self.priority,
            'status': self.status,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }