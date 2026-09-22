# 📘 Assignment: SQLite Persistence with FastAPI

## 🎯 Objective

Build a small FastAPI application that stores and retrieves task records from a SQLite database. Students will practice database setup, CRUD operations, request validation, and API design in a real-world backend workflow.

## 📝 Tasks

### 🛠️ Set up the database

#### Description
Create a SQLite database and a `tasks` table to store task information for the application.

#### Requirements
The completed program must:

- Create a SQLite database file, such as `tasks.db`.
- Define a `tasks` table with fields such as `id`, `title`, `description`, and `completed`.
- Initialize the database when the app starts.
- Use Python code to connect to SQLite safely and execute SQL statements.

### 🛠️ Build CRUD endpoints

#### Description
Implement API routes to create, read, update, and delete tasks using FastAPI.

#### Requirements
The completed program must:

- Implement `GET /tasks` to list all tasks.
- Implement `GET /tasks/{task_id}` to get a single task by ID.
- Implement `POST /tasks` to create a new task.
- Implement `PUT /tasks/{task_id}` to update an existing task.
- Implement `DELETE /tasks/{task_id}` to remove a task.
- Return clear error messages when a task is not found.
- Use `HTTPException` for proper status codes such as `404`.

### 🛠️ Add validation and filtering

#### Description
Improve the API by validating incoming data and allowing users to filter tasks by completed status.

#### Requirements
The completed program must:

- Define a Pydantic model for creating and updating tasks.
- Validate that `title` is not empty.
- Support filtering with a query parameter such as `?completed=true`.
- Return JSON responses that are easy for a frontend or API client to consume.
- Keep the code organized into small, readable functions.

