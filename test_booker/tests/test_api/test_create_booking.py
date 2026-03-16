from constants import BOOKING_ENDPOINT, BOOKING_BY_ID_ENDPOINT


class TestBookings:

    def test_create_booking(self, requester, booking_data):
        # Создаем бронирование
        create_booking = requester.send_request(
            method="POST",
            endpoint=BOOKING_ENDPOINT,
            data=booking_data
        )

        body = create_booking.json()

        booking_id = body.get("bookingid")

        assert booking_id is not None, "Идентификатор брони не найден в ответе"
        assert body["booking"]["firstname"] == booking_data["firstname"], \
            "Заданное имя не совпадает"
        assert body["booking"]["totalprice"] == booking_data["totalprice"], \
            "Заданная стоимость не совпадает"

        # Проверяем, что бронирование можно получить по ID
        get_booking = requester.send_request(
            method="GET",
            endpoint=BOOKING_BY_ID_ENDPOINT.format(booking_id=booking_id)
        )

        assert get_booking.json()["lastname"] == booking_data["lastname"], \
            "Заданная фамилия не совпадает"

        # Удаляем бронирование
        requester.send_request(
            method="DELETE",
            endpoint=BOOKING_BY_ID_ENDPOINT.format(booking_id=booking_id),
            expected_status=201
        )

        # Проверяем, что бронирование больше недоступно
        requester.send_request(
            method="GET",
            endpoint=BOOKING_BY_ID_ENDPOINT.format(booking_id=booking_id),
            expected_status=404
        )
