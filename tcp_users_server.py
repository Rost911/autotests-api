import socket

HOST = '127.0.0.1'  # localhost
PORT = 12345        # порт сервера

def main():
    # Список для хранения всех сообщений
    messages = []

    # Создаём TCP-сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Позволяем быстро переиспользовать порт после перезапуска сервера
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Привязываем сокет к адресу и порту
    server_socket.bind((HOST, PORT))

    # Начинаем слушать (очередь до 10 подключений)
    server_socket.listen(10)
    print(f"Сервер запущен на {HOST}:{PORT}")

    try:
        while True:
            # Ожидаем нового клиента
            client_socket, client_address = server_socket.accept()
            print(f"Пользователь с адресом: {client_address} подключился к серверу")

            try:
                # Получаем данные от клиента
                data = client_socket.recv(1024)
                if not data:
                    # Клиент ничего не отправил — закрываем соединение
                    client_socket.close()
                    continue

                message = data.decode('utf-8').strip()

                print(
                    f"Пользователь с адресом: {client_address} "
                    f"отправил сообщение: {message}"
                )

                # Добавляем сообщение в общую историю
                messages.append(message)

                # Формируем ответ — вся история сообщений, каждое с новой строки
                response = '\n'.join(messages)

                # Отправляем ответ клиенту
                client_socket.send(response.encode('utf-8'))

            finally:
                # Закрываем соединение с клиентом
                client_socket.close()

    except KeyboardInterrupt:
        print("\nСервер остановлен пользователем.")
    finally:
        server_socket.close()


if __name__ == '__main__':
    main()
