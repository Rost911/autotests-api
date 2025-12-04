import httpx
from tools.fakers import get_random_email
CREATE_USER_URL = "http://localhost:8000/api/v1/users"
payload = {
  "email": f"{get_random_email()}",
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}
response = httpx.post(CREATE_USER_URL, json=payload)
print(response.status_code)
print(response.json())
