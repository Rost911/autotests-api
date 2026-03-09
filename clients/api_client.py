from typing import Any
from httpx import Client, URL, QueryParams, Response
from httpx._types import RequestData, RequestFiles

import allure


class APIClient:
    """
    Base API client that accepts an httpx.Client instance and
    provides methods for executing HTTP requests.
    """
    def __init__(self, client: Client):
        """
        Initialization of the base client.

        :param client: httpx.Client object that will perform HTTP requests.
        """
        self.client = client

    @allure.step("Make GET request to {url}")
    def get(self, url: URL | str, params: QueryParams | None = None) -> Response:
        """
        Performs a GET request.

        :param url: Endpoint URL.
        :param params: GET query parameters (for example, ?key=value).
        :return: A Response object containing the response data.
        """
        return self.client.get(url, params=params)

    @allure.step("Make POST request to {url}")
    def post(
        self,
        url: URL | str,
        json: Any | None = None,
        data: RequestData | None = None,
        files: RequestFiles | None = None,
    ) -> Response:
        """
        Performs a POST request.

        :param url: Endpoint URL.
        :param json: Data in JSON format.
        :param data: Form data (application/x-www-form-urlencoded).
        :param files: Files to upload (multipart/form-data).
        :return: A Response object containing the response data.
        """
        return self.client.post(url, json=json, data=data, files=files)

    @allure.step("Make PATCH request to {url}")
    def patch(self, url: URL | str, json: Any | None = None) -> Response:
        """
        Performs a PATCH request (partial data update).

        :param url: Endpoint URL.
        :param json: Data for updating in JSON format.
        :return: A Response object containing the response data.
        """
        return self.client.patch(url, json=json)

    @allure.step("Make DELETE request to {url}")
    def delete(self, url: URL | str) -> Response:
        """
        Performs a DELETE request (data deletion).

        :param url: Endpoint URL.
        :return: A Response object containing the response data.
        """
        return self.client.delete(url)
