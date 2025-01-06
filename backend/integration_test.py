from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_item():
    # Send POST request to create an order
    response = client.post("/orders/", json={"name": "Pizza", "quantity": 2})
    
    # Ensure the response status code is 200
    assert response.status_code == 200
    
    # Ensure the response contains the success message and the created order
    assert response.json() == {"message": "Order added successfully!", "order": {"name": "Pizza", "quantity": 2}}

    # Ensure the order was added to the in-memory database
    created_order = next((order for order in orders_db if order["name"] == "Pizza"), None)
    assert created_order is not None
    assert created_order["name"] == "Pizza"
    assert created_order["quantity"] == 2

