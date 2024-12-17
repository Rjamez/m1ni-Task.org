from flask import Flask  
from lib.db.models import db, Task  
from datetime import datetime  
import click  

app = Flask(__name__)  
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
db.init_app(app)  

def init_db():  
    with app.app_context():  
        db.create_all()  

def add_task(title, description, due_date, priority):  
    with app.app_context():  
        new_task = Task(title=title, description=description, due_date=due_date, priority=priority)  
        db.session.add(new_task)  
        db.session.commit()  
        print("Task added successfully!")  

def view_tasks(filter_status=None, sort_by=None):  
    with app.app_context():  
        tasks = Task.query  
        if filter_status is not None:  
            tasks = tasks.filter(Task.status == filter_status)  
        if sort_by:  
            if sort_by == 'due_date':  
                tasks = tasks.order_by(Task.due_date)  
            elif sort_by == 'priority':  
                tasks = tasks.order_by(Task.priority)  
        for task in tasks.all():  
            status = "✔️ Completed" if task.status else "❌ Incomplete"  
            print(f"ID: {task.id}, Title: {task.title}, Description: {task.description}, Due: {task.due_date}, Priority: {task.priority}, Status: {status}")  

def update_task(task_id, title=None, description=None, due_date=None, priority=None, status=None):  
    with app.app_context():  
        task = Task.query.get(task_id)  
        if task:  
            if title is not None:  
                task.title = title  
            if description is not None:  
                task.description = description  
            if due_date is not None:  
                task.due_date = datetime.strptime(due_date, "%Y-%m-%d")  
            if priority is not None:  
                task.priority = priority  
            if status is not None:  
                task.status = status.lower() == 'true'  
            
            db.session.commit()  
            print("Task updated successfully!")  
        else:  
            print("Task not found.")  

def delete_task(task_id):  
    with app.app_context():  
        task = Task.query.get(task_id)  
        if task:  
            db.session.delete(task)  
            db.session.commit()  
            print("Task deleted successfully!")  
        else:  
            print("Task not found.")  

#### CLI Commands  
@click.command()  
@click.option('--action', help='Action to perform: add, view, update, delete, filter', required=True)  
@click.option('--title', help='Title of the task')  
@click.option('--description', help='Description of the task')  
@click.option('--due_date', help='Due date of the task, format: YYYY-MM-DD')  
@click.option('--priority', type=click.Choice(['Low', 'Medium', 'High']), help='Priority of the task')  
@click.option('--task_id', type=int, help='ID of the task to update/delete')  
@click.option('--status', type=click.BOOL, help='Task completion status (True/False)')  
@click.option('--filter', type=click.Choice(['completed', 'incomplete']), help='Filter tasks by status')  
@click.option('--sort_by', type=click.Choice(['due_date', 'priority']), help='Sort tasks')  
def cli(action, title, description, due_date, priority, task_id, status, filter, sort_by):  
    if action == 'add':  
        add_task(title, description, due_date, priority)  
    elif action == 'view':  
        view_tasks()  
    elif action == 'update':  
        update_task(task_id, title, description, due_date, priority, status)  
    elif action == 'delete':  
        delete_task(task_id)  
    elif action == 'filter':  
        filter_status = status == "true" if status else None  
        view_tasks(filter_status, sort_by)  
    else:  
        print("Invalid action")  

if __name__ == '__main__':  
    init_db()  
    cli()