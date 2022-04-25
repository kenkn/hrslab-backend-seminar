from pydantic import BaseModel

class PostSchema(BaseModel):
    name: str
    password: str