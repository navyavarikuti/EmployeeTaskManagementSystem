from datetime import datetime


class Task:
    # Represents a task assigned to an employee.

    VALID_STATUSES = {"Pending", "In Progress", "Completed"}

    def __init__(self, task_id, title, description):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.status = "Pending"
        self.assigned_to = None
        self.created_at = datetime.now()

    def assign_task(self, employee):
        if not isinstance(employee, Employee):
            raise TypeError("Task can only be assigned to an Employee.")

        self.assigned_to = employee

    def update_status(self, status):
        if status not in self.VALID_STATUSES:
            raise ValueError(
                "Invalid status. Choose: Pending, In Progress, or Completed."
            )

        self.status = status

    def display_task(self):
        employee_name = (
            self.assigned_to.name if self.assigned_to else "Not Assigned"
        )

        return (
            f"\nTask ID: {self.task_id}\n"
            f"Title: {self.title}\n"
            f"Description: {self.description}\n"
            f"Status: {self.status}\n"
            f"Assigned To: {employee_name}\n"
        )


class Employee:
    # Represents an employee who can be assigned tasks.

    def __init__(self, employee_id, name, department):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.tasks = []

    def add_task(self, task):
        if not isinstance(task, Task):
            raise TypeError("Only Task objects can be assigned.")

        task.assign_task(self)
        self.tasks.append(task)

    def view_tasks(self):
        if not self.tasks:
            print(f"\nNo tasks assigned to {self.name}.")
            return

        print(f"\nTasks assigned to {self.name}:")
        for task in self.tasks:
            print(task.display_task())


class TaskManager:
    # Manages employees and tasks.

    def __init__(self):
        self.employees = {}
        self.tasks = {}

    def add_employee(self, employee):
        if employee.employee_id in self.employees:
            raise ValueError("Employee ID already exists.")

        self.employees[employee.employee_id] = employee

    def create_task(self, task):
        if task.task_id in self.tasks:
            raise ValueError("Task ID already exists.")

        self.tasks[task.task_id] = task

    def assign_task(self, task_id, employee_id):
        if task_id not in self.tasks:
            raise KeyError("Task not found.")

        if employee_id not in self.employees:
            raise KeyError("Employee not found.")

        task = self.tasks[task_id]
        employee = self.employees[employee_id]

        employee.add_task(task)

    def update_task_status(self, task_id, status):
        if task_id not in self.tasks:
            raise KeyError("Task not found.")

        self.tasks[task_id].update_status(status)

    def display_all_tasks(self):
        if not self.tasks:
            print("\nNo tasks available.")
            return

        print("\n========== ALL TASKS ==========")

        for task in self.tasks.values():
            print(task.display_task())


def get_non_empty_input(message):
    # Validates that the user does not enter an empty value.

    while True:
        value = input(message).strip()

        if value:
            return value

        print("Input cannot be empty. Please try again.")


def run_application():
    manager = TaskManager()

    # Sample employees
    employee1 = Employee("E001", "Navya", "Software Development")
    employee2 = Employee("E002", "Rahul", "Testing")

    manager.add_employee(employee1)
    manager.add_employee(employee2)

    # Sample tasks
    task1 = Task(
        "T001",
        "Develop Login Module",
        "Create login functionality using clean and reusable code."
    )

    task2 = Task(
        "T002",
        "Test Application",
        "Identify and report application defects."
    )

    manager.create_task(task1)
    manager.create_task(task2)

    # Assign tasks
    manager.assign_task("T001", "E001")
    manager.assign_task("T002", "E002")

    # Update task status
    manager.update_task_status("T001", "In Progress")
    manager.update_task_status("T002", "Completed")

    # Display results
    manager.display_all_tasks()

    employee1.view_tasks()
    employee2.view_tasks()


if __name__ == "__main__":
    try:
        run_application()

    except (ValueError, KeyError, TypeError) as error:
        print(f"Application Error: {error}")

    except Exception as error:
        print(f"Unexpected Error: {error}")