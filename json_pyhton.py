import json

json_data = [
  {
    "id": 1,
    "name": "John",
    "role": "admin"
  },
  {
    "id": 2,
    "name": "Alice",
    "role": "user"
  },
  {
    "id": 3,
    "name": "Bob",
    "role": "moderator"
  }
]
parsed_data = json.loads(json.dumps(json_data))
print(parsed_data)
