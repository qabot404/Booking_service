import json
import requests
import logging
import os


class CustomRequester:
    """
    Кастомный реквестер для стандартизации и упрощения отправки HTTP-запросов.
    """

    base_headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    def __init__(self, session: requests.Session, base_url: str):
        """
        Инициализация кастомного реквестера.

        :param session: объект requests.Session
        :param base_url: базовый URL API
        """
        self.session = session
        self.base_url = base_url
        self.headers = self.base_headers.copy()

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

    def send_request(
        self,
        method: str,
        endpoint: str,
        data: dict | None = None,
        params: dict | None = None,
        expected_status: int = 200,
        need_logging: bool = True
    ):
        """
        Универсальный метод отправки HTTP-запросов.

        :param method: HTTP метод (GET, POST, PUT, DELETE и т.д.)
        :param endpoint: endpoint API (например "/booking")
        :param data: тело запроса
        :param params: query параметры
        :param expected_status: ожидаемый статус код
        :param need_logging: флаг включения логирования
        :return: response
        """

        url = f"{self.base_url}{endpoint}"

        response = self.session.request(
            method=method,
            url=url,
            json=data,
            params=params
        )

        if need_logging:
            self.log_request_and_response(response)

        if response.status_code != expected_status:
            raise ValueError(
                f"Unexpected status code: {response.status_code}. Expected: {expected_status}"
            )

        return response

    def _update_session_headers(self, **kwargs):
        """
        Обновляет headers сессии.

        :param kwargs: дополнительные headers
        """

        self.headers.update(kwargs)
        self.session.headers.update(self.headers)

    def log_request_and_response(self, response: requests.Response):
        """
        Логирует HTTP запрос и ответ.

        :param response: объект requests.Response
        """

        try:
            request = response.request

            GREEN = "\033[32m"
            RED = "\033[31m"
            RESET = "\033[0m"

            headers = " \\\n".join(
                [f"-H '{header}: {value}'" for header, value in request.headers.items()]
            )

            full_test_name = f"pytest {os.environ.get('PYTEST_CURRENT_TEST', '').replace(' (call)', '')}"

            body = ""

            if hasattr(request, "body") and request.body is not None:
                if isinstance(request.body, bytes):
                    body = request.body.decode("utf-8")

                body = f"-d '{body}' \n" if body != "{}" else ""

            # Лог запроса
            self.logger.info(f"\n{'=' * 40} REQUEST {'=' * 40}")
            self.logger.info(
                f"{GREEN}{full_test_name}{RESET}\n"
                f"curl -X {request.method} '{request.url}' \\\n"
                f"{headers} \\\n"
                f"{body}"
            )

            response_status = response.status_code
            is_success = response.ok
            response_data = response.text

            # форматирование JSON
            try:
                response_data = json.dumps(
                    json.loads(response.text),
                    indent=4,
                    ensure_ascii=False
                )
            except json.JSONDecodeError:
                pass

            # Лог ответа
            self.logger.info(f"\n{'=' * 40} RESPONSE {'=' * 40}")

            if not is_success:
                self.logger.info(
                    f"\tSTATUS_CODE: {RED}{response_status}{RESET}\n"
                    f"\tDATA: {RED}{response_data}{RESET}"
                )
            else:
                self.logger.info(
                    f"\tSTATUS_CODE: {GREEN}{response_status}{RESET}\n"
                    f"\tDATA:\n{response_data}"
                )

            self.logger.info(f"{'=' * 80}\n")

        except Exception as e:
            self.logger.error(f"\nLogging failed: {type(e)} - {e}")