from flask_sqlalchemy import SQLAlchemy  
from datetime import datetime  

db = SQLAlchemy()  

class Category(db.Model):  
    __tablename__ = 'categories'  
    
    id = db.Column(db.Integer, primary_key=True)  
    name = db.Column(db.String, nullable=False)  
    description = db.Column(db.String)  
    tasks = db.relationship('Task', backref='category', lazy=True)  # One-to-many relationship

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
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)  # Foreign key for category

class TaskHistory(db.Model):  
    __tablename__ = 'task_history'  
    
    id = db.Column(db.Integer, primary_key=True)  
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'), nullable=False)  
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)  
    old_status = db.Column(db.String)  
    new_status = db.Column(db.String)  
    old_priority = db.Column(db.String)  
    new_priority = db.Column(db.String)  
    task = db.relationship('Task', backref='history', lazy=True)  # One-to-many relationship

class TaskReminder(db.Model):  
    __tablename__ = 'task_reminders'  
    
    id = db.Column(db.Integer, primary_key=True)  
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'), nullable=False)  
    reminder_date = db.Column(db.DateTime, nullable=False)  
    task = db.relationship('Task', backref='reminders', lazy=True)  # One-to-many relationship