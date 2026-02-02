import pytest
import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

BASE_URL = "https://petstore.swagger.io/v2"

class TestDeleteUser:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.endpoint = "/user"

    def test_delete_user_positive(self):
        username = "testuser"
        url = f"{BASE_URL}{self.endpoint}/{username}"
        
        logging.info(f"Sending DELETE request to {url}")
        response = requests.delete(url)
        logging.info(f"Received response: Status {response.status_code}, Body: {response.text}")
        
        assert response.status_code == 200

    def test_delete_user_not_found(self):
        username = "non_existent_user_12345"
        url = f"{BASE_URL}{self.endpoint}/{username}"
        
        logging.info(f"Sending DELETE request to {url}")
        response = requests.delete(url)
        logging.info(f"Received response: Status {response.status_code}, Body: {response.text}")
        
        assert response.status_code == 404

    def test_delete_user_invalid_username(self):
        username = "invalid@user!name"
        url = f"{BASE_URL}{self.endpoint}/{username}"
        
        logging.info(f"Sending DELETE request to {url}")
        response = requests.delete(url)
        logging.info(f"Received response: Status {response.status_code}, Body: {response.text}")
        
        assert response.status_code == 400