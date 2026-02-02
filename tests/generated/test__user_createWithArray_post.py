import logging
import pytest
import requests

BASE_URL = "https://petstore.swagger.io/v2"
ENDPOINT = "/user/createWithArray"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class TestCreateUserWithArray:
    valid_users = [
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

    invalid_users = [
        {
            "id": 3,
            "firstName": "Invalid",
            "lastName": "User",
            "email": "invalid@example.com",
            "password": "pass3",
            "phone": "112233",
            "userStatus": 1
        }
    ]

    def test_create_users_with_valid_array(self):
        logging.info("Sending POST request with valid user array")
        response = requests.post(
            url=f"{BASE_URL}{ENDPOINT}",
            json=self.valid_users
        )
        logging.info(f"Received response: Status {response.status_code}, Body: {response.text}")
        assert response.status_code == 200

    def test_create_users_with_invalid_array(self):
        logging.info("Sending POST request with invalid user array (missing username)")
        response = requests.post(
            url=f"{BASE_URL}{ENDPOINT}",
            json=self.invalid_users
        )
        logging.info(f"Received response: Status {response.status_code}, Body: {response.text}")
        assert response.status_code == 400