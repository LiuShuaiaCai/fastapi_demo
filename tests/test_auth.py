"""Auth Endpoint Tests"""
import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_register():
    """Test user registration"""
    response = client.post(
        "/api/v1/auth/register",
        json={"username": "testuser", "email": "test@example.com", "password": "password123"},
    )
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"


def test_register_duplicate():
    """Test duplicate user registration"""
    client.post(
        "/api/v1/auth/register",
        json={"username": "testuser", "email": "test@example.com", "password": "password123"},
    )
    response = client.post(
        "/api/v1/auth/register",
        json={"username": "testuser", "email": "test2@example.com", "password": "password123"},
    )
    assert response.status_code == 400


def test_login():
    """Test user login"""
    client.post(
        "/api/v1/auth/register",
        json={"username": "testuser2", "email": "test2@example.com", "password": "password123"},
    )
    response = client.post(
        "/api/v1/auth/login",
        json={"username": "testuser2", "password": "password123"},
    )
    assert response.status_code == 200
    assert "access_token" in response.json()


def test_login_invalid():
    """Test login with invalid credentials"""
    response = client.post(
        "/api/v1/auth/login",
        json={"username": "nonexistent", "password": "wrongpassword"},
    )
    assert response.status_code == 401
