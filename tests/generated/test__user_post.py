import pytest
import requests
import logging

BASE_URL = "https://petstore.swagger.io/v2"
ENDPOINT = "/user"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)

def test_create_user_positive():
    user_data = {
        "id": 12345,
        "username": "testuser",
        "firstName": "Test",
        "lastName": "User",
        "email": "test.user@example.com",
        "password": "testpassword",
        "phone": "+1234567890",
        "userStatus": 1
    }

    logging.info(f"Sending POST request to {BASE_URL}{ENDPOINT} with data: {user_data}")
    response = requests.post(f"{BASE_URL}{ENDPOINT}", json=user_data)
    logging.info(f"Received response - Status Code: {response.status_code}, Body: {response.text}")

    assert response.status_code == 200

def test_create_user_negative():
    invalid_user_data = {
        "firstName": "Invalid",
        "lastName": "User",
        "email": "invalid.email"
    }

    logging.info(f"Sending POST request to {BASE_URL}{ENDPOINT} with invalid data: {invalid_user_data}")
    response = requests.post(f"{BASE_URL}{ENDPOINT}", json=invalid_user_data)
    logging.info(f"Received response - Status Code: {response.status_code}, Body: {response.text}")

    assert response.status_code != 200