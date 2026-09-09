from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Todo(BaseModel):
    id:int
    todo:str
    completed:bool = False

todos = []

@app.post('/todos')
def create(todo:Todo):
    todos.append(todo)
    return todos


@app.get('/todos')
def get():
    return todos

@app.get('/todos/{todo_id}')
def read(todo_id:int = 1):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    else: return {"wah re"}    

@app.put('/todos/{todo_id}')
def put(todo_id:int,updated_todo:Todo):
    for index , todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updated_todo
            return{
                "updated",
            }
    else : return {"wah re"}

@app.delete('/todos/{todo_id}')
def delete(todo_id:int):
    for index , todo in enumerate(todos):
        if todo.id == todo_id:
            print(todos[index],"poped")
            todos.pop(index)
    else : return {"wah re"}
      