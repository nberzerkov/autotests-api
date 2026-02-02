from httpx import Response

from typing import TypedDict

from clients.api_client import APIClient

class CreateUserRequest(TypedDict):
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    def create_user_api(self, request: CreateUserRequest) -> Response:
        """
        Метод для создания пользователя.

        :param request: Словарь с данными юзера.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/users", json=request)
