from constants import BOOKING_BY_ID_ENDPOINT


def test_put_booking_with_invalid_token(requester, booking_data):
    # Отправка PUT-запроса с неверным токеном
    requester.session.headers.update(
        {
            "Cookie": "token=invalidtoken",
        }
    )

    requester.send_request(
        method="PUT",
        endpoint=BOOKING_BY_ID_ENDPOINT.format(
            booking_id=99999
        ),
        data=booking_data,
        expected_status=403,
    )


def test_update_booking_missing_required_field(requester, booking_data):
    # Отправка PUT-запроса с пропущенным обязательным полем
    updated_booking_data = {
        "firstname": "Jane",
        "totalprice": 99999,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2025-05-05",
            "checkout": "2025-05-08",
        },
        "additionalneeds": "Breakfast",
    }

    requester.send_request(
        method="PUT",
        endpoint=BOOKING_BY_ID_ENDPOINT.format(
            booking_id=1
        ),
        data=updated_booking_data,
        expected_status=400,
    )
