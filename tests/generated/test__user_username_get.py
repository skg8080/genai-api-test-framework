import logging
import pytest
import requests

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("api_tests.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

BASE_URL = "https://petstore.swagger.io/v2"

class TestGetUserByUsername:
    @pytest.mark.positive
    def test_get_user_valid_username(self):
        username = "user1"
        url = f"{BASE_URL}/user/{username}"
        logger.info(f"Sending GET request to {url}")
        response = requests.get(url)
        logger.info(f"Received response with status code: {response.status_code}")
        assert response.status_code == 200

    @pytest.mark.negative
    def test_get_user_not_found(self):
        username = "non_existent_user_12345"
        url = f"{BASE_URL}/user/{username}"
        logger.info(f"Sending GET request to {url}")
        response = requests.get(url)
        logger.info(f"Received response with status code: {response.status_code}")
        assert response.status_code == 404

    @pytest.mark.negative
    def test_get_user_invalid_username(self):
        username = ""
        url = f"{BASE_URL}/user/{username}"
        logger.info(f"Sending GET request to {url}")
        response = requests.get(url)
        logger.info(f"Received response with status code: {response.status_code}")
        assert response.status_code == 400