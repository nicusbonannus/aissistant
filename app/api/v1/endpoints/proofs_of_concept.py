from fastapi import Depends
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from starlette import status

from app.api.v1.endpoints.events import router
from app.db import crud
from app.db.database import get_db
from app.db.schemas import UserCreate
from app.services.llm_handler import LLMHandler


class CreateUserInfo(BaseModel):
    name: str = Field(...)
    email: str = Field(...)


class UserInformation(BaseModel):
    id: int = Field(...)
    name: str = Field(...)
    email: str = Field(...)


@router.post(
    "/user", status_code=status.HTTP_201_CREATED, response_model=UserInformation
)
def create_user(user_info: CreateUserInfo, db: Session = Depends(get_db)):
    user_create = UserCreate(name=user_info.name, email=user_info.email)
    response = crud.create_user(db, user_create)
    return UserInformation(name=response.name, email=response.email, id=response.id)


class DiscountInfo(BaseModel):
    price: float = Field(..., gt=0)
    discount: float = Field(..., gt=0, le=100)


@router.post("/discount", status_code=status.HTTP_200_OK)
def calculate_discount(discount_info: DiscountInfo):
    response = LLMHandler().tool_example(
        price=discount_info.price, discount=discount_info.discount
    )

    return {"response": response}
