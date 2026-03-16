from constants import BOOKING_BY_ID_ENDPOINT


def test_patch_booking_invalid_json(requester):
    # Запрос с некорректным JSON
    responses = requester.session.patch(
        f"{requester.base_url}/booking/1",
        data="{invalid_json",
    )

    assert responses.status_code == 400


def test_patch_invalid_token(requester):
    # Запрос с неверным токеном
    requester.session.headers.update(
        {
            "Cookie": "token=invalidtoken",
        }
    )

    requester.send_request(
        method="PATCH",
        endpoint=BOOKING_BY_ID_ENDPOINT.format(
            booking_id=1
        ),
        data={"firstname": "Test"},
        expected_status=403,
    )