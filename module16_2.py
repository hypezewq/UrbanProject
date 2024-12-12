from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/user/{username}/{age}")
async def abcde(
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter Username", example="hypezewq")],
        age: Annotated[int, Path(ge=18, le=120, description="Enter Age", example="24")]):
    return {username: age}


@app.get("/user/{user_id}")
async def print_user_id(user_id: Annotated[int, Path(gt=1, le=100, description="Enter User ID", example="1")]):
    return user_id
