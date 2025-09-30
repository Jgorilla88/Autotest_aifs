import pytest
import requests
from .base_api import BaseApi


class TestUser(BaseApi):
    def test_take_token(self):
        login_url = self.BASE_URL + self.LOGIN_ENDPOINT
        login_payload = {
            "email": "aifstesters@gmail.com",
            "password": "Aifromspace1"
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
    pass
