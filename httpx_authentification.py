import httpx

login_payload = {
  "email": "n1k@mail.ru",
  "password": "123pwe"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

print("Status Code:", login_response.status_code)
print("Login Response", login_response_data)

refresh_payload = {
  "refreshToken": login_response_data["token"]["refreshToken"]
}

login_refresh_response = httpx.post("http://localhost:8000/api/v1/authentication/refresh", json=refresh_payload)
login_refresh_response_data = login_refresh_response.json()

print("Status Code:", login_refresh_response.status_code)
print("Login Refresh Response", login_refresh_response_data)