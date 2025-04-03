import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

from app.core.config import settings

SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]

"""
This script generates the token.json based on the client.json created on the Google Console with Oauth2
Run it like:
$ python auth.py
"""


def get_google_calendar_token():
    creds = None
    if os.path.exists("app/token.json"):
        creds = Credentials.from_authorized_user_file("app/token.json", SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                settings.google_client_json_path, SCOPES
            )
            creds = flow.run_local_server(port=8000)

        with open("app/token.json", "w") as token_file:
            token_file.write(creds.to_json())

    return creds


get_google_calendar_token()
