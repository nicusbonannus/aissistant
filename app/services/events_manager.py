from datetime import datetime

from app.services.calendar_reader import CalendarReader
from app.services.llm_handler import LLMHandler


class EventsManager:
    def today_s_summary(self) -> str:
        agenda_events = CalendarReader().get_calendar_events()
        return LLMHandler().find_spot(agenda=agenda_events)

    def analyze_agenda_for(self, start: datetime, end: datetime) -> str:
        agenda_events = CalendarReader().get_calendar_events(start=start, end=end)
        return LLMHandler().analyze_agenda(agenda_events=agenda_events)
