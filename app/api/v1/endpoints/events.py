from fastapi import APIRouter, status

from app.services.events_manager import EventsManager
from app.services.llm_handler import LLMHandler

router = APIRouter()


@router.get("/today", status_code=status.HTTP_200_OK)
def describe_today():
    events_manager = EventsManager()
    return {"summary": events_manager.today_s_summary()}


@router.get("/discount", status_code=status.HTTP_200_OK)
def calculate_discount():
    response = LLMHandler().tool_example(price=100.0, discount=10.0)

    return {"response": response}
