from app.utils.google_calendar import get_google_calendar_token

"""
This script generates the token.json based on the client.json created on the Google Console with Oauth2
Run it like:
$ python auth.py
"""
get_google_calendar_token()
