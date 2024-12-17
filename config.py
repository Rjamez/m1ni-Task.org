# config.py

# SQLite database file path (this can be changed to a different location if needed)
DATABASE_PATH = 'task_manager.db'

# Default values
DEFAULT_PRIORITY = 'Medium'
DEFAULT_STATUS = 0  # 0 for Incomplete, 1 for Completed

# Logging configuration (if you choose to add logging in the future)
LOGGING_ENABLED = False
LOG_FILE_PATH = 'task_manager.log'

# Task categories (optional, can be used to create predefined categories)
DEFAULT_CATEGORIES = [
    {"name": "Work", "description": "Tasks related to work", "status": 1},
    {"name": "Personal", "description": "Personal tasks", "status": 1},
    {"name": "Leisure", "description": "Leisure activities", "status": 1}
]
