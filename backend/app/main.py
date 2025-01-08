from fastapi import FastAPI, HTTPException
from typing import Optional
from .schemas import ItemCreate, Item  # שים לב לייבוא הנכון
from .crud import create_order, get_orders, update_order, delete_order

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

@app.put("/orders/{order_id}")
async def update_order_endpoint(order_id: int, updated_order: Item):
    updated_order = await update_order(str(order_id), updated_order.dict())
    return {"message": "Order updated successfully!", "order": updated_order}

@app.delete("/orders/{order_id}")
async def delete_order_endpoint(order_id: int):
    result = await delete_order(str(order_id))
    if result["deleted_count"] == 0:
        raise HTTPException(status_code=404, detail="Order not found")
    return {"message": "Order deleted successfully!"}

@app.get("/orders/search")
async def search_orders(name: Optional[str] = None, category: Optional[str] = None):
    results = [order for order in await get_orders() if (name in order["name"]) or (category in order["category"])]
    return {"orders": results}
