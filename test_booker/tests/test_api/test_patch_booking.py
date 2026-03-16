from constants import BOOKING_ENDPOINT, BOOKING_BY_ID_ENDPOINT


def test_patch_booking(requester, booking_data):
    # Создаем бронирование
    create_booking = requester.send_request(
        method="POST",
        endpoint=BOOKING_ENDPOINT,
        data=booking_data,
    )

    booking_id = create_booking.json().get("bookingid")
    assert booking_id is not None, "Идентификатор брони не найден в ответе"

    # Обновляем только некоторые данные бронирования
    updated_booking_data = {
        "firstname": "John",
        "totalprice": 10000,
    }

    # Выполняем PATCH запрос
    requester.send_request(
        method="PATCH",
        endpoint=BOOKING_BY_ID_ENDPOINT.format(
            booking_id=booking_id
        ),
        data=updated_booking_data,
    )

    # Проверка на то, что бронирование обновилось
    get_booking = requester.send_request(
        method="GET",
        endpoint=BOOKING_BY_ID_ENDPOINT.format(
            booking_id=booking_id
        ),
    )

    body = get_booking.json()

    assert body["firstname"] == updated_booking_data["firstname"], "Имя не обновилось"
    assert body["totalprice"] == updated_booking_data["totalprice"], "Стоимость не обновилась"