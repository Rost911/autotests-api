from httpx import Client, URL, QueryParams, Response
from httpx._types import RequestData, RequestFiles
from typing import Any


class APIClient:
    """
    Базовый API клиент, который принимает экземпляр httpx.Client и
    предоставляет методы для выполнения HTTP-запросов.
    """

    def __init__(self, client: Client):
        """
        Инициализация базового клиента.

        :param client: объект httpx.Client, который будет выполнять HTTP-запросы.
        """
        self.client = client

    def get(self, url: URL | str, params: QueryParams | None = None) -> Response:
        """
        Выполняет GET-запрос.

        :param url: URL-адрес эндпоинта.
        :param params: GET-параметры запроса (например, ?key=value).
        :return: Объект Response с данными ответа.
        """
        return self.client.get(url, params=params)

    def post(
        self,
        url: URL | str,
        json: Any | None = None,
        data: RequestData | None = None,
        files: RequestFiles | None = None,
    ) -> Response:
        """
        Выполняет POST-запрос.

        :param url: URL-адрес эндпоинта.
        :param json: Данные в формате JSON.
        :param data: Данные формы (application/x-www-form-urlencoded).
        :param files: Файлы для загрузки (multipart/form-data).
        :return: Объект Response с данными ответа.
        """
        return self.client.post(url, json=json, data=data, files=files)

    def patch(self, url: URL | str, json: Any | None = None) -> Response:
        """
        Выполняет PATCH-запрос (частичное обновление данных).

        :param url: URL-адрес эндпоинта.
        :param json: Данные для обновления в формате JSON.
        :return: Объект Response с данными ответа.
        """
        return self.client.patch(url, json=json)

    def delete(self, url: URL | str) -> Response:
        """
        Выполняет DELETE-запрос (удаление данных).

        :param url: URL-адрес эндпоинта.
        :return: Объект Response с данными ответа.
        """
        return self.client.delete(url)
