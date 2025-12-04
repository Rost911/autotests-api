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
print("Create user status code:", create_user_response.status_code)
print(f"Create user data: {create_user_response_data}")
login_payload = {
    "email": create_user_payload["email"],
    "password": create_user_payload["password"]
}

login_response = httpx.post(AUTHENTICATION_LOGIN_URL, json=login_payload)
login_response_data = login_response.json()
print("Login status code:", login_response.status_code)
print(f"Login data: {login_response_data}")
update_user_headers ={
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}
updated_email = get_random_email()

update_user_data = {
    "email": updated_email,
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
UPDATE_USER_URL = f"{CREATE_USER_URL}/{create_user_response_data['user']['id']}"
update_user_response = httpx.patch(UPDATE_USER_URL, headers=update_user_headers, json=update_user_data)
print("Update user status code:", update_user_response.status_code)
print(f"Updated user data: {update_user_response.json()}")