from constants import BASE_URL


def test_update_booking(aut_session, booking_data):
    # Создаем бронирование
    create_booking = aut_session.post(
        f"{BASE_URL}/booking",
        json=booking_data
    )
    assert create_booking.status_code == 200, "Ошибка при создании брони"

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
            "checkout": "2025-05-08"
        },
        "additionalneeds": "Breakfast"
    }

    # Выполняем PUT запрос
    updated_booking = aut_session.put(
        f"{BASE_URL}/booking/{booking_id}",
        json=updated_booking_data
    )
    assert updated_booking.status_code == 200, "Ошибка при обновлении брони"

    # Проверяем, что бронирование обновилось
    get_booking = aut_session.get(
        f"{BASE_URL}/booking/{booking_id}"
    )
    assert get_booking.status_code == 200, "Бронь не найдена"
    assert get_booking.json()["firstname"] == updated_booking_data["firstname"], "Имя не обновилось"
    assert get_booking.json()["totalprice"] == updated_booking_data["totalprice"], "Стоимость не обновилась"
