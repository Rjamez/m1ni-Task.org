import unittest  
from lib.cli import app  
from lib.db.models import db, Task  

class IntegrationTestCase(unittest.TestCase):  
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

    def test_task_crud_operations(self):  
        # Creating a task  
        new_task = Task(title="Integrated Test Task", description="Testing integration", due_date="2024-12-31", priority="Low")  
        db.session.add(new_task)  
        db.session.commit()  
        
        # Read the task back  
        task = Task.query.filter_by(title="Integrated Test Task").first()  
        self.assertIsNotNone(task)  

        # Update the task  
        task.priority = "High"  
        db.session.commit()  
        self.assertEqual(task.priority, "High")  

        # Delete the task  
        db.session.delete(task)  
        db.session.commit()  
        deleted_task = Task.query.filter_by(title="Integrated Test Task").first()  
        self.assertIsNone(deleted_task)  

if __name__ == '__main__':  
    unittest.main()