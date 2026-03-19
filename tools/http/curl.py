from httpx import Request, RequestNotRead


def make_curl_from_request(request: Request) -> str:
    """
    Generates a cURL command from a httpx HTTP request.

    :param request: The HTTP request from which the cURL command will be generated.
    :return: A string with the cURL command containing the request method, URL, headers, and body (if present).
    """
    # Create a list with the base cURL command, including method and URL
    result: list[str] = [f"curl -X '{request.method}'", f"'{request.url}'"]

    # Add headers in the format -H "Header: Value"
    for header, value in request.headers.items():
        result.append(f"-H '{header}: {value}'")

    # Add request body if present (e.g., for POST, PUT)
    try:
        if body := request.content:
            result.append(f"-d '{body.decode('utf-8')}'")
    except RequestNotRead:
        pass

    # Join parts with line breaks, excluding trailing '\'
    return " \\\n  ".join(result)