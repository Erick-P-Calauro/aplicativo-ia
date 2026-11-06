import uuid
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class UserResponse(BaseModel):
    id: uuid.UUID
    name: str
    photo_path: str
    created_at: datetime

    model_config = {"from_attributes": True}


class FaceBox(BaseModel):
    x: int
    y: int
    w: int
    h: int


class FaceResult(BaseModel):
    box: FaceBox
    name: str
    user_id: Optional[uuid.UUID] = None
    score: float


class RecognitionResponse(BaseModel):
    faces: List[FaceResult]


class RecognitionEmptyResponse(BaseModel):
    message: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class LoginRequest(BaseModel):
    root_user: str
    root_passwd: str
