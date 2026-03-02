import allure
from clients.api_client import APIClient
from httpx import Response
from tools.routes import APIRoutes
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client


class FilesClient(APIClient):
    """
    Client for working with /api/v1/files.
    """
    @allure.step("Get file by id {file_id}")
    def get_file_api(self, file_id: str) -> Response:
        """
        Method for retrieving a file.

        :param file_id: File identifier.
        :return: Server response as an httpx.Response object.
        """
        return self.get(f"{APIRoutes.FILES}/{file_id}")

    @allure.step("Create file")
    def create_file_api(self, request: CreateFileRequestSchema) -> Response:
        """
        Method for creating a file.

        :param request: Dictionary containing filename, directory, upload_file.
        :return: Server response as an httpx.Response object.
        """
        return self.post(
            APIRoutes.FILES,
            data=request.model_dump(by_alias=True, exclude={'upload_file'}),
            files={"upload_file": open(request.upload_file, 'rb')}
        )

    @allure.step("Delete file by id {file_id}")
    def delete_file_api(self, file_id: str) -> Response:
        """
        Method for deleting a file.

        :param file_id: File identifier.
        :return: Server response as an httpx.Response object.
        """
        return self.delete(f"{APIRoutes.FILES}/{file_id}")


    def create_file(self, request: CreateFileRequestSchema) -> CreateFileResponseSchema:
        response = self.create_file_api(request)
        return CreateFileResponseSchema.model_validate_json(response.text)


def get_files_client(user: AuthenticationUserSchema) -> FilesClient:
    """
    The function creates an instance of FilesClient with a preconfigured HTTP client.

    :return: A ready-to-use FilesClient.
    """
    return FilesClient(client=get_private_http_client(user))
