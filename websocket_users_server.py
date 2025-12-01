import asyncio
import sys
import websockets

HOST = "localhost"
PORT = 8765

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass


async def handle_client(websocket):
    try:
        async for message in websocket:
            try:
                print(f"Получено сообщение от пользователя: {message}")
            except UnicodeEncodeError:
                print("Получено сообщение от пользователя (проблема с кодировкой при выводе)")

            for i in range(1, 6):
                response = f"{i} Сообщение пользователя: {message}"
                await websocket.send(response)

    except Exception as e:

        print(f"Ошибка в обработчике клиента: {e}")


async def main():
    async with websockets.serve(handle_client, HOST, PORT):
        print(f"WebSocket сервер запущен на ws://{HOST}:{PORT}")
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
