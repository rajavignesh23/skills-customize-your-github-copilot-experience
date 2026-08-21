from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str = ""


items = [
    {"id": 1, "name": "Laptop", "description": "A portable computer"},
    {"id": 2, "name": "Mouse", "description": "Used to control the cursor"},
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}


# TODO: Add GET /items
# TODO: Add POST /items
# TODO: Add GET /items/{item_id}
# TODO: Add PUT /items/{item_id}
