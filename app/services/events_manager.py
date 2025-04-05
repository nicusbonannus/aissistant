from datetime import datetime

from app.services.calendar_reader import CalendarReader
from app.services.llm_handler import LLMHandler


class EventsManager:
    def find_spot(self, event_description: str) -> str:
        agenda_events = CalendarReader().get_calendar_events()
        return LLMHandler().find_spot(
            agenda=agenda_events, event_description=event_description
        )

    def analyze_agenda_for(self, start: datetime, end: datetime) -> str:
        agenda_events = CalendarReader().get_calendar_events(start=start, end=end)
        return LLMHandler().analyze_agenda(agenda_events=agenda_events)
