import httpx
from tools.fakers import get_random_email

CREATE_USER_URL = "http://localhost:8000/api/v1/users"
AUTHENTICATION_LOGIN_URL = "http://localhost:8000/api/v1/authentication/login"
create_user_payload = {
  "email": f"{get_random_email()}",
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

create_user_response = httpx.post(CREATE_USER_URL, json=create_user_payload)
create_user_response_data = create_user_response.json()
print(f"Create user data: {create_user_response_data}")

login_payload = {
    "email": create_user_payload["email"],
    "password": create_user_payload["password"]
}

login_response = httpx.post(AUTHENTICATION_LOGIN_URL, json=login_payload)
login_response_data = login_response.json()
print(f"Login data: {login_response_data}")

delete_user_headers ={
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}
DELETE_USER_URL = f"{CREATE_USER_URL}/{create_user_response_data['user']['id']}"
delete_user_response = httpx.delete(DELETE_USER_URL, headers=delete_user_headers)
print(f"Delete user status code: {delete_user_response.status_code}")