# app/crud.py

from bson.objectid import ObjectId
from .database import order_collection
from .schemas import ItemCreate, Item  # חשוב לשים לב לייבוא הנכון

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

# עדכון הזמנה קיימת
async def update_order(order_id: str, new_data: Item):  # השם כאן בסדר, נכון ל-FoodItem.
    order_object_id = ObjectId(order_id)
    updated_order = await order_collection.find_one_and_update(
        {"_id": order_object_id},
        {"$set": new_data.dict()},
        return_document=True
    )
    return order_helper(updated_order)

# מחיקת הזמנה
async def delete_order(order_id: str):
    order_object_id = ObjectId(order_id)
    result = await order_collection.delete_one({"_id": order_object_id})
    return {"deleted_count": result.deleted_count}
