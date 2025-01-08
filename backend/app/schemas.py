# app/schemas.py
from pydantic import BaseModel

class ItemCreate(BaseModel):
    name: str
    description: str
    price: float

class Item(ItemCreate):  # כולל id
    id: str
