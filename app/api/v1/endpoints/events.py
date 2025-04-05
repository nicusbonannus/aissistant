from fastapi import APIRouter, Depends, status
from pydantic import BaseModel, Field

from app.api.v1.deps.events_params import RequestByDateRangeParams
from app.services.events_manager import EventsManager
from app.services.llm_handler import LLMHandler

router = APIRouter()


class DiscountInfo(BaseModel):
    price: float = Field(..., gt=0)
    discount: float = Field(..., gt=0, le=100)


@router.get("/find_spot", status_code=status.HTTP_200_OK)
def describe_today():
    events_manager = EventsManager()
    return {"summary": events_manager.today_s_summary()}


@router.get("/agenda", status_code=status.HTTP_200_OK)
def describe_agenda(date_range_params: RequestByDateRangeParams = Depends()):
    events_manager = EventsManager()
    agenda_analysis = events_manager.analyze_agenda_for(
        start=date_range_params.start, end=date_range_params.end
    )
    return {"summary": agenda_analysis}


# Example
@router.post("/discount", status_code=status.HTTP_200_OK)
def calculate_discount(discount_info: DiscountInfo):
    response = LLMHandler().tool_example(
        price=discount_info.price, discount=discount_info.discount
    )

    return {"response": response}
