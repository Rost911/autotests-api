import socket

HOST = '127.0.0.1'  # localhost
PORT = 12345        # порт сервера

def main():
    # Создаём TCP-клиентский сокет
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Подключаемся к серверу
        client_socket.connect((HOST, PORT))

        # Сообщение, которое нужно отправить серверу
        message = "Привет, сервер!"

        # Отправляем сообщение
        client_socket.send(message.encode('utf-8'))

        # Получаем ответ от сервера
        response = client_socket.recv(1024).decode('utf-8')

        # Выводим ответ сервера в консоль
        print(response)

    finally:
        # Закрываем соединение
        client_socket.close()


if __name__ == '__main__':
    main()
