from lib.db.models import db, Task, Category

def seed_tasks():
    with app.app_context():
        # Clear existing data
        db.drop_all()  # Caution: This will drop all tables. Use in development!
        db.create_all()  # Recreate tables

        # Seed categories
        work_category = Category(name="Work", description="Tasks related to work")
        personal_category = Category(name="Personal", description="Personal tasks")
        db.session.add(work_category)
        db.session.add(personal_category)
        db.session.commit()

        # Seed tasks
        tasks = [
            Task(title="Buy groceries", description="Milk, Bread, Eggs", due_date="2024-12-20", priority="High", category_id=personal_category.id),
            Task(title="Read a book", description="Finish reading 'The Great Gatsby'", due_date="2024-12-22", priority="Medium", category_id=personal_category.id),
            Task(title="Workout", description="Gym session", due_date="2024-12-19", priority="Low", category_id=personal_category.id),
            Task(title="Submit report", description="Submit the annual report to the manager", due_date="2024-12-25", priority="High", category_id=work_category.id)
        ]

        # Add tasks to the session and commit to the database
        db.session.bulk_save_objects(tasks)
        db.session.commit()
        print("Database seeded!")

if __name__ == "__main__":
    seed_tasks()