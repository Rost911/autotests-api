import httpx

# response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")
# print(response.status_code)
# print(response.json())
#
# data = {
#     "title": "New task",
#     "completed": False,
#     "userId": 1
#
# }
#
# response_2 = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)
# print(response_2.status_code)
# print(response_2.json())
#
# data_2 = {"username": "test_user", "password": "12345"}
# response_3 = httpx.post("https://httpbin.org/post", data=data_2)
# print(response_3.status_code)
# print(response_3.json())
#
# headers = {"Authorization": "Bearer my_secret_token"}
# response_4 = httpx.get("https://httpbin.org/get", headers=headers)
# print(response_4.status_code)
# print(response_4.request.headers)
# print(response_4.json())
#
# params = {"userId": 1}
# response_5 = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)

# files = {"file": ("example.txt", open("example.txt", "rb"))}
# response_6 = httpx.post("https://httpbin.org/post", files=files)
# print(response_6.json())
#
# with httpx.Client() as client:
#     response1 = client.get(url)
#     response2 = client.get(url2)

# client = httpx.Client(headers={"Authorization": "Bearer my_secret_token"})
# response_7 = client.get("https://httpbin.org/get")
# print(response_7.json())

try:
    response_8 = httpx.get("https://jsonplaceholder.typicode.com/tssss")
    response_8.raise_for_status()
except httpx.HTTPStatusError as e:
    print(f"Error code: {e}")