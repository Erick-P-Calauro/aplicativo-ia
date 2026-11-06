from pydantic import BaseModel


class LoginRequest(BaseModel):
    root_user: str
    root_passwd: str
