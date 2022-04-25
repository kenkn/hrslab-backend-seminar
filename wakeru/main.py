from fastapi import FastAPI
from routers.router import router

app = FastAPI()

# router 登録
app.include_router(router)
