from pydantic import BaseModel


class FaceBox(BaseModel):
    x: int
    y: int
    w: int
    h: int
