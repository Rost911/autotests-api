import httpx
from tools.fakers import fake
CREATE_USER_URL = "http://localhost:8000/api/v1/users"
payload = {
  "email": f"{fake.email()}",
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}
response = httpx.post(CREATE_USER_URL, json=payload)
print(response.status_code)
print(response.json())
