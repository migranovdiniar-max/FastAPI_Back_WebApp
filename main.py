from fastapi import FastAPI
from pydantic import EmailStr, BaseModel

app = FastAPI()


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


@app.get("/items/")
def list_items():
    return [
        {"id": 1, "name": "Item 1"},
        {"id": 2, "name": "Item 2"},
    ]


@app.get("/item/latest/")
def get_latest_item():
    return {
        "id": 2,
        "name": "Item 2",
    }


@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {
        "id": item_id,
    }