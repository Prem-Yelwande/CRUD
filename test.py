from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Todo CRUD")


class Todo(BaseModel):
    id: int
    todo: str
    completed: bool = False


todos: list[Todo] = []


def _find_index(todo_id: int) -> int:
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            return index
    return -1


@app.post("/todos", status_code=201)
def create(todo: Todo):
    if _find_index(todo.id) != -1:
        raise HTTPException(status_code=409, detail="Todo id already exists")
    todos.append(todo)
    return todo


@app.get("/todos")
def get():
    return todos


@app.get("/todos/{todo_id}")
def read(todo_id: int):
    index = _find_index(todo_id)
    if index == -1:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todos[index]


@app.put("/todos/{todo_id}")
def put(todo_id: int, updated_todo: Todo):
    index = _find_index(todo_id)
    if index == -1:
        raise HTTPException(status_code=404, detail="Todo not found")
    # Keep the path id authoritative so the body cannot silently retarget another record.
    todos[index] = updated_todo.model_copy(update={"id": todo_id})
    return todos[index]


@app.delete("/todos/{todo_id}")
def delete(todo_id: int):
    index = _find_index(todo_id)
    if index == -1:
        raise HTTPException(status_code=404, detail="Todo not found")
    todos.pop(index)
    return {"detail": "Todo deleted successfully"}
