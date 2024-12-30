from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define Pydantic model for food order
class FoodItem(BaseModel):
    name: str
    quantity: int

# Mock in-memory database
orders_db = []

# GET endpoint to retrieve all orders
@app.get("/orders")
def get_orders():
    return {"orders": orders_db}

# POST endpoint to add a new order
@app.post("/orders")
def create_order(order: FoodItem):
    orders_db.append(order)
    return {"message": "Order added successfully!", "order": order}
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the food ordering API!"}

