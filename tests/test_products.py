"""Product Endpoint Tests"""
import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_product():
    """Test product creation"""
    response = client.post(
        "/api/v1/products/",
        json={
            "name": "Test Product",
            "description": "A test product",
            "price": 99.99,
            "stock": 10,
        },
    )
    assert response.status_code == 201
    assert response.json()["name"] == "Test Product"


def test_get_products():
    """Test get all products"""
    response = client.get("/api/v1/products/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_nonexistent_product():
    """Test get nonexistent product"""
    response = client.get("/api/v1/products/99999")
    assert response.status_code == 404
