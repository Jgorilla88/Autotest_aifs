import pytest
import os
import requests
from dotenv import load_dotenv
from .base_api import BaseApi  # Импортируем наш базовый класс

# Создаём класс для тестов, который наследуется от BaseApi
load_dotenv()


@pytest.mark.api
class TestApiLogin(BaseApi):

    def test_successful_api_login(self):
        # Arrange
        # Используем данные из базового класса
        url = self.BASE_URL + self.LOGIN_ENDPOINT

        login = os.getenv('LOGIN')
        password = os.getenv('PASSWORD')

        payload = {
            "email": login,
            "password": password
        }
        headers = {"Content-Type": "application/json"}

        # Act
        response = requests.post(url, headers=headers, json=payload)

        # Assert
        assert response.status_code == 200
        response_data = response.json()
        assert "accessToken" in response_data
        assert response_data["user"]["email"] == payload["email"]

    def test_failed_api_login_with_wrong_password(self):
        # Arrange
        # Используем данные из базового класса
        url = self.BASE_URL + self.LOGIN_ENDPOINT

        login = os.getenv('LOGIN')

        payload = {
            "email": login,
            "password": "WrongPassword123"
        }
        headers = {"Content-Type": "application/json"}

        # Act
        response = requests.post(url, headers=headers, json=payload)

        # Assert
        assert response.status_code == 401
        response_data = response.json()
        assert response_data["message"] == "Invalid email or password"
