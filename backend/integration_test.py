from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_item():
    response = client.post("/items/", json={"name": "Pizza", "description": "Delicious pizza", "price": 10.0, "tax": 2.0})
    assert response.status_code == 200
    assert response.json() == {"item": {"name": "Pizza", "description": "Delicious pizza", "price": 10.0, "tax": 2.0}}

