"""Simple in-memory Todo CRUD API.

Data lives in a Python list and resets when the process restarts.
Useful as a minimal FastAPI example of create/read/update/delete.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Todo CRUD")


class Todo(BaseModel):
    """A simple todo item with an id, description, and completion status."""
    id: int
    todo: str
    completed: bool = False


todos: list[Todo] = []


def _find_index(todo_id: int) -> int:
    """Return the list index of a todo by id, or -1 if not found."""
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            return index
    return -1


@app.get("/")
def root() -> dict:
    """Simple health check and API entry point."""
    return {"message": "Todo CRUD API is running", "docs": "/docs", "todos_count": len(todos)}


@app.post("/todos", status_code=201)
def create(todo: Todo) -> Todo:
    if _find_index(todo.id) != -1:
        raise HTTPException(status_code=409, detail=f"Todo with id {todo.id} already exists")
    todos.append(todo)
    return todo


@app.get("/todos")
def list_todos() -> list[Todo]:
    """Return all todos currently stored in memory."""
    return todos


@app.get("/todos/{todo_id}")
def read(todo_id: int) -> Todo:
    index = _find_index(todo_id)
    if index == -1:
        raise HTTPException(status_code=404, detail=f"Todo with id {todo_id} not found")
    return todos[index]


@app.put("/todos/{todo_id}")
def put(todo_id: int, updated_todo: Todo) -> Todo:
    index = _find_index(todo_id)
    if index == -1:
        raise HTTPException(status_code=404, detail=f"Todo with id {todo_id} not found")
    # Keep the path id authoritative so the body cannot silently retarget another record.
    todos[index] = updated_todo.model_copy(update={"id": todo_id})
    return todos[index]


@app.delete("/todos/{todo_id}")
def delete(todo_id: int) -> dict:
    index = _find_index(todo_id)
    if index == -1:
        raise HTTPException(status_code=404, detail=f"Todo with id {todo_id} not found")
    todos.pop(index)
    return {"detail": f"Todo with id {todo_id} deleted successfully"}
