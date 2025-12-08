from clients.api_client import APIClient
from typing import TypedDict
from httpx import Response


class CreateUserDict(TypedDict):
    """
    Описание структуры POST запроса
    на создание нового пользователя.
    """

    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    """
    Клиент для работы с публичными методами /api/v1/users,
    которые не требуют авторизации (создание пользователя).
    """

    def create_user_api(self, request: CreateUserDict) -> Response:
        """
        Выполняет POST-запрос для создания нового пользователя.

        :param request: Данные пользователя для создания
                        (email, password, ФИО).
        :return: Объект httpx.Response с ответом сервера.
        """
        return self.post("/api/v1/users", json=request)
