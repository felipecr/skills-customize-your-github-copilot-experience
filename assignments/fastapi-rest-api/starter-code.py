from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel

app = FastAPI(title="Task API")


class Task(BaseModel):
    id: int
    title: str
    description: str = ""


tasks = [
    Task(id=1, title="Learn FastAPI", description="Build a small API."),
    Task(id=2, title="Write tests", description="Verify endpoints work correctly."),
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI task API!"}


@app.get("/tasks")
def get_tasks():
    # TODO: return the full list of tasks
    return tasks


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    # TODO: find and return the task by id
    # TODO: raise HTTPException(404, detail="Task not found") if missing
    return tasks[0]


@app.post("/tasks")
def create_task(task: Task):
    # TODO: append the new task to the list
    return task


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    # TODO: update the existing task by id
    # TODO: raise HTTPException(404, detail="Task not found") if missing
    return task


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    # TODO: remove the task by id
    # TODO: raise HTTPException(404, detail="Task not found") if missing
    return {"message": "Task deleted"}
