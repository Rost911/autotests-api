import allure
from httpx import Request, Response
from tools.logger import get_logger
from tools.http.curl import make_curl_from_request


logger = get_logger("HTTP_CLIENT")


def curl_event_hook(request: Request):
    """
    Event hook for automatically attaching a cURL command
    to the Allure report.

    :param request: HTTP request object passed to the `httpx` client.
    """
    # Generate a cURL command from the request object
    curl_command = make_curl_from_request(request)

    # Attach the generated cURL command to the Allure report
    allure.attach(curl_command, "cURL command", allure.attachment_type.TEXT)


def log_request_event_hook(request: Request):  # Create an event hook for request logging
    """
    Logs information about the outgoing HTTP request.

    :param request: HTTPX request object.
    """
    # Log an informational message about the outgoing request
    logger.info(f"Make {request.method} request to {request.url}")


def log_response_event_hook(response: Response):  # Create an event hook for response logging
    """
    Logs information about the received HTTP response.

    :param response: HTTPX response object.
    """
    # Log an informational message about the received response
    logger.info(
        f"Got response {response.status_code} {response.reason_phrase} from {response.url}"
    )