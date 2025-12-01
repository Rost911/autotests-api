import asyncio
import websockets

URI = "ws://localhost:8765"


async def main():
    async with websockets.connect(URI) as websocket:
        await websocket.send("Привет, сервер!")


        for _ in range(5):
            message = await websocket.recv()
            print(message)


if __name__ == "__main__":
    asyncio.run(main())
