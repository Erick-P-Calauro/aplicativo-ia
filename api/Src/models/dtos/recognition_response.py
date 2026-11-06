from typing import List

from pydantic import BaseModel

from .face_result import FaceResult


class RecognitionResponse(BaseModel):
    faces: List[FaceResult]
