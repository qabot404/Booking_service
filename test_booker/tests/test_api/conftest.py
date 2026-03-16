import pytest
import requests
from faker import Faker

from constants import HEADERS, BASE_URL
from requester.custom_requester import CustomRequester

faker = Faker()


@pytest.fixture(scope="session")
def session():
    session = requests.Session()
    session.headers.update(HEADERS)

    # Получаем токен
    response = session.post(
        f"{BASE_URL}/auth",
        json={
            "username": "admin",
            "password": "password123"
        }
    )

    token = response.json()["token"]

    # Добавляем токен в cookie
    session.headers.update(
        {
            "Cookie": f"token={token}"
        }
    )

    return session


@pytest.fixture(scope="session")
def requester(session):
    return CustomRequester(session, BASE_URL)


@pytest.fixture
def booking_data():
    return {
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
        "totalprice": faker.random_int(min=100, max=100000),
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-04-05",
            "checkout": "2024-04-08"
        },
        "additionalneeds": "Cigars"
    }
