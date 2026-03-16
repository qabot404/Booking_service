from constants import BOOKING_BY_ID_ENDPOINT
from test_booker.tests.test_api.conftest import requester


def test_get_nonexistent_booking(requester):
    # Запрос несуществующего ресурса
    requester.send_request(
        method="GET",
        endpoint=BOOKING_BY_ID_ENDPOINT.format(
            booking_id="nonexistent_id"
        ),
        expected_status=404,
    )


def test_get_booking_invalid_id(requester):
    # Запрос с некорректным форматом идентификатора
    requester.send_request(
        method="GET",
        endpoint=BOOKING_BY_ID_ENDPOINT.format(
            booking_id="@#@!"
        ),
        expected_status=404,
    )
