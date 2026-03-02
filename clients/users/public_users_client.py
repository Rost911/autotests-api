import allure
from clients.api_client import APIClient
from httpx import Response
from tools.routes import APIRoutes
from clients.public_http_builder import get_public_http_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema

class PublicUsersClient(APIClient):
    """
    Client for working with public /api/v1/users methods
    that do not require authorization (user creation).
    """
    @allure.step("Create user")
    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """
        Performs a POST request to create a new user.

        :param request: User data for creation
                        (email, password, full name).
        :return: An httpx.Response object with the server response.
        """
        return self.post(APIRoutes.USERS, json=request.model_dump(by_alias=True))

    def create_user(self, request: CreateUserRequestSchema) -> CreateUserResponseSchema:
        response = self.create_user_api(request=request)
        return CreateUserResponseSchema.model_validate_json(response.text)

def get_public_users_client() -> PublicUsersClient:
    """
    The function creates an instance of PublicUsersClient with a preconfigured HTTP client.

    :return: A ready-to-use PublicUsersClient.
    """
    return PublicUsersClient(client=get_public_http_client())