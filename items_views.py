from fastapi import APIRouter, Path
from typing import Annotated


router = APIRouter(
    prefix="/items",
)

@router.get("/")
def list_items():
    return [
        {"id": 1, "name": "Item 1"},
        {"id": 2, "name": "Item 2"},
    ]


@router.get("/latest/")
def get_latest_item():
    return {
        "id": 2,
        "name": "Item 2",
    }


@router.get("/{item_id}/")
def get_item(item_id: Annotated[int, Path(ge=1, lt=1_000_000)]):
    return {
        "id": item_id,
    }