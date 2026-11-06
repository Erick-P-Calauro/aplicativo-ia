import uuid
from datetime import datetime

from pydantic import BaseModel


class UserResponse(BaseModel):
    id: uuid.UUID
    name: str
    photo_path: str
    created_at: datetime

    model_config = {"from_attributes": True}
