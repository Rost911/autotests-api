from clients.api_client import APIClient
from httpx import Response
from clients.public_http_builder import get_public_http_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema

class PublicUsersClient(APIClient):
    """
    Клиент для работы с публичными методами /api/v1/users,
    которые не требуют авторизации (создание пользователя).
    """

    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """
        Выполняет POST-запрос для создания нового пользователя.

        :param request: Данные пользователя для создания
                        (email, password, ФИО).
        :return: Объект httpx.Response с ответом сервера.
        """
        return self.post("/api/v1/users", json=request.model_dump(by_alias=True))

    def create_user(self, request: CreateUserRequestSchema) -> CreateUserResponseSchema:
        response = self.create_user_api(request=request)
        return CreateUserResponseSchema.model_validate_json(response.text)

def get_public_users_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр PublicUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PublicUsersClient.
    """
    return PublicUsersClient(client=get_public_http_client())