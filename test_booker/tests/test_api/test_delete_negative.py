from constants import BOOKING_BY_ID_ENDPOINT


def test_delete_booking_with_invalid_token(requester):
    # Запрос на удаление с неверным токеном
    requester._update_session_headers(
        Cookie="token=invalidtoken",
    )

    requester.send_request(
        method="DELETE",
        endpoint=BOOKING_BY_ID_ENDPOINT.format(booking_id=99999),
        expected_status=403,
    )


def test_delete_booking_twice(requester):
    # Попытка удалить несуществующее бронирование
    requester.send_request(
        method="DELETE",
        endpoint=BOOKING_BY_ID_ENDPOINT.format(booking_id=99999),
        expected_status=405,
    )

    # Повторная попытка удаления того же ID
    requester.send_request(
        method="DELETE",
        endpoint=BOOKING_BY_ID_ENDPOINT.format(booking_id=99999),
        expected_status=405,
    )
