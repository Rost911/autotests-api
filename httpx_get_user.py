import httpx
from tools.fakers import fake

CREATE_USER_URL = "http://localhost:8000/api/v1/users"
AUTHENTICATION_LOGIN_URL = "http://localhost:8000/api/v1/authentication/login"
create_user_payload = {
  "email": f"{fake.email()}",
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
get_user_headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}
user_id = create_user_response_data["user"]["id"]
get_user_url = f"{CREATE_USER_URL}/{user_id}"
get_user_response = httpx.get(get_user_url,headers=get_user_headers)
get_user_response_data = get_user_response.json()
print(f"Get user data: {get_user_response_data}")