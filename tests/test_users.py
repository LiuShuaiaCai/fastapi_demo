"""User Endpoint Tests"""
import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_users():
    """Test get all users"""
    response = client.get("/api/v1/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_nonexistent_user():
    """Test get nonexistent user"""
    response = client.get("/api/v1/users/99999")
    assert response.status_code == 404
