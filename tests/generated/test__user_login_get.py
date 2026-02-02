import logging
import pytest
import requests

BASE_URL = "https://petstore.swagger.io/v2"
ENDPOINT = "/user/login"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)

class TestUserLogin:
    @pytest.mark.positive
    def test_login_with_valid_credentials(self):
        params = {"username": "testUser", "password": "testPass123"}
        url = f"{BASE_URL}{ENDPOINT}"
        
        logging.info(f"Sending GET request to {url} with params: {params}")
        response = requests.get(url, params=params)
        logging.info(f"Received response with status code: {response.status_code}")
        logging.debug(f"Response body: {response.text}")
        
        assert response.status_code == 200
        assert "message" in response.json()
        assert "logged in user session" in response.json()["message"].lower()

    @pytest.mark.negative
    def test_login_with_missing_password(self):
        params = {"username": "testUser"}
        url = f"{BASE_URL}{ENDPOINT}"
        
        logging.info(f"Sending GET request to {url} with params: {params}")
        response = requests.get(url, params=params)
        logging.info(f"Received response with status code: {response.status_code}")
        logging.debug(f"Response body: {response.text}")
        
        assert response.status_code == 400