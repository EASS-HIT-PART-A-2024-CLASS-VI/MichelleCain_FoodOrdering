from fastapi import FastAPI, HTTPException
from typing import Optional
from .schemas import ItemCreate, FoodItem
from .crud import create_order, get_orders, delete_order, update_order

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
def update_order_endpoint(order_id: int, updated_order: FoodItem):
    for i, order in enumerate(orders_db):
        if order.id == order_id:
            orders_db[i] = updated_order
            return {"message": "Order updated successfully!", "order": updated_order}
    raise HTTPException(status_code=404, detail="Order not found")

@app.delete("/orders/{order_id}")
def delete_order_endpoint(order_id: int):
    global orders_db
    for order in orders_db:
        if order.id == order_id:
            orders_db.remove(order)
            return {"message": "Order deleted successfully!"}
    raise HTTPException(status_code=404, detail="Order not found")

@app.get("/orders/search")
def search_orders(name: Optional[str] = None, category: Optional[str] = None):
    results = [order for order in orders_db if (name in order.name) or (category in order.category)]
    return {"orders": results}

