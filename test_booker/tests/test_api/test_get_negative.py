from constants import BASE_URL


def test_get_nonexistent_booking(aut_session):
    # Запрос несуществующего ресурса
    get_booking = aut_session.get(
        f"{BASE_URL}/booking/nonexistent_id"
    )
    assert get_booking.status_code == 404, "Бронирование с указанными параметрами не найдено"


def test_get_booking_invalid_id(aut_session):
    # Запрос с некорректным форматом идентификатора
    get_booking = aut_session.get(
        f"{BASE_URL}/booking/@#@!"
    )
    assert get_booking.status_code == 404, "Ожидалась ошибка валидации из-за некорректного формата идентификатора"
