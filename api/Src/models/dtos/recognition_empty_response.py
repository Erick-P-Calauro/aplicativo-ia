from pydantic import BaseModel


class RecognitionEmptyResponse(BaseModel):
    message: str
