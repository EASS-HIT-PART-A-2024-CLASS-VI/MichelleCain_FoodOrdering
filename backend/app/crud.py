from bson.objectid import ObjectId
from .database import order_collection
from .schemas import ItemCreate

# המרת MongoDB ObjectID ל-JSON
def order_helper(order) -> dict:
    return {
        "id": str(order["_id"]),
        "name": order["name"],
        "description": order["description"],
        "price": order["price"],
    }

# יצירת הזמנה חדשה
async def create_order(order: ItemCreate):
    order = await order_collection.insert_one(order.dict())
    new_order = await order_collection.find_one({"_id": order.inserted_id})
    return order_helper(new_order)

# קבלת כל ההזמנות
async def get_orders():
    orders = []
    async for order in order_collection.find():
        orders.append(order_helper(order))
    return orders

