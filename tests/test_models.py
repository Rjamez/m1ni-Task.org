import unittest  
from lib.cli import app  
from lib.db.models import db, Task  

class TaskModelTestCase(unittest.TestCase):  
    def setUp(self):  
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  
        app.config['TESTING'] = True  
        self.app = app  
        self.app_context = self.app.app_context()  
        self.app_context.push()  
        db.create_all()  

    def tearDown(self):  
        db.session.remove()  
        db.drop_all()  
        self.app_context.pop()  

    def test_create_task(self):  
        task = Task(title="Sample Task", description="Sample Description", due_date="2024-12-31", priority="High")  
        db.session.add(task)  
        db.session.commit()  

        retrieved_task = Task.query.first()  
        self.assertEqual(retrieved_task.title, "Sample Task")  
        self.assertEqual(retrieved_task.description, "Sample Description")  
        self.assertEqual(retrieved_task.priority, "High")  

    def test_due_date_format(self):  
        # Example for date format checking or other validation  
        with self.assertRaises(ValueError):  
            Task(title="Invalid Task", description="Invalid date", due_date="invalid-date", priority="Medium")  

if __name__ == '__main__':  
    unittest.main()