from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def main_page():
    return "Главная страница"


@app.get("/user/admin")
async def admin_page():
    return "Вы вошли как администратор"


@app.get("/user/{user_id}")
async def user_page(user_id):
    return f"Вы вошли как пользователь № {user_id}"


@app.get("/user/")
async def user_list(username=None, age=None):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}."
