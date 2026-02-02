import pytest
import requests
import logging
import uuid

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

BASE_URL = "https://petstore.swagger.io/v2"

def generate_unique_username():
    return f"testuser_{uuid.uuid4().hex}"

def test_update_user_positive():
    username = generate_unique_username()
    user_data = {
        "username": username,
        "firstName": "Initial",
        "lastName": "User",
        "email": "initial@example.com",
        "password": "test123",
        "phone": "1234567890",
        "userStatus": 1
    }

    logger.info(f"Creating user {username} for positive test")
    create_response = requests.post(f"{BASE_URL}/user", json=user_data)
    assert create_response.status_code == 200

    updated_data = {
        "username": username,
        "firstName": "Updated",
        "lastName": "Name",
        "email": "updated@example.com",
        "password": "newpassword",
        "phone": "9876543210",
        "userStatus": 2
    }

    logger.info(f"Sending PUT request to update user {username}")
    response = requests.put(f"{BASE_URL}/user/{username}", json=updated_data)
    logger.info(f"Received response with status code: {response.status_code}")
    assert response.status_code == 200

def test_update_user_not_found():
    username = "non_existent_user_123"
    user_data = {
        "username": username,
        "firstName": "Test",
        "lastName": "User",
        "email": "test@example.com",
        "password": "password",
        "phone": "1234567890",
        "userStatus": 1
    }

    logger.info(f"Sending PUT request for non-existent user {username}")
    response = requests.put(f"{BASE_URL}/user/{username}", json=user_data)
    logger.info(f"Received response with status code: {response.status_code}")
    assert response.status_code == 404

def test_update_user_invalid_data():
    username = generate_unique_username()
    valid_data = {
        "username": username,
        "firstName": "Valid",
        "lastName": "User",
        "email": "valid@example.com",
        "password": "validpass",
        "phone": "1234567890",
        "userStatus": 1
    }

    logger.info(f"Creating user {username} for invalid data test")
    create_response = requests.post(f"{BASE_URL}/user", json=valid_data)
    assert create_response.status_code == 200

    invalid_data = {"firstName": "Invalid"}
    logger.info(f"Sending PUT request with invalid data for user {username}")
    response = requests.put(f"{BASE_URL}/user/{username}", json=invalid_data)
    logger.info(f"Received response with status code: {response.status_code}")
    assert response.status_code == 400