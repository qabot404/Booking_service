from constants import BASE_URL



def test_create_without_body(aut_session):
    # Запрос с некорректным JSON
    create_booking = aut_session.post(
        f"{BASE_URL}/booking",
        json="{invalid_json}"
    )
    assert create_booking.status_code == 400, "Ожидалась ошибка 400: некорректный JSON в теле запроса"


