from constants import BASE_URL, HEADERS


def test_delete_booking_with_invalid_token(aut_session):
    # Запрос на удаление с неверным токеном
    response = aut_session.delete(
        f"{BASE_URL}/booking/99999",
        headers={"Cookie": "token=invalidtoken"}
    )
    assert response.status_code == 403, "Удаление с неверным токеном должно быть отклонено"


def test_delete_booking_twice(aut_session):
    # Попытка удалить несуществующее бронирование
    aut_session.delete(
        f"{BASE_URL}/booking/99999",
        headers=HEADERS
    )

    # Повторная попытка удаления того же ID
    response = aut_session.delete(
        f"{BASE_URL}/booking/99999",
        headers=HEADERS
    )

    assert response.status_code == 405, "Повторное удаление бронирования должно быть отклонено"
