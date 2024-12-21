from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_item():
    response = client.post("/items/", json={"name": "Pizza", "description": "Delicious pizza", "price": 10.0})
    assert response.status_code == 200
    assert response.json() == {"item": {"name": "Pizza", "description": "Delicious pizza", "price": 10.0}}

    created_item = Item.query.filter_by(name="Pizza").first()  
    assert created_item is not None
    assert created_item.name == "Pizza"
    assert created_item.description == "Delicious pizza"
    assert created_item.price == 10.0
