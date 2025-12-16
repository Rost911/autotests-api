from clients.api_client import APIClient
from typing import TypedDict
from httpx import Response
from clients.public_http_builder import get_public_http_client

class CreateUserRequestDict(TypedDict):
    """
    Описание структуры POST запроса
    на создание нового пользователя.
    """

    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class User(TypedDict):
    """
    Описание структуры пользователя.
    """
    id: str
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class CreateUserResponseDict(TypedDict):
    """
    Описание структуры ответа создания пользователя.
    """
    user: User

class PublicUsersClient(APIClient):
    """
    Клиент для работы с публичными методами /api/v1/users,
    которые не требуют авторизации (создание пользователя).
    """

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания нового пользователя.

        :param request: Данные пользователя для создания
                        (email, password, ФИО).
        :return: Объект httpx.Response с ответом сервера.
        """
        return self.post("/api/v1/users", json=request)

    def create_user(self, request: CreateUserRequestDict) -> CreateUserResponseDict:
        response = self.create_user_api(request=request)
        return response.json()

def get_public_users_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр PublicUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PublicUsersClient.
    """
    return PublicUsersClient(client=get_public_http_client())