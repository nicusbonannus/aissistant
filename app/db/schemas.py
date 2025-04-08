from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str


class UserOur(UserCreate):
    id: int

    model_config = {"from_attributes": True}
