"""Order Endpoint Tests"""
import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_order():
    """Test order creation"""
    response = client.post(
        "/api/v1/orders/",
        json={
            "user_id": 1,
            "product_id": 1,
            "quantity": 2,
            "total_price": 199.98,
        },
    )
    assert response.status_code == 201
    assert response.json()["status"] == "pending"


def test_get_orders():
    """Test get all orders"""
    response = client.get("/api/v1/orders/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_nonexistent_order():
    """Test get nonexistent order"""
    response = client.get("/api/v1/orders/99999")
    assert response.status_code == 404
