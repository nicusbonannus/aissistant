from app.services.events_manager import EventsManager


class TestGetTodaySSummary:
    def test_get_today_s_summary__happy_path(self):
        # given
        events_manager = EventsManager()

        # when
        summary = events_manager.today_s_summary()

        # then
        assert summary == "Today you have to work the whole day"
