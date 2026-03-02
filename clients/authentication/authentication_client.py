import allure
from clients.api_client import APIClient
from httpx import Response

from clients.public_http_builder import get_public_http_client
from clients.authentication.authentication_schema import LoginRequestSchema, RefreshRequestSchema,LoginResponseSchema
from tools.routes import APIRoutes


class AuthenticationClient(APIClient):
    """
    Client for working with /api/v1/authentication.
    """
    @allure.step("Authenticate user")
    def login_api(self, request: LoginRequestSchema) -> Response:
        """
        Method for authenticating a user.

        :param request: Dictionary containing email and password.
        :return: Server response as an httpx.Response object.
        """
        return self.post(
            f"{APIRoutes.AUTHENTICATION}/login",
            json=request.model_dump(by_alias=True))

    def login(self, request: LoginRequestSchema) -> LoginResponseSchema:
        response = self.login_api(request)
        return LoginResponseSchema.model_validate_json(response.text)

    @allure.step("Refresh authentication token")
    def refresh_api(self, request: RefreshRequestSchema) -> Response:
        """
        Method for refreshing the authorization token.

        :param request: Dictionary containing refreshToken.
        :return: Server response as an httpx.Response object.
        """
        return self.post(f"{APIRoutes.AUTHENTICATION}/refresh",
                         json=request.model_dump(by_alias=True))


def get_authentication_client() -> AuthenticationClient:
    """
    The function creates an instance of AuthenticationClient with a preconfigured HTTP client.

    :return: A ready-to-use AuthenticationClient.
    """
    return AuthenticationClient(client=get_public_http_client())