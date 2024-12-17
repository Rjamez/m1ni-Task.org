from database import create_tables, add_task, view_tasks, add_category, update_task_status, add_reminder, view_categories
from utils import get_input # type: ignore

def main_menu():
    while True:
        print("\n=== Task Manager CLI ===")
        print("1. Add a Task")
        print("2. View Tasks")
        print("3. Add a Category")
        print("4. View Categories")
        print("5. Update Task Status")
        print("6. Add Reminder to Task")
        print("7. Exit")

        choice = get_input("Enter your choice: ")

        if choice == '1':
            # Add Task
            title = get_input("Enter task title: ")
            description = get_input("Enter task description: ")
            due_date = get_input("Enter due date (YYYY-MM-DD): ")
            priority = get_input("Enter priority (Low, Medium, High): ")
            category_id = int(get_input("Enter category ID (e.g., 1 for 'Work'): "))
            add_task(title, description, due_date, priority, category_id)

        elif choice == '2':
            # View Tasks
            view_tasks()

        elif choice == '3':
            # Add Category
            name = get_input("Enter category name: ")
            description = get_input("Enter category description: ")
            add_category(name, description)

        elif choice == '4':
            # View Categories
            view_categories()

        elif choice == '5':
            # Update Task Status
            task_id = int(get_input("Enter task ID to update: "))
            new_status = int(get_input("Enter new status (0 for Incomplete, 1 for Completed): "))
            new_priority = get_input("Enter new priority (Low, Medium, High): ")
            update_task_status(task_id, new_status, new_priority)

        elif choice == '6':
            # Add Reminder to Task
            task_id = int(get_input("Enter task ID for reminder: "))
            reminder_date = get_input("Enter reminder date (YYYY-MM-DD HH:MM:SS): ")
            add_reminder(task_id, reminder_date)

        elif choice == '7':
            # Exit
            print("Exiting Task Manager CLI...")
            break

        else:
            print("Invalid choice. Please try again.")

# Initialize the tables
create_tables()

# Start the application
main_menu()
