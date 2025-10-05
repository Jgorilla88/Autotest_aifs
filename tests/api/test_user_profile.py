import pytest
import os
import requests
from dotenv import load_dotenv
from .base_api import BaseApi

load_dotenv()


@pytest.mark.api
class TestUser(BaseApi):
    def test_take_token(self):
        login_url = self.BASE_URL + self.LOGIN_ENDPOINT
        login = os.getenv('LOGIN')
        password = os.getenv('PASSWORD')

        login_payload = {
            "email": login,
            "password": password
        }
        login_headers = {"Content-Type": "application/json"}

        login_response = requests.post(
            url=login_url, headers=login_headers, json=login_payload)

        login_data = login_response.json()
        access_token = login_data['accessToken']

        user_url = self.BASE_URL + self.USER_ENDPOINT
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        user_response = requests.get(url=user_url, headers=headers)

        assert user_response.status_code == 200

        user_data = user_response.json()

        assert user_data['email'] == login_payload['email']
