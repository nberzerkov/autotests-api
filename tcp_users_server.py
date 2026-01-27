import socket


HOST = "127.0.0.1"
PORT = 12345
MAX_CONNECTIONS = 10


def main():
    messages = []  # история всех сообщений

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(MAX_CONNECTIONS)

    print(f"TCP сервер запущен на {HOST}:{PORT}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Пользователь с адресом: {client_address} подключился к серверу")

        try:
            data = client_socket.recv(1024)
            if not data:
                continue

            message = data.decode()
            print(
                f"Пользователь с адресом: {client_address} "
                f"отправил сообщение: {message}"
            )

            messages.append(message)

            # Отправляем всю историю сообщений
            response = "\n".join(messages)
            client_socket.send(response.encode())

        finally:
            client_socket.close()


if __name__ == "__main__":
    main()
