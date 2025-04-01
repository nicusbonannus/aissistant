import datetime


class EventsManager:
    def day_agenda(self):
        return [
            dict(
                id=1,
                start_at=datetime.datetime.now(),
                end_at=datetime.datetime.now() + datetime.timedelta(hours=1),
                title="Brush teeth",
            ),
            dict(
                id=2,
                start_at=datetime.datetime.now() + datetime.timedelta(hours=2),
                end_at=datetime.datetime.now() + datetime.timedelta(hours=10),
                title="Work",
            ),
        ]

    def today_s_summary(self):
        return "Today you have to work the whole day"
