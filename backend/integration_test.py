# integration_test.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_item():
    response = client.post("/orders/", json={"name": "Pizza", "quantity": 2})
    print(response.json())  # הדפסה של התשובה
    assert response.status_code == 200
