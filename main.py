from fastapi import FastAPI, Path
from typing import Annotated
from pydantic import EmailStr, BaseModel
from items_views import router as items_router


app = FastAPI()
app.include_router(items_router)


class CreateUser(BaseModel):
    email: EmailStr


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/hello/")
def read_hello(name: str = "World"):
    if name:
        return {
            "Hello": name,
        }
    

@app.post("/users/")
def create_user(user: CreateUser):
    return user


@app.post("/calc/add/")
def calc_add(a: int, b: int):
    return {
        "result": a + b 
    }