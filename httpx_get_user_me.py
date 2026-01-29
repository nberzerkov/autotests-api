import httpx

# === auth

login_payload = {
  "email": "n1k@mail.ru",
  "password": "123pwe"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

print("Status code:", login_response.status_code)
print("Login response data:", login_response_data)

# === get user

auth_access_token = login_response_data["token"]["accessToken"]
auth_jwt_bearer = {"Authorization": f"Bearer {auth_access_token}"}

user_info_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=auth_jwt_bearer)
user_info_response_data = user_info_response.json()

print("Status code:", user_info_response.status_code)
print("User info response data:", user_info_response_data)
