from constants import BOOKING_ENDPOINT, BOOKING_BY_ID_ENDPOINT


def test_update_booking(requester, booking_data):
    # Создаем бронирование
    create_booking = requester.send_request(
        method="POST",
        endpoint=BOOKING_ENDPOINT,
        data=booking_data,
    )

    booking_id = create_booking.json().get("bookingid")
    assert booking_id is not None, "Идентификатор брони не найден в ответе"

    # Обновление данных для бронирования
    updated_booking_data = {
        "firstname": "Jane",
        "lastname": "Smith",
        "totalprice": 99999,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2025-05-05",
            "checkout": "2025-05-08",
        },
        "additionalneeds": "Breakfast",
    }

    # Выполняем PUT запрос
    requester.send_request(
        method="PUT",
        endpoint=BOOKING_BY_ID_ENDPOINT.format(
            booking_id=booking_id
        ),
        data=updated_booking_data,
    )

    # Проверяем, что бронирование обновилось
    get_booking = requester.send_request(
        method="GET",
        endpoint=BOOKING_BY_ID_ENDPOINT.format(
            booking_id=booking_id
        ),
    )

    body = get_booking.json()

    assert body["firstname"] == updated_booking_data["firstname"]
    assert body["totalprice"] == updated_booking_data["totalprice"]
