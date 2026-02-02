import pytest
import requests
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

BASE_URL = "https://petstore.swagger.io/v2"
ENDPOINT = "/user/createWithList"

VALID_USERS = [
    {
        "id": 1,
        "username": "user1",
        "firstName": "John",
        "lastName": "Doe",
        "email": "john@example.com",
        "password": "pass1",
        "phone": "123456",
        "userStatus": 1
    },
    {
        "id": 2,
        "username": "user2",
        "firstName": "Jane",
        "lastName": "Smith",
        "email": "jane@example.com",
        "password": "pass2",
        "phone": "654321",
        "userStatus": 0
    }
]

INVALID_USERS = [
    {
        "id": "invalid_id",
        "username": 12345,
        "firstName": None,
        "lastName": "Doe",
        "email": "not-an-email",
        "password": "",
        "phone": True,
        "userStatus": "active"
    }
]

def test_create_users_with_valid_list():
    logger.info("Sending POST request with valid user list")
    response = requests.post(
        f"{BASE_URL}{ENDPOINT}",
        json=VALID_USERS
    )
    logger.info(f"Received response with status code: {response.status_code}")
    
    assert response.status_code == 200
    logger.info("Status code validation passed")

def test_create_users_with_invalid_list():
    logger.info("Sending POST request with invalid user list")
    response = requests.post(
        f"{BASE_URL}{ENDPOINT}",
        json=INVALID_USERS
    )
    logger.info(f"Received response with status code: {response.status_code}")
    
    assert response.status_code == 500
    logger.info("Status code validation passed")