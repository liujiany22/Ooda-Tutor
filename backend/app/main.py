from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from routes.ws import websocket_endpoint
import uvicorn

# 创建 FastAPI 应用实例
app = FastAPI()

# 示例路由：根路径返回简单的文本
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Touch Signature API"}

# WebSocket 路由
app.add_websocket_route("/ws", websocket_endpoint)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=7777, reload=True)