from fastapi import APIRouter, Depends, Query, status

from app.api.v1.deps.events_params import RequestByDateRangeParams
from app.services.events_manager import EventsManager

router = APIRouter()


@router.get("/find_spot", status_code=status.HTTP_200_OK)
def find_spot(
    event: str = Query(
        max_length=200,
        description="Description of the eevent i not more than 200 characters",
    )
):
    events_manager = EventsManager()
    return {"summary": events_manager.find_spot(event_description=event)}


@router.get("/agenda", status_code=status.HTTP_200_OK)
def describe_agenda(date_range_params: RequestByDateRangeParams = Depends()):
    events_manager = EventsManager()
    agenda_analysis = events_manager.analyze_agenda_for(
        start=date_range_params.start, end=date_range_params.end
    )
    return {"summary": agenda_analysis}
