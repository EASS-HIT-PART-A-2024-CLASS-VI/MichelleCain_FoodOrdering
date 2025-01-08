from pydantic import BaseModel

class ItemCreate(BaseModel):
    name: str
    description: str
    price: float

class Item(ItemCreate):
    id: str


