from datetime import datetime, timedelta
from typing import Optional, Tuple

import pytz
from googleapiclient.discovery import build

from app.utils.google_calendar import get_google_calendar_token


class CalendarReader:
    def get_calendar_events(
        self, start: Optional[datetime] = None, end: Optional[datetime] = None
    ):
        creds = get_google_calendar_token()
        service = build("calendar", "v3", credentials=creds)

        start_date, end_date = self.format_dates(start, end)
        events_result = (
            service.events()
            .list(
                calendarId="primary",
                timeMin=start_date,
                timeMax=end_date,
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )

        events = events_result.get("items", [])

        calendar_events = []
        for event in events:
            start = event["start"].get("dateTime", event["start"].get("date"))
            calendar_events.append(
                dict(start=start, end=event["end"].get("date"), title=event["summary"])
            )

        return calendar_events

    @staticmethod
    def format_dates(
        start_date: Optional[datetime] = None, end_date: Optional[datetime] = None
    ) -> Tuple[str, str]:
        tz = pytz.timezone("America/Argentina/Buenos_Aires")
        if start_date is None:
            start_date = datetime.now().replace(
                hour=0, minute=0, second=0, microsecond=0
            )
        start_date = start_date.replace(tzinfo=tz)
        if end_date is None:
            end_date = (datetime.now() + timedelta(days=1)).replace(
                hour=0, minute=0, second=0, microsecond=0
            )
        end_date = end_date.replace(tzinfo=tz)
        return start_date.isoformat(), end_date.isoformat()
