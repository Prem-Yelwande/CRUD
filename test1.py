from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Users(BaseModel):
    id : int
    name:str
    age:int

users = []

@app.get("/users")
def read():
    return users

@app.post("/users")
def create(user:Users):
    users.append(user)
    return users

@app.put("/users{user_id}")
def update(user_id:int,updated_user:Users,notify:bool = False):
    if user_id < len(users):
        for index, userr in enumerate(users):
            if userr.id == user_id:
                users[index] = updated_user
                return {
                    "updated"
                    "notify": notify
                }
        else: return {"user does not exist"}
    else: return {"user does not exist"}
