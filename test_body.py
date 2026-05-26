import requests

response = requests.post(
    "http://127.0.0.1:8000/users",
    json={
        "username": "finito",
        "email": "finito@busaraspace.com",
        "age": 17,
        "bio": None,
        "is_active": False
    }
)

print(response.json())
