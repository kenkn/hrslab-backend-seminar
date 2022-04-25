from fastapi import APIRouter
from schemas.post_schema import PostSchema

router = APIRouter()


@router.get("/qparam/")
async def qparam(
    param_a: str,
    param_b: int
):
    return {
        "message": 'a is ' + param_a + ' b is ' + str(param_b)
    }


@router.post("/post/")
async def post(req: PostSchema):
    return {
        "message": 'name is ' + req.name + ' pass is ' + req.password
    }
    

