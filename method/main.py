from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/qparam/")
async def qparam(
    param_a: str,
    param_b: int
):
    return {
        "message": 'a is ' + param_a + ' b is ' + str(param_b)
    }


class Schema(BaseModel):
    name: str
    password: str

@app.post("/post/")
async def post(req: Schema):
    return {
        "message": 'name is ' + req.name + ' pass is ' + req.password
    }
