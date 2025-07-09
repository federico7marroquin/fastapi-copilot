from fastapi import FastAPI

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_read_item():
    response = client.get("/items/1?q=testq&p=testp")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1, "q": "testq"}

def test_create_item():
    data = {"name": "item1", "value": 123}
    response = client.post("/items/", json=data)
    assert response.status_code == 200
    assert response.json() == {"item": data}
