import unittest

from TaskManagement import Task, Employee, TaskManager


class TestTaskManagement(unittest.TestCase):

    def setUp(self):
        self.manager = TaskManager()

        self.employee = Employee(
            "E001",
            "Navya",
            "Software Development"
        )

        self.task = Task(
            "T001",
            "Develop Login",
            "Create login module"
        )

        self.manager.add_employee(self.employee)
        self.manager.create_task(self.task)

    def test_employee_creation(self):
        self.assertEqual(self.employee.name, "Navya")
        self.assertEqual(
            self.employee.department,
            "Software Development"
        )

    def test_task_creation(self):
        self.assertEqual(self.task.status, "Pending")
        self.assertIsNone(self.task.assigned_to)

    def test_task_assignment(self):
        self.manager.assign_task("T001", "E001")

        self.assertEqual(
            self.task.assigned_to,
            self.employee
        )

        self.assertIn(self.task, self.employee.tasks)

    def test_status_update(self):
        self.manager.update_task_status(
            "T001",
            "Completed"
        )

        self.assertEqual(
            self.task.status,
            "Completed"
        )

    def test_invalid_status(self):
        with self.assertRaises(ValueError):
            self.task.update_status("Invalid Status")

    def test_duplicate_task(self):
        duplicate_task = Task(
            "T001",
            "Another Task",
            "Duplicate task"
        )

        with self.assertRaises(ValueError):
            self.manager.create_task(duplicate_task)

    def test_missing_employee(self):
        with self.assertRaises(KeyError):
            self.manager.assign_task("T001", "E999")


if __name__ == "__main__":
    unittest.main()