from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="问候应用", version="1.0.0")


@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <html>
        <head><title>问候应用</title></head>
        <body style="text-align:center;padding-top:100px;font-family:Arial;">
            <h2>欢迎使用问候应用</h2>
            <p>访问 <a href="/greet/World">/greet/World</a> 试试看！</p>
        </body>
    </html>
    """


@app.get("/greet/{name}")
async def greet(name: str):
    return {"message": f"你好，{name}！欢迎使用 FastAPI。"}


@app.get("/health")
async def health():
    return {"status": "ok"}