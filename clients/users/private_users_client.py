import allure
from httpx import Response
from tools.routes import APIRoutes
from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from clients.users.users_schema import UpdateUserRequestSchema, GetUserResponseSchema


class PrivateUsersClient(APIClient):
    """
    Client for working with /api/v1/users.
    """

    @allure.step("Get user me")
    def get_user_me_api(self)-> Response:
        """
        Method for retrieving the current user.

        :return: Server response as an httpx.Response object.
        """
        return self.get(f"{APIRoutes.USERS}/me")

    @allure.step("Get user by id {user_id}")
    def get_user_api(self, user_id: str)-> Response:
        """
        Method for retrieving a user by ID.

        :param user_id: User identifier.
        :return: Server response as a httpx.Response object.
        """
        return self.get(f"{APIRoutes.USERS}/{user_id}")

    @allure.step("Update user by id {user_id}")
    def update_user_api(self, user_id: str, request : UpdateUserRequestSchema) -> Response:
        """
        Method for updating a user by ID.

        :param user_id: User identifier.
        :param request: Dictionary containing email, lastName, firstName, middleName.
        :return: Server response as a httpx.Response object.
        """
        return self.patch(f"{APIRoutes.USERS}/{user_id}",json=request.model_dump(by_alias=True))

    @allure.step("Delete user by id {user_id}")
    def delete_user_api(self, user_id: str) -> Response:
        """
        Method for deleting a user by ID.

        :param user_id: User identifier.
        :return: Server response as an httpx.Response object.
        """
        return self.delete(f"{APIRoutes.USERS}/{user_id}")

    def get_user(self, user_id: str) -> GetUserResponseSchema:
        response = self.get_user_api(user_id)
        return GetUserResponseSchema.model_validate_json(response.text)


def get_private_users_client(user: AuthenticationUserSchema) -> PrivateUsersClient:
    """
    The function creates an instance of PrivateUsersClient with a preconfigured HTTP client.

    :return: A ready-to-use PrivateUsersClient.
    """
    return PrivateUsersClient(client=get_private_http_client(user))