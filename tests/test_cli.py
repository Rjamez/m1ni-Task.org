import unittest  
from click.testing import CliRunner  
from lib.cli import cli  
from lib.db.models import db, Task  
from lib.cli import app  

class CliTestCase(unittest.TestCase):  
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

    def test_add_task_via_cli(self):  
        runner = CliRunner()  
        result = runner.invoke(cli, ['add', '--title', 'CLI Test Task', '--description', 'Testing CLI', '--due_date', '2024-12-31', '--priority', 'Medium'])  
        self.assertEqual(result.exit_code, 0)  
        self.assertIn("Task added successfully!", result.output)  

        # Verify the task was added to the database  
        task = Task.query.first()  
        self.assertEqual(task.title, "CLI Test Task")  

    def test_view_tasks_via_cli(self):  
        # Add a sample task first  
        db.session.add(Task(title="View Test Task", description="Testing View", due_date="2024-12-31", priority="High"))  
        db.session.commit()  

        runner = CliRunner()  
        result = runner.invoke(cli, ['view'])  
        self.assertEqual(result.exit_code, 0)  
        self.assertIn("View Test Task", result.output)  

if __name__ == '__main__':  
    unittest.main()