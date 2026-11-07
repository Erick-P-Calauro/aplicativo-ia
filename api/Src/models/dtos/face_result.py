import uuid
from typing import Optional

from pydantic import BaseModel

from .face_box import FaceBox


class FaceResult(BaseModel):
    box: FaceBox
    name: str
    score: float
