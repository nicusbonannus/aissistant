from datetime import datetime

import pytz
from googleapiclient.discovery import build

from app.utils.google_calendar import get_google_calendar_token


class CalendarReader:
    def get_calendar_events(self, start: datetime = None, end: datetime = None):
        creds = get_google_calendar_token()
        service = build("calendar", "v3", credentials=creds)
        tz = pytz.timezone("America/Argentina/Buenos_Aires")
        now = datetime.now(tz)
        start_of_day = (
            start.replace(tzinfo=tz)
            or now.replace(hour=0, minute=0, second=0, microsecond=0)
        ).isoformat()
        end_of_day = (
            end.replace(tzinfo=tz)
            or now.replace(hour=23, minute=59, second=59, microsecond=999999)
        ).isoformat()
        events_result = (
            service.events()
            .list(
                calendarId="primary",
                timeMin=start_of_day,
                timeMax=end_of_day,
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
