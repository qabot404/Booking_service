from constants import BASE_URL


def test_put_booking_with_invalid_token(aut_session, booking_data):
    # Отправка PUT-запроса с неверным токеном
    update_booking = aut_session.put(
        f"{BASE_URL}/booking/99999",
        json=booking_data,
        headers={"Cookie": "token=invalidtoken"}
    )
    assert update_booking.status_code == 403, "Обновление бронирования с недействительным токеном запрещено"


def test_update_booking_missing_required_field(aut_session, booking_data):
    # Отправка PUT-запроса с пропущенным обязательным полем
    updated_booking_data = {
        "firstname": "Jane",
        "totalprice": 99999,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2025-05-05",
            "checkout": "2025-05-08"
        },
        "additionalneeds": "Breakfast"
    }

    update_booking = aut_session.put(
        f"{BASE_URL}/booking/1",
        json=updated_booking_data
    )
    assert update_booking.status_code == 400, "Ошибка при попытке обновления бронирования с пропущенными обязательными полями"
