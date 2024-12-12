from fastapi import FastAPI, Path, HTTPException
from typing import Annotated

app = FastAPI()
users = {"1": f"Имя: Example, возраст: 18"}


@app.get("/users")
async def get_users():
    return users


@app.post("/user/{username}/{age}")
async def add_user(username: Annotated[str, Path(min_length=4, max_length=15)],
                   age: Annotated[int, Path(ge=12, le=100)]):
    id = max([int(i) for i in users.keys()])
    users[str(id + 1)] = f"Имя: {username}, возраст: {age}"
    return f"User {id + 1} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: Annotated[str, Path(min_length=1)], username: Annotated[str, Path(min_length=4, max_length=15)], age: Annotated[
    int, Path(ge=12, le=100)]):
    if user_id in users:
        users[user_id] = f"Имя: {username}, возраст: {age}"
        return f"The user {user_id} is updated"
    return HTTPException(status_code=404, detail="User not found")


@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[str, Path(min_length=1)]):
    if user_id in users:
        del users[user_id]
        return f"The user {user_id} is deleted"
    return HTTPException(status_code=404, detail="User not found")


