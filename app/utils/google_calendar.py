import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

from app.core.config import settings

SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]


def get_google_calendar_token():
    creds = None
    if os.path.exists(settings.google_token_json_path):
        creds = Credentials.from_authorized_user_file(
            settings.google_token_json_path, SCOPES
        )

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                settings.google_client_json_path, SCOPES
            )
            creds = flow.run_local_server(
                port=8000, access_type="offline", prompt="consent"
            )

        with open(settings.google_token_json_path, "w") as token_file:
            token_file.write(creds.to_json())

    return creds
