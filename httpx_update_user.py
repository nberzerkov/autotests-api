import httpx
from tools.fakers import get_random_email

BASE_URL = "http://localhost:8000"

create_user_payload = {
  "email": get_random_email(),
  "password": "123pwe",
  "lastName": "End",
  "firstName": "Nick",
  "middleName": "MiddleName"
}

create_user_response = httpx.post(f"{BASE_URL}/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()

print("CREATE USER:")
print("status code:", create_user_response.status_code)
print("create user data:", create_user_response_data)

login_payload = {
  "email": create_user_payload["email"],
  "password": create_user_payload["password"]
}

auth_login_response = httpx.post(f"{BASE_URL}/api/v1/authentication/login", json=login_payload)
auth_login_response_data = auth_login_response.json()

print("LOGIN:")
print("status code:", auth_login_response.status_code)
print("login data:", auth_login_response_data)

update_user_headers = {
    "Authorization": f"Bearer {auth_login_response_data['token']['accessToken']}"
}

update_payload = {
    "email": get_random_email(),
    "lastName": "Dne",
    "firstName": "K1n",
    "middleName": "NameMiddle"
}


update_user_response = httpx.patch(f"{BASE_URL}/api/v1/users/{create_user_response_data['user']['id']}", headers=update_user_headers, json=update_payload)
update_user_response_data = update_user_response.json()

print("UPDATE USER:")
print("status code:", update_user_response.status_code)
print("update user data:", update_user_response_data)