from fastapi import APIRouter, status

from app.services.events_manager import EventsManager

router = APIRouter()


SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]


@router.get("/today", status_code=status.HTTP_200_OK)
def describe_today():
    events_manager = EventsManager()
    return {"summary": events_manager.today_s_summary()}


#
# @router.get("/auth", status_code=status.HTTP_200_OK)
# def describe_auth():
#     creds = get_google_calendar_token()
# service = build("calendar", "v3", credentials=creds)
#
# # Definir el rango de tiempo (desde la medianoche hasta las 23:59:59 del día actual)
# tz = pytz.timezone("America/Argentina/Buenos_Aires")  # Ajusta a tu zona horaria
# now = datetime.now(tz)
# start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0).isoformat()
# end_of_day = now.replace(hour=23, minute=59, second=59, microsecond=999999).isoformat()
#
# # Obtener eventos del día actual
# events_result = service.events().list(
#     calendarId="primary",  # Calendario principal
#     timeMin=start_of_day,
#     timeMax=end_of_day,
#     singleEvents=True,
#     orderBy="startTime"
# ).execute()
#
# events = events_result.get("items", [])
#
# if not events:
#     print("No hay eventos para hoy.")
#     return
#
# for event in events:
#     start = event["start"].get("dateTime", event["start"].get("date"))  # Puede ser todo el día
#     print(f"{start} - {event['summary']}")
