from fastapi import APIRouter
from pydantic import BaseModel, Field
from starlette import status

from app.services.llm_handler import LLMHandler

router = APIRouter()


class DiscountInfo(BaseModel):
    price: float = Field(..., gt=0)
    discount: float = Field(..., gt=0, le=100)


@router.post("/discount", status_code=status.HTTP_200_OK)
def calculate_discount(discount_info: DiscountInfo):
    response = LLMHandler().tool_example(
        price=discount_info.price, discount=discount_info.discount
    )

    return {"response": response}
