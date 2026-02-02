import pytest
import requests
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

BASE_URL = "https://petstore.swagger.io/v2"

def test_logout_positive():
    logger = logging.getLogger(__name__)
    login_payload = {"username": "testuser", "password": "testpassword"}
    login_url = f"{BASE_URL}/user/login"
    
    logger.info("Creating session through login")
    login_response = requests.get(login_url, params=login_payload)
    logger.info(f"Login response status: {login_response.status_code}")
    
    assert login_response.status_code == 200
    
    logger.info("Sending logout request with valid session")
    logout_url = f"{BASE_URL}/user/logout"
    logout_response = requests.get(logout_url, cookies=login_response.cookies)
    logger.info(f"Logout response status: {logout_response.status_code}")
    
    assert logout_response.status_code == 200
    assert logout_response.json()["message"] == "ok"

def test_logout_negative():
    logger = logging.getLogger(__name__)
    logout_url = f"{BASE_URL}/user/logout"
    
    logger.info("Sending logout request without active session")
    logout_response = requests.get(logout_url)
    logger.info(f"Logout response status: {logout_response.status_code}")
    
    assert logout_response.status_code == 200