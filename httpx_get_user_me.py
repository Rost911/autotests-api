import httpx

USER_LOGIN_URL = "http://localhost:8000/api/v1/authentication/login"
GET_USER_ME_URL = "http://localhost:8000/api/v1/users/me"

credentials = {
  "email": "testAPI@example.com",
  "password": "qwerty12345"
}
login_response = httpx.post(USER_LOGIN_URL, json=credentials)
print(f"Status code of POST request: {login_response.status_code}")
login_data = login_response.json()
accessToken = login_data["token"]["accessToken"]

headers = {"Authorization": f"Bearer {accessToken}"}
request_get_me = httpx.get(GET_USER_ME_URL, headers=headers)
print(f"Status code of GET request: {request_get_me.status_code}")
print(f"Client`s data: {request_get_me.json()}")