# backend/app/routes/ws.py

from fastapi import WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
import json

# WebSocket 管理器
class WebSocketManager:
    def __init__(self):
        self.active_connections = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    async def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)
        await websocket.close()

    async def send_message(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = WebSocketManager()

# WebSocket 路由
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()  # 接收前端发来的消息
            message = json.loads(data)  # 解析 JSON 数据
            await manager.send_message(f"Received data: {message}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)

