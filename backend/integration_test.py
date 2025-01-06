from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_item():
    response = client.post("/orders/", json={"name": "Pizza", "quantity": 2})
    assert response.status_code == 200
    assert response.json() == {"message": "Order added successfully!", "order": {"name": "Pizza", "quantity": 2}}


    created_order = next((order for order in orders_db if order["name"] == "Pizza"), None)
    assert created_order is not None
    assert created_order["name"] == "Pizza"
    assert created_order["quantity"] == 2
