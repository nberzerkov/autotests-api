# тут вся база работы с httpx

import httpx


# response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")
#
# print(response.status_code)
# print(response.json())

# ===

# data = {
#     "title": "Новая задача123",
#     "completed": False,
#     "userId": 1
# }
#
# response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)
# print(response.status_code)
# print(response.request.headers)
# print(response.json())

# ===

# data = {"username123": "test_user123", "password": "123456"}
#
# response = httpx.post("https://httpbin.org/post", data=data)
#
# print(response.status_code)
# print(response.json())

# ===

# headers = {"Authorization": "Bearer 123iksdijIsjdjsi"}
#
# response = httpx.get("c", headers=headers)
# print(response.status_code)
# print(response.request.headers)
# print(response.json())

# ===

# params = {"userId": 1,}
# response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)
#
# print(response.url)
# print(response.json()

# ===
#
# files = {"file": ("example.txt", open("example.txt", "rb"))}
#
# response = httpx.post("https://httpbin.org/post", files=files)
# print(response.json())

# ===

# with httpx.Client() as client:
#     response1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
#     response2 = client.get("https://jsonplaceholder.typicode.com/todos/2")
#
# print(response1.json())
# print(response2.json())

# ===

# with httpx.Client(headers={"Authorization": "Bearer 123iksdijIsjdjsi"}) as client:
#     response1 = client.get("https://httpbin.org/get")
#
# print(f"Status code: {response1.status_code}")
# print(response1.text)
# print(response1.json())

# ===

# try:
#     response = httpx.get("https://jsonplaceholder.typicode.com/invalid-url")
#     response.raise_for_status()
#     print(response.status_code)
# except httpx.HTTPStatusError as e:
#     print(f"Ошибка запроса '{e}'")

# ===

# try:
#     response = httpx.get("https://httpbin.org/delay/5", timeout=2)
# except httpx.ReadTimeout:
#     print(f"Запрос превысил лимит времени")