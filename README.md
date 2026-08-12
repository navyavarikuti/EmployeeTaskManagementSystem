# Employee Task Management System

A Python-based task management application designed to manage employees, create and assign tasks, update task status, and handle application errors using object-oriented programming principles.

## Features

- Create and manage employee records
- Create and manage tasks
- Assign tasks to employees
- Update task status
- View all tasks
- View employee-specific tasks
- Validate user input and task status
- Handle application errors using exceptions
- Unit testing with Python's `unittest` framework
- Clean and maintainable object-oriented code

## Technologies Used

- Python
- Object-Oriented Programming (OOP)
- Git & GitHub
- Python unittest
- Exception Handling
- Input Validation

## OOP Concepts Demonstrated

### Classes and Objects

- `Task` - Represents an individual task
- `Employee` - Represents an employee
- `TaskManager` - Manages employees and tasks

### Encapsulation

Task and employee data is managed within their respective classes using attributes and methods.

### Abstraction

Task management operations are handled through dedicated methods to keep the code organized and maintainable.

### Modular Design

The application separates responsibilities between the `Task`, `Employee`, and `TaskManager` classes.

## Project Structure

```text
EmployeeTaskManagement/
│
├── TaskManagement.py
├── TestTaskManagement.py
└── README.md
```
## How to Run

### Step 1: Clone the Repository

```bash
git clone <your-github-repository-url>
```
### Step 2: Navigate to the Project

```bash
cd EmployeeTaskManagement
```
### Step 3: Run the Application

```bash
python TaskManagement.py
```
### Step 4: Run Unit Tests

```bash
python -m unittest TestTaskManagement.py -v

```
## Application Workflow

### 1. Create Employees

Create employee records with an employee ID, name, and department.

### 2. Create Tasks

Create tasks with a task ID, title, and description.

### 3. Assign Tasks

Assign tasks to specific employees.

### 4. Update Task Status

Tasks can have the following statuses:

- Pending
- In Progress
- Completed

### 5. View Tasks

View all tasks or tasks assigned to a specific employee.

## Error Handling

The application uses Python exception handling to manage common software issues.

### Handled Errors

- Duplicate employee IDs
- Duplicate task IDs
- Missing employees
- Missing tasks
- Invalid task statuses
- Invalid object types
- Unexpected runtime errors

Exception handling improves application reliability and makes the application easier to debug and maintain.

## Testing

The project uses Python's built-in `unittest` framework.

### Test Cases

- Employee creation
- Task creation
- Task assignment
- Task status updates
- Invalid task status handling
- Duplicate task handling
- Missing employee handling

### Run Tests

```bash
python -m unittest TestTaskManagement.py -v
```
## Future Enhancements

- Add an interactive command-line menu
- Store employee and task data in MySQL
- Add user authentication
- Add task priorities and deadlines
- Add task search and filtering
- Build a REST API
- Add more automated test cases
- Add a web-based user interface

## Author

**Navya Varikuti**

Computer Science Undergraduate | Python | Software Development | OOP | Git
