from lib.db.models import db, Task  
from lib.cli import app  # Import the Flask app for the application context  

def seed_tasks():  
    with app.app_context():  # Initialize the app context for database operations  
        # Clear existing data  
        db.drop_all()  # Caution: This will drop all tables. Use in development!  
        db.create_all()  # Recreate tables  

        # Seed the database with initial tasks  
        tasks = [  
            Task(title="Buy groceries", description="Milk, Bread, Eggs", due_date="2024-12-20", priority="High"),  
            Task(title="Read a book", description="Finish reading 'The Great Gatsby'", due_date="2024-12-22", priority="Medium"),  
            Task(title="Workout", description="Gym session", due_date="2024-12-19", priority="Low"),  
            Task(title="Submit report", description="Submit the annual report to the manager", due_date="2024-12-25", priority="High")  
        ]  

        # Add tasks to the session and commit to the database  
        db.session.bulk_save_objects(tasks)  
        db.session.commit()  
        print("Database seeded!")  

if __name__ == "__main__":  
    seed_tasks()