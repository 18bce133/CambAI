from fastapi.testclient import TestClient
from main import app
import fakeredis
from unittest.mock import patch


client = TestClient(app)
fake_redis = fakeredis.FakeStrictRedis()

@patch('main.r', fake_redis)
@patch('main.huey.enqueue')
def test_write_item(mock_enqueue):
    mock_enqueue.return_value = None
    response = client.post("/items/test_item", json={"item_value": "test_value"})
    assert response.status_code == 200
    assert response.json() == {"item_id": "test_item", "item_value": "test_value"}
    mock_enqueue.assert_called_once()

    print("test_write_item passed")
    
@patch('main.r', fake_redis)
def test_read_item():
    fake_redis.set("test_item", "test_value")
    response = client.get("/items/test_item")
    assert response.status_code == 200
    assert response.json() == {"item_id": "test_item", "item_value": "test_value"}
    print("test_read_item passed")

@patch('main.r', fake_redis)
def test_read_non_existent_item():
    response = client.get("/items/non_existent_item")
    assert response.status_code == 404
    print("test_read_non_existent_item passed")

@patch('main.r', fake_redis)
def test_write_item_without_value():
    response = client.post("/items/test_item", json={})
    assert response.status_code == 422
    print("test_write_item_without_value passed")

@patch('main.r', fake_redis)
def test_write_item_with_empty_value():
    response = client.post("/items/test_item", json={"item_value": ""})
    assert response.status_code == 400
    print("test_write_item_with_empty_value passed")
