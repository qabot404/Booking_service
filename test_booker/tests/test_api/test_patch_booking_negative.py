from constants import BASE_URL, HEADERS



def test_patch_booking_invalid_json(aut_session):
    # Запрос с некорректным JSON
    update_booking = aut_session.patch(
        f"{BASE_URL}/booking/1",
        data="{invalid_json",
        headers=HEADERS
    )
    assert update_booking.status_code == 400, "Некорректный JSON в PATCH-запросе должен приводить к ошибке"


def test_patch_invalid_token(aut_session):
    # Запрос с неверным токеном
    update_booking = aut_session.patch(
        f"{BASE_URL}/booking/1",
        json={"firstname": "Test"},
        headers={"Cookie": "token=invalidtoken"}
    )

    assert update_booking.status_code == 403, "PATCH с некорректной авторизацией должен быть отклонён"


