from fastapi import APIRouter, status

from app.services.events_manager import EventsManager

router = APIRouter()

@router.get("/today", status_code=status.HTTP_200_OK)
def describe_today():
    events_manager = EventsManager()
    return {"summary": events_manager.today_s_summary()}
