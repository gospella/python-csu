from typing import Optional

from fastapi import FastAPI, Body, status, Query
from fastapi.responses import JSONResponse, FileResponse

from src.schemas import people, Person
from src.crud import find_person
from src.utils import logger
from src.models import User, UserResponse

app = FastAPI()


@app.get("/")
async def return_index():
    return FileResponse("src/public/index.html")


@app.get("/csu/example/sadas/asdasd")
async def return_example():
    return "help"


@app.get("/film/comedy/2022/{id}")
async def main(id: str):
    return id + " ваш ID"


@app.get("/edu/")
async def edu_query_params(id: str, name: str = "Ivan", surname: str = "Medvedev"):
    return id + name + surname


@app.get("/edu/query_params")
def get_query_params(first_param: str = Query(default=None, min_length=2)):
    resp = {"resp": f"Вы передали {first_param}"}
    return resp


@app.post("/edu/model/user", response_model=UserResponse)
async def main(user: User):

    return {"id": f"{user.id}/{user.name}"}


@app.get("/api/users")
def get_people():
    return people


@app.get("/api/users/{id}")
def get_person(id):
    # получаем пользователя по id
    person = find_person(id)
    print(person)
    # если не найден, отправляем статусный код и сообщение об ошибке
    if person == None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Пользователь не найден"},
        )
    # если пользователь найден, отправляем его
    return person


@app.post("/api/users")
def create_person(data=Body()):
    person = Person(data["name"], data["age"])
    # добавляем объект в список people
    people.append(person)
    return person


@app.put("/api/users")
def edit_person(data=Body()):

    # получаем пользователя по id
    person = find_person(data["id"])
    # если не найден, отправляем статусный код и сообщение об ошибке
    if person == None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Пользователь не найден"},
        )
    # если пользователь найден, изменяем его данные и отправляем обратно клиенту
    person.age = data["age"]
    person.name = data["name"]
    return person


@app.delete("/api/users/{id}")
def delete_person(id):
    # получаем пользователя по id
    person = find_person(id)

    # если не найден, отправляем статусный код и сообщение об ошибке
    if person == None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Пользователь не найден"},
        )

    # если пользователь найден, удаляем его
    people.remove(person)
    return person
