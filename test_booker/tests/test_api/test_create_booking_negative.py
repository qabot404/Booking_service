from constants import BOOKING_ENDPOINT


def test_create_without_body(requester):
    # Запрос с некорректным JSON
    requester.send_request(
        method="POST",
        endpoint=BOOKING_ENDPOINT,
        data={},
        expected_status=500,
    )
