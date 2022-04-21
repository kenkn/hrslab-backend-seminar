from fastapi import FastAPI # FastAPI のインポート

app = FastAPI() # FastAPI のオブジェクト生成


@app.get("/hello")  # エンドポイント "http://localhost:8000/hello" にアクセスしたとき
async def hello():
    return "Hello, world!"
