from app.services.calendar_reader import CalendarReader
from app.services.llm_handler import LLMHandler


class EventsManager:
    def today_s_summary(self) -> str:
        agenda_events = CalendarReader().get_calendar_events()
        return LLMHandler().analyze_agenda(agenda=agenda_events)
