from fastapi import FastAPI, HTTPException
from .schemas import ItemCreate
from .crud import create_order, get_orders

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the food ordering API!"}

@app.post("/orders")
async def create_order_endpoint(order: ItemCreate):
    new_order = await create_order(order)
    return {"message": "Order added successfully!", "order": new_order}

@app.get("/orders")
async def get_orders_endpoint():
    return await get_orders()

