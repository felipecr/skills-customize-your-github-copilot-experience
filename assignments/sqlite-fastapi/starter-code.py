import sqlite3
from typing import Optional

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel

app = FastAPI(title="SQLite Task API")


class TaskCreate(BaseModel):
    title: str
    description: str = ""
    completed: bool = False


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


def get_db_connection():
    connection = sqlite3.connect("tasks.db")
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    with get_db_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT DEFAULT '',
                completed BOOLEAN DEFAULT 0
            )
            """
        )
        connection.commit()


init_db()


@app.get("/")
def read_root():
    return {"message": "Welcome to the SQLite Task API!"}


@app.get("/tasks")
def get_tasks(completed: Optional[bool] = Query(None)):
    # TODO: list tasks from the database
    # TODO: if completed is provided, filter by completed status
    return []


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    # TODO: fetch a single task by id from SQLite
    # TODO: raise HTTPException(404, detail="Task not found") if missing
    return {"id": task_id, "title": "Example task"}


@app.post("/tasks")
def create_task(task: TaskCreate):
    # TODO: insert the task into the database
    return task


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskUpdate):
    # TODO: update the existing task in the database
    # TODO: raise HTTPException(404, detail="Task not found") if missing
    return {"id": task_id, "title": "Updated task"}


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    # TODO: delete the task from the database
    # TODO: raise HTTPException(404, detail="Task not found") if missing
    return {"message": "Task deleted"}
