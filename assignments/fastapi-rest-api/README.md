# 📘 Activity: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API using the FastAPI framework to manage a collection of books or tasks. The goal is to practice API design, HTTP methods, request validation, and response handling in Python.

## 📝 Tasks

### 🛠️ Create the FastAPI app

#### Description
Create a FastAPI application that exposes endpoints for creating, reading, updating, and deleting records.

#### Requirements
The completed program must:

- Import and initialize a FastAPI app.
- Define endpoints using HTTP methods such as `GET`, `POST`, `PUT`, and `DELETE`.
- Use a simple in-memory data store or a list of objects.
- Return JSON responses with appropriate status codes.
- Run the app locally with Uvicorn.

### 🛠️ Define data models

#### Description
Use Pydantic models to validate the request payload and shape the API responses.

#### Requirements
The completed program must:

- Define a model for the resource (for example, `Book` or `Task`).
- Include fields such as `id`, `title`, and `description`.
- Validate that required fields are present.
- Use type hints and default values appropriately.

### 🛠️ Implement CRUD endpoints

#### Description
Develop the core API routes for common CRUD operations.

#### Requirements
The completed program must:

- Implement `GET /items` to list all records.
- Implement `GET /items/{item_id}` to fetch one record by ID.
- Implement `POST /items` to create a new record.
- Implement `PUT /items/{item_id}` to update an existing record.
- Implement `DELETE /items/{item_id}` to remove a record.
- Return clear error responses when an item is not found.

### 🛠️ Add request and response examples

#### Description
Improve the API by adding documentation examples and optional query parameters.

#### Requirements
The completed program must:

- Include at least one query parameter in an endpoint.
- Add a `response_model` to improve API documentation.
- Provide example request bodies or sample responses.
- Ensure the endpoint documentation is readable in the FastAPI Swagger UI.

## ✅ Evaluation Criteria

Your submission will be evaluated based on:

- Correct use of FastAPI and Pydantic.
- Clean and readable Python code.
- Functional CRUD endpoints.
- Validation and error handling.
- Successful local app execution with Uvicorn.

## 💡 Bonus Challenge

Add a search feature such as:

- `GET /items?category=programming`
- `GET /items?search=python`

Or add a small authentication step using dependencies and API tokens.
